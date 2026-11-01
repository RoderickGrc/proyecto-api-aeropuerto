#!/usr/bin/env python3
"""Genera la curva S del programa en PDF A4 horizontal, lista para insertarse en el documento.

Lee curva_s_mensual.csv, curva_s_anual.csv e hitos.csv (salidas de build_planificacion.py) y escribe
curva_s_ES-L1173.pdf en esta carpeta. Sigue los componentes de la curva de uso de recursos de la clase 6
(identificación, fechas, valor planificado del período y acumulado) con la paleta del Gantt de Open Planner.
Requiere matplotlib y PyMuPDF (fitz).
"""
from __future__ import annotations
import csv
import io
import json
from datetime import date, timedelta
from pathlib import Path

import sys
sys.dont_write_bytecode = True  # no dejar __pycache__ en el repositorio
import fitz
import matplotlib
matplotlib.use('Agg')
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

HERE = Path(__file__).resolve().parent
MESES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
MESES_L = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
# Paleta del Gantt exportado de Open Planner Studio (la misma del anexo del cronograma).
BLUE, PURPLE, GRAY, INK, MUTED, GRID = '#2563eb', '#7c3aed', '#8b909a', '#1f2430', '#5b6270', '#e3e6ea'
RES = json.loads((HERE / 'resumen.json').read_text(encoding='utf-8'))
START, FINISH = date.fromisoformat(RES['inicio']), date.fromisoformat(RES['fin'])
BAC, LOAN, CONT, PRES = RES['bac_musd'], RES['prestamo_musd'], RES['contingencia_musd'], RES['presupuesto_musd']
EST, GEST = RES['estimacion_pert_musd'], RES['reserva_gestion_musd']
COST = json.loads((HERE / 'estimacion_costos.json').read_text(encoding='utf-8'))

mensual = list(csv.DictReader((HERE / 'curva_s_mensual.csv').open(encoding='utf-8-sig')))
anual = list(csv.DictReader((HERE / 'curva_s_anual.csv').open(encoding='utf-8-sig')))
CORTE = date.fromisoformat(RES['corte'])  # fecha a reportar
hitos = {h['id']: h for h in csv.DictReader((HERE / 'hitos.csv').open(encoding='utf-8-sig'))}
FIN = list(csv.DictReader((HERE / 'requisitos_financiamiento.csv').open(encoding='utf-8-sig')))
ACTS = list(csv.DictReader((HERE / 'cronograma_actividades.csv').open(encoding='utf-8-sig')))
SEM_START = [date(2026 + i // 2, 1 if i % 2 == 0 else 7, 1) for i in range(len(FIN))]
# Desembolsos previstos del BID en el PEP y requisitos de financiamiento con anticipo y reserva de gestión: el acumulado
# que se necesita al cierre de cada semestre debe estar disponible desde su inicio (clase 6, figura de línea base,
# gastos y requisitos de financiamiento: el financiamiento va en escalones por delante del gasto).
PEP = [(d, float(r['desembolso_pep_acum_musd'])) for d, r in zip(SEM_START, FIN)]
FUND = [(d, float(r['requisito_con_anticipo_acum_musd'])) for d, r in zip(SEM_START, FIN)]


def jy(items) -> str:
    """Enumeración con comas y 'y' antes del último elemento."""
    items = list(items)
    return items[0] if len(items) == 1 else ', '.join(items[:-1]) + ' y ' + items[-1]


def dmy(x) -> str:
    x = date.fromisoformat(x) if isinstance(x, str) else x
    return f'{x.day}-{MESES[x.month - 1]}-{x.year}'


def weekdays(a: date, b: date) -> int:
    """Días laborables (lunes a viernes) entre a y b, ambos incluidos."""
    return sum(1 for i in range((b - a).days + 1) if (a + timedelta(days=i)).weekday() < 5)


def month_end(ym: str) -> date:
    y, m = map(int, ym.split('-'))
    return (date(y + m // 12, m % 12 + 1, 1)) - timedelta(days=1)


def mlabel(ym: str) -> str:
    y, m = map(int, ym.split('-'))
    return f'{MESES[m - 1]}-{y}'


def mlong(ym: str) -> str:
    y, m = map(int, ym[:7].split('-'))
    return f'{MESES_L[m - 1].lower()} de {y}'


def mnext(ym: str) -> str:
    y, m = map(int, ym[:7].split('-'))
    return f'{y + m // 12}-{m % 12 + 1:02d}'


def money(v: float) -> str:
    return f'{v:,.2f}'


months = [r['mes'] for r in mensual]
PV_CORTE = float(next(r['acumulado_linea_base_musd'] for r in mensual if r['mes'] == f'{CORTE.year}-{CORTE.month:02d}'))
AC_CORTE = RES['costo_real_corte_musd']
AC_TXT = f'US${AC_CORTE:.2f} M estimado (UEP); sin desembolsos del BID publicados'
ends = [min(month_end(m), FINISH) for m in months]
pv = [float(r['gasto_mensual_musd']) for r in mensual]
cum = [float(r['acumulado_linea_base_musd']) for r in mensual]
cum_sc = [float(r['acumulado_sin_contingencia_musd']) for r in mensual]
peak = max(range(len(pv)), key=pv.__getitem__)
quart = {q: next(i for i, c in enumerate(cum) if c >= BAC * q / 100 - 1e-6) for q in (25, 50, 75, 90)}

plt.rcParams.update({'font.family': 'Arial', 'font.size': 8.5, 'text.color': INK, 'axes.labelcolor': MUTED,
                     'xtick.color': MUTED, 'ytick.color': MUTED, 'axes.edgecolor': '#9ca3af', 'pdf.fonttype': 42})
def make_chart(w_pt: float, h_pt: float) -> bytes:
    fig = plt.figure(figsize=(w_pt / 72, h_pt / 72))
    gs = fig.add_gridspec(2, 1, height_ratios=[3.1, 1], hspace=0.12)
    ax, bx = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])
    x0, x1 = START - timedelta(days=18), FINISH + timedelta(days=135)

    # Curva S acumulada: línea base de costos (con contingencia) y estimación de los paquetes (sin contingencia).
    xs, ys, ys_sc = [START] + ends, [0.0] + cum, [0.0] + cum_sc
    ax.axhline(LOAN, color=MUTED, lw=0.8, ls=(0, (4, 3)), zorder=1)
    ax.text(x0 + timedelta(days=20), LOAN + 3, f'Préstamo: US${LOAN:.1f} M', fontsize=7.5, color=MUTED, va='bottom')
    ax.axhline(PRES, color=MUTED, lw=0.8, ls=(0, (1, 2)), zorder=1)
    ax.text(x1 - timedelta(days=10), PRES + 1.5, f'Presupuesto del proyecto: US${PRES:.1f} M', fontsize=7.5, color=MUTED, va='bottom', ha='right')
    for k in ('H03', 'H05', 'H07', 'H09'):
        hd = date.fromisoformat(hitos[k]['date'])
        ax.axvline(hd, color=PURPLE, lw=0.8, ls=(0, (2, 2)), alpha=0.75, zorder=1)
        bx.axvline(hd, color=PURPLE, lw=0.8, ls=(0, (2, 2)), alpha=0.75, zorder=1)
        ax.text(hd + timedelta(days=12), 6, k, color=PURPLE, fontsize=7.5, fontweight='bold', va='bottom')
    ax.plot(xs, ys_sc, color=GRAY, lw=1.6, ls=(0, (5, 2)), zorder=2, label='Estimación PERT (sin reserva)')
    ax.plot(xs, ys, color=BLUE, lw=2.2, zorder=3, label='Línea base (BAC, con reserva de contingencia)')
    # Escalón: el acumulado que se necesita al cierre de cada semestre, disponible desde el inicio del semestre.
    fx = [d for d, _ in FUND] + [x1]
    fy = [v for _, v in FUND] + [FUND[-1][1]]
    ax.step(fx, fy, where='post', color='#0d9488', lw=1.1, alpha=0.9, zorder=2, label='Requisitos de financiamiento con anticipo y reserva de gestión (disponible desde el inicio de cada semestre)')
    px = [d for d, _ in PEP] + [x1]
    py = [v for _, v in PEP] + [PEP[-1][1]]
    ax.step(px, py, where='post', color='#b45309', lw=1.1, ls=(0, (3, 1.5)), alpha=0.85, zorder=2, label='Desembolsos previstos del BID en el PEP (desde el inicio de cada semestre)')
    ax.axvline(CORTE, color=INK, lw=0.8, ls=(0, (1, 1.5)), zorder=1)
    ax.text(CORTE + timedelta(days=8), 60, 'Fecha a reportar\n31-10-2026', fontsize=7, color=INK, va='bottom')
    ax.text(FINISH + timedelta(days=12), ys[-1] + 2, f'US${ys[-1]:.1f} M', color=INK, fontsize=7.5, fontweight='bold', va='bottom')
    ax.text(FINISH + timedelta(days=12), ys_sc[-1] - 4, f'US${ys_sc[-1]:.1f} M', color=MUTED, fontsize=7.5, va='center')
    for q, i in quart.items():
        ax.plot(ends[i], cum[i], 'o', ms=5.5, color=BLUE, mec='white', mew=1.3, zorder=4)
        ax.annotate(f'{q}%  {mlabel(months[i])}', (ends[i], cum[i]), xytext=(-8, 0), textcoords='offset points', ha='right', va='center', fontsize=7.5, color=INK)
    ax.set_ylim(0, 212)
    ax.set_ylabel('Valor planificado acumulado (US$ M)')
    ax.legend(loc='center right', bbox_to_anchor=(1.0, 0.17), frameon=False, fontsize=7.8, handlelength=2.6)

    # Valor planificado de cada mes, en un panel aparte con su propio eje (no se mezcla con la escala acumulada).
    bx.bar([d - timedelta(days=14) for d in ends], pv, width=20, color=BLUE, alpha=0.55, zorder=2)
    bx.annotate(f'Pico: US${pv[peak]:.1f} M ({mlabel(months[peak])})', (ends[peak] - timedelta(days=14), pv[peak]), xytext=(10, -2),
                textcoords='offset points', fontsize=7.5, color=INK, va='top')
    bx.set_ylim(0, max(pv) * 1.15)
    bx.set_ylabel('Mensual (US$ M)')

    for a in (ax, bx):
        a.set_xlim(x0, x1)
        a.grid(axis='y', color=GRID, lw=0.6, zorder=0)
        a.spines[['top', 'right']].set_visible(False)
        a.tick_params(length=0)
        a.xaxis.set_major_locator(mdates.YearLocator())
        a.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=7))
        a.tick_params(axis='x', which='major', length=6, color='#9ca3af')
        a.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f'{v:,.0f}'))
    ax.tick_params(labelbottom=False)
    bx.xaxis.set_major_formatter(FuncFormatter(lambda v, _: ''))
    bx.xaxis.set_minor_formatter(mdates.DateFormatter('%Y'))
    bx.tick_params(axis='x', which='minor', length=0, labelsize=8.5)
    ax.tick_params(axis='x', which='minor', length=0, labelbottom=False)
    fig.subplots_adjust(left=0.07, right=0.93, top=0.98, bottom=0.06)
    chart = io.BytesIO()
    fig.savefig(chart, format='pdf')
    plt.close(fig)
    return chart.getvalue()

# ---------- página 1: identificación + gráfico; página 2: tabla mensual + interpretación ----------
CSS = f'''
body {{ font-family: sans-serif; font-size: 8pt; color: {INK}; }}
h1 {{ font-size: 13pt; margin: 0 0 3pt 0; }}
h2 {{ font-size: 10pt; margin: 6pt 0 3pt 0; color: {INK}; }}
p {{ margin: 0 0 3pt 0; }}
p.nota {{ font-size: 7pt; color: {MUTED}; }}
ul {{ margin: 0 0 0 12pt; padding: 0; }}
li {{ margin: 0 0 2pt 0; }}
table {{ border-collapse: collapse; width: 100%; }}
th {{ background-color: #f1f3f6; color: #444a57; padding: 3pt 10pt 3pt 8pt; font-size: 8pt; border-bottom: 1pt solid #9ca3af; }}
td {{ padding: 3pt 10pt 3pt 8pt; border-bottom: 0.4pt solid {GRID}; font-size: 8pt; }}
td.n {{ text-align: right; }}
td.k {{ font-weight: bold; }}
td.c {{ color: {MUTED}; }}
tr.t td {{ background-color: #f3effd; color: {PURPLE}; font-weight: bold; border-top: 1pt solid #9ca3af; }}
table.id td {{ border-bottom: 0; padding: 0.8pt 6pt 0.8pt 0; font-size: 7.8pt; }}
'''
ID = f'''<table class="id">
<tr><td class="k">Proyecto</td><td>Programa de Modernización del Aeropuerto Internacional de El Salvador</td><td class="k">Fecha inicial</td><td>{START:%d-%m-%Y}</td><td class="k">Línea base (BAC)</td><td>US${BAC * 1e6:,.0f}</td></tr>
<tr><td class="k">Código</td><td>ES-L1173 (BID / CEPA)</td><td class="k">Fecha final</td><td>{FINISH:%d-%m-%Y}</td><td class="k">Unidad de tiempo</td><td>Mes ({len(months)} períodos)</td></tr>
<tr><td class="k">Fecha a reportar</td><td>{CORTE:%d-%m-%Y}</td><td class="k">Valor planificado a la fecha</td><td>US${PV_CORTE:.2f} M</td><td class="k">Costo real a la fecha</td><td>{AC_TXT}</td></tr>
</table>'''
P1 = f'''<h1>Curva S del programa ES-L1173: valor planificado acumulado</h1>{ID}'''

# Tabla mensual: filas = meses, columnas = años (mensual y acumulado), como el ejemplo de la clase 6.
years = sorted({m[:4] for m in months})
data = {m: (p, c) for m, p, c in zip(months, pv, cum)}
head = '<tr><th style="width:10%">Mes</th>' + ''.join(f'<th style="width:9%;text-align:right">{y}<br>Mensual</th><th style="width:9%;text-align:right">{y}<br>Acumulado</th>' for y in years) + '</tr>'
body = []
for mi in range(12):
    cells = []
    for y in years:
        v = data.get(f'{y}-{mi + 1:02d}')
        cells.append(f'<td class="n">{money(v[0])}</td><td class="n c">{money(v[1])}</td>' if v else '<td class="n c">-</td><td class="n c">-</td>')
    body.append(f'<tr><td class="k">{MESES_L[mi]}</td>{"".join(cells)}</tr>')
by = {r['anio']: r for r in anual}
body.append('<tr class="t"><td>Total del año</td>' + ''.join(f'<td class="n">{money(float(by[y]["gasto_anual_musd"]))}</td><td class="n">{money(cum[max(i for i, m in enumerate(months) if m.startswith(y))])}</td>' for y in years) + '</tr>')
body.append('<tr class="t"><td>Avance acumulado</td>' + ''.join(f'<td class="n"></td><td class="n">{float(by[y]["avance_pct"]):.1f}%</td>' for y in years) + '</tr>')

H03, H07 = hitos['H03']['date'][:7], hitos['H07']['date'][:7]
Q90 = months[quart[90]]
PEAK_I = peak
qtxt_acc = jy(f'el {q}% en {mlabel(months[i])}' for q, i in quart.items() if i <= PEAK_I)
qtxt_dec = jy(f'el {q}% en {mlabel(months[i])}' for q, i in quart.items() if i > PEAK_I)


def hname(h: str) -> str:
    n = hitos[h]['name']
    return n if n.split()[0].isupper() else n[0].lower() + n[1:]


def month_value(row: dict, ym: str) -> float:
    """Valor planificado de una actividad en un mes: prorrateo lineal por días laborables (como la curva)."""
    a, b = date.fromisoformat(row['start']), date.fromisoformat(row['finish'])
    lo, hi = max(a, date.fromisoformat(ym + '-01')), min(b, month_end(ym))
    return float(row['budget']) * weekdays(lo, hi) / weekdays(a, b) if hi >= lo else 0.0


def remaining(row: dict, d: date) -> float:
    """Valor planificado de una actividad posterior al día d (prorrateo lineal)."""
    a, b = date.fromisoformat(row['start']), date.fromisoformat(row['finish'])
    return float(row['budget']) * weekdays(max(a, d + timedelta(days=1)), b) / weekdays(a, b) if b > d else 0.0


GRP = [('la terminal', ('1.2.',)), ('el estacionamiento y el sistema solar', ('1.5.',)), ('las plataformas y la calle Foxtrot', ('1.3.', '1.4.')),
       ('el SSEI', ('1.6.',)), ('la supervisión de las obras', ('1.7.',)), ('las consultorías del Componente II', ('2.',))]
UEP_CODE = '3.1.1-06'
obras_acts = [r for r in ACTS if r['owner'] == 'Contratista de obra' and float(r['budget']) > 0]
assert all(date.fromisoformat(r['finish']) <= month_end(H07) for r in obras_acts), 'el texto supone que las obras terminan con H07'

# Pico mensual: aporte de cada grupo en ese mes
pm = months[peak]
peak_parts = sorted(((n, sum(month_value(r, pm) for r in ACTS if r['package'].startswith(pre) and r['code'] != UEP_CODE)) for n, pre in GRP), key=lambda x: -x[1])
peak_txt = jy(f'{n} (US${v:.1f} millones)' for n, v in peak_parts if v >= 0.05)
contratos = {c['nombre']: c for c in RES['contratos']}
obra_k = sorted((c for c in RES['contratos'] if c['nombre'].startswith('Obra')), key=lambda c: c['firma'])
first = obra_k[0]
cum_first = float(next(r['acumulado_linea_base_musd'] for r in mensual if r['mes'] == first['firma'][:7]))
start_txt = jy(f'{c["nombre"][5:]} ({dmy(c["inicio"])})' for c in sorted(RES['contratos'], key=lambda c: c['inicio']) if c['nombre'].startswith('Obra'))
# Después del 90%: lo que queda por ejecutar al cierre de ese mes
d90 = month_end(Q90)
done_h = [h for h in ('H05', 'H06', 'H08') if date.fromisoformat(hitos[h]['date']) <= d90]
rem90 = sorted(((n, sum(remaining(r, d90) for r in ACTS if r['package'].startswith(pre) and r['code'] != UEP_CODE)) for n, pre in GRP[:5]), key=lambda x: -x[1])
rem90_txt = jy(f'{n} (US${v:.1f} millones)' for n, v in rem90 if v >= 0.05)
cut7 = max((r for r in mensual if r['mes'] <= H07), key=lambda r: r['mes'])
tail = {k: float(next(r for r in mensual if r['mes'] == months[-1])[k]) - float(cut7[k]) for k in ('c1_acumulado_musd', 'c2_acumulado_musd', 'c3_acumulado_musd')}
tail_txt = jy(f'US${tail[k]:.1f} millones {lab}' for k, lab in (('c1_acumulado_musd', 'de la supervisión y la recepción de las obras'),
                                                           ('c2_acumulado_musd', 'de las consultorías del Componente II'),
                                                           ('c3_acumulado_musd', 'de la UEP, las auditorías y las evaluaciones')) if tail[k] >= 0.05)
BAC_TAIL = BAC - float(cut7['acumulado_linea_base_musd'])
P2 = f'''<h1>Curva S del programa ES-L1173: distribución mensual del valor planificado</h1>
<p>Valor planificado de cada mes y acumulado, en millones de US$. El costo de cada actividad se prorratea en los días laborables en que el cronograma la programa; la suma de cada mes se acumula hasta el final del programa.</p>
<table>{head}{"".join(body)}</table>
<h2>Interpretación</h2>
<ul>
<li>Arranque ({mlong(START.isoformat())} a {mlong(first['firma'][:7])}): hasta la firma del primer contrato de obra ({first['nombre'][5:]}, {dmy(first['firma'])}) el valor planificado acumulado es de US${cum_first:.1f} millones ({cum_first / BAC:.1%} del total) y es solo de la UEP: la revisión de diseños y la contratación no tienen costo propio.</li>
<li>Aceleración ({mlong(mnext(first['firma'][:7]))} a {mlong(pm)}): el valor mensual sube de US${pv[months.index(mnext(first['firma'][:7]))]:.1f} millones a US${pv[peak]:.1f} millones, el máximo de todo el programa, en {mlabel(pm)}. Las obras se encadenan por contrato, con inicio de obra en {start_txt}; los cuatro contratos de obra y de supervisión están firmados en H03 ({mlong(H03)}). En este tramo se alcanza {qtxt_acc}. El pico de {mlabel(pm)} reúne {peak_txt}.</li>
<li>Desaceleración ({mlong(mnext(pm))} a {mlong(FINISH.isoformat())}): el valor mensual baja desde el pico; se alcanza {qtxt_dec}. Al cierre de {mlong(Q90)} ya concluyeron {jy(f'{hname(h)} (H{h[1:]}, {mlabel(hitos[h]["date"][:7])})' for h in sorted(done_h, key=lambda h: hitos[h]['date']))}; quedan por ejecutar {rem90_txt}. La terminal concluye en {mlong(H07)} (H07) y después de esa fecha restan US${BAC_TAIL:.1f} millones ({BAC_TAIL / BAC:.1%} de la línea base): {tail_txt}.</li>
<li>La línea base de costos (US${BAC:.1f} millones) es la estimación PERT de los paquetes de trabajo asignada a sus actividades (US${EST:.1f} millones) más la reserva de contingencia (US${CONT:.1f} millones, percentil 80), asignada a cada paquete según su incertidumbre. La distancia entre las dos curvas es esa reserva, que se consume solo si se materializan los riesgos de costo.</li>
<li>Una vez aprobada, esta curva se fija como línea base: en cada fecha de corte se le superpone el costo real acumulado del trabajo realizado y la diferencia entre ambas curvas indica si el desempeño requiere ajustes (PMBOK 6, cap. 7; dominio de medición de PMBOK 7).</li>
</ul>'''

GROUPS = [('Terminal', 'Lineal en cada actividad del contratista, con pesos por recurso (puentes y sistemas a su fabricación e instalación)'),
          ('Lado aire', 'Lineal en cada actividad del contratista'),
          ('Estacionamiento', 'Lineal en cada actividad del contratista'),
          ('SSEI', 'Lineal en cada actividad del contratista'),
          ('Supervisión', 'Lineal en cada contrato de supervisión (honorarios por tiempo), repartida entre los cuatro contratos según su obra'),
          ('Gestión socioambiental', 'Lineal dentro de los contratos de supervisión (seguimiento del PGAS)'),
          ('Componente II', 'Lineal en las actividades de la firma consultora de cada producto'),
          ('Componente III', 'UEP: costo indirecto mensual por puesto desde su contratación; auditorías y evaluaciones lineales en cada actividad')]
G = COST['por_grupo']
crow = []
for g, perfil in GROUPS:
    v = G[g]
    crow.append(f'<tr><td class="k">{g}</td><td class="n">{money(v["E"] / 1e6)}</td><td class="n">{money(v["reserva"] / 1e6)}</td>'
                f'<td class="n">{money((v["E"] + v["reserva"]) / 1e6)}</td><td class="n">{(v["E"] + v["reserva"]) / 1e6 / BAC:.1%}</td><td>{perfil}</td></tr>')
crow.append(f'<tr class="t"><td>Línea base (BAC)</td><td class="n">{money(EST)}</td><td class="n">{money(CONT)}</td><td class="n">{money(BAC)}</td><td class="n">100.0%</td><td></td></tr>')
obras = sum(G[g]['E'] + G[g]['reserva'] for g in ('Terminal', 'Lado aire', 'Estacionamiento', 'SSEI')) / 1e6
SD = RES['sensibilidad_dhss']
NACT = sum(1 for r in ACTS if float(r['budget']) > 0)
uep_total = float(next(r['budget'] for r in ACTS if r['code'] == UEP_CODE))
P3 = f'''<h1>Curva S del programa ES-L1173: composición y fundamento de la forma</h1>
<p>La curva suma, mes a mes, el costo de las {NACT} actividades que lo llevan, como la línea base de costos (PMI, 2017, sección 7.3): EDT, paquetes, actividades y costo de las actividades. El costo de cada paquete sale de la estimación de costos del programa (paramétrica, análoga, por tarifas, ascendente y de tres puntos PERT) y se asigna a las actividades de quien cobra el contrato (contratista, firma de supervisión, firma consultora o auditor); las actividades de la UEP, CEPA, el BID y la AAC no tienen costo propio, salvo el costo indirecto de la UEP (US${uep_total:.1f} millones con su contingencia), que lleva la actividad de nivel de esfuerzo 3.1.1-06.</p>
<table><tr><th style="width:15%">Grupo</th><th style="width:10%;text-align:right">Estimación PERT (US$ M)</th><th style="width:10%;text-align:right">Reserva de contingencia (US$ M)</th><th style="width:10%;text-align:right">Línea base (US$ M)</th><th style="width:7%;text-align:right">Peso</th><th style="width:48%">Distribución en el tiempo</th></tr>{"".join(crow)}</table>
<h2>Por qué la curva tiene esta forma</h2>
<ul>
<li>Las obras físicas pesan el {obras / BAC:.0%} de la línea base, así que la forma de la S la dan las obras: casi no hay gasto hasta la firma del primer contrato de obra y la pendiente máxima coincide con la construcción simultánea de la terminal, el estacionamiento y las plataformas.</li>
<li>Es un valor planificado: cada actividad se prorratea de forma lineal en su duración, también las fabricaciones, las consultorías, las auditorías y las evaluaciones. La S no se impone con una función, sale de la secuencia del cronograma (pocas actividades al inicio, muchas en paralelo en 2027 y 2028, pocas al cierre). Con la curva DHSS del Reino Unido para contratos grandes aplicada a cada contrato de obra en todo su plazo (Hudson, 1978; C = 0.063, K = 3.344), la curva acumulada cambia como máximo US${abs(RES['sensibilidad_dhss_dif_max_musd']):.1f} millones y el 25%, 50%, 75% y 90% se alcanzan en {jy(mlabel(v['dhss']) for v in SD.values())}.</li>
<li>Dentro de cada paquete, el costo de cada elemento se reparte entre las actividades según el recurso. Movilización y pruebas llevan 2% (las pruebas de 1.2.4-05 del mobiliario y de los sistemas de la terminal llevan 3%) y el informe final de la supervisión 4%; los puentes de abordaje llevan 85% a su fabricación y entrega, 11% a su instalación y 4% a los planos de taller y las pruebas; los sistemas de la terminal van a su instalación; la supervisión y el seguimiento del PGAS, al período de supervisión de cada obra. El resto de cada elemento se reparte entre sus actividades de construcción en proporción a su duración, porque el listado no da cantidades de obra comparables entre actividades distintas.</li>
<li>La UEP es un costo indirecto: su actividad sigue la incorporación de cada puesto (siete consultores clave desde abril y mayo de 2026 y la plantilla ampliada del Plan de Adquisiciones desde sus firmas), en lugar de un prorrateo lineal. Por eso el valor planificado a la fecha a reportar (US${PV_CORTE:.2f} millones) se acerca al costo real estimado de los contratos en ejecución (US${AC_CORTE:.2f} millones), que no es un desembolso del BID.</li>
<li>El diseño final de la fachada sur de la terminal no tiene costo propio: 1.1.1-06 (del contratista) forma parte del contrato de obra, que es de diseño y construcción, y su pago está dentro del precio de la obra (T1); 1.1.1-07 (de la supervisión) forma parte del contrato de supervisión (V1). Que lo diseñe el contratista es una inferencia (S-I.8 del listado de actividades).</li>
<li>La curva no incluye anticipos, retenciones ni el desfase de pago de los certificados, ni pagos contra entrega: esa lógica de pagos solo está en los requisitos de financiamiento de la página siguiente, que los comparan con los desembolsos previstos del préstamo.</li>
<li>Presupuesto frente al préstamo: con la reserva de gestión (US${GEST:.1f} millones, 5% de la línea base) el presupuesto del proyecto suma US${PRES:.1f} millones, US${LOAN - PRES:.1f} millones por debajo del préstamo de US${LOAN:.0f} millones. La diferencia viene sobre todo del estacionamiento, que el estudio del préstamo extrapoló de un diseño de 700 plazas (US$64.2 millones, monto que conserva el Plan de Adquisiciones de 2026), y de una terminal estimada con obras de CEPA en el mismo aeropuerto; el escalamiento de precios hasta los años de ejecución, que el estudio del préstamo no incluye, compensa una parte.</li>
</ul>'''

# ---------- página 4: requisitos de financiamiento frente a los desembolsos del préstamo ----------
frow = []
for r in FIN:
    if float(r['desembolso_pep_musd']) == 0 and float(r['requisito_con_anticipo_musd']) == 0:
        continue
    frow.append(f'<tr><td class="k">{r["semestre"]}</td><td class="n">{money(float(r["desembolso_pep_musd"]))}</td><td class="n c">{money(float(r["desembolso_pep_acum_musd"]))}</td>'
                f'<td class="n">{money(float(r["requisito_musd"]))}</td><td class="n c">{money(float(r["requisito_acum_musd"]))}</td>'
                f'<td class="n">{money(float(r["requisito_con_anticipo_musd"]))}</td><td class="n c">{money(float(r["requisito_con_anticipo_acum_musd"]))}</td>'
                f'<td class="n">{money(float(r["diferencia_con_anticipo_acum_musd"]))}</td></tr>')
F = {r['semestre']: r for r in FIN}
EV = {e['tipo']: e for e in RES['evaluaciones']}
MT, FL = EV['Medio término'], EV['Final']
fv = lambda k, c: float(F[k][c])
pct = RES['anticipo_pct']
assert all(float(r['diferencia_con_anticipo_acum_musd']) > 0 for r in FIN if float(r['desembolso_pep_musd']) > 0), 'el PEP acumulado debe ir por delante del requisito'
yr_pep = {y: sum(float(r['desembolso_pep_musd']) for r in FIN if r['semestre'].startswith(str(y))) for y in range(2026, 2031)}
yr_req = {y: sum(float(r['requisito_con_anticipo_musd']) for r in FIN if r['semestre'].startswith(str(y))) for y in range(2026, 2031)}
up = [y for y in yr_pep if yr_req[y] > yr_pep[y] + 1.0]
down = [y for y in yr_pep if yr_req[y] < yr_pep[y] - 1.0]


def sem_reach(col: str, p: float) -> int:
    return next(i for i, r in enumerate(FIN) if float(r[col]) >= LOAN * p - 1e-6)


lag = {p: sem_reach('requisito_con_anticipo_acum_musd', p) - sem_reach('desembolso_pep_acum_musd', p) for p in (.25, .5, .75)}
lag_txt = f'{min(lag.values())} a {max(lag.values())}' if min(lag.values()) != max(lag.values()) else f'{min(lag.values())}'
reach_txt = lambda col: jy(f'al {int(p * 100)}% en {FIN[sem_reach(col, p)]["semestre"]}' for p in (.25, .5, .75))
ad_txt = 'obra y supervisión: ' + jy(f'{n} {pct["obra"][g]:.0%} y {pct["sup"][g]:.0%}' for g, n in (('T', 'terminal'), ('E', 'estacionamiento'), ('P', 'plataformas y Foxtrot'), ('S', 'SSEI')))
d_ult = date.fromisoformat(RES['ultimo_desembolso'])
late = [(r['semestre'], float(r['requisito_con_anticipo_musd'])) for r in FIN if date(int(r['semestre'][:4]), 1 if r['semestre'][-1] == '1' else 7, 1) > d_ult and float(r['requisito_con_anticipo_musd']) > 0.005]
LATE_TXT = ('El requisito de ' + jy(f'US${v:.2f} millones en {sem}' for sem, v in late) + f' cae después del último desembolso ({dmy(d_ult)}): se cubre con el último anticipo de fondos o con el saldo de la cuenta especial.') if late else ''
P4 = f'''<h1>Requisitos de financiamiento frente a los desembolsos del préstamo</h1>
<p>Millones de US$ por semestre. Desembolsos del PEP: pagos estimados del BID en el Plan de Ejecución de noviembre de 2025 (BID, 2025e, hoja Payments Flow), que reparte los US${LOAN:.0f} millones del préstamo en ocho semestres desde enero de 2026. Requisito: línea base más reserva de gestión (PMI, 2017, sección 7.3), esta última en proporción al valor planificado de cada semestre. Requisito con anticipo: el mismo valor, más un pago a cada contrato en el semestre de su firma que se amortiza descontando el mismo porcentaje de cada avance. Los porcentajes salen de las hojas Payments y Payments Flow Output del PEP ({ad_txt}) y se aplican a la base sin contingencia, porque la contingencia solo se gasta si ocurren los riesgos. Que ese pago sea un anticipo es una inferencia: los avisos de adquisiciones no lo mencionan. Las diferencias son acumuladas: PEP menos requisito con anticipo.</p>
<table><tr><th style="width:9%">Semestre</th><th style="width:11%;text-align:right">Desembolso PEP</th><th style="width:11%;text-align:right">Acumulado PEP</th><th style="width:11%;text-align:right">Requisito</th><th style="width:11%;text-align:right">Acumulado</th><th style="width:12%;text-align:right">Requisito con anticipo</th><th style="width:11%;text-align:right">Acumulado</th><th style="width:12%;text-align:right">Diferencia acumulada con anticipo</th></tr>{"".join(frow)}</table>
<h2>Lectura</h2>
<ul>
<li>El monto del préstamo alcanza: el programa necesita US${BAC:.1f} millones de línea base (US${PRES:.1f} millones con la reserva de gestión) frente a US${LOAN:.0f} millones. La diferencia con el PEP es de calendario, no de monto.</li>
<li>El PEP preveía desembolsar US${fv('2026-S2', 'desembolso_pep_acum_musd'):.1f} millones hasta diciembre de 2026, con las licitaciones y las firmas en 2026. Como el primer contrato de obra se firma el {dmy(first['firma'])}, el programa solo necesita US${fv('2026-S2', 'requisito_con_anticipo_acum_musd'):.1f} millones en 2026; los US$29.7 millones que la reforma a la Ley de Presupuesto 2026 asignó al estacionamiento no se ejecutarán ese año y deben pasar al presupuesto de 2027.</li>
<li>Es una reprogramación, no una falta de fondos: el PEP acumulado va por delante del requisito con anticipo en todos los semestres, entre US${min(float(r['diferencia_con_anticipo_acum_musd']) for r in FIN if float(r['desembolso_pep_musd']) > 0):.1f} y US${max(float(r['diferencia_con_anticipo_acum_musd']) for r in FIN):.1f} millones. El PEP llega {reach_txt('desembolso_pep_acum_musd')} del préstamo, y el requisito con anticipo {reach_txt('requisito_con_anticipo_acum_musd')}: un desfase de {lag_txt} semestres. Por año, el PEP prevé US${yr_pep[2027]:.1f} millones en 2027 y US${yr_pep[2028]:.1f} millones en 2028, frente a los US${yr_req[2027]:.1f} y US${yr_req[2028]:.1f} millones que requiere el programa; en {jy(str(y) for y in down)} ocurre lo contrario. Hay que reprogramar el PEP y los POA 2027 y 2028 y las asignaciones de las leyes de presupuesto de {jy(str(y) for y in up)}, y dimensionar los anticipos de fondos que la UEP solicita al BID.</li>
<li>El último desembolso se tramita el {dmy(d_ult)} (3.5.4-02), dentro del plazo original de desembolsos, que vence el {dmy(RES['fin_plazo_desembolsos'])}: cinco años desde la vigencia, supuesta el {dmy(RES['vigencia'])} (ratificación D.L. 505; falta la fecha de publicación, cláusula 6.01).</li>
<li>Evaluación de medio término (cláusula 5.03): se presenta a más tardar 60 días después de que se desembolse el 50% de los recursos o de que transcurra el 50% del tiempo de ejecución planificado, lo que ocurra primero. El 50% del tiempo (del {dmy(START)} al {dmy(FINISH)}) llega el {dmy(MT['hito_50_tiempo'])} y el límite es el {dmy(MT['limite_tiempo'])}; con los requisitos de financiamiento de la tabla (con anticipo y con reserva de gestión), el 50% del préstamo se desembolsa en {mlong(MT['hito_50_requisito'][:7])} y el límite es el {dmy(MT['limite_requisito'])}. El informe está programado para el {dmy(MT['informe'])}: {MT['margen_tiempo_dl']} días laborables antes del límite por tiempo y {MT['margen_dl']} antes del límite por desembolso, que es el primero. Riesgo: un desembolso no es un gasto, y las Normas Generales (art. 4.07) permiten anticipos de fondos de hasta {RES['lead_anticipo_meses']} meses de liquidez. Si los desembolsos siguieran el PEP, el 50% llegaría el {dmy(MT['hito_50_pep'])} y el plazo vencería el {dmy(MT['limite_pep'])}; con un anticipo de {RES['lead_anticipo_meses']} meses, el 50% se desembolsaría en {mlong(MT['hito_50_acelerado'][:7])} y el plazo vencería el {dmy(MT['limite_acelerado'])}, antes de la firma del contrato de la evaluación ({dmy(MT['firma'])}). La UEP debe pactar con el BID el monto de los anticipos o adelantar la contratación de la evaluación.</li>
<li>{LATE_TXT}</li>
<li>Evaluación final: la línea base no llega al 95% del préstamo, así que vence 90 días después del fin del plazo original de desembolsos ({dmy(FL['limite'])}); su informe está programado para el {dmy(FL['informe'])}.</li>
</ul>'''

mediabox = fitz.paper_rect('a4-l')
where = mediabox + (30, 28, -30, -34)
buf = io.BytesIO()
writer = fitz.DocumentWriter(buf)
heights = []
for html in (P1, P2, P3, P4):
    story = fitz.Story(html=f'<html><head><style>{CSS}</style></head><body>{html}</body></html>')
    dev = writer.begin_page(mediabox)
    more, filled = story.place(where)
    assert not more, 'el contenido no cabe en la página'
    story.draw(dev)
    writer.end_page()
    heights.append(fitz.Rect(filled).y1)
writer.close()

doc = fitz.open('pdf', buf.getvalue())
p1 = doc[0]
top = heights[0] + 8
legend_y = mediabox.height - 50
src = fitz.open('pdf', make_chart(mediabox.width - 60, legend_y - 4 - top))
p1.show_pdf_page(fitz.Rect(30, top, mediabox.width - 30, legend_y - 4), src, 0)
p1.insert_htmlbox(fitz.Rect(30, legend_y, mediabox.width - 30, mediabox.height - 26),
                  f'<p style="font-family:sans-serif;font-size:7pt;color:{MUTED};margin:0">Hitos (líneas moradas): H03 contratos de obra y supervisión firmados ({mlabel(hitos["H03"]["date"][:7])}); H05 SSEI reubicado ({mlabel(hitos["H05"]["date"][:7])}); H07 terminal ampliada concluida ({mlabel(hitos["H07"]["date"][:7])}); H09 obras recibidas ({mlabel(hitos["H09"]["date"][:7])}). Puntos azules: mes en que la línea base alcanza el 25%, 50%, 75% y 90% de su total. Valores al cierre de cada mes.</p>')
for k, page in enumerate(doc, start=1):
    page.insert_text((mediabox.width - 90, mediabox.height - 18), f'Página {k} de {len(doc)}', fontsize=7, color=(0.4, 0.42, 0.45))
    page.insert_text((30, mediabox.height - 18), 'ES-L1173 | Curva S del programa', fontsize=7, color=(0.4, 0.42, 0.45))
out = HERE / 'curva_s_ES-L1173.pdf'
doc.save(str(out), garbage=3, deflate=True)
print(f'{out.name}: {len(doc)} páginas; 25/50/75/90% en {[mlabel(months[i]) for i in quart.values()]}; pico {pv[peak]:.2f} en {mlabel(months[peak])}')

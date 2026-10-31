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
CORTE = date(2026, 10, 31)  # fecha a reportar
# Requisitos de financiamiento: escalones anuales (uno por POA) que cubren el valor planificado del año más la reserva de
# gestión en proporción, disponibles desde el inicio de cada año (PMBOK 6, 7.3.3.2; clase 6, línea base y financiamiento).
FUND = []
_acc = 0.0
for a in anual:
    _acc += float(a['gasto_anual_musd']) * (1 + GEST / BAC)
    FUND.append((max(date(int(a['anio']), 1, 1), START), _acc))
hitos = {h['id']: h for h in csv.DictReader((HERE / 'hitos.csv').open(encoding='utf-8-sig'))}


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
AC_TXT = 'Sin desembolsos publicados (UEP en funciones desde abr-2026)'
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
    fx = [d for d, _ in FUND] + [FINISH]
    fy = [v for _, v in FUND] + [FUND[-1][1]]
    ax.step(fx, fy, where='post', color='#0d9488', lw=1.1, alpha=0.8, zorder=2, label='Requisitos de financiamiento (anuales, con reserva de gestión)')
    ax.axvline(CORTE, color=INK, lw=0.8, ls=(0, (1, 1.5)), zorder=1)
    ax.text(CORTE + timedelta(days=8), 60, 'Fecha a reportar\n31-10-2026', fontsize=7, color=INK, va='bottom')
    ax.text(FINISH + timedelta(days=12), ys[-1] + 2, f'US${ys[-1]:.1f} M', color=INK, fontsize=7.5, fontweight='bold', va='bottom')
    ax.text(FINISH + timedelta(days=12), ys_sc[-1] - 4, f'US${ys_sc[-1]:.1f} M', color=MUTED, fontsize=7.5, va='center')
    for q, i in quart.items():
        ax.plot(ends[i], cum[i], 'o', ms=5.5, color=BLUE, mec='white', mew=1.3, zorder=4)
        ax.annotate(f'{q}%  {mlabel(months[i])}', (ends[i], cum[i]), xytext=(-8, 0), textcoords='offset points', ha='right', va='center', fontsize=7.5, color=INK)
    ax.set_ylim(0, 212)
    ax.set_ylabel('Valor planificado acumulado (US$ M)')
    ax.legend(loc='upper left', bbox_to_anchor=(0.0, 0.72), frameon=False, fontsize=7.8, handlelength=2.6)

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
qtxt = ', '.join(f'el {q}% en {mlabel(months[i])}' for q, i in quart.items())
P2 = f'''<h1>Curva S del programa ES-L1173: distribución mensual del valor planificado</h1>
<p>Valor planificado de cada mes y acumulado, en millones de US$. El costo de cada paquete de trabajo de la EDT se distribuye en los meses en que el cronograma lo programa; la suma de cada mes se acumula hasta el final del programa.</p>
<table>{head}{"".join(body)}</table>
<h2>Interpretación</h2>
<ul>
<li>Arranque lento ({mlong(START.isoformat())} a {mlong(H03)}): el gasto acumulado llega a US${data[H03][1]:.1f} millones ({data[H03][1] / BAC:.1%} del total) porque corresponde a la conformación de la UEP, la revisión de diseños y la contratación. El tramo inclinado de la S empieza con la firma de los contratos de obra y supervisión (H03, {mlong(H03)}).</li>
<li>Aceleración ({mlong(mnext(H03))} a {mlong(Q90)}): las obras concentran el gasto; se alcanza {qtxt}. El mayor valor mensual es de US${pv[peak]:.1f} millones en {mlabel(months[peak])}, cuando coinciden la terminal, el estacionamiento y las plataformas; es el período de mayor exigencia de liquidez y de supervisión.</li>
<li>Desaceleración ({mlong(mnext(Q90))} a {mlong(FINISH.isoformat())}): con el SSEI (H05), el estacionamiento (H08) y la plataforma remota (H06) ya concluidos, termina la terminal (H07); después de {mlong(H07)} restan US${BAC - data[H07][1]:.1f} millones ({(BAC - data[H07][1]) / BAC:.1%} de la línea base) para la señalización de plataformas, supervisión, recepción de obras (H09) y cierre.</li>
<li>La línea base de costos (US${BAC:.1f} millones) es la estimación PERT de los paquetes de trabajo (US${EST:.1f} millones) más la reserva de contingencia (US${CONT:.1f} millones, percentil 80), asignada a cada paquete según su incertidumbre. La distancia entre las dos curvas es esa reserva, que se consume solo si se materializan los riesgos de costo.</li>
<li>Una vez aprobada, esta curva se fija como línea base: en cada fecha de corte se le superpone el costo real acumulado del trabajo realizado y la diferencia entre ambas curvas indica si el desempeño requiere ajustes (PMBOK 6, cap. 7; dominio de medición de PMBOK 7).</li>
</ul>'''

GROUPS = [('Terminal', 'Obra civil 3t²−2t³; puentes, sistemas y mobiliario: 70 % a la entrega y 30 % de instalación'),
          ('Lado aire', 'Obra civil 3t²−2t³; balizamiento: 70 % a la entrega y 30 % de instalación'),
          ('Estacionamiento', 'Obra civil 3t²−2t³; accesos y sistema solar: 70 % a la entrega y 30 % de instalación'),
          ('SSEI', 'Obra civil 3t²−2t³; puesta en marcha: 70 % a la entrega y 30 % de instalación'),
          ('Supervisión', 'Lineal durante las obras (honorarios por tiempo trabajado)'),
          ('Gestión socioambiental', 'Lineal durante las obras'),
          ('Componente II', 'Escalones contra productos: 20 % al 25 % del plazo, 40 % al 65 % y 40 % al final'),
          ('Componente III', 'UEP lineal en todo el programa; auditoría en cada 30 de abril y estados financieros finales en el cierre; evaluaciones al entregar cada informe')]
G = COST['por_grupo']
crow = []
for g, perfil in GROUPS:
    v = G[g]
    crow.append(f'<tr><td class="k">{g}</td><td class="n">{money(v["E"] / 1e6)}</td><td class="n">{money(v["reserva"] / 1e6)}</td>'
                f'<td class="n">{money((v["E"] + v["reserva"]) / 1e6)}</td><td class="n">{(v["E"] + v["reserva"]) / 1e6 / BAC:.1%}</td><td>{perfil}</td></tr>')
crow.append(f'<tr class="t"><td>Línea base (BAC)</td><td class="n">{money(EST)}</td><td class="n">{money(CONT)}</td><td class="n">{money(BAC)}</td><td class="n">100.0%</td><td></td></tr>')
obras = sum(G[g]['E'] + G[g]['reserva'] for g in ('Terminal', 'Lado aire', 'Estacionamiento', 'SSEI')) / 1e6
SD = RES['sensibilidad_dhss']
P3 = f'''<h1>Curva S del programa ES-L1173: composición y fundamento de la forma</h1>
<p>La curva suma, mes a mes, el costo de los 54 paquetes de trabajo distribuido según el tipo de trabajo. El costo de cada paquete sale de la estimación de costos del programa (paramétrica, análoga, por tarifas, ascendente y de tres puntos PERT); el detalle está en el documento de estimación de costos.</p>
<table><tr><th style="width:15%">Grupo</th><th style="width:10%;text-align:right">Estimación PERT (US$ M)</th><th style="width:10%;text-align:right">Reserva de contingencia (US$ M)</th><th style="width:10%;text-align:right">Línea base (US$ M)</th><th style="width:7%;text-align:right">Peso</th><th style="width:48%">Perfil de distribución en el tiempo</th></tr>{"".join(crow)}</table>
<h2>Por qué la curva tiene esta forma</h2>
<ul>
<li>Las obras físicas pesan el {obras / BAC:.0%} de la línea base, así que la forma de la S la dan las obras: casi no hay gasto hasta la firma de los contratos (H03) y la pendiente máxima coincide con la construcción simultánea de la terminal, el estacionamiento y las plataformas.</li>
<li>Obra civil: 3t²−2t³ sobre la duración de cada paquete, una aproximación simétrica al modelo logit de Kenley y Wilson (1986) con α = 0 y β ≈ 1.5. Ejecuta el 15.6% del valor en el primer cuarto del plazo y el 15.6% en el último, dentro del rango de los modelos publicados (12% a 26% en el primer cuarto; Skitmore, 1992; Kenley, 2003; RICS GN 79/2011). Con la curva DHSS del Reino Unido para contratos grandes (Hudson, 1978; C = 0.063, K = 3.344), la curva acumulada cambia como máximo US${abs(RES['sensibilidad_dhss_dif_max_musd']):.1f} millones y el 25%, 50%, 75% y 90% se alcanzan en {", ".join(mlabel(v['dhss']) for v in SD.values())}: la forma elegida no condiciona la lectura de la curva.</li>
<li>Equipos (puentes de abordaje, balizamiento, sistema solar, accesos y puesta en marcha del SSEI): el suministro se reconoce con las entregas, escalonadas entre el 30% y el 60% del plazo del paquete, y la instalación se distribuye en todo el plazo, como separan los términos de pago del documento estándar del Banco Mundial para planta (2015). La partición 70/30 es un supuesto.</li>
<li>Supervisión, UEP y gestión socioambiental: gasto lineal, porque son contratos por tiempo trabajado que se pagan por honorario mensual (GN-2350-15, párr. 4.2 y 4.9). Consultorías del Componente II: escalones al entregar cada producto (GN-2350-15, párr. 4.1); los porcentajes por producto se negocian en cada contrato y aquí son un supuesto. Auditoría: un escalón por ejercicio, al vencer el plazo de los estados financieros auditados (120 días después del cierre del ejercicio, Anexo III de la Propuesta de Préstamo).</li>
<li>La curva representa valor planificado, no flujo de caja: no incluye anticipos, retenciones ni el desfase de pago de los certificados, que son condiciones de pago de los contratos (FIDIC 2017, cláusula 14) y no trabajo ejecutado.</li>
<li>Presupuesto frente al préstamo: con la reserva de gestión (US${GEST:.1f} millones, 5% de la línea base) el presupuesto del proyecto suma US${PRES:.1f} millones, US${LOAN - PRES:.1f} millones por debajo del préstamo de US${LOAN:.0f} millones. La diferencia viene sobre todo del estacionamiento, que el estudio del préstamo extrapoló de un diseño de 700 plazas (US$64.2 millones, monto que conserva el Plan de Adquisiciones de 2026), y de una terminal estimada con obras de CEPA en el mismo aeropuerto; el escalamiento de precios hasta los años de ejecución, que el estudio del préstamo no incluye, compensa una parte.</li>
</ul>'''

mediabox = fitz.paper_rect('a4-l')
where = mediabox + (30, 28, -30, -34)
buf = io.BytesIO()
writer = fitz.DocumentWriter(buf)
heights = []
for html in (P1, P2, P3):
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

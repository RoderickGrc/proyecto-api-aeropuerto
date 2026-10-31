#!/usr/bin/env python3
"""Genera el cronograma por actividades, los hitos, la ruta critica y la curva S del ES-L1173.

Entradas (en esta carpeta): actividades.csv y dependencias.csv (listado de actividades con estimacion PERT, ver
docs/listado-actividades.md), hitos_programa.py y estimacion_costos.py.
Salidas: cronograma_actividades.csv, cronograma_paquetes.csv, hitos.csv, curva_s_mensual.csv, curva_s_anual.csv,
curva_s.png, cronograma_ES-L1173.xml, resumen.json. Sin red, sin dependencias salvo matplotlib (opcional).

1. CPM por actividades con la duracion estimada De = (O + 4M + P) / 6 redondeada, relaciones FI, II, FF e IF con desfase,
   restricciones "no comenzar antes de" y actividades de nivel de esfuerzo (empiezan con sus predecesoras y terminan con
   la ultima actividad de termina_con, sin empujarla).
2. Los paquetes de trabajo de la EDT son filas resumen: empiezan con su primera actividad y terminan con la ultima.
3. Costos: estimacion propia por paquete (estimacion_costos.py), distribuida sobre las fechas del paquete. La curva S es
   la linea base de costos: estimacion PERT mas la reserva de contingencia (P80) asignada a cada paquete. La reserva de
   gestion y el monto del prestamo (US$195M) se muestran como referencia.
Calendario lunes a viernes, 8 h/dia, sin feriados.
"""
from __future__ import annotations
import csv, json, functools
from datetime import date, timedelta
from pathlib import Path
from xml.sax.saxutils import escape

import sys
sys.dont_write_bytecode = True  # no dejar __pycache__ en el repositorio
import estimacion_costos  # noqa: E402

OUT = Path(__file__).resolve().parent
PROJECT_START = date(2026, 2, 2)
LOAN_MUSD = 195.0  # monto autorizado del prestamo, solo como referencia

# Paquetes de trabajo de la EDT: codigo|nombre (duraciones y precedencias en actividades.csv y dependencias.csv)
PAQUETES = '''
1.1.1|Diseños de la terminal revisados y aprobados
1.1.2|Diseños de plataformas y calle Foxtrot revisados y aprobados
1.1.3|Diseños del estacionamiento y del sistema solar revisados y aprobados
1.1.4|Diseños del SSEI revisados y aprobados
1.2.1|Estructura y envolvente de la terminal construidas
1.2.2|Salas de espera, circulación y áreas de apoyo terminadas
1.2.3|Instalaciones eléctricas, hidráulicas, climatización y contra incendio recibidas
1.2.4|Puentes de abordaje, mobiliario y equipos instalados
1.2.5|Accesibilidad universal, movilidad del cuidado y criterios de sostenibilidad incorporados
1.3.1|Plataforma de posiciones de contacto construida
1.3.2|Plataforma de posiciones remotas construida
1.3.3|Señalización, luces y torres de iluminación de plataforma instaladas
1.4.1|Pavimento y hombros de la calle Foxtrot construidos
1.4.2|Señalización y balizamiento de la calle Foxtrot instalados
1.5.1|Edificio de estacionamiento construido
1.5.2|Sistemas de acceso, tráfico y áreas de alquiler instalados
1.5.3|Sistema de generación solar instalado
1.6.1|Edificio del SSEI y vías de acceso construidos
1.6.2|SSEI en funcionamiento en la nueva ubicación
1.7.1|Supervisión de la terminal y del estacionamiento ejecutada
1.7.2|Supervisión de plataformas, calle Foxtrot y SSEI ejecutada
1.7.3|PGAS de construcción implementado
1.7.4|Planos de obra ejecutada y actas de recepción aprobados
2.1|Plan estratégico del sistema aeronáutico aprobado
2.2.1|Plan Maestro Aeroportuario actualizado y aprobado
2.2.2|Funcionarios capacitados en planificación, gestión y operación
2.3.1|Estrategia BIM aprobada
2.3.2|Personal de ingeniería capacitado en BIM
2.4|Estudio de conectividad terrestre entregado
2.5|Estudio de diversificación de destinos entregado
2.6.1|Auditoría para la certificación EDGE realizada
2.6.2|Personal capacitado en certificación EDGE
2.7|Estudio de separación de flujos entregado
2.8|Estudio de movilidad interna entregado
2.9|Programa de igualdad e inclusión ejecutado
3.1.1|Unidad ejecutora conformada y en funciones
3.1.2|Reglamento operativo vigente
3.1.3|Convenio de transferencia de recursos vigente
3.1.4|Cuenta especial aperturada
3.2.1|Plan de ejecución plurianual aprobado
3.2.2|Planes operativos anuales aprobados
3.2.3|Plan de adquisiciones aprobado
3.3.1|Sistema de gestión ambiental y social y plan de acción vigentes
3.3.2|Protocolo de seguridad operacional aprobado por la AAC
3.3.3|Mecanismo de quejas y reclamos en operación
3.3.4|Informes de cumplimiento socioambiental presentados
3.4.1|Contratos de obras del Componente I firmados
3.4.2|Contrato de supervisión firmado
3.4.3|Contratos de consultorías del Componente II firmados
3.4.4|Contratos de la unidad ejecutora, evaluación y auditoría firmados
3.5.1|Desembolsos justificados e informes financieros presentados
3.5.2|Auditorías externas emitidas
3.5.3|Evaluaciones de medio término y de cierre realizadas
3.5.4|Informe de terminación y cierre administrativo del programa
'''

# Nodos resumen de la EDT: codigo -> nombre
SUMMARIES = {
    '1': 'Obras y adecuaciones', '1.1': 'Diseños de las obras aprobados', '1.2': 'Terminal de pasajeros ampliada',
    '1.3': 'Plataformas de contacto y remotas', '1.4': 'Calle de rodaje Foxtrot', '1.5': 'Estacionamiento y energía solar',
    '1.6': 'SSEI reubicado y en operación', '1.7': 'Supervisión, PGAS de obra y recepción',
    '2': 'Fortalecimiento institucional', '2.2': 'Plan Maestro actualizado y funcionarios capacitados',
    '2.3': 'Estrategia y capacitación BIM', '2.6': 'Auditoría y capacitación EDGE',
    '3': 'Administración, evaluación y auditorías', '3.1': 'Condiciones de arranque cumplidas',
    '3.2': 'Planes de ejecución aprobados', '3.3': 'Condiciones socioambientales y de seguridad operacional',
    '3.4': 'Contratos del programa firmados', '3.5': 'Control financiero, evaluación y cierre',
}
ROOT_NAME = 'Programa de Modernización del AIES ES-L1173'

from hitos_programa import HITOS  # noqa: E402

pk = {}
for line in PAQUETES.strip().splitlines():
    code, name = line.split('|', 1)
    pk[code] = name
assert len(pk) == 54
acts = list(csv.DictReader((OUT / 'actividades.csv').open(encoding='utf-8-sig')))
deps = list(csv.DictReader((OUT / 'dependencias.csv').open(encoding='utf-8-sig')))
act = {a['codigo']: a for a in acts}
assert {a['paquete'] for a in acts} == set(pk), 'cada paquete debe tener actividades'

# ---- calendario lunes a viernes (indice de dia laborable) ----
def workday(i: int) -> date:
    """Fecha del dia laborable numero i (0 = PROJECT_START)."""
    d, n = PROJECT_START, i
    full, rem = divmod(n, 5)
    d += timedelta(weeks=full)
    while rem:
        d += timedelta(days=1)
        if d.weekday() < 5:
            rem -= 1
    return d

def wd_index(d: date) -> int:
    n, cur = 0, PROJECT_START
    while cur < d:
        cur += timedelta(days=1)
        if cur.weekday() < 5:
            n += 1
    return n

assert PROJECT_START.weekday() == 0

# ---- CPM por actividades ----
LOE = {c for c, a in act.items() if a['tecnica'] == 'Nivel de esfuerzo'}
dur = {c: None if c in LOE else int((int(a['O']) + 4 * int(a['M']) + int(a['P'])) / 6 + 0.5) for c, a in act.items()}
pred = {c: [] for c in act}
succ = {c: [] for c in act}
for d in deps:
    pred[d['sucesora']].append((d['predecesora'], d['tipo'], int(d['desfase'])))
    succ[d['predecesora']].append((d['sucesora'], d['tipo'], int(d['desfase'])))
ends_with = {c: act[c]['termina_con'].split(',') for c in LOE}
snet = {c: wd_index(date.fromisoformat(a['restriccion'][4:])) for c, a in act.items() if a['restriccion']}
ES, EF = {}, {}

def forward(c: str, stack=()) -> None:
    if c in EF:
        return
    assert c not in stack, 'ciclo: ' + ' > '.join(stack + (c,))
    es = ef_min = 0
    for p, t, lag in pred[c]:
        forward(p, stack + (c,))
        if t == 'FI': es = max(es, EF[p] + lag)
        elif t == 'II': es = max(es, ES[p] + lag)
        elif t == 'FF': ef_min = max(ef_min, EF[p] + lag)
        else: ef_min = max(ef_min, ES[p] + lag)
    es = max(es, snet.get(c, 0))
    if c in LOE:
        for t in ends_with[c]:
            forward(t, stack + (c,))
        ES[c], EF[c] = es, max([es + 1, ef_min] + [EF[t] for t in ends_with[c]])
        dur[c] = EF[c] - ES[c]
    else:
        ES[c] = max(es, ef_min - dur[c])
        EF[c] = ES[c] + dur[c]

sys.setrecursionlimit(10000)
for c in act:
    forward(c)
END = max(EF.values())
LS, LF = {}, {}

def backward(c: str) -> None:
    if c in LF:
        return
    lf = END
    for s, t, lag in succ[c]:
        backward(s)
        lf = min(lf, {'FI': LS[s] - lag, 'II': LS[s] - lag + dur[c], 'FF': LF[s] - lag, 'IF': LF[s] - lag + dur[c]}[t])
    LF[c], LS[c] = lf, lf - dur[c]

for c in act:
    backward(c)
akey = lambda c: ([int(x) for x in c.split('-')[0].split('.')], int(c.split('-')[1]))
arows = []
for c in sorted(act, key=akey):
    a = act[c]
    arows.append({'code': c, 'name': a['actividad'], 'package': a['paquete'], 'phase': a['fase'], 'owner': a['responsable'],
                  'dur': dur[c], 'es': ES[c], 'ef': EF[c], 'start': workday(ES[c]), 'finish': workday(EF[c] - 1),
                  'float': LS[c] - ES[c], 'critical': LS[c] == ES[c],
                  'deps': ','.join(p + ('' if t == 'FI' and not lag else f':{t}{lag:+d}') for p, t, lag in pred[c])})
abyid = {r['code']: r for r in arows}
assert all(r['float'] >= 0 for r in arows)
PROJECT_END = workday(END - 1)
assert ES['1.3.2-01'] >= EF['1.6.2-04'], 'el SSEI debe estar operativo antes de la plataforma remota'

# ---- paquetes: filas resumen de sus actividades ----
rows = []
for code, name in pk.items():
    sub = [r for r in arows if r['package'] == code]
    es, ef = min(r['es'] for r in sub), max(r['ef'] for r in sub)
    pdeps = sorted({act[p]['paquete'] for r in sub for p, _, _ in pred[r['code']] if act[p]['paquete'] != code},
                   key=lambda x: [int(y) for y in x.split('.')])
    rows.append({'code': code, 'name': name, 'dur': ef - es, 'deps': ','.join(pdeps), 'es': es, 'ef': ef,
                 'start': workday(es), 'finish': workday(ef - 1), 'float': min(r['float'] for r in sub),
                 'critical': any(r['critical'] for r in sub), 'activities': len(sub)})
byid = {r['code']: r for r in rows}

# ---- hitos ----
milestones = []
for hid, name, preds in HITOS:
    milestones.append({'id': hid, 'name': name, 'preds': preds, 'date': workday(max(EF[p] for p in preds) - 1)})

# ---- costos: estimacion propia (estimacion_costos.py) con la reserva de contingencia asignada por incertidumbre ----
is_works = lambda c: any(c.startswith(f'1.{i}.') for i in range(2, 7))
COST = estimacion_costos.estimate({r['code']: (r['start'], r['finish']) for r in rows}, PROJECT_START, PROJECT_END)
estimacion_costos.write_outputs(COST, OUT, {r['code']: (r['start'], r['finish']) for r in rows}, PROJECT_START, PROJECT_END)
for r in rows:
    c = r['code']
    r['base'] = COST['packages'].get(c, 0.0) / 1e6
    r['contingency'] = COST['package_reserve'].get(c, 0.0) / 1e6
    r['budget'] = r['base'] + r['contingency']
TOTAL_MUSD = COST['linea_base'] / 1e6
CONTINGENCY_MUSD = COST['contingencia'] / 1e6
assert abs(sum(r['budget'] for r in rows) - TOTAL_MUSD) < 1e-7
assert abs(sum(r['contingency'] for r in rows) - CONTINGENCY_MUSD) < 1e-7
assert set(COST['packages']) <= set(byid), set(COST['packages']) - set(byid)

# Perfiles de distribucion del valor planificado (fundamento en docs/estimacion-costos.md):
# civil: 3t^2 - 2t^3, aproximacion simetrica al logit de Kenley y Wilson (alfa 0, beta ~1.5); DHSS como sensibilidad.
# equipment: suministro (70 %) reconocido a la entrega, escalonada entre el 30 y el 60 % del paquete, e instalacion (30 %) lineal
#   (WB SBD Plant 2015).
# consulting: pagos contra productos (GN-2350-15 4.1): 20 % al 25 % del plazo, 40 % al 65 % y 40 % al final.
# audit: un escalon por ejercicio auditado, al vencer el plazo de los estados financieros (30 de abril).
# operations: lineal, honorarios mensuales (GN-2350-15 4.2 y 4.9).
SUPPLY = {'1.2.4', '1.3.3', '1.4.2', '1.5.2', '1.5.3', '1.6.2'}
ONGOING = {'1.7.1', '1.7.2', '1.7.3', '1.7.4', '3.3.4', '3.3.3', '3.1.1'}
for r in rows:
    c = r['code']
    typ = 'civil' if is_works(c) else ('consulting' if c.startswith('2.') else 'operations')
    if c in SUPPLY: typ = 'equipment'
    if c in ONGOING: typ = 'operations'
    if c == '3.5.2': typ = 'audit'
    if c == '3.5.4': typ = 'consulting'
    r['profile'] = typ
    # la UEP se paga durante todo el programa, no solo los 50 dias de su conformacion
    r['cf_es'], r['cf_ef'] = (0, END) if c == '3.1.1' else (r['es'], r['ef'])

def apr30(y):
    d = date(y, 4, 30)
    while d.weekday() >= 5: d -= timedelta(days=1)
    return d
# los estados financieros auditados de cada ejercicio se entregan al terminar 3.5.2-03, -06 y -09
AUDIT_DATES = [abyid[c]['finish'] for c in ('3.5.2-03', '3.5.2-06', '3.5.2-09')]

def piece(t, anchors):
    if t <= 0: return 0
    if t >= 1: return 1
    for (x0, y0), (x1, y1) in zip(anchors, anchors[1:]):
        if t <= x1: return y0 + (y1 - y0) * (t - x0) / (x1 - x0)
    return 1

def civil_curve(t, model):
    if model == 'dhss':  # Hudson (1978), banda de contratos grandes (Kenley 2003, tabla 3.11): C = 0.063, K = 3.344
        C, K = 0.063, 3.344
        return t + C * (t * t - t) - (6 * t ** 3 - 9 * t * t + 3 * t) / K
    return t * t * (3 - 2 * t)

def profile(r, t, model='smooth'):
    p = r['profile']
    if t <= 0: return 0.0
    if t >= 1: return 1.0
    if p == 'civil': return civil_curve(t, model)
    if p == 'equipment': return 0.3 * t + 0.7 * min(1.0, max(0.0, (t - 0.3) / 0.3))
    if p == 'consulting': return piece(t, [(0, 0), (.249, 0), (.25, .2), (.649, .2), (.65, .6), (.999, .6), (1, 1)])
    return t

def frac(r, d: date) -> float:
    """Fraccion transcurrida del paquete al cierre del dia d (en dias laborables)."""
    idx = wd_index(d) + 1 if d.weekday() < 5 else wd_index(d)  # dias laborables completados al cierre de d
    span = r['cf_ef'] - r['cf_es']
    return max(0.0, min(1.0, (idx - r['cf_es']) / span))

months = []
y, m = PROJECT_START.year, PROJECT_START.month
while (y, m) <= (PROJECT_END.year, PROJECT_END.month):
    months.append((y, m))
    y, m = (y + 1, 1) if m == 12 else (y, m + 1)

def month_end(y, m): return date(y + (m == 12), 1 if m == 12 else m + 1, 1) - timedelta(days=1)

def build_monthly(eval_idx, model='smooth'):
    """Curva mensual. El costo de 3.5.3 se reparte por mitades al presentar cada informe de evaluacion y el de 3.5.2 por
    partes iguales en cada fecha de entrega de estados financieros auditados."""
    out, prev = [], 0.0
    for y, m in months:
        last = month_end(y, m)
        done = wd_index(last) + 1 if last.weekday() < 5 else wd_index(last)
        comp = {k: 0.0 for k in '123'}
        base = cont = 0.0
        for r in rows:
            if r['code'] == '3.5.3':
                f = sum(0.5 for i in eval_idx if done > i)
            elif r['profile'] == 'audit':
                f = sum(1 for d in AUDIT_DATES if d <= last) / len(AUDIT_DATES)
            else:
                f = profile(r, frac(r, last), model)
            comp[r['code'][0]] += r['budget'] * f
            base += r['base'] * f
            cont += r['contingency'] * f
        total = sum(comp.values())
        out.append({
            'mes': f'{y:04d}-{m:02d}',
            'gasto_mensual_musd': round(total - prev, 6),
            'acumulado_linea_base_musd': round(total, 6),
            'avance_pct': round(100 * total / TOTAL_MUSD, 2),
            'acumulado_sin_contingencia_musd': round(base, 6),
            'contingencia_acumulada_musd': round(cont, 6),
            'c1_acumulado_musd': round(comp['1'], 6), 'c2_acumulado_musd': round(comp['2'], 6), 'c3_acumulado_musd': round(comp['3'], 6),
        })
        prev = total
    return out

def last_workday(d: date) -> int:
    while d.weekday() >= 5: d -= timedelta(days=1)
    return wd_index(d)

# Informes de evaluacion (3.5.3-03 y 3.5.3-05): el costo de 3.5.3 se reconoce por mitades al presentarlos.
eval_idx = (EF['3.5.3-03'] - 1, EF['3.5.3-05'] - 1)
monthly = build_monthly(eval_idx)

def reached(p):
    y, m = map(int, next(x['mes'] for x in monthly if x['acumulado_linea_base_musd'] >= TOTAL_MUSD * p - 1e-6).split('-'))
    return month_end(y, m)

# Verificacion de la regla del contrato (clausula 5.03) y del MEL con la curva de la linea base
evals = [{'tipo': 'Medio término', 'firma': workday(EF['3.4.4-35'] - 1), 'informe': workday(eval_idx[0]),
          'hito': reached(.5), 'limite': reached(.5) + timedelta(days=60)},
         {'tipo': 'Final', 'firma': workday(EF['3.4.4-40'] - 1), 'informe': workday(eval_idx[1]),
          'hito': reached(.95), 'limite': reached(.95) + timedelta(days=90)}]
assert abs(monthly[-1]['acumulado_linea_base_musd'] - TOTAL_MUSD) < 1e-4, monthly[-1]
assert all(b['acumulado_linea_base_musd'] >= a['acumulado_linea_base_musd'] for a, b in zip(monthly, monthly[1:]))
# Sensibilidad de la forma de la curva: obras civiles con la curva DHSS en lugar de 3t^2 - 2t^3.
for x, s in zip(monthly, build_monthly(eval_idx, 'dhss')):
    x['acumulado_dhss_musd'] = s['acumulado_linea_base_musd']

def reach(key, p):
    return next(x['mes'] for x in monthly if x[key] >= TOTAL_MUSD * p - 1e-6)
SENS = {f'{int(p * 100)}%': {'base': reach('acumulado_linea_base_musd', p), 'dhss': reach('acumulado_dhss_musd', p)} for p in (.25, .5, .75, .9)}
SENS_MAX = max((x['acumulado_dhss_musd'] - x['acumulado_linea_base_musd'] for x in monthly), key=abs)

annual = []
for yr in sorted({int(x['mes'][:4]) for x in monthly}):
    sub = [x for x in monthly if x['mes'].startswith(str(yr))]
    annual.append({'anio': yr, 'gasto_anual_musd': round(sum(x['gasto_mensual_musd'] for x in sub), 3),
                   'acumulado_musd': round(sub[-1]['acumulado_linea_base_musd'], 3), 'avance_pct': round(sub[-1]['avance_pct'], 1)})

# ---- CSV ----
def write_csv(name, fields, data):
    with (OUT / name).open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(data)

write_csv('cronograma_actividades.csv',
          ['code', 'name', 'package', 'phase', 'owner', 'dur', 'deps', 'start', 'finish', 'float', 'critical'],
          [{**r, 'critical': 'si' if r['critical'] else ''} for r in arows])
write_csv('cronograma_paquetes.csv',
          ['code', 'name', 'activities', 'dur', 'deps', 'start', 'finish', 'float', 'critical', 'budget', 'base', 'contingency', 'profile'],
          [{**r, 'dur': r['dur'], 'float': r['float'], 'critical': 'si' if r['critical'] else '',
            'budget': f"{r['budget']:.8f}", 'base': f"{r['base']:.8f}", 'contingency': f"{r['contingency']:.8f}"} for r in rows])
write_csv('hitos.csv', ['id', 'name', 'preds', 'date'],
          [{'id': h['id'], 'name': h['name'], 'preds': ','.join(h['preds']), 'date': h['date']} for h in milestones])
write_csv('curva_s_mensual.csv', list(monthly[0]), monthly)
write_csv('curva_s_anual.csv', list(annual[0]), annual)

# ---- XML MSPDI para Open Planner Studio / MS Project ----
# Arbol: componentes y elementos de la EDT (resumen) > paquetes de trabajo (resumen) > actividades.
def depth(code): return code.count('.') + 1
nodes = ([(c, n, 'edt') for c, n in SUMMARIES.items()] + [(r['code'], r['name'], 'paquete') for r in rows]
         + [(r['code'], r['name'], 'actividad') for r in arows])
order = lambda x: ([int(p) for p in x[0].split('-')[0].split('.')] + ([int(x[0].split('-')[1])] if '-' in x[0] else []))
nodes.sort(key=order)
uid = {'__root__': 0}
for i, (c, n, s) in enumerate(nodes, start=1): uid[c] = i
hito_summary_uid = len(nodes) + 1
for j, h in enumerate(milestones, start=1): uid[h['id']] = hito_summary_uid + j

def span(prefix):
    sub = [r for r in rows if r['code'] == prefix or r['code'].startswith(prefix + '.')]
    return min(r['es'] for r in sub), max(r['ef'] for r in sub)

MSP_LINK = {'FF': 0, 'FI': 1, 'IF': 2, 'II': 3}  # codigos <Type> de MSPDI

def iso(i, end=False):
    d = workday(i)
    return d.isoformat() + ('T17:00:00' if end else 'T08:00:00')

def hrs(days): return f'PT{days * 8}H0M0S'

x = ["<?xml version='1.0' encoding='utf-8'?>",
     '<Project xmlns="http://schemas.microsoft.com/project">',
     '<Name>ES-L1173 Cronograma del programa</Name><Title>Programa de Modernización del Aeropuerto Internacional de El Salvador</Title>',
     f'<StartDate>{PROJECT_START.isoformat()}T08:00:00</StartDate><FinishDate>{PROJECT_END.isoformat()}T17:00:00</FinishDate>',
     '<MinutesPerDay>480</MinutesPerDay><MinutesPerWeek>2400</MinutesPerWeek><DaysPerMonth>20</DaysPerMonth><CalendarUID>1</CalendarUID>',
     # Marca de unidad de Open Planner: sin ella muestra las duraciones en horas; con 'days' las muestra en dias laborables.
     '<ExtendedAttributes><ExtendedAttribute><FieldID>188744016</FieldID><FieldName>OPS_TaskDurationUnit</FieldName>'
     '<Alias>OPS_TaskDurationUnit</Alias></ExtendedAttribute>'
     # Hitos como hitos de fin: sin esta marca Open Planner los desplaza un dia al abrir en modo dias.
     '<ExtendedAttribute><FieldID>188744015</FieldID><FieldName>OPS_MilestoneKind</FieldName>'
     '<Alias>OPS_MilestoneKind</Alias></ExtendedAttribute></ExtendedAttributes>',
     # Calendario explicito: sin el, Open Planner usa su calendario NL por defecto (07:00 a 16:00, con feriados de Paises Bajos)
     # y convierte las horas en jornadas de 9 h, lo que acorta el cronograma un 11 %.
     '<Calendars><Calendar><UID>1</UID><Name>Lunes a viernes 08:00-17:00</Name><IsBaseCalendar>1</IsBaseCalendar><BaseCalendarUID>-1</BaseCalendarUID><WeekDays>'
     '<WeekDay><DayType>1</DayType><DayWorking>0</DayWorking></WeekDay>'
     + ''.join(f'<WeekDay><DayType>{d}</DayType><DayWorking>1</DayWorking><WorkingTimes>'
               '<WorkingTime><FromTime>08:00:00</FromTime><ToTime>12:00:00</ToTime></WorkingTime>'
               '<WorkingTime><FromTime>13:00:00</FromTime><ToTime>17:00:00</ToTime></WorkingTime></WorkingTimes></WeekDay>' for d in range(2, 7))
     + '<WeekDay><DayType>7</DayType><DayWorking>0</DayWorking></WeekDay></WeekDays></Calendar></Calendars>',
     '<Tasks>']
x.append(f'<Task><UID>0</UID><ID>0</ID><Name>{escape(ROOT_NAME)}</Name><OutlineLevel>0</OutlineLevel>'
         f'<Start>{iso(0)}</Start><Finish>{iso(END - 1, True)}</Finish><Duration>{hrs(END)}</Duration><DurationFormat>7</DurationFormat>'
         '<Milestone>0</Milestone><Summary>1</Summary></Task>')
for c, n, kind in nodes:
    if kind == 'edt':
        a, b = span(c)
        x.append(f'<Task><UID>{uid[c]}</UID><ID>{uid[c]}</ID><Name>{escape(n)}</Name><WBS>{c}</WBS><OutlineLevel>{depth(c)}</OutlineLevel>'
                 f'<Start>{iso(a)}</Start><Finish>{iso(b - 1, True)}</Finish><Duration>{hrs(b - a)}</Duration><DurationFormat>7</DurationFormat>'
                 '<Milestone>0</Milestone><Summary>1</Summary><PercentComplete>0</PercentComplete></Task>')
    elif kind == 'paquete':
        r = byid[c]
        if r['budget'] > 0:
            note = f'Costo en la línea base: US$ {r["budget"]:.3f} millones' + (f', de los cuales US$ {r["contingency"]:.3f} millones son contingencia.' if r['contingency'] > 0 else '.')
        else:
            note = 'Ejecutado por el personal de la UEP, sin costo adicional en la línea base.'
        x.append(f'<Task><UID>{uid[c]}</UID><ID>{uid[c]}</ID><Name>{escape(n)}</Name><WBS>{c}</WBS><OutlineLevel>{depth(c)}</OutlineLevel>'
                 f'<Start>{iso(r["es"])}</Start><Finish>{iso(r["ef"] - 1, True)}</Finish><Duration>{hrs(r["dur"])}</Duration><DurationFormat>7</DurationFormat>'
                 f'<Milestone>0</Milestone><Summary>1</Summary><PercentComplete>0</PercentComplete><Notes>{escape(note)}</Notes></Task>')
    else:
        r, a = abyid[c], act[c]
        links = ''.join(f'<PredecessorLink><PredecessorUID>{uid[p]}</PredecessorUID><Type>{MSP_LINK[t]}</Type>'
                        f'<LinkLag>{lag * 4800}</LinkLag><LagFormat>7</LagFormat></PredecessorLink>' for p, t, lag in pred[c])
        note = f'Fase: {a["fase"]}. Responsable: {a["responsable"]}.'
        if c in LOE:
            note += f' Nivel de esfuerzo: su duración se fijó para terminar con {", ".join(ends_with[c])}.'
        else:
            note += f' PERT: O {a["O"]}, M {a["M"]}, P {a["P"]} días laborables; De = {(int(a["O"]) + 4 * int(a["M"]) + int(a["P"])) / 6:.1f}. Técnica: {a["tecnica"]}.'
        cons = (f'<ConstraintType>4</ConstraintType><ConstraintDate>{a["restriccion"][4:]}T08:00:00</ConstraintDate>' if a['restriccion'] else '')
        x.append(f'<Task><UID>{uid[c]}</UID><ID>{uid[c]}</ID><Name>{escape(n)}</Name><WBS>{c}</WBS><OutlineLevel>{depth(r["package"]) + 1}</OutlineLevel>'
                 f'<Start>{iso(r["es"])}</Start><Finish>{iso(r["ef"] - 1, True)}</Finish><Duration>{hrs(r["dur"])}</Duration><DurationFormat>7</DurationFormat>'
                 f'<Milestone>0</Milestone><Summary>0</Summary><PercentComplete>0</PercentComplete>{cons}<Notes>{escape(note)}</Notes>{links}</Task>')
hs, he = min(wd_index(h['date']) for h in milestones), max(wd_index(h['date']) for h in milestones)
# Open Planner arma el arbol con <OutlineLevel>, salvo que los WBS con punto formen un arbol completo que lo contradiga
# (importNormalize.ts, rebuildImportedHierarchy). Los codigos de actividad "1.1.1-01" colgarian de "1.1"; con el WBS
# "Hitos" en esta fila los hitos "H.1" no tienen padre por codigo, el arbol de WBS queda incompleto y manda el esquema.
x.append(f'<Task><UID>{hito_summary_uid}</UID><ID>{hito_summary_uid}</ID><Name>Hitos del programa</Name><WBS>Hitos</WBS><OutlineLevel>1</OutlineLevel>'
         f'<Start>{iso(hs)}</Start><Finish>{iso(he, True)}</Finish><Duration>{hrs(he - hs + 1)}</Duration><DurationFormat>7</DurationFormat>'
         '<Milestone>0</Milestone><Summary>1</Summary><PercentComplete>0</PercentComplete></Task>')
for j, h in enumerate(milestones, start=1):
    i = wd_index(h['date'])
    links = ''.join(f'<PredecessorLink><PredecessorUID>{uid[p]}</PredecessorUID><Type>1</Type><LinkLag>0</LinkLag><LagFormat>7</LagFormat></PredecessorLink>' for p in h['preds'])
    x.append(f'<Task><UID>{uid[h["id"]]}</UID><ID>{uid[h["id"]]}</ID><Name>{escape(h["name"])}</Name><WBS>H.{j}</WBS><OutlineLevel>2</OutlineLevel>'
             f'<Start>{iso(i, True)}</Start><Finish>{iso(i, True)}</Finish><Duration>PT0H0M0S</Duration><DurationFormat>7</DurationFormat>'
             f'<Milestone>1</Milestone><Summary>0</Summary><PercentComplete>0</PercentComplete>{links}</Task>')
DAYS = '<ExtendedAttribute><FieldID>188744016</FieldID><Value>days</Value></ExtendedAttribute>'
FINISH = '<ExtendedAttribute><FieldID>188744015</FieldID><Value>FINISH</Value></ExtendedAttribute>'
x = [l.replace('</Task>', DAYS + (FINISH if '<Milestone>1</Milestone>' in l else '') + '</Task>') if l.startswith('<Task>') else l for l in x]
x.append('</Tasks></Project>')
(OUT / 'cronograma_ES-L1173.xml').write_text('\n'.join(x), encoding='utf-8')

# ---- resumen ----
crit = [r['code'] for r in sorted(arows, key=lambda r: (r['es'], r['ef'])) if r['critical']]
crit_pk = [r['code'] for r in sorted(rows, key=lambda r: r['es']) if r['critical']]
peak = max(monthly, key=lambda r: r['gasto_mensual_musd'])
summary = {'inicio': PROJECT_START, 'fin': PROJECT_END, 'dias_laborables': END, 'actividades': len(arows),
           'ruta_critica': crit, 'paquetes_criticos': crit_pk,
           'pico_mensual': peak, 'anual': annual, 'hitos': [{**h, 'date': h['date']} for h in milestones],
           'tareas_xml': 1 + len(nodes) + 1 + len(milestones),
           'evaluaciones': evals,
           'bac_musd': TOTAL_MUSD, 'contingencia_musd': CONTINGENCY_MUSD, 'estimacion_pert_musd': COST['total_E'] / 1e6,
           'reserva_gestion_musd': COST['reserva_gestion'] / 1e6, 'presupuesto_musd': COST['presupuesto'] / 1e6, 'prestamo_musd': LOAN_MUSD,
           'sensibilidad_dhss': SENS, 'sensibilidad_dhss_dif_max_musd': SENS_MAX,
           'nota': 'Valor planificado acumulado; no corresponde a desembolsos ni pagos'}
(OUT / 'resumen.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2, default=str), encoding='utf-8')

# ---- grafico ----
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    xs = [date(int(r['mes'][:4]), int(r['mes'][5:]), 15) for r in monthly]
    fig, ax = plt.subplots(figsize=(11, 5.2))
    ax.plot(xs, [r['acumulado_linea_base_musd'] for r in monthly], color='#1f4e79', linewidth=2, label='Línea base de costos (con contingencia)')
    ax.plot(xs, [r['acumulado_sin_contingencia_musd'] for r in monthly], color='#8a8f98', linewidth=2, label='Estimación PERT (sin contingencia)')
    ax.axhline(LOAN_MUSD, color='#c9cdd3', linewidth=1, linestyle=(0, (4, 3)))
    ax.text(xs[0], LOAN_MUSD + 2.5, f'Préstamo autorizado US${LOAN_MUSD:.0f} M', fontsize=9, color='#4a4f57')
    ax.annotate(f"US${TOTAL_MUSD:.1f} M", (xs[-1], TOTAL_MUSD), xytext=(-6, 6), textcoords='offset points', ha='right', fontsize=9, color='#1f4e79')
    ax.annotate(f"US${monthly[-1]['acumulado_sin_contingencia_musd']:.1f} M", (xs[-1], monthly[-1]['acumulado_sin_contingencia_musd']),
                xytext=(-6, -14), textcoords='offset points', ha='right', fontsize=9, color='#4a4f57')
    ax.set_ylabel('US$ millones acumulados'); ax.set_ylim(0, 210)
    ax.set_title('ES-L1173: curva S del valor planificado', loc='left', fontsize=12)
    ax.xaxis.set_major_locator(mdates.YearLocator()); ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.grid(axis='y', color='#e6e8eb', linewidth=.8); ax.set_axisbelow(True)
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    ax.legend(loc='upper left', bbox_to_anchor=(0, .9), frameon=False)
    fig.tight_layout(); fig.savefig(OUT / 'curva_s.png', dpi=160); plt.close(fig)
except ImportError:
    pass

print(json.dumps({'inicio': PROJECT_START, 'fin': PROJECT_END, 'dias_laborables': END, 'ruta_critica': crit,
                  'pico': peak['mes'], 'pico_musd': peak['gasto_mensual_musd'], 'meses': len(monthly), 'anual': annual,
                  'hitos': {h['id']: h['date'] for h in milestones}}, ensure_ascii=False, default=str, indent=1))

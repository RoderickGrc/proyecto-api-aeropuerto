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
3. Costos: estimacion propia por elemento y por paquete (estimacion_costos.py), asignada a las actividades de quien cobra el
   contrato con pesos por elemento y por actividad segun el recurso (regla en estimacion_costos.py); el costo indirecto de la
   UEP lo lleva 3.1.1-06. La curva S es el valor planificado de la linea base de costos (estimacion PERT mas la reserva de
   contingencia, P80): cada actividad se prorratea en su duracion, sin anticipos ni pagos contra entrega. La logica de pagos
   (anticipos por contrato segun el PEP) solo esta en los requisitos de financiamiento, que suman la reserva de gestion y se
   comparan con los desembolsos del PEP. Tambien verifica los plazos de las evaluaciones (clausula 5.03 del contrato).
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

# ---- costos por actividad (clase 6: EDT > paquetes > actividades > costo de las actividades) ----
# El costo de cada elemento de la estimación (estimacion_costos.py) llega a sus paquetes y, dentro de cada paquete, a las
# actividades de quien cobra el contrato (contratista, firma de supervisión, firma consultora, auditor), con pesos por elemento
# y por actividad según el recurso (regla en estimacion_costos.py). Las actividades de la UEP, CEPA, el BID y la AAC no tienen
# costo propio; la única excepción es el costo indirecto de la UEP (3.1.1), que lleva la actividad de nivel de esfuerzo
# 3.1.1-06. Si un paquete con costo no tiene actividades de quien cobra, el reparto falla con assert.
SUP_CONTRACT, SUP_WORKS = estimacion_costos.SUP_CONTRACT, estimacion_costos.SUP_WORKS
SUP_WORD = {'T': 'terminal', 'E': 'estacionamiento', 'P': 'plataformas', 'S': 'SSEI'}
assert all(SUP_WORD[g] in act[c]['actividad'] for c, g in SUP_CONTRACT.items())
INDIRECT, INDIRECT_ACT = '3.1.1', estimacion_costos.UEP_INDIRECT
assert act[INDIRECT_ACT]['tecnica'] == 'Nivel de esfuerzo' and act[INDIRECT_ACT]['paquete'] == INDIRECT

tech_sign = next(c for c, a in act.items() if a['actividad'].startswith('Firmar el contrato del técnico de apoyo'))
CTX = {'acts': {c: {'pkg': r['package'], 'name': r['name'], 'dur': r['dur'], 'start': r['start'], 'finish': r['finish'], 'owner': r['owner']}
                for c, r in abyid.items()},
       'uep': {'start': abyid[INDIRECT_ACT]['start'], 'end': abyid[INDIRECT_ACT]['finish'], 'tech_start': abyid[tech_sign]['finish'],
               'lot_sign': {code: abyid[code]['finish'] for _, code, _ in estimacion_costos.PLANTILLA}}}
COST = estimacion_costos.estimate(CTX)
estimacion_costos.write_outputs(COST, OUT, CTX)
ALLOC = estimacion_costos.allocate(COST, CTX)
for r in rows:
    c = r['code']
    r['base'] = COST['packages'].get(c, 0.0) / 1e6
    r['contingency'] = COST['package_reserve'].get(c, 0.0) / 1e6
    r['budget'] = r['base'] + r['contingency']
    r['profile'] = 'escalonado por puestos' if c == INDIRECT else 'lineal'
TOTAL_MUSD = COST['linea_base'] / 1e6
CONTINGENCY_MUSD = COST['contingencia'] / 1e6
assert abs(sum(r['budget'] for r in rows) - TOTAL_MUSD) < 1e-7
assert abs(sum(r['contingency'] for r in rows) - CONTINGENCY_MUSD) < 1e-7
assert set(COST['packages']) <= set(byid), set(COST['packages']) - set(byid)
for r in arows:
    c = r['code']
    r['base'], r['contingency'] = ALLOC['base'].get(c, 0.0) / 1e6, ALLOC['cont'].get(c, 0.0) / 1e6
    r['budget'] = r['base'] + r['contingency']
    tot = sum(ALLOC['parts'].get(c, {}).values())
    r['cost_elements'] = '; '.join(f'{e} {v / tot:.0%}' for e, v in sorted(ALLOC['parts'].get(c, {}).items(), key=lambda x: -x[1])) if tot else ''
    r['profile'] = 'escalonado por puestos' if c == INDIRECT_ACT else 'lineal'
for r in rows:
    assert abs(sum(a['budget'] for a in arows if a['package'] == r['code']) - r['budget']) < 1e-9, r['code']
assert abs(sum(a['budget'] for a in arows) - TOTAL_MUSD) < 1e-7
assert all(a['budget'] == 0 or a['owner'] in estimacion_costos.PAYEES or a['code'] == INDIRECT_ACT for a in arows)
UEP_ACT = abyid[INDIRECT_ACT]
UEP_PARTS = {e['id']: (e['E'] / 1e6, e['reserve'] / 1e6) for e in COST['elements'] if e['id'] in estimacion_costos.UEP_ELEMENTS}
assert abs(sum(v[0] + v[1] for v in UEP_PARTS.values()) - UEP_ACT['budget']) < 1e-9

# Costo real estimado al corte: honorarios mensuales de los contratos de la UEP en ejecución (siete consultores clave, PA 2026-2)
# por los meses transcurridos desde su inicio. Es un costo incurrido estimado, no un desembolso del BID.
CORTE = date(2026, 10, 31)
AC_CORTE_MUSD = sum(p['M'] * estimacion_costos.months_from(p['inicio'], CORTE) for p in COST['uep']['posts'][:7]) / 1e6

# ---- curva S: valor planificado ----
# Cada actividad se prorratea de forma lineal en su duración (fabricaciones, consultorías, auditorías y evaluaciones incluidas):
# la curva no incluye anticipos ni pagos contra entrega; esa lógica de pagos solo está en los requisitos de financiamiento.
# Excepción: el costo indirecto de la UEP (3.1.1-06) sigue la incorporación de sus puestos (costo mensual por puesto desde su
# contratación real) en lugar de un prorrateo lineal, porque es un flujo mensual por plaza y no un producto.
def dhss(t):  # Hudson (1978), banda de contratos grandes (Kenley 2003, tabla 3.11): C = 0.063, K = 3.344
    C, K = 0.063, 3.344
    return t + C * (t * t - t) - (6 * t ** 3 - 9 * t * t + 3 * t) / K

def done_days(d: date) -> int:
    """Dias laborables completados al cierre del dia d (en sábado o domingo, incluido el viernes anterior)."""
    return wd_index(d) + 1

def linear(r, done: int) -> float:
    return max(0.0, min(1.0, (done - r['es']) / max(1, r['ef'] - r['es'])))

# Contratos de obra: actividades del contratista de cada obra y su plazo completo (para la sensibilidad DHSS)
OBRA_ACTS = {g: [r for r in arows if r['budget'] and r['owner'] == 'Contratista de obra' and r['package'].startswith(pre)] for g, pre in SUP_WORKS.items()}
OBRA_SPAN = {g: (min(r['es'] for r in v), max(r['ef'] for r in v)) for g, v in OBRA_ACTS.items()}
OBRA_OF = {r['code']: g for g, v in OBRA_ACTS.items() for r in v}

months = []
y, m = PROJECT_START.year, PROJECT_START.month
while (y, m) <= (PROJECT_END.year, PROJECT_END.month):
    months.append((y, m))
    y, m = (y + 1, 1) if m == 12 else (y, m + 1)

def month_end(y, m): return date(y + (m == 12), 1 if m == 12 else m + 1, 1) - timedelta(days=1)

def frac(r, done: int, model: str) -> float:
    if model == 'dhss' and r['code'] in OBRA_OF:
        a, b = OBRA_SPAN[OBRA_OF[r['code']]]
        return dhss(max(0.0, min(1.0, (done - a) / max(1, b - a))))
    return linear(r, done)

def build_monthly(model='lineal'):
    """Curva mensual: suma del costo de las actividades que corresponde al avance de cada mes (clase 6)."""
    out, prev = [], 0.0
    for y, m in months:
        d = month_end(y, m)
        done = done_days(d)
        comp = {k: 0.0 for k in '123'}
        base = cont = 0.0
        uf = estimacion_costos.uep_fraction(COST['uep'], d)
        ub = sum(UEP_PARTS[e][0] * uf[e] for e in UEP_PARTS)
        uc = sum(UEP_PARTS[e][1] * uf[e] for e in UEP_PARTS)
        comp['3'] += ub + uc
        base += ub
        cont += uc
        for r in arows:
            if not r['budget'] or r['code'] == INDIRECT_ACT:
                continue
            f = frac(r, done, model)
            comp[r['package'][0]] += r['budget'] * f
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

monthly = build_monthly()

def reached(p):
    y, m = map(int, next(x['mes'] for x in monthly if x['acumulado_linea_base_musd'] >= TOTAL_MUSD * p - 1e-6).split('-'))
    return month_end(y, m)

assert abs(monthly[-1]['acumulado_linea_base_musd'] - TOTAL_MUSD) < 1e-4, monthly[-1]
assert all(b['acumulado_linea_base_musd'] >= a['acumulado_linea_base_musd'] - 1e-9 for a, b in zip(monthly, monthly[1:]))
# Sensibilidad de la forma de la curva: cada contrato de obra con la curva DHSS en todo su plazo en lugar de lineal.
for x, s in zip(monthly, build_monthly('dhss')):
    x['acumulado_dhss_musd'] = s['acumulado_linea_base_musd']

def reach(key, p):
    return next(x['mes'] for x in monthly if x[key] >= TOTAL_MUSD * p - 1e-6)
SENS = {f'{int(p * 100)}%': {'base': reach('acumulado_linea_base_musd', p), 'dhss': reach('acumulado_dhss_musd', p)} for p in (.25, .5, .75, .9)}
SENS_MAX = max((x['acumulado_dhss_musd'] - x['acumulado_linea_base_musd'] for x in monthly), key=abs)

# ---- requisitos de financiamiento frente al flujo de desembolsos del PEP ----
# Aquí sí entra la lógica de pagos. PEP (EER#3, nov-2025), hoja Payments Flow Output: pagos estimados del BID por semestre desde la
# firma prevista del préstamo (31-dic-2025); Sem I = ene-jun 2026. En la hoja Payments, el primer pago de cada contrato cae en el
# semestre de su firma y no es uniforme (ver PEP_FIRST). Que sea un anticipo es una inferencia: los avisos de adquisiciones no lo
# mencionan, pero el pago inicial equivale a un porcentaje del contrato antes de cualquier avance. El escenario con anticipo lo
# paga en el semestre de la firma y lo amortiza descontando el mismo porcentaje de cada avance, sobre la base sin contingencia (el
# precio del contrato; la contingencia solo se gasta si ocurren los riesgos). Los requisitos de financiamiento son la línea base
# más la reserva de gestión (clase 6), esta última en proporción al valor planificado de cada semestre.
PEP_FLOW_MUSD = [0.608875, 58.365642, 29.448411, 29.149918, 29.407026, 22.578669, 12.625730, 12.815729]
# (primer pago, monto total) por contrato en US$ del PEP: obras (procesos 1 a 4) y supervisiones (PEP 1.4.1 a 1.4.3)
PEP_FIRST = {
    'obra': {'T': (23_697_761, 78_992_537), 'E': (19_260_784, 64_202_613), 'P': (6_786_640 + 3_656_291, 15_081_421 + 8_125_092), 'S': (1_421_036, 9_473_574)},
    'sup': {'T': (2_147_927, 7_159_759), 'E': (2_147_927, 7_159_759), 'P': (406_114, 1_160_295), 'S': (165_798, 473_709)},
}
PEP_PCT = {k: {g: round(a / b, 2) for g, (a, b) in v.items()} for k, v in PEP_FIRST.items()}
assert all(abs(a / b - PEP_PCT[k][g]) < 0.001 for k, v in PEP_FIRST.items() for g, (a, b) in v.items())
WORK_SIGN = {'T': '3.4.1-12', 'E': '3.4.1-06', 'P': '3.4.1-24', 'S': '3.4.1-18'}
SUP_SIGN = {'T': '3.4.2-12', 'E': '3.4.2-06', 'P': '3.4.2-24', 'S': '3.4.2-18'}
assert all(act[c]['actividad'].startswith('Adjudicar y firmar el contrato de obra') or act[c]['actividad'].startswith('Firmar el contrato de supervisión') for c in [*WORK_SIGN.values(), *SUP_SIGN.values()])
CONTRACTS = []  # (nombre, firma, porcentaje, actividades)
for g in 'TEPS':
    CONTRACTS.append((f'Obra {SUP_WORD[g]}', abyid[WORK_SIGN[g]]['finish'], PEP_PCT['obra'][g], OBRA_ACTS[g]))
    CONTRACTS.append((f'Supervisión {SUP_WORD[g]}', abyid[SUP_SIGN[g]]['finish'], PEP_PCT['sup'][g], [abyid[c] for c, k in SUP_CONTRACT.items() if k == g]))

def semester(d: date) -> int:
    return (d.year - 2026) * 2 + (0 if d.month <= 6 else 1)

for _, _, _, v in CONTRACTS:
    assert all(r['budget'] for r in v)
n_sem = semester(PROJECT_END) + 1
GEST_RATE = COST['reserva_gestion'] / COST['linea_base']  # reserva de gestión en proporción al valor planificado
cash, cash_m, prev_base = [], [], {n: 0.0 for n, *_ in CONTRACTS}
ADV_TOTAL = 0.0
for x in monthly:
    y, mth = map(int, x['mes'].split('-'))
    d = month_end(y, mth)
    done = done_days(d)
    adv = amort = 0.0
    for name, sign, pct, v in CONTRACTS:
        b = sum(r['base'] * linear(r, done) for r in v)
        amort += pct * (b - prev_base[name])
        prev_base[name] = b
        if (sign.year, sign.month) == (y, mth):
            adv += pct * sum(r['base'] for r in v)
    ADV_TOTAL += adv
    pv = x['gasto_mensual_musd']
    cash_m.append({'mes': x['mes'], 'fin': d, 'pv': pv, 'gestion': pv * GEST_RATE, 'desembolso': pv + adv - amort})
assert abs(sum(c['desembolso'] for c in cash_m) - TOTAL_MUSD) < 1e-4
pv_sem, cash_sem = [0.0] * n_sem, [0.0] * n_sem
for c in cash_m:
    s = semester(c['fin'])
    pv_sem[s] += c['pv'] * (1 + GEST_RATE)
    cash_sem[s] += c['desembolso'] + c['gestion']
financing = []
acc = {'pep': 0.0, 'pv': 0.0, 'cash': 0.0}
for i in range(max(n_sem, len(PEP_FLOW_MUSD))):
    pep = PEP_FLOW_MUSD[i] if i < len(PEP_FLOW_MUSD) else 0.0
    pv = pv_sem[i] if i < n_sem else 0.0
    ca = cash_sem[i] if i < n_sem else 0.0
    acc['pep'] += pep; acc['pv'] += pv; acc['cash'] += ca
    financing.append({'semestre': f'{2026 + i // 2}-S{i % 2 + 1}', 'desembolso_pep_musd': round(pep, 6), 'desembolso_pep_acum_musd': round(acc['pep'], 6),
                      'requisito_musd': round(pv, 6), 'requisito_acum_musd': round(acc['pv'], 6),
                      'requisito_con_anticipo_musd': round(ca, 6), 'requisito_con_anticipo_acum_musd': round(acc['cash'], 6),
                      'diferencia_con_anticipo_semestre_musd': round(pep - ca, 6), 'diferencia_con_anticipo_acum_musd': round(acc['pep'] - acc['cash'], 6)})
PRESUPUESTO_MUSD = COST['presupuesto'] / 1e6
assert abs(acc['cash'] - acc['pv']) < 1e-6 and abs(acc['pv'] - PRESUPUESTO_MUSD) < 1e-4

# Verificación de los plazos de las evaluaciones (contrato, cláusula 5.03).
# Medio término: a más tardar 60 días después de que se desembolse el 50 % de los recursos o transcurra el 50 % del tiempo de
# ejecución planificado, lo que ocurra primero. El tiempo de ejecución planificado es el del cronograma (inicio y fin del programa);
# no se mide sobre el plazo de desembolsos. Un desembolso no es gasto: las Normas Generales (art. 4.07) permiten anticipos de fondos
# para las necesidades de liquidez de hasta seis meses, así que el 50 % desembolsado podría llegar antes que el 50 % gastado.
# Final: hasta 90 días después de terminar el plazo original de desembolsos o de desembolsar el 95 %, lo que ocurra primero.
# Vigencia (cláusula 6.01: plena validez jurídica): supuesto, la ratificación D.L. 505 del 29-ene-2026; se desconoce la fecha de su
# publicación. Plazo original de desembolsos: cinco años desde la vigencia (cláusula 2.04).
VIGENCIA = date(2026, 1, 29)
DISB_END = date(VIGENCIA.year + 5, VIGENCIA.month, VIGENCIA.day)
LEAD_MESES = 6  # anticipo de fondos: liquidez de hasta seis meses (art. 4.07 de las Normas Generales)
cum_cash, a_ = [], 0.0
for c in cash_m:
    a_ += c['desembolso'] + c['gestion']  # la misma serie de la tabla de requisitos de financiamiento (con anticipo y reserva de gestión)
    cum_cash.append((c['fin'], a_))

def disbursed(p, lead=0):
    """Fecha (fin de mes) en que se desembolsa el p del préstamo; con lead, el desembolso incluye la liquidez de los siguientes lead meses."""
    for i, (d, _) in enumerate(cum_cash):
        if cum_cash[min(i + lead, len(cum_cash) - 1)][1] >= LOAN_MUSD * p - 1e-6:
            return d
    return None

def pep_date(p):
    cum = 0.0
    for i, v in enumerate(PEP_FLOW_MUSD):
        cum += v
        if cum >= LOAN_MUSD * p - 1e-6:
            return date(2026 + i // 2, 6 if i % 2 == 0 else 12, 30 if i % 2 == 0 else 31)
    return None

T50 = PROJECT_START + (PROJECT_END - PROJECT_START) // 2
mt_inf = workday(EF['3.5.3-03'] - 1)
mt = {'tipo': 'Medio término', 'firma': workday(EF['3.4.4-35'] - 1), 'informe': mt_inf,
      'hito_50_tiempo': T50, 'limite_tiempo': T50 + timedelta(days=60),
      'hito_50_requisito': disbursed(.5), 'hito_50_pep': pep_date(.5), 'hito_50_acelerado': disbursed(.5, LEAD_MESES)}
for k in ('tiempo', 'requisito', 'pep', 'acelerado'):
    mt[f'limite_{k}'] = mt[f'hito_50_{k}'] + timedelta(days=60)
    mt[f'cumple_{k}'] = mt_inf <= mt[f'limite_{k}']
mt['margen_tiempo_dl'] = wd_index(mt['limite_tiempo']) - wd_index(mt_inf)
# Plazo que se programa: el primero entre el 50 % del tiempo y el 50 % desembolsado según los requisitos con anticipo. El PEP y el
# anticipo de fondos de seis meses adelantarían el segundo: son riesgos, no el plan.
mt['limite'] = min(mt['limite_tiempo'], mt['limite_requisito'])
mt['margen_dl'] = wd_index(mt['limite']) - wd_index(mt_inf)
h95 = disbursed(.95)
fin_inf = workday(EF['3.5.3-05'] - 1)
fl = {'tipo': 'Final', 'firma': workday(EF['3.4.4-40'] - 1), 'informe': fin_inf, 'hito_95_desembolsado': h95, 'fin_plazo_desembolsos': DISB_END,
      'limite': min(d for d in (h95, DISB_END) if d) + timedelta(days=90)}
fl['cumple'] = fin_inf <= fl['limite']
evals = [mt, fl]
assert mt['cumple_tiempo'] and mt['cumple_requisito'], mt
print('margen del informe de medio término (días laborables):', mt['margen_dl'], 'límite', mt['limite'], 'por tiempo', mt['limite_tiempo'], 'por requisitos', mt['limite_requisito'], file=sys.stderr)
assert fl['cumple'], fl

annual = []
for yr in sorted({int(x['mes'][:4]) for x in monthly}):
    sub = [x for x in monthly if x['mes'].startswith(str(yr))]
    annual.append({'anio': yr, 'gasto_anual_musd': round(sum(x['gasto_mensual_musd'] for x in sub), 6),
                   'acumulado_musd': round(sub[-1]['acumulado_linea_base_musd'], 6), 'avance_pct': round(sub[-1]['avance_pct'], 1)})

# ---- CSV ----
def write_csv(name, fields, data):
    with (OUT / name).open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(data)

write_csv('cronograma_actividades.csv',
          ['code', 'name', 'package', 'phase', 'owner', 'dur', 'deps', 'start', 'finish', 'float', 'critical', 'budget', 'base', 'contingency', 'profile', 'cost_elements'],
          [{**r, 'critical': 'si' if r['critical'] else '', 'budget': f"{r['budget']:.8f}", 'base': f"{r['base']:.8f}",
            'contingency': f"{r['contingency']:.8f}"} for r in arows])
write_csv('cronograma_paquetes.csv',
          ['code', 'name', 'activities', 'dur', 'deps', 'start', 'finish', 'float', 'critical', 'budget', 'base', 'contingency', 'profile'],
          [{**r, 'dur': r['dur'], 'float': r['float'], 'critical': 'si' if r['critical'] else '',
            'budget': f"{r['budget']:.8f}", 'base': f"{r['base']:.8f}", 'contingency': f"{r['contingency']:.8f}"} for r in rows])
write_csv('hitos.csv', ['id', 'name', 'preds', 'date'],
          [{'id': h['id'], 'name': h['name'], 'preds': ','.join(h['preds']), 'date': h['date']} for h in milestones])
write_csv('curva_s_mensual.csv', list(monthly[0]), monthly)
write_csv('curva_s_anual.csv', list(annual[0]), annual)
write_csv('requisitos_financiamiento.csv', list(financing[0]), financing)

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
           'requisitos_financiamiento': financing, 'anticipo_pct': PEP_PCT, 'anticipo_total_musd': ADV_TOTAL,
           'reserva_gestion_tasa': GEST_RATE, 'vigencia': VIGENCIA, 'fin_plazo_desembolsos': DISB_END, 'lead_anticipo_meses': LEAD_MESES,
           'contratos': [{'nombre': n, 'firma': sg, 'anticipo_pct': pc, 'base_musd': sum(r['base'] for r in v), 'inicio': min(r['start'] for r in v),
                          'fin': max(r['finish'] for r in v)} for n, sg, pc, v in CONTRACTS],
           'ultimo_desembolso': workday(EF['3.5.4-02'] - 1),
           'costo_real_corte_musd': AC_CORTE_MUSD, 'corte': CORTE, 'uep_inicio': UEP_ACT['start'], 'uep_fin': UEP_ACT['finish'],
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

#!/usr/bin/env python3
"""Genera el cronograma, los hitos, la ruta critica y la curva S del ES-L1173 .

Entradas: las 54 filas de paquetes de trabajo de docs/edt.md (duraciones y precedencias SUPUESTAS).
Salidas (en esta carpeta): cronograma_paquetes.csv, hitos.csv, curva_s_mensual.csv, curva_s_anual.csv,
curva_s.png, cronograma_ES-L1173.xml, resumen.json. Sin red, sin dependencias salvo matplotlib (opcional).

Cambios respecto a la v3 del traspaso previo:
1. Inicio del plan el 2026-02-02, alineado con el Anexo III de la Propuesta de Prestamo (UEP: feb/2026;
   licitaciones de obra: ago/2026 a dic/2026). La v3 iniciaba en 2026-11-02 y firmaba los contratos de obra en 2028.
2. Paquetes de nivel de esfuerzo (HAMMOCKS): supervision, PGAS, quejas, informes socioambientales, POA, desembolsos,
   auditorias y evaluaciones duran lo que duran los paquetes que acompanan y no fijan el fin del proyecto.
   La ruta critica pasa por contratacion y obra.
3. Se agregan 10 hitos (no son paquetes de la EDT).
4. Componente III: la UEP se fija en US$4,071,000 (Anexo III, consultores individuales). Los paquetes de gestion que
   ejecuta el personal de la UEP (3.1.2 a 3.1.4, 3.2.x, 3.3.1, 3.4.x, 3.5.1) quedan en costo 0 para no duplicar,
   igual que las revisiones de diseno 1.1.x. Se conservan 3.3.2 a 3.3.4, 3.5.2, 3.5.3 y 3.5.4 (suman US$0.96M + 0.30M).
5. La curva S incluye la contingencia (US$15,098,589.16, EEO3) y cierra en US$195M. Se reporta tambien la serie
   sin contingencia para comparacion.
Las duraciones y precedencias son estimaciones de planificacion. Calendario lunes a viernes, 8 h/dia, sin feriados.
"""
from __future__ import annotations
import csv, json, functools
from datetime import date, timedelta
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent
PROJECT_START = date(2026, 2, 2)
TOTAL_MUSD = 195.0
CONTINGENCY_MUSD = 15.09858916
WORKS_TOTAL_MUSD = 175.87523812

# codigo|duracion (dias laborables)|precedencias|costo MUSD (con contingencia)|nombre
RAW = '''
1.1.1|90|3.1.1|0|Diseños de la terminal revisados y aprobados
1.1.2|100|3.1.1|0|Diseños de plataformas y calle Foxtrot revisados y aprobados
1.1.3|105|3.1.1|0|Diseños del estacionamiento y del sistema solar revisados y aprobados
1.1.4|70|3.1.1|0|Diseños del SSEI revisados y aprobados
1.2.1|330|3.4.1,3.4.2,1.1.1,3.3.2|31.824|Estructura y envolvente de la terminal construidas
1.2.2|240|1.2.1:SS+150|8.860|Salas de espera, circulación y áreas de apoyo terminadas
1.2.3|250|1.2.1:SS+160|22.484|Instalaciones eléctricas, hidráulicas, climatización y contra incendio recibidas
1.2.4|130|1.2.2,1.2.3|15.495|Puentes de abordaje, mobiliario y equipos instalados
1.2.5|135|1.2.2:SS+100|0.330|Accesibilidad universal, movilidad del cuidado y criterios de sostenibilidad incorporados
1.3.1|250|1.1.2,3.3.2,3.4.1,3.4.2|7.610|Plataforma de posiciones de contacto construida
1.3.2|220|1.6.2,1.1.2,3.3.2,3.4.1,3.4.2|7.081|Plataforma de posiciones remotas construida
1.3.3|110|1.3.1,1.3.2|0.390|Señalización, luces y torres de iluminación de plataforma instaladas
1.4.1|220|1.1.2,3.3.2,3.4.1,3.4.2|7.800|Pavimento y hombros de la calle Foxtrot construidos
1.4.2|70|1.4.1|0.325|Señalización y balizamiento de la calle Foxtrot instalados
1.5.1|370|1.1.3,3.4.1,3.4.2|53.99923812|Edificio de estacionamiento construido
1.5.2|140|1.5.1:SS+250|6.401|Sistemas de acceso, tráfico y áreas de alquiler instalados
1.5.3|160|1.5.1:SS+195|3.802|Sistema de generación solar instalado
1.6.1|190|1.1.4,3.3.2,3.4.1,3.4.2|9.000|Edificio del SSEI y vías de acceso construidos
1.6.2|35|1.6.1|0.474|SSEI en funcionamiento en la nueva ubicación
1.7.1|0|3.4.1,3.4.2|6.659|Supervisión de la terminal y del estacionamiento ejecutada
1.7.2|0|3.4.1,3.4.2|1.520|Supervisión de plataformas, calle Foxtrot y SSEI ejecutada
1.7.3|0|3.4.1,3.4.2,3.3.1|0.440|PGAS de construcción implementado
1.7.4|90|1.2.1,1.2.4,1.2.5,1.3.3,1.4.2,1.5.1,1.5.2,1.5.3,1.6.2,1.7.1,1.7.2,1.7.3|0.17476188|Planos de obra ejecutada y actas de recepción aprobados
2.1|150|3.4.3,3.2.1|0.800|Plan estratégico del sistema aeronáutico aprobado
2.2.1|210|3.4.3,2.1|2.700|Plan Maestro Aeroportuario actualizado y aprobado
2.2.2|45|2.2.1|0.300|Funcionarios capacitados en planificación, gestión y operación
2.3.1|95|3.4.3|0.120|Estrategia BIM aprobada
2.3.2|65|2.3.1|0.060|Personal de ingeniería capacitado en BIM
2.4|160|3.4.3|0.350|Estudio de conectividad terrestre entregado
2.5|160|3.4.3|0.350|Estudio de diversificación de destinos entregado
2.6.1|100|1.2.4,1.2.5,1.5.1,1.5.3|0.060|Auditoría para la certificación EDGE realizada
2.6.2|50|2.6.1:SS|0.035|Personal capacitado en certificación EDGE
2.7|160|3.4.3|0.100|Estudio de separación de flujos entregado
2.8|135|3.4.3|0.100|Estudio de movilidad interna entregado
2.9|150|3.4.3|0.025|Programa de igualdad e inclusión ejecutado
3.1.1|50||4.071|Unidad ejecutora conformada y en funciones
3.1.2|35|3.3.1|0|Reglamento operativo vigente
3.1.3|25|3.1.2|0|Convenio de transferencia de recursos vigente
3.1.4|15|3.1.3|0|Cuenta especial aperturada
3.2.1|35|3.1.1|0|Plan de ejecución plurianual aprobado
3.2.2|0|3.2.1|0|Planes operativos anuales aprobados
3.2.3|35|3.2.1|0|Plan de adquisiciones aprobado
3.3.1|45|3.1.1|0|Sistema de gestión ambiental y social y plan de acción vigentes
3.3.2|45|1.1.2,3.3.1|0.090|Protocolo de seguridad operacional aprobado por la AAC
3.3.3|0|3.3.1|0.140|Mecanismo de quejas y reclamos en operación
3.3.4|0|3.4.1,3.4.2,3.3.1|0.260|Informes de cumplimiento socioambiental presentados
3.4.1|195|1.1.1,1.1.2,1.1.3,1.1.4,3.2.3,3.1.2|0|Contratos de obras del Componente I firmados
3.4.2|85|3.2.3,3.3.1,3.1.2|0|Contrato de supervisión firmado
3.4.3|100|3.2.3,3.1.2|0|Contratos de consultorías del Componente II firmados
3.4.4|0|3.1.1|0|Contratos de la unidad ejecutora, evaluación y auditoría firmados
3.5.1|0|3.1.4|0|Desembolsos justificados e informes financieros presentados
3.5.2|0|3.1.4|0.350|Auditorías externas emitidas
3.5.3|0|3.4.1|0.300|Evaluaciones de medio término y de cierre realizadas
3.5.4|85|1.7.4,2.2.2,2.3.2,2.4,2.5,2.6.1,2.6.2,2.7,2.8,2.9,3.3.3,3.3.4,3.4.4|0.12|Informe de terminación y cierre administrativo del programa
'''

# Paquetes de nivel de esfuerzo (duracion 0 en RAW): empiezan con sus precedencias y terminan con el ultimo de sus
# paquetes de referencia, sin empujarlos. Se calculan en este orden y se exportan con la duracion resultante.
WORKS = ['1.2.1', '1.2.2', '1.2.3', '1.2.4', '1.2.5', '1.3.1', '1.3.2', '1.3.3', '1.4.1', '1.4.2',
         '1.5.1', '1.5.2', '1.5.3', '1.6.1', '1.6.2']
HAMMOCKS = {
    '1.7.1': ['1.2.4', '1.2.5', '1.5.2', '1.5.3'],  # supervision de las obras que supervisa
    '1.7.2': ['1.3.3', '1.4.2', '1.6.2'],
    '1.7.3': WORKS,  # el PGAS acompana todas las obras
    '3.3.3': WORKS,  # el mecanismo de quejas opera hasta el fin de las obras
    '3.3.4': WORKS,
    '3.2.2': ['1.7.4'],  # un POA por ano hasta la recepcion de obras
    '3.5.1': ['1.7.4'],  # desembolsos desde H02 hasta los ultimos pagos de obra; la justificacion final va en 3.5.4
    '3.5.2': ['1.7.4'],  # auditorias anuales; los estados financieros auditados finales se entregan en el cierre 3.5.4
    '3.5.3': None,  # termina con el informe de la evaluacion final
    '3.4.4': None,  # termina con la firma del contrato de la evaluacion final
}
# Evaluaciones (3.5.3), segun el plan MEL (EER#2): la de medio termino se presenta al cumplirse el 50% del tiempo de
# ejecucion o 60 dias despues de ejecutado el 50% de los recursos, lo que ocurra primero; la final, 90 dias despues de
# ejecutado el 95%. El contrato se firma EVAL_FIRMA dias laborables antes del informe y el proceso (SCC) inicia
# EVAL_PROCESO dias laborables antes de la firma.
EVAL_FIRMA, EVAL_PROCESO = 45, 60

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

# Hitos: (id, nombre, paquetes cuya terminacion lo habilita)
MILESTONES = [
    ('H01', 'Unidad Ejecutora conformada', ['3.1.1']),
    ('H02', 'Condiciones previas al primer desembolso cumplidas (ROP, convenio, cuenta)', ['3.1.4']),
    ('H03', 'Contratos de obra y de supervisión firmados', ['3.4.1', '3.4.2']),
    ('H04', 'Protocolo de seguridad operacional aprobado por la AAC', ['3.3.2']),
    ('H05', 'SSEI reubicado y en funcionamiento', ['1.6.2']),
    ('H06', 'Plataforma de posiciones remotas concluida', ['1.3.2']),
    ('H07', 'Terminal ampliada concluida y equipada', ['1.2.4', '1.2.5']),
    ('H08', 'Estacionamiento con sistema solar concluido', ['1.5.2', '1.5.3']),
    ('H09', 'Obras recibidas (planos de obra ejecutada y actas aprobados)', ['1.7.4']),
    # 3.2.2 y 3.5.1 a 3.5.3 se enlazan al hito de cierre para no quedar sin sucesor, sin volverse criticos
    ('H10', 'Cierre administrativo del programa', ['3.5.4', '3.2.2', '3.5.1', '3.5.2', '3.5.3']),
]

rows = []
for line in RAW.strip().splitlines():
    code, dur, deps, cost, name = line.split('|', 4)
    rows.append({'code': code, 'name': name, 'dur': int(dur), 'deps': deps, 'budget': float(cost)})
byid = {r['code']: r for r in rows}
assert len(rows) == len(byid) == 54

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

# ---- precedencias ----
pred = {}
for r in rows:
    pred[r['code']] = []
    for part in filter(None, r['deps'].split(',')):
        a, _, rel = part.partition(':')
        kind, lag = 'FS', 0
        if rel:
            kind = rel[:2]
            lag = int(rel.split('+', 1)[1]) if '+' in rel else 0
        pred[r['code']].append((a, kind, lag))
succ = {c: [] for c in byid}
for c, ps in pred.items():
    for a, kind, lag in ps:
        succ[a].append((c, kind, lag))

dur = {r['code']: r['dur'] for r in rows}

@functools.lru_cache(None)
def ES(c: str) -> int:
    v = 0
    for a, kind, lag in pred[c]:
        v = max(v, ES(a) + lag if kind == 'SS' else ES(a) + dur[a] + lag)
    return v

def EF(c: str) -> int:
    return ES(c) + dur[c]

for c, ends in HAMMOCKS.items():
    # 3.5.3 y 3.4.4 dependen de las fechas de las evaluaciones, que salen de la curva S: se fijan despues (set_eval_dates)
    dur[c] = 1 if ends is None else max(EF(e) for e in ends) - ES(c)
    byid[c]['dur'] = dur[c]
    assert dur[c] > 0, c
    ES.cache_clear()
END = max(EF(c) for c in byid)

@functools.lru_cache(None)
def LF(c: str) -> int:
    v = END
    for s, kind, lag in succ[c]:
        ls = LF(s) - dur[s]
        v = min(v, ls - lag if kind == 'FS' else ls - lag + dur[c])
    return v

for r in rows:
    c = r['code']
    r['es'], r['ef'] = ES(c), EF(c)
    r['start'], r['finish'] = workday(ES(c)), workday(EF(c) - 1)
    r['float'] = LF(c) - EF(c)
    r['critical'] = r['float'] == 0
assert all(r['float'] >= 0 for r in rows)
PROJECT_END = workday(END - 1)
assert byid['1.3.2']['es'] >= byid['1.6.2']['ef'], 'SSEI debe estar operativo antes de la plataforma remota'

# ---- hitos ----
milestones = []
for hid, name, preds in MILESTONES:
    idx = max(byid[p]['ef'] for p in preds) - 1
    milestones.append({'id': hid, 'name': name, 'preds': preds, 'date': workday(idx)})

# ---- costos: contingencia prorrateada en obras fisicas 1.2 a 1.6 ----
is_works = lambda c: any(c.startswith(f'1.{i}.') for i in range(2, 7))
factor = (WORKS_TOTAL_MUSD - CONTINGENCY_MUSD) / WORKS_TOTAL_MUSD
for r in rows:
    c = r['code']
    r['base'] = r['budget'] * (factor if is_works(c) else 1)
    r['contingency'] = r['budget'] - r['base']
assert abs(sum(r['budget'] for r in rows) - TOTAL_MUSD) < 1e-7
for k, v in (('1', 184.669), ('2', 5.0), ('3', 5.331)):
    assert abs(sum(r['budget'] for r in rows if r['code'][0] == k) - v) < 1e-7, k
assert abs(sum(r['contingency'] for r in rows) - CONTINGENCY_MUSD) < 1e-7

SUPPLY = {'1.2.4', '1.3.3', '1.4.2', '1.5.2', '1.5.3', '1.6.2', '1.7.4'}
ONGOING = {'1.7.1', '1.7.2', '1.7.3', '3.3.4', '3.3.3', '3.1.1'}
for r in rows:
    c = r['code']
    typ = 'civil' if is_works(c) else ('consulting' if c.startswith('2.') else 'operations')
    if c in SUPPLY: typ = 'equipment'
    if c in ONGOING: typ = 'operations'
    if c in ('3.5.2', '3.5.3'): typ = 'audit'
    if c == '3.5.4': typ = 'consulting'
    r['profile'] = typ
    # la UEP se paga durante todo el programa, no solo los 35 dias de su conformacion
    r['cf_es'], r['cf_ef'] = (0, END) if c == '3.1.1' else (r['es'], r['ef'])

def piece(t, anchors):
    if t <= 0: return 0
    if t >= 1: return 1
    for (x0, y0), (x1, y1) in zip(anchors, anchors[1:]):
        if t <= x1: return y0 + (y1 - y0) * (t - x0) / (x1 - x0)
    return 1

def profile(r, t):
    p = r['profile']
    if p == 'civil': return t * t * (3 - 2 * t)
    if p == 'equipment': return piece(t, [(0, 0), (.15, .15), (.4, .5), (.8, .85), (1, 1)])
    if p == 'consulting': return piece(t, [(0, 0), (.249, 0), (.25, .2), (.649, .2), (.65, .6), (.999, .6), (1, 1)])
    if p == 'audit':
        return piece(t, [(0, 0), (.2, 0), (.201, .25), (.45, .25), (.451, .5), (.7, .5), (.701, .75), (.95, .75), (.951, 1), (1, 1)])
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

def build_monthly(eval_idx):
    """Curva mensual. El costo de 3.5.3 se reparte por mitades al presentar cada informe de evaluacion."""
    out, prev = [], 0.0
    for y, m in months:
        last = month_end(y, m)
        done = wd_index(last) + 1 if last.weekday() < 5 else wd_index(last)
        comp = {k: 0.0 for k in '123'}
        base = cont = 0.0
        for r in rows:
            f = sum(0.5 for i in eval_idx if done > i) if r['code'] == '3.5.3' else profile(r, frac(r, last))
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

def eval_dates(curve):
    """Indices de dia laborable de los informes de medio termino y final (plan MEL)."""
    def reached(p):
        y, m = map(int, next(x['mes'] for x in curve if x['acumulado_linea_base_musd'] >= TOTAL_MUSD * p - 1e-6).split('-'))
        return month_end(y, m)
    mid = min(END // 2, last_workday(reached(.5) + timedelta(days=60)))
    return (mid, last_workday(reached(.95) + timedelta(days=90)))

eval_idx = (END // 2, END - 1)
for _ in range(5):  # punto fijo: el costo de 3.5.3 depende de las fechas que a su vez salen de la curva
    monthly = build_monthly(eval_idx)
    new = eval_dates(monthly)
    if new == eval_idx: break
    eval_idx = new
else:
    raise RuntimeError('las fechas de evaluacion no convergen')
evals = [{'tipo': t, 'informe': i, 'firma': i - EVAL_FIRMA, 'inicio': i - EVAL_FIRMA - EVAL_PROCESO}
         for t, i in zip(('Medio término', 'Final'), eval_idx)]

# 3.5.3 termina con el informe final y 3.4.4 con la firma de su contrato. Ninguno tiene sucesores que puedan moverse.
for c, target in (('3.5.3', eval_idx[1] + 1), ('3.4.4', evals[1]['firma'] + 1)):
    r = byid[c]
    dur[c] = r['dur'] = target - r['es']
    r['ef'] = target
    r['finish'] = workday(target - 1)
    assert dur[c] > 0, c
ES.cache_clear()
LF.cache_clear()
assert max(EF(c) for c in byid) == END and all(EF(c) == byid[c]['ef'] for c in byid)
for r in rows:
    r['float'] = LF(r['code']) - r['ef']
    r['critical'] = r['float'] == 0
assert byid['3.5.3']['float'] > 0 and byid['3.4.4']['float'] > 0
for h in milestones:
    h['date'] = workday(max(byid[p]['ef'] for p in h['preds']) - 1)
assert abs(monthly[-1]['acumulado_linea_base_musd'] - TOTAL_MUSD) < 1e-4, monthly[-1]
assert all(b['acumulado_linea_base_musd'] >= a['acumulado_linea_base_musd'] for a, b in zip(monthly, monthly[1:]))

annual = []
for yr in sorted({int(x['mes'][:4]) for x in monthly}):
    sub = [x for x in monthly if x['mes'].startswith(str(yr))]
    annual.append({'anio': yr, 'gasto_anual_musd': round(sum(x['gasto_mensual_musd'] for x in sub), 3),
                   'acumulado_musd': round(sub[-1]['acumulado_linea_base_musd'], 3), 'avance_pct': round(sub[-1]['avance_pct'], 1)})

# ---- CSV ----
def write_csv(name, fields, data):
    with (OUT / name).open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(data)

write_csv('cronograma_paquetes.csv',
          ['code', 'name', 'dur', 'deps', 'start', 'finish', 'float', 'critical', 'budget', 'base', 'contingency', 'profile'],
          [{**r, 'dur': r['dur'], 'float': r['float'], 'critical': 'si' if r['critical'] else '',
            'budget': f"{r['budget']:.8f}", 'base': f"{r['base']:.8f}", 'contingency': f"{r['contingency']:.8f}"} for r in rows])
write_csv('hitos.csv', ['id', 'name', 'preds', 'date'],
          [{'id': h['id'], 'name': h['name'], 'preds': ','.join(h['preds']), 'date': h['date']} for h in milestones])
write_csv('curva_s_mensual.csv', list(monthly[0]), monthly)
write_csv('curva_s_anual.csv', list(annual[0]), annual)

# ---- XML MSPDI para Open Planner Studio / MS Project ----
def depth(code): return code.count('.') + 1
leafs = sorted(rows, key=lambda r: [int(p) for p in r['code'].split('.')])
nodes = [(c, n, True) for c, n in SUMMARIES.items()] + [(r['code'], r['name'], False) for r in leafs]
nodes.sort(key=lambda x: [int(p) for p in x[0].split('.')] + [0 if x[2] else 1])
nodes = sorted(nodes, key=lambda x: ([int(p) for p in x[0].split('.')], 0 if x[2] else 1))
uid = {'__root__': 0}
for i, (c, n, s) in enumerate(nodes, start=1): uid[c] = i
hito_summary_uid = len(nodes) + 1
for j, h in enumerate(milestones, start=1): uid[h['id']] = hito_summary_uid + j

def span(prefix):
    sub = [r for r in rows if r['code'] == prefix or r['code'].startswith(prefix + '.')]
    return min(r['es'] for r in sub), max(r['ef'] for r in sub)

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
for c, n, is_sum in nodes:
    lvl = depth(c) + 0
    if is_sum:
        a, b = span(c)
        x.append(f'<Task><UID>{uid[c]}</UID><ID>{uid[c]}</ID><Name>{escape(n)}</Name><WBS>{c}</WBS><OutlineLevel>{lvl}</OutlineLevel>'
                 f'<Start>{iso(a)}</Start><Finish>{iso(b - 1, True)}</Finish><Duration>{hrs(b - a)}</Duration><DurationFormat>7</DurationFormat>'
                 '<Milestone>0</Milestone><Summary>1</Summary><PercentComplete>0</PercentComplete></Task>')
    else:
        r = byid[c]
        links = ''
        for a, kind, lag in pred[c]:
            t = 3 if kind == 'SS' else 1
            links += (f'<PredecessorLink><PredecessorUID>{uid[a]}</PredecessorUID><Type>{t}</Type>'
                      f'<LinkLag>{lag * 4800}</LinkLag><LagFormat>7</LagFormat></PredecessorLink>')
        if r['budget'] > 0:
            note = f'Costo en la línea base: US$ {r["budget"]:.3f} millones' + (f', de los cuales US$ {r["contingency"]:.3f} millones son contingencia.' if r['contingency'] > 0 else '.')
        else:
            note = 'Ejecutado por el personal de la UEP, sin costo adicional en la línea base.'
        if c in HAMMOCKS:
            ends = HAMMOCKS[c]
            ref = ('el informe de la evaluación final' if c == '3.5.3' else
                   'la firma del contrato de la evaluación final' if ends is None else
                   'el fin de las obras' if ends == WORKS else 'el fin de ' + ', '.join(ends))
            note += f' Tarea de nivel de esfuerzo: su duración se fijó para terminar con {ref}.'
        x.append(f'<Task><UID>{uid[c]}</UID><ID>{uid[c]}</ID><Name>{escape(n)}</Name><WBS>{c}</WBS><OutlineLevel>{lvl}</OutlineLevel>'
                 f'<Start>{iso(r["es"])}</Start><Finish>{iso(r["ef"] - 1, True)}</Finish><Duration>{hrs(r["dur"])}</Duration><DurationFormat>7</DurationFormat>'
                 f'<Milestone>0</Milestone><Summary>0</Summary><PercentComplete>0</PercentComplete><Notes>{escape(note)}</Notes>{links}</Task>')
hs, he = min(wd_index(h['date']) for h in milestones), max(wd_index(h['date']) for h in milestones)
x.append(f'<Task><UID>{hito_summary_uid}</UID><ID>{hito_summary_uid}</ID><Name>Hitos del programa</Name><WBS>H</WBS><OutlineLevel>1</OutlineLevel>'
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
crit = [r['code'] for r in sorted(rows, key=lambda r: r['es']) if r['critical']]
peak = max(monthly, key=lambda r: r['gasto_mensual_musd'])
summary = {'inicio': PROJECT_START, 'fin': PROJECT_END, 'dias_laborables': END, 'ruta_critica': crit,
           'pico_mensual': peak, 'anual': annual, 'hitos': [{**h, 'date': h['date']} for h in milestones],
           'tareas_xml': 1 + len(nodes) + 1 + len(milestones),
           'evaluaciones': [{'tipo': e['tipo'], 'inicio_proceso': workday(e['inicio']), 'firma': workday(e['firma']),
                             'informe': workday(e['informe'])} for e in evals],
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
    ax.plot(xs, [r['acumulado_linea_base_musd'] for r in monthly], color='#1f4e79', linewidth=2, label='Línea base con contingencia')
    ax.plot(xs, [r['acumulado_sin_contingencia_musd'] for r in monthly], color='#8a8f98', linewidth=2, label='Sin contingencia')
    ax.axhline(TOTAL_MUSD, color='#c9cdd3', linewidth=1, linestyle=(0, (4, 3)))
    ax.text(xs[0], TOTAL_MUSD + 2.5, 'Presupuesto autorizado US$195 M', fontsize=9, color='#4a4f57')
    ax.annotate(f"US$195.0 M", (xs[-1], TOTAL_MUSD), xytext=(-6, -14), textcoords='offset points', ha='right', fontsize=9, color='#1f4e79')
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

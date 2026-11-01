#!/usr/bin/env python3
"""Genera docs/cronograma-y-curva-s.md con los resultados de build_planificacion.py.

Lee resumen.json, hitos.csv, cronograma_actividades.csv, curva_s_anual.csv, requisitos_financiamiento.csv y
actividades.csv (O, M y P de cada actividad, para la reserva de contingencia del cronograma).
"""
from __future__ import annotations
import csv
import json
import math
import sys
from datetime import date, timedelta
from pathlib import Path

sys.dont_write_bytecode = True  # no dejar __pycache__ en el repositorio
HERE = Path(__file__).resolve().parent
OUT = HERE.parent / 'docs' / 'cronograma-y-curva-s.md'
MES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
MESL = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

R = json.loads((HERE / 'resumen.json').read_text(encoding='utf-8'))
rd = lambda f: list(csv.DictReader((HERE / f).open(encoding='utf-8-sig')))
hitos, acts, anual, fin = rd('hitos.csv'), rd('cronograma_actividades.csv'), rd('curva_s_anual.csv'), rd('requisitos_financiamiento.csv')
pert = {a['codigo']: a for a in rd('actividades.csv')}
mensual = rd('curva_s_mensual.csv')
A = {a['code']: a for a in acts}


def d(s: str) -> date:
    return date.fromisoformat(s[:10])


def fd(s: str) -> str:
    x = d(s)
    return f'{x.day}-{MES[x.month - 1]}-{x.year}'


def fl(s: str) -> str:
    x = d(s)
    return f'{x.day} de {MESL[x.month - 1]} de {x.year}'


def ml(ym: str) -> str:
    y, m = map(int, ym[:7].split('-'))
    return f'{MESL[m - 1]} de {y}'


def wd_add(start: date, n: int) -> date:
    x = start
    while n > 0:
        x += timedelta(days=1)
        if x.weekday() < 5:
            n -= 1
    return x


crit = R['ruta_critica']
# Reserva de contingencia del cronograma (clase 5): desviacion PERT de la ruta critica, sigma = (P - O) / 6 por actividad.
sig = math.sqrt(sum(((int(pert[c]['P']) - int(pert[c]['O'])) / 6) ** 2 for c in crit if pert[c]['O']))
res80, res90 = math.ceil(0.8416 * sig), math.ceil(1.2816 * sig)
FIN = d(R['fin'])
near = sorted((a for a in acts if 0 < int(a['float']) <= 10), key=lambda a: (int(a['float']), a['code']))
loe = sum(1 for c in pert.values() if c['tecnica'] == 'Nivel de esfuerzo')
nres = sum(1 for c in pert.values() if c['restriccion'])
q = R['sensibilidad_dhss']
ev = R['evaluaciones']
peak = R['pico_mensual']
F = {r['semestre']: r for r in fin}
fv = lambda k, c: float(F[k][c])
BAC, EST, CONT, GEST, PRES, LOAN = (R[k] for k in ('bac_musd', 'estimacion_pert_musd', 'contingencia_musd', 'reserva_gestion_musd', 'presupuesto_musd', 'prestamo_musd'))
H = {h['id']: h for h in hitos}
GRP = [('la terminal', ('1.2.',)), ('el estacionamiento y el sistema solar', ('1.5.',)), ('las plataformas y la calle Foxtrot', ('1.3.', '1.4.')),
       ('el SSEI', ('1.6.',)), ('la supervisión de las obras', ('1.7.',)), ('las consultorías del Componente II', ('2.',))]
UEP_CODE = '3.1.1-06'
months = [m['mes'] for m in mensual]
cum = [float(m['acumulado_linea_base_musd']) for m in mensual]
pvm = [float(m['gasto_mensual_musd']) for m in mensual]
quart = {q: months[next(i for i, c in enumerate(cum) if c >= BAC * q / 100 - 1e-6)] for q in (25, 50, 75, 90)}
SENS_Q = q
ncost = sum(1 for a in acts if float(a['budget']) > 0)
uep_total = float(A[UEP_CODE]['budget'])


def jy(items):
    items = list(items)
    return items[0] if len(items) == 1 else ', '.join(items[:-1]) + ' y ' + items[-1]


def weekdays(a, b):
    return sum(1 for i in range((b - a).days + 1) if (a + timedelta(days=i)).weekday() < 5)


def mend(ym):
    y, m = map(int, ym.split('-'))
    return date(y + m // 12, m % 12 + 1, 1) - timedelta(days=1)


def month_value(row, ym):
    a, b = d(row['start']), d(row['finish'])
    lo, hi = max(a, d(ym + '-01')), min(b, mend(ym))
    return float(row['budget']) * weekdays(lo, hi) / weekdays(a, b) if hi >= lo else 0.0


def remaining(row, x):
    a, b = d(row['start']), d(row['finish'])
    return float(row['budget']) * weekdays(max(a, x + timedelta(days=1)), b) / weekdays(a, b) if b > x else 0.0


def hname(h):
    n = H[h]['name']
    return n if n.split()[0].isupper() else n[0].lower() + n[1:]


def crit_desc(codes):
    return ', '.join(f'{c} ({A[c]["name"][0].lower() + A[c]["name"][1:]})' for c in codes)


L = []
w = L.append
w('# Cronograma, ruta crítica y curva S')
w('')
w(f'Cronograma del programa ES-L1173 construido a partir del listado de actividades: {R["actividades"]} actividades con estimación PERT, agrupadas en los 54 paquetes de trabajo de la EDT, y 10 hitos. Los paquetes son filas resumen que empiezan con su primera actividad y terminan con la última. El diagrama de Gantt y la tabla completa con duraciones, fechas, predecesoras y holguras se presentan como anexos.')
w('')
w('## Supuestos del cronograma')
w('')
w('- Calendario de lunes a viernes, 8 horas por día, sin feriados. Inicio el 2 de febrero de 2026, días después de la ratificación del préstamo (29 de enero de 2026).')
w('- La duración de cada actividad es su duración estimada PERT, De = (O + 4M + P) / 6, redondeada al día laborable entero. Las precedencias son las de la tabla de dependencias del listado (fin a inicio, inicio a inicio y fin a fin, con desfase).')
w(f'- {nres} actividades tienen una restricción "no comenzar antes de" con una fecha documentada. Con ellas el cronograma reproduce las fechas reales de 2026: incorporación de la UEP (abril y mayo), Aviso General de Adquisiciones (5 de mayo), avisos de licitación del estacionamiento (4 de septiembre) y de la terminal (8 de octubre), y las firmas que estima el Plan de Adquisiciones 2026-2 para las obras (27 de enero, 24 de abril, 27 de mayo y 22 de julio de 2027) y las supervisiones (3 de febrero, 19 de mayo, 10 de junio y 28 de julio de 2027). El 24 de abril de 2027 es sábado y el calendario del modelo es de lunes a viernes, así que la firma de la terminal cae el viernes {fl(A["3.4.1-12"]["finish"])}.')
w(f'- {loe} actividades de seguimiento son de nivel de esfuerzo (supervisión, PGAS, mecanismo de quejas, informes socioambientales y desembolsos): duran lo que el trabajo que acompañan y no fijan el fin del programa.')
w('- Condiciones del contrato de préstamo reflejadas como dependencias: el Plan de Gestión del Riesgo de Desastres y Cambio Climático final antes de cualquier obra, el protocolo de seguridad operacional aprobado por la AAC antes de las obras del lado aire y el SSEI funcionando antes de la plataforma remota.')
w('- Los supuestos de cada actividad, las inconsistencias entre fuentes y las fuentes están en las secciones 9 a 11 del listado de actividades.')
w('')
w('## Hitos')
w('')
w('| Hito | Fecha |')
w('|---|---|')
for h in sorted(hitos, key=lambda h: h['date']):
    w(f'| {h["id"]} {h["name"]} | {fd(h["date"])} |')
w('')
w('## Ruta crítica')
w('')
w(f'Duración total: {R["dias_laborables"]:,} días laborables, del {fl(R["inicio"])} al {fl(R["fin"])}.')
w('')
w(f'La ruta crítica tiene {len(crit)} actividades: {crit_desc(crit)}.')
w('')
w('Empieza con la licitación de las plataformas y la calle Foxtrot, la última de las cuatro licitaciones de obra, sigue con la construcción de la plataforma de contacto en dos fases y pasa a la terminal, porque los puentes de abordaje se conectan a esa plataforma. Después vienen las pruebas integradas de la terminal, la evaluación final, el último desembolso, los estados financieros finales auditados, el informe de terminación y el cierre administrativo. La evaluación final está en la ruta porque se contrata con el fin de la terminal y el cierre la espera.')
w('')
w('Actividades casi críticas (holgura de 10 días laborables o menos):')
w('')
w('| Actividad | Holgura (dl) |')
w('|---|---:|')
for a in near:
    w(f'| {a["code"]} {a["name"]} | {a["float"]} |')
w('')
w('## Reserva de contingencia del cronograma')
w('')
w(f'La clase 5 (Góchez de Peñate, 2026) pide una reserva de tiempo explícita. Con la estimación de tres valores, la desviación de cada actividad es σ = (P − O) / 6, y la de la ruta crítica es la raíz de la suma de los cuadrados de sus actividades: σ = {sig:.1f} días laborables. Para cumplir el fin con 80% de probabilidad se agregan {res80} días laborables (0.84 σ), es decir hasta el {fl(wd_add(FIN, res80).isoformat())}; con 90% de probabilidad, {res90} días laborables (1.28 σ), hasta el {fl(wd_add(FIN, res90).isoformat())}. La reserva no se reparte entre las actividades: la administra el coordinador del programa y se consume solo si se materializan los atrasos. Es una aproximación: supone actividades independientes y no considera que una ruta casi crítica pueda volverse crítica.')
w('')
w('## Curva S')
w('')
w(f'La curva muestra el valor planificado acumulado, no desembolsos ni pagos. Su total es la línea base de costos (BAC) de US${BAC:.1f} millones: la estimación propia de los paquetes de trabajo (US${EST:.1f} millones, valor esperado PERT) más la reserva de contingencia (US${CONT:.1f} millones, percentil 80). Con la reserva de gestión (US${GEST:.1f} millones, fuera de la línea base) el presupuesto del proyecto suma US${PRES:.1f} millones, US${LOAN - PRES:.1f} millones por debajo del préstamo de US${LOAN:.0f} millones. La composición de la estimación y sus fuentes se detallan en la estimación de costos.')
w('')
w(f'Como pide la clase 6 (Góchez de Peñate, 2026), la curva suma mes a mes el costo de las actividades. El costo de cada paquete se asigna a las actividades de quien cobra el contrato (contratista, firma de supervisión, firma consultora o auditor) con pesos por elemento de costo y por actividad según el recurso: movilización y pruebas 2% (3% en las pruebas de 1.2.4-05 del mobiliario y de los sistemas de la terminal), informe final de la supervisión 4%, puentes de abordaje 85% a su fabricación y 11% a su instalación, sistemas de la terminal a su instalación, y el resto de cada elemento entre sus actividades de construcción en proporción a su duración (el listado no da cantidades de obra comparables entre actividades distintas). La supervisión se reparte antes entre sus cuatro contratos según el costo de la obra que supervisa, e incluye el seguimiento del PGAS y el apoyo a las recepciones. Las actividades de la UEP, CEPA, el BID y la AAC no tienen costo propio, salvo el costo indirecto de la UEP (US${uep_total:.1f} millones con su contingencia), que lleva la actividad de nivel de esfuerzo 3.1.1-06. El diseño final de la fachada sur de la terminal tampoco tiene costo propio: 1.1.1-06 (del contratista) está dentro del precio del contrato de obra, que es de diseño y construcción (T1), y 1.1.1-07 (de la supervisión) dentro del contrato de supervisión (V1); que lo diseñe el contratista es una inferencia (S-I.8). Tienen costo {ncost} actividades.')
w('')
w('| Año | Gasto del año (US$ M) | Acumulado (US$ M) | Avance |')
w('|---|---:|---:|---:|')
for a in anual:
    w(f'| {a["anio"]} | {float(a["gasto_anual_musd"]):.1f} | {float(a["acumulado_musd"]):.1f} | {float(a["avance_pct"]):.1f}% |')
w('')
w('Interpretación:')
w('')
first = sorted((c for c in R['contratos'] if c['nombre'].startswith('Obra')), key=lambda c: c['firma'])[0]
cum_first = float(next(m['acumulado_linea_base_musd'] for m in mensual if m['mes'] == first['firma'][:7]))
start_txt = jy(f'{c["nombre"][5:]} ({fd(c["inicio"])})' for c in sorted(R['contratos'], key=lambda c: c['inicio']) if c['nombre'].startswith('Obra'))
w(f'- Hasta la firma del primer contrato de obra ({first["nombre"][5:]}, {fl(first["firma"])}) el valor planificado acumulado es de US${cum_first:.1f} millones ({cum_first / BAC:.1%} del total) y es solo de la UEP: la revisión de diseños y la contratación no tienen costo propio. Los cuatro contratos de obra y de supervisión están firmados en H03 ({fl(H["H03"]["date"])}).')
pm = peak['mes']
peak_parts = sorted(((n, sum(month_value(r, pm) for r in acts if r['package'].startswith(pre) and r['code'] != UEP_CODE)) for n, pre in GRP), key=lambda x: -x[1])
pk_i = months.index(pm)
q_acc = jy(f'el {q}% en {ml(m)}' for q, m in quart.items() if months.index(m) <= pk_i)
q_dec = jy(f'el {q}% en {ml(m)}' for q, m in quart.items() if months.index(m) > pk_i)
nxt = months[months.index(first['firma'][:7]) + 1]
w(f'- Aceleración ({ml(nxt)} a {ml(pm)}): las obras se encadenan por contrato, con inicio de obra en {start_txt}. El valor mensual sube de US${pvm[months.index(nxt)]:.1f} millones a US${peak["gasto_mensual_musd"]:.1f} millones, el máximo de todo el programa, en {ml(pm)}, con aportes de {jy(f"{n} (US${v:.1f} millones)" for n, v in peak_parts if v >= 0.05)}. En este tramo se alcanza {q_acc}.')
d90 = mend(quart[90])
done_h = sorted((h for h in ('H05', 'H06', 'H08') if d(H[h]['date']) <= d90), key=lambda h: H[h]['date'])
rem90 = sorted(((n, sum(remaining(r, d90) for r in acts if r['package'].startswith(pre) and r['code'] != UEP_CODE)) for n, pre in GRP[:5]), key=lambda x: -x[1])
cut7 = max((m for m in mensual if m['mes'] <= H['H07']['date'][:7]), key=lambda m: m['mes'])
tail = {k: float(mensual[-1][k]) - float(cut7[k]) for k in ('c1_acumulado_musd', 'c2_acumulado_musd', 'c3_acumulado_musd')}
tail_txt = jy(f'US${tail[k]:.1f} millones {lab}' for k, lab in (('c1_acumulado_musd', 'de la supervisión y la recepción de las obras'), ('c2_acumulado_musd', 'de las consultorías del Componente II'), ('c3_acumulado_musd', 'de la UEP, las auditorías y las evaluaciones')) if tail[k] >= 0.05)
BAC_TAIL = BAC - float(cut7['acumulado_linea_base_musd'])
assert all(d(r['finish']) <= mend(H['H07']['date'][:7]) for r in acts if r['owner'] == 'Contratista de obra' and float(r['budget']) > 0)
w(f'- Desaceleración ({ml(months[pk_i + 1])} a {ml(months[-1])}): el valor mensual baja desde el pico y se alcanza {q_dec}. Al cierre de {ml(quart[90])} ya concluyeron {jy(f"{hname(h)} ({h}, {ml(H[h]["date"][:7])})" for h in done_h)}; quedan por ejecutar {jy(f"{n} (US${v:.1f} millones)" for n, v in rem90 if v >= 0.05)}. Después del fin de la terminal (H07, {fl(H["H07"]["date"])}) quedan US${BAC_TAIL:.1f} millones ({BAC_TAIL / BAC:.1%} de la línea base): {tail_txt}.')
w('')
w('Distribución de cada actividad en el tiempo:')
w('')
w('| Tipo de actividad | Distribución | Fundamento |')
w('|---|---|---|')
w('| Todas las actividades con costo, salvo 3.1.1-06 | Lineal en su duración (días laborables) | Es valor planificado: la forma de S sale de la secuencia del cronograma (pocas actividades al inicio, muchas en paralelo en 2027 y 2028, pocas al cierre), no de una función impuesta. Los pagos contra entrega y los anticipos no están en la curva. |')
w('| Costo indirecto de la UEP (3.1.1-06) | Mensual por puesto desde su contratación | Es un flujo mensual por plaza: siete consultores clave desde abril y mayo de 2026, el técnico de apoyo y la plantilla ampliada del Plan de Adquisiciones desde sus firmas en el cronograma. |')
w('')
SENS_TXT = jy(ml(v['dhss']) for v in q.values())
w(f'Sensibilidad de la forma: con la curva DHSS del Reino Unido para contratos grandes (Hudson, 1978, citado en Ross et al., 2013; C = 0.063, K = 3.344) aplicada a cada contrato de obra en todo su plazo, la curva acumulada cambia como máximo US${abs(R["sensibilidad_dhss_dif_max_musd"]):.1f} millones y el 25%, 50%, 75% y 90% se alcanzan en {SENS_TXT}.')
w('')
w(f'Costo real a la fecha de corte ({fl(R["corte"])}): US${R["costo_real_corte_musd"]:.2f} millones estimados, que son los honorarios mensuales de los siete contratos de la UEP en ejecución (Plan de Adquisiciones 2026-2) por los meses transcurridos desde su inicio. Es un costo incurrido estimado, no un desembolso del BID, que no registra desembolsos publicados. El valor planificado a esa fecha es de US${float(next(m["acumulado_linea_base_musd"] for m in mensual if m["mes"] == R["corte"][:7])):.2f} millones.')
w('')
w('## Requisitos de financiamiento frente a los desembolsos del préstamo')
w('')
pct = R['anticipo_pct']
ad_txt = jy(f'{n} {pct["obra"][g]:.0%} y {pct["sup"][g]:.0%}' for g, n in (('T', 'terminal'), ('E', 'estacionamiento'), ('P', 'plataformas y Foxtrot'), ('S', 'SSEI')))
w(f'El Plan de Ejecución del Programa (PEP, noviembre de 2025; BID, 2025e) reparte los US${LOAN:.0f} millones del préstamo en ocho semestres desde enero de 2026 (hoja Payments Flow). En la hoja Payments, cada contrato recibe un pago en el semestre de su firma, y el porcentaje no es uniforme (obra y supervisión: {ad_txt}). Que ese pago sea un anticipo es una inferencia: los avisos de adquisiciones no lo mencionan. La tabla compara los desembolsos del PEP con los requisitos de financiamiento, que son la línea base más la reserva de gestión (Góchez de Peñate, 2026, clase 6) en proporción al valor planificado de cada semestre, y con los mismos requisitos más ese anticipo, que se paga en el semestre de la firma de cada contrato y se amortiza descontando el mismo porcentaje de cada avance, sobre la base sin contingencia (millones de US$).')
w('')
w('| Semestre | Desembolso PEP | Acumulado PEP | Requisito | Acumulado | Requisito con anticipo | Acumulado | Diferencia acumulada con anticipo (PEP menos requisito) |')
w('|---|---:|---:|---:|---:|---:|---:|---:|')
for r in fin:
    if float(r['desembolso_pep_musd']) == 0 and float(r['requisito_con_anticipo_musd']) == 0:
        continue
    w(f'| {r["semestre"]} | {float(r["desembolso_pep_musd"]):.2f} | {float(r["desembolso_pep_acum_musd"]):.2f} | {float(r["requisito_musd"]):.2f} | {float(r["requisito_acum_musd"]):.2f} | {float(r["requisito_con_anticipo_musd"]):.2f} | {float(r["requisito_con_anticipo_acum_musd"]):.2f} | {float(r["diferencia_con_anticipo_acum_musd"]):.2f} |')
w('')
dmin = min(float(r['diferencia_con_anticipo_acum_musd']) for r in fin if float(r['desembolso_pep_musd']) > 0)
dmax = max(float(r['diferencia_con_anticipo_acum_musd']) for r in fin)
assert dmin > 0, 'el PEP acumulado debe ir por delante del requisito'
yr_pep = {y: sum(float(r['desembolso_pep_musd']) for r in fin if r['semestre'].startswith(str(y))) for y in range(2026, 2031)}
yr_req = {y: sum(float(r['requisito_con_anticipo_musd']) for r in fin if r['semestre'].startswith(str(y))) for y in range(2026, 2031)}
up = [y for y in yr_pep if yr_req[y] > yr_pep[y] + 1.0]
down = [y for y in yr_pep if yr_req[y] < yr_pep[y] - 1.0]
sem_reach = lambda col, p: next(i for i, r in enumerate(fin) if float(r[col]) >= LOAN * p - 1e-6)
lag = [sem_reach('requisito_con_anticipo_acum_musd', p) - sem_reach('desembolso_pep_acum_musd', p) for p in (.25, .5, .75)]
lag_txt = f'{min(lag)} a {max(lag)}' if min(lag) != max(lag) else f'{min(lag)}'
reach = lambda col: jy(f'al {int(p * 100)}% en {fin[sem_reach(col, p)]["semestre"]}' for p in (.25, .5, .75))
w(f'- El monto alcanza: el programa necesita US${BAC:.1f} millones de línea base (US${PRES:.1f} millones con la reserva de gestión) frente a US${LOAN:.0f} millones. La diferencia con el PEP es de calendario, no de monto.')
w(f'- El PEP preveía desembolsar US${fv("2026-S2", "desembolso_pep_acum_musd"):.1f} millones hasta diciembre de 2026, con licitaciones y firmas en 2026. Como el primer contrato de obra se firma el {fl(first["firma"])}, en 2026 el programa solo necesita US${fv("2026-S2", "requisito_con_anticipo_acum_musd"):.1f} millones: los US$29.7 millones que la reforma a la Ley de Presupuesto 2026 asignó al estacionamiento no se ejecutarán ese año y deben pasar al presupuesto de 2027.')
w(f'- Es una reprogramación del PEP, no una falta de fondos: el PEP acumulado va por delante del requisito con anticipo en todos los semestres, entre US${dmin:.1f} y US${dmax:.1f} millones. El PEP llega {reach("desembolso_pep_acum_musd")} del préstamo, y el requisito con anticipo {reach("requisito_con_anticipo_acum_musd")}: un desfase de {lag_txt} semestres. Por año, el PEP prevé US${yr_pep[2027]:.1f} millones en 2027 y US${yr_pep[2028]:.1f} millones en 2028, frente a los US${yr_req[2027]:.1f} y US${yr_req[2028]:.1f} millones que requiere el programa; en {jy(str(y) for y in down)} ocurre lo contrario. Hay que reprogramar el PEP y los POA 2027 y 2028 y las asignaciones de las leyes de presupuesto de {jy(str(y) for y in up)}, y dimensionar los anticipos de fondos que la UEP pide al BID.')
w(f'- El último desembolso se tramita el {fl(R["ultimo_desembolso"])} (3.5.4-02), dentro del plazo original de desembolsos, que vence el {fl(R["fin_plazo_desembolsos"])}: cinco años desde la vigencia, que se supone el {fl(R["vigencia"])} (ratificación D.L. 505; falta la fecha de publicación, cláusula 6.01).')
late = [(r['semestre'], float(r['requisito_con_anticipo_musd'])) for r in fin if date(int(r['semestre'][:4]), 1 if r['semestre'][-1] == '1' else 7, 1) > d(R['ultimo_desembolso']) and float(r['requisito_con_anticipo_musd']) > 0.005]
if late:
    w(f'- El requisito de {jy(f"US${v:.2f} millones en {sem}" for sem, v in late)} cae después del último desembolso ({fl(R["ultimo_desembolso"])}): se cubre con el último anticipo de fondos o con el saldo de la cuenta especial.')
w('')
w('## Evaluaciones')
w('')
EV = {e['tipo']: e for e in ev}
MT, FL = EV['Medio término'], EV['Final']
w(f'La cláusula 5.03(a) del contrato exige presentar la evaluación de medio término a más tardar 60 días después de que se haya desembolsado el 50% de los recursos o haya transcurrido el 50% del tiempo de ejecución planificado, lo que ocurra primero. El plazo no se mide sobre el plazo de desembolsos. El tiempo de ejecución planificado es el del cronograma, del {fl(R["inicio"])} al {fl(R["fin"])}: el 50% se cumple el {fl(MT["hito_50_tiempo"])} y el límite es el {fl(MT["limite_tiempo"])}. Con los requisitos de financiamiento de la tabla (con anticipo y con reserva de gestión), el 50% del préstamo se desembolsa en {ml(MT["hito_50_requisito"])} y el límite es el {fl(MT["limite_requisito"])}. El informe está programado para el {fl(MT["informe"])} (contrato de la evaluación firmado el {fl(MT["firma"])}): {MT["margen_tiempo_dl"]} días laborables antes del límite por tiempo y {MT["margen_dl"]} antes del límite por desembolso, que es el primero, y cumple.')
w('')
w(f'Riesgo: un desembolso no es un gasto. Las Normas Generales (art. 4.07) permiten anticipos de fondos para la liquidez de hasta {R["lead_anticipo_meses"]} meses, así que el 50% desembolsado podría llegar antes que el 50% gastado. Si los desembolsos siguieran el PEP, el 50% llegaría el {fl(MT["hito_50_pep"])} y el plazo vencería el {fl(MT["limite_pep"])}, antes del informe programado. Con un anticipo de {R["lead_anticipo_meses"]} meses, el 50% se desembolsaría en {ml(MT["hito_50_acelerado"])} y el plazo vencería el {fl(MT["limite_acelerado"])}, antes de la firma del contrato de la evaluación. La actividad 3.5.3-01 proyecta el hito con los contratos firmados y la UEP debe pactar con el BID el monto de los anticipos o adelantar la contratación de la evaluación.')
w('')
w(f'La evaluación final vence hasta 90 días después de terminar el plazo original de desembolsos o de desembolsar el 95% del préstamo, lo que ocurra primero. La línea base no llega al 95% del préstamo, así que vence 90 días después del fin del plazo de desembolsos ({fl(R["fin_plazo_desembolsos"])}), es decir el {fl(FL["limite"])}; su informe está programado para el {fl(FL["informe"])}. El plazo de desembolsos de cinco años (cláusula 2.04) cuenta desde la vigencia del contrato (cláusula 6.01), que se supone el {fl(R["vigencia"])}.')
w('')
OUT.write_text('\n'.join(L), encoding='utf-8')
print(f'{OUT.name}: ruta crítica {len(crit)} actividades, sigma {sig:.1f} dl, reserva P80 {res80} dl, P90 {res90} dl, casi críticas {len(near)}')

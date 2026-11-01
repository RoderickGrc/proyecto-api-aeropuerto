#!/usr/bin/env python3
"""Genera docs/listado-actividades.md, el insumo del cronograma: actividades por paquete de trabajo con fase, responsable,
estimacion PERT (O, M, P y De) y tabla de dependencias.

Lee actividades.csv, dependencias.csv y cronograma_paquetes.csv (nombres de los paquetes) de esta carpeta. Valida la lista
(codigos, fases, PERT, referencias y ciclos) antes de escribir.
"""
from __future__ import annotations
import csv
from collections import Counter
from pathlib import Path
import sys

sys.dont_write_bytecode = True  # no dejar __pycache__ en el repositorio
from hitos_programa import HITOS  # noqa: E402

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / 'docs' / 'listado-actividades.md'

acts = list(csv.DictReader((HERE / 'actividades.csv').open(encoding='utf-8-sig')))
deps = list(csv.DictReader((HERE / 'dependencias.csv').open(encoding='utf-8-sig')))
pk = {r['code']: r['name'] for r in csv.DictReader((HERE / 'cronograma_paquetes.csv').open(encoding='utf-8-sig'))}
by = {a['codigo']: a for a in acts}

FASES = ['Inicio', 'Planificación', 'Ejecución', 'Monitoreo y control', 'Cierre']
COMPONENTES = [('1', 'Componente I. Obras y adecuaciones'), ('2', 'Componente II. Fortalecimiento institucional'),
               ('3', 'Administración, evaluación y auditorías')]


# ---- validacion ----
def check() -> None:
    errs = []
    for a in acts:
        c = a['codigo']
        if a['paquete'] not in pk or not c.startswith(a['paquete'] + '-'):
            errs.append(f'{c}: paquete')
        if a['fase'] not in FASES:
            errs.append(f'{c}: fase')
        if a['tecnica'] == 'Nivel de esfuerzo':
            if not a['termina_con'] or any(x not in by for x in a['termina_con'].split(',')):
                errs.append(f'{c}: termina_con')
        elif not int(a['O']) <= int(a['M']) <= int(a['P']):
            errs.append(f'{c}: PERT')
        if any('\u2014' in v for v in a.values()):
            errs.append(f'{c}: raya larga')
    for d in deps:
        if d['sucesora'] not in by or d['predecesora'] not in by:
            errs.append(f'dependencia {d["predecesora"]} -> {d["sucesora"]}')
    for p in pk:
        if not any(a['paquete'] == p for a in acts):
            errs.append(f'paquete {p} sin actividades')
    for _, _, cs in HITOS:
        errs += [f'hito: {c}' for c in cs if c not in by]
    # ciclos (incluye la terminacion de las actividades de nivel de esfuerzo)
    g = {c: [] for c in by}
    for d in deps:
        g[d['predecesora']].append(d['sucesora'])
    for a in acts:
        for t in filter(None, a['termina_con'].split(',')):
            g[t].append(a['codigo'])
    state = {}

    def visit(c):
        state[c] = 1
        for s in g[c]:
            if state.get(s) == 1:
                errs.append(f'ciclo en {c} -> {s}')
            elif s not in state:
                visit(s)
        state[c] = 2

    for c in by:
        if c not in state:
            visit(c)
    if errs:
        raise SystemExit('Errores en el listado:\n' + '\n'.join(errs))


def de(a) -> float | None:
    if a['tecnica'] == 'Nivel de esfuerzo':
        return None
    return (int(a['O']) + 4 * int(a['M']) + int(a['P'])) / 6


def comp(code: str) -> str:
    return code.split('.')[0]


def key(c: str):
    p, n = c.split('-')
    return [int(x) for x in p.split('.')], int(n)


check()
acts.sort(key=lambda a: key(a['codigo']))
deps.sort(key=lambda d: (key(d['sucesora']), key(d['predecesora'])))
fase_n = Counter(a['fase'] for a in acts)
tec_n = Counter(a['tecnica'] for a in acts)
tipo_n = Counter(d['tipo'] for d in deps)
clase_n = Counter(d['clase'] for d in deps)
loe = [a for a in acts if a['tecnica'] == 'Nivel de esfuerzo']
restr = [a for a in acts if a['restriccion']]
preds = {}
for d in deps:
    preds.setdefault(d['sucesora'], []).append(d['predecesora'])

L = []
w = L.append
w('# Listado de actividades del cronograma')
w('')
w(f'Este documento descompone los {len(pk)} paquetes de trabajo de la EDT en {len(acts)} actividades y es el insumo del cronograma del Programa de Modernización del Aeropuerto Internacional de El Salvador (ES-L1173). Para cada actividad indica la fase, el entregable (paquete de trabajo) al que pertenece, el responsable y la estimación de su duración por tres valores (PERT). Al final están la tabla de dependencias, las restricciones de fecha, las actividades de nivel de esfuerzo y los hitos. El cronograma toma de aquí las duraciones y las precedencias; las fechas, la ruta crítica y las holguras se calculan en él.')
w('')
w('## 1. Cómo se obtuvo el listado')
w('')
w('La EDT termina en paquetes de trabajo, que son entregables; las actividades se definen en el cronograma (clase 4, EDT: "La EDT no debe llegar al nivel de actividades"). El desglose sigue los tres pasos de la clase 5 ("Desglose de paquetes en actividades"):')
w('')
w('1. **Identificar las actividades necesarias.** Para cada paquete se listaron las acciones que producen su entregable, a partir del diccionario de la EDT (sección 5) y de los documentos del programa: el Reglamento Operativo (ROP), el contrato de préstamo, el Plan de Ejecución (PEP), el Plan de Adquisiciones 2026-2, los avisos de licitación, el análisis de costos (EEO#3), la evaluación y el plan de gestión ambiental y social (PGAS) y el plan de monitoreo y evaluación (MEL).')
w('2. **Usar verbos de acción.** Cada actividad empieza con un verbo en infinitivo y nombra un objeto concreto ("Construir la estructura de concreto de los niveles 1 a 3 de la terminal", "Obtener la no objeción del BID a los documentos de licitación del SSEI").')
w('3. **Verificar que cada actividad se pueda estimar, secuenciar, asignar y controlar.** Cada una tiene un solo responsable, un resultado verificable, una duración estimada y al menos una relación de precedencia. La duración más probable va de 5 a 130 días laborables; los trabajos más largos se dividieron en etapas o frentes.')
w('')
w('Criterios adicionales:')
w('')
w('- **Actividades recurrentes por periodo.** Los planes operativos anuales, los informes semestrales, las solicitudes de desembolso y las auditorías se desglosan por año o por semestre.')
w('- **Adquisiciones por contrato.** Cada contratación tiene sus propias actividades (preparar documentos, obtener la no objeción del BID, publicar y recibir ofertas o propuestas, evaluar, adjudicar y firmar). Por eso los paquetes 3.4.1 a 3.4.4 tienen más actividades que el resto.')
w('- **Actividades de terceros.** Las no objeciones del BID y las aprobaciones de la AAC son actividades con su propia duración y con el tercero como responsable, porque consumen tiempo del cronograma aunque la UEP no las ejecute.')
w('- **Responsables.** Los puestos de la Unidad Ejecutora (UEP) del diccionario de la EDT, CEPA, los contratistas de obra, las firmas de supervisión y consultoría, el auditor externo, el BID y la AAC.')
w('')
w('### Fases')
w('')
w('Cada actividad se asigna a una de las cinco fases de la administración de proyectos de la clase 1, las mismas que agrupan las actividades en la plantilla RACI de la clase 10:')
w('')
w('| Fase | Qué incluye | Actividades |')
w('|---|---|---:|')
desc = {
    'Inicio': 'Condiciones de arranque del programa: conformar la UEP, aprobar el ROP, suscribir el convenio de transferencia y abrir la cuenta especial.',
    'Planificación': 'Planes (PEP, POA, Plan de Adquisiciones), revisión de diseños, sistemas de gestión ambiental y social, documentos de licitación y términos de referencia.',
    'Ejecución': 'Conducir las adquisiciones (publicar, evaluar, adjudicar y firmar), construir, instalar, elaborar estudios y capacitar.',
    'Monitoreo y control': 'Supervisar las obras, dar seguimiento al PGAS, informar al BID, auditar, evaluar a medio término y revisar productos.',
    'Cierre': 'Recibir las obras, aprobar productos finales, evaluar al cierre, liquidar contratos, presentar los estados financieros finales y el informe de terminación.',
}
for f in FASES:
    w(f'| {f} | {desc[f]} | {fase_n[f]} |')
w(f'| **Total** | | **{len(acts)}** |')
w('')
w('## 2. Estimación de las duraciones')
w('')
w('Todas las duraciones están en días laborables (dl), de lunes a viernes, sin feriados; un mes equivale a unos 21.7 dl. Cada actividad tiene tres valores, según la estimación por tres valores de la clase 5:')
w('')
w('- **O (optimista):** la duración si todo sale bien.')
w('- **M (más probable):** la duración en condiciones normales.')
w('- **P (pesimista):** la duración si se presentan los problemas razonables de ese tipo de trabajo (lluvias, revisiones adicionales, reprocesos).')
w('- **Estimada (De):** De = (O + 4M + P) / 6. El cronograma usa De redondeada al día laborable entero.')
w('')
w('La clase 5 pide además una reserva por contingencia. No se agrega a cada actividad: con O y P se obtiene la desviación de cada actividad, σ = (P − O) / 6, y el cronograma fija con la desviación de la ruta crítica una reserva de tiempo explícita para el programa.')
w('')
w('Los tres valores se fijaron con las técnicas de la clase 5. La columna "Técnica" de cada actividad indica cuál se usó y la columna "Fuente" su fundamento:')
w('')
w('| Técnica | Cuándo se usó | Actividades |')
w('|---|---|---:|')
tdesc = {
    'Dato del programa': 'La duración o la fecha sale de un documento del propio programa: plazos del ROP y del contrato de préstamo, fechas del Plan de Adquisiciones 2026-2 y de los avisos de licitación, plazos de contrato del PEP.',
    'Calibrada': 'La duración se dedujo de dos fechas documentadas del programa (inicio del proceso o apertura de ofertas y firma estimada en el Plan de Adquisiciones 2026-2 o en el PEP), repartiendo el intervalo entre las etapas del proceso. O y P se fijaron un 20% por debajo y por encima.',
    'Análoga': 'Plazos reales de proyectos similares: ampliaciones de terminales, estacionamientos de varios niveles, puentes de abordaje y consultorías equivalentes.',
    'Paramétrica': 'Cantidad de obra por rendimiento: m² de pavimento por mes con el aeropuerto en operación, m² de estructura por mes, cantidades del EEO#3 y del PGAS.',
    'Juicio de expertos': 'Pasos administrativos y técnicos sin dato publicado (revisiones internas, aprobaciones de CEPA, pruebas); la fuente explica el razonamiento.',
    'Nivel de esfuerzo': 'Actividades de acompañamiento (supervisión, seguimiento del PGAS, mecanismo de quejas, informes socioambientales, desembolsos) que no tienen duración propia: empiezan con sus predecesoras y terminan con las actividades que acompañan (sección 6, "Actividades de nivel de esfuerzo"). Se marcan con NE.',
}
for t in ['Dato del programa', 'Calibrada', 'Análoga', 'Paramétrica', 'Juicio de expertos', 'Nivel de esfuerzo']:
    w(f'| {t} | {tdesc[t]} | {tec_n[t]} |')
w('')
w('## 3. Dependencias')
w('')
w('La tabla de dependencias (sección 7) tiene una fila por cada par de actividades relacionadas. Usa los tipos de relación y las clases de dependencia de la clase 5:')
w('')
w(f'- **Tipo de relación:** FI, fin a inicio ({tipo_n["FI"]}); II, inicio a inicio ({tipo_n["II"]}); FF, fin a fin ({tipo_n["FF"]}); IF, inicio a fin ({tipo_n["IF"]}). El desfase está en días laborables; un desfase positivo es una espera y uno negativo, un adelanto. Las relaciones II con desfase permiten superponer etapas de obra, como las instalaciones con la estructura.')
w(f'- **Clase:** obligatoria ({clase_n["Obligatoria"]}), cuando la impone la lógica técnica, el contrato o la norma; discrecional ({clase_n["Discrecional"]}), cuando la decide el equipo; externa ({clase_n["Externa"]}), cuando depende de un tercero (BID, AAC u otra autoridad).')
w(f'- **Restricciones de fecha:** {len(restr)} actividades no pueden comenzar antes de una fecha documentada (sección 6, "Restricciones de fecha"): los avisos de licitación publicados, el inicio de los procesos según el Plan de Adquisiciones 2026-2, la incorporación real de los consultores de la UEP y los periodos que fija el contrato (ejercicios fiscales y semestres).')
w('- **Condiciones del contrato de préstamo que se reflejan como dependencias:** ninguna obra empieza sin el Plan de Gestión del Riesgo de Desastres y Cambio Climático final presentado al BID (cláusula 4.06); ninguna obra del lado aire empieza sin el protocolo de seguridad operacional aprobado por la AAC; y la plataforma de posiciones remotas no empieza hasta que el SSEI esté reubicado y en funcionamiento (Propuesta de Préstamo, párrafo 4.6).')
w('- **Un vínculo por par.** Entre dos actividades hay una sola relación, para que la red se pueda exportar a MS Project y Open Planner. Las actividades sin predecesora son las primeras del programa (Plan de Adquisiciones inicial y contratación de la UEP), y toda actividad sin otra sucesora termina antes del cierre administrativo (3.5.4-06).')
w('')
w('## 4. Cambios respecto del cronograma por paquetes')
w('')
w('- Las duraciones únicas por paquete, que eran estimaciones de planificación sin fuente, se reemplazan por estimaciones PERT por actividad con su fundamento.')
w('- La licitación de obras (3.4.1) se separa en cuatro licitaciones públicas internacionales, una por obra (estacionamiento, terminal, SSEI y plataformas con calle Foxtrot), con las fechas de los avisos publicados y las firmas estimadas en el Plan de Adquisiciones 2026-2. Ninguna tiene precalificación: el plan y los avisos son licitación directa.')
w('- La supervisión (3.4.2 y 1.7.1 a 1.7.2) pasa de un contrato a cuatro, uno por obra, como en el Plan de Adquisiciones 2026-2. La recepción definitiva (1.7.4) también es por contrato, de modo que cada obra se recibe sin esperar a las demás.')
w('- Se agregan el Aviso General de Adquisiciones (5 de mayo de 2026), que precede a todos los procesos, y el diseño de la fachada sur que elabora el contratista de la terminal con la revisión de la supervisión (avisos de 2026).')
w('- Se agrega el Plan de Gestión del Riesgo de Desastres y Cambio Climático final (3.3.1), que el contrato exige antes del inicio de las obras.')
w('- La evaluación de medio término se contrata al firmarse el contrato de obra y el de supervisión del SSEI, para que su informe quede antes del plazo de 60 días posterior al 50% del tiempo de ejecución planificado (S-III.10), y la evaluación final con el fin de la terminal, en lugar de las fechas del PEP de noviembre de 2025. El último desembolso incluye el pago de la evaluación final.')
w('- Las consultorías del Componente II (3.4.3) se contratan por separado, una por producto del PEP. Como no figuran en el Plan de Adquisiciones 2026-2, sus procesos empiezan después de incluirlas en una revisión del plan posterior al 31 de octubre de 2026.')
w('- Todas las contrataciones del Componente II (3.4.3), las evaluaciones y las auditorías (3.4.4) tienen revisión ex ante del BID (Anexo III.i, 2.5; Plan de Adquisiciones 2026-2), con sus no objeciones como actividades del BID. La estrategia y capacitación BIM (2.3.1 y 2.3.2) pasa a lista corta internacional porque su contrato supera los US$200,000 de la tabla 10 del ROP.')
w('- Se agregan la plantilla ampliada de la UEP del Plan de Adquisiciones 2026-2 (21 procesos de consultores individuales, en seis lotes de fechas, 3.4.4-45 a 3.4.4-74) y la actividad de nivel de esfuerzo que administra el programa desde la UEP (3.1.1-06).')
w('- Los paquetes 1.2.5 (accesibilidad y medidas EDGE de la terminal) y 1.6.2 (equipamiento del SSEI) tienen actividades del contratista de obra que ejecutan el trabajo; las de la UEP, CEPA y la supervisión verifican, trasladan o prueban.')
w('- Las auditorías (3.4.4 y 3.5.2) son contratos anuales; la auditoría del último ejercicio queda dentro de la auditoría de los estados financieros finales del cierre (3.5.4).')
w('- Los plazos de obra se estimaron por etapas y se contrastaron con los avisos de licitación, el sondeo de mercado de la terminal, el PEP y obras análogas.')
w('')
w('## 5. Resumen')
w('')
w('| Componente | Paquetes | Actividades | ' + ' | '.join(FASES) + ' |')
w('|---|---:|---:|' + '---:|' * len(FASES))
for k, name in COMPONENTES:
    sub = [a for a in acts if comp(a['paquete']) == k]
    w(f'| {name} | {sum(1 for p in pk if comp(p) == k)} | {len(sub)} | ' + ' | '.join(str(sum(1 for a in sub if a['fase'] == f)) for f in FASES) + ' |')
w(f'| **Total** | **{len(pk)}** | **{len(acts)}** | ' + ' | '.join(f'**{fase_n[f]}**' for f in FASES) + ' |')
w('')
w('## 6. Listado de actividades')
w('')
w('Las actividades se agrupan por entregable (paquete de trabajo de la EDT). El código de cada actividad es el del paquete seguido de un correlativo. O, M, P y Estimada están en días laborables.')
for k, name in COMPONENTES:
    w('')
    w(f'### {name}')
    for p in sorted({a['paquete'] for a in acts if comp(a['paquete']) == k}, key=lambda p: [int(x) for x in p.split('.')]):
        w('')
        w(f'#### {p} {pk[p]}')
        w('')
        w('| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |')
        w('|---|---|---|---|---:|---:|---:|---:|---|---|')
        for a in (x for x in acts if x['paquete'] == p):
            e = de(a)
            o, m, pp, est = (a['O'], a['M'], a['P'], f'{e:.1f}') if e is not None else ('NE', 'NE', 'NE', 'NE')
            w(f'| {a["codigo"]} | {a["actividad"]} | {a["fase"]} | {a["responsable"]} | {o} | {m} | {pp} | {est} | {a["tecnica"]} | {a["fuente"]} |')
w('')
w('### Restricciones de fecha')
w('')
w('| Código | Actividad | No comenzar antes de | Fundamento |')
w('|---|---|---|---|')
for a in restr:
    y, mth, dd = a['restriccion'][4:].split('-')
    w(f'| {a["codigo"]} | {a["actividad"]} | {dd}-{mth}-{y} | {a["nota"] or a["fuente"]} |')
w('')
w('### Actividades de nivel de esfuerzo')
w('')
w('| Código | Actividad | Empieza después de | Termina con |')
w('|---|---|---|---|')
for a in loe:
    w(f'| {a["codigo"]} | {a["actividad"]} | {", ".join(preds.get(a["codigo"], [])) or "Inicio del programa"} | {a["termina_con"].replace(",", ", ")} |')
w('')
w('## 7. Tabla de dependencias')
w('')
w('| Sucesora | Predecesora | Tipo | Desfase (dl) | Clase | Justificación |')
w('|---|---|---|---:|---|---|')
for d in deps:
    w(f'| {d["sucesora"]} | {d["predecesora"]} | {d["tipo"]} | {d["desfase"]} | {d["clase"]} | {d["justificacion"]} |')
w('')
w('## 8. Hitos')
w('')
w('Los hitos tienen duración cero y se cumplen cuando terminan las actividades indicadas.')
w('')
w('| Hito | Nombre | Se cumple al terminar |')
w('|---|---|---|')
for h, n, cs in HITOS:
    w(f'| {h} | {n} | {", ".join(cs)} |')
w('')
w((HERE / 'listado_actividades_fuentes.md').read_text(encoding='utf-8').strip())
w('')
OUT.write_text('\n'.join(L), encoding='utf-8')
print(f'{OUT.name}: {len(acts)} actividades, {len(deps)} dependencias, {len(restr)} restricciones, {len(loe)} de nivel de esfuerzo')

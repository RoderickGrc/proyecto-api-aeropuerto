#!/usr/bin/env python3
"""Genera docs/estimacion-costos.md con los resultados de build_planificacion.py.

Lee resumen.json, estimacion_costos.json, estimacion_costos.csv, curva_s_mensual.csv y las reglas de estimacion_costos.py (esta carpeta);
el texto del documento está en este script. Se ejecuta sin argumentos desde planificacion/ después de build_planificacion.py:
python -B build_estimacion_doc.py
"""
import csv, json, pathlib, sys
sys.dont_write_bytecode = True  # no dejar __pycache__ en el repositorio
PL = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(PL))
import estimacion_costos as EC
R = json.load(open(PL / 'resumen.json', encoding='utf-8'))
E = json.load(open(PL / 'estimacion_costos.json', encoding='utf-8'))
el = {r['id']: r for r in csv.DictReader(open(PL / 'estimacion_costos.csv', encoding='utf-8-sig'))}
U = lambda x: f'{float(x) / 1e6:,.2f}'
m = lambda k: f"{E[k] / 1e6:,.1f}"
uep = E['uep']
uo, um, up = (sum(p[k] for p in uep) for k in 'OMP')
plan = E['plantilla']
mes_min, mes_max = min(p['meses'] for p in uep), max(p['meses'] for p in uep)
plan_pa = sum(x['monto_pa'] for x in plan)
plan_m = sum(x['mensual'] * x['meses'] for x in plan)
PERIODO = E['uep_periodo']
cr = E['contingencia_por_rho']

BASE = {
    'T1': f'{EC.TERMINAL_M2:,} m² × US$1,700 / 2,250 / 2,900 por m²',
    'T2': '6 puentes × US$1.27 / 1.64 / 2.41 M',
    'T3': f'Obras exteriores reales de la Fase 1 prorrateadas por área ({EC.TERMINAL_M2:,} / 21,673 m²): US${EC.EXT_O / 1e6:.2f} / {EC.EXT_M / 1e6:.2f} / {EC.EXT_P / 1e6:.2f} M',
    'T4': 'Sistemas FIDS, CUTE y SATE (US$1.6 / 2.6 / 3.9 M) más 0 / 2 / 4 escáneres CT a US$0.77 M',
    'A1': '47,638 m² × US$130 / 150 / 190 por m²',
    'A2': '20,849 m² × US$90 / 105 / 140 por m²',
    'A3': '22,344 m² × US$90 / 105 / 140 por m²',
    'A4': '2.6 / 8 / 12% del pavimento',
    'E1': f"2,050 plazas × US$9,000 / 12,600 / {float(el['E1']['unit_P']):,.0f} por plaza",
    'E2': '1,920 kWp × US$940 / 1,160 / 1,600 por kWp',
    'S1': '1,200 / 1,600 / 2,630 m² × US$1,700 / 2,100 / 3,200 por m²',
    'V1': '2.0 / 3.0 / 5.0% de las obras',
    'V2': '0.33 / 0.72 / 1.8% de las obras, dentro de los contratos de supervisión',
    'C1': 'Contratos comparables: US$110,000 / 500,000 / 1,900,000',
    'C2': 'Contratos comparables: US$0.43 / 1.07 / 2.66 M',
    'C3': '1 / 1.5 / 2 meses-persona internacionales',
    'C4': 'Contratos comparables: US$150,000 / 209,000 / 500,000',
    'C5': '2 / 3 / 4 meses-persona internacionales y 10 / 15 / 20 nacionales',
    'C6': 'Contratos comparables: US$110,000 / 165,000 / 250,000',
    'C7': 'Tarifa GBCI más 2 / 4 / 6 meses-persona del auditor',
    'C8': '1 / 1.5 / 2 meses-persona internacionales y 8 / 12 / 16 nacionales',
    'C9': '1 / 1.5 / 2 meses-persona internacionales y 8 / 12 / 16 nacionales',
    'C10': '2 / 3 / 4 meses-persona nacionales',
    'U1': f'Planilla mensual de los 8 puestos (US${uo:,} / {um:,} / {up:,}) × meses desde la contratación real de cada puesto ({mes_min:.0f} a {mes_max:.0f})',
    'U3': f'21 procesos 3CV del PA 2026-2 (US${plan_pa / 1e6:.2f} M): monto mensual implícito × meses desde la firma del cronograma; O y P: 0.85 y 1.15 veces',
    'U2': 'Ascendente propio / US$200,000 del Anexo III / ascendente propio',
    'U4': 'Contratos en El Salvador: US$148,000 / 191,000 / 320,000',
    'U5': 'Préstamos BID en El Salvador: US$90,000 / 150,000 / 172,500',
}
assert set(BASE) == set(el), set(el) ^ set(BASE)
pk = lambda s: ', '.join(x.split(' ')[0] for x in s.split('; '))
ACT_TXT = {'1.2.4-01': 'planos de taller', '1.2.4-02': 'fabricación y entrega', '1.2.4-03': 'instalación', '1.2.4-04': 'instalación de mobiliario y sistemas', '1.2.4-05': 'pruebas', '2.6.1-03': 'acompañamiento', '3.5.3-02': 'evaluación de medio término, un tercio', '3.5.3-04': 'evaluación final'}
EL_TXT = {'T1': 'mobiliario de la terminal', 'T2': 'puentes de abordaje', 'T4': 'sistemas de la terminal', 'A1': 'plataformas de concreto', 'A2': 'asfalto', 'C7': 'EDGE', 'U5': 'evaluaciones', 'V2': 'seguimiento del PGAS'}
AUTOTXT = '; '.join(f'las actividades que empiezan por "{p.lower()}" llevan {x:.0%}' for p, x in EC.AUTO)
RULESTXT = []
for (ek, pkk), r in EC.RULES.items():
    parts = []
    if r.get('fixed'):
        parts.append(', '.join(f'{ACT_TXT.get(c, c)} {x:.0%}' for c, x in r['fixed'].items()))
    if r.get('rest'):
        parts.append('el resto, a ' + (ACT_TXT.get(r['rest'][0], r['rest'][0]) if len(r['rest']) == 1 else 'la demolición, la terracería, el drenaje y el pavimento de concreto, actividades 1.3.2-01 a 1.3.2-04, sin el asfalto, que lleva A2' if ek == 'A1' else ', '.join(r['rest'])))
    if r.get('auto') is False:
        parts.append('sin porcentajes de movilización ni de informe final')
    RULESTXT.append(f'{EL_TXT.get(ek, ek)} en {pkk} ({"; ".join(parts)})')
RULESTXT = '; '.join(RULESTXT)
tabla = '\n'.join(f"| {i} | {r['elemento']} | {pk(r['paquetes'])} | {r['metodo']} | {BASE[i]} | {U(r['O_usd'])} | {U(r['M_usd'])} | {U(r['P_usd'])} | **{U(r['E_usd'])}** | {U(r['sigma_usd'])} |" for i, r in el.items())
tabla += f"\n| | **Total** | | | | {U(E['total_O'])} | {U(E['total_M'])} | {U(E['total_P'])} | **{U(E['total_E'])}** | |"
uept = '\n'.join(f"| {p['puesto']} | {p['inicio'][8:]}-{p['inicio'][5:7]}-{p['inicio'][:4]} | {p['meses']:.1f} | {p['O']:,} | {p['M']:,} | {p['P']:,} |" for p in uep)
plant = '\n'.join(f"| {x['proceso']} | {x['puesto']} | {x['monto_pa']:,.0f} | {x['firma_pa'][8:]}-{x['firma_pa'][5:7]}-{x['firma_pa'][:4]} | {x['firma_modelo'][8:]}-{x['firma_modelo'][5:7]}-{x['firma_modelo'][:4]} | {x['mensual']:,.0f} | {x['meses']:.1f} | {x['mensual'] * x['meses']:,.0f} |" for x in plan)
notas = '\n'.join(f"| {i} | {r['nota']} | {r['fuentes']} |" for i, r in el.items())

G, F = E['por_grupo'], E['sin_escalamiento']['por_grupo']
grows = []
for g, v in G.items():
    ref, flat = v['referencia'], F[g]
    esc = v['E'] + v['reserva'] - flat
    if ref:
        grows.append(f"| {g} | {U(flat)} | {U(ref)} | {'+' if flat > ref else ''}{U(flat - ref)} | {U(esc)} | {U(v['E'] + v['reserva'])} |")
    else:
        grows.append(f"| {g} | {U(flat)} | (incluido en supervisión) | | {U(esc)} | {U(v['E'] + v['reserva'])} |")
flat_bac = E['sin_escalamiento']['linea_base']
ref_tot = sum(v['referencia'] for v in G.values() if v['referencia'])
grows.append(f"| **Total** | **{U(flat_bac)}** | **{U(ref_tot)}** | **{U(flat_bac - ref_tot)}** | **{U(E['linea_base'] - flat_bac)}** | **{U(E['linea_base'])}** |")
grupos = '\n'.join(grows)
sens = '\n'.join(f"| {c['supuesto']} | {c['cambio']} | {c['estimacion'] / 1e6:,.2f} | {'+' if c['diferencia'] > 0 else ''}{c['diferencia'] / 1e6:,.2f} | {c['presupuesto'] / 1e6:,.2f} |" for c in E['sensibilidad'])
over = [c for c in E['sensibilidad'] if c['presupuesto'] > 195e6]
sens_pa = next(c['diferencia'] for c in E['sensibilidad'] if 'Plan de Adquisiciones 2026' in c['cambio'] and 'plaza' in c['cambio']) / 1e6
sens_cepa = next(c['diferencia'] for c in E['sensibilidad'] if 'diseño de CEPA 2022' in c['cambio']) / 1e6
src = '\n'.join(f'- **{k}.** {v}' for k, v in E['fuentes'].items())
gap = 195 - E['presupuesto'] / 1e6
PV_CORTE = float(next(r['acumulado_linea_base_musd'] for r in csv.DictReader(open(PL / 'curva_s_mensual.csv', encoding='utf-8-sig')) if r['mes'] == '2026-10'))
flat_gap = flat_bac / 1e6 - 195
esc_tot = (E['linea_base'] - flat_bac) / 1e6
ff = lambda g: F[g] / 1e6
rf = lambda g: G[g]['referencia'] / 1e6
obras_E = sum(G[g]['E'] for g in ('Terminal', 'Lado aire', 'Estacionamiento', 'SSEI')) / 1e6
local_E = sum(float(el[i]['E_usd']) for i in ('T1', 'T3', 'A1', 'A2', 'A3', 'A4', 'E1', 'S1', 'U1', 'U2')) / E['total_E']

RULEBLOCK = f'''**Regla de pesos por elemento y por actividad.** La estimación ascendente costea por recursos (EDT, paquetes, actividades, recursos, cantidades y tarifas), no por duración (PMI, 2017, sección 7.2.2). Cada elemento de costo llega a sus paquetes por su reparto y, dentro de cada paquete, a las actividades de quien cobra el contrato (contratista de obra, firma de supervisión, firma consultora o auditor externo); las actividades de la UEP, CEPA, el BID y la AAC no tienen costo propio. El reparto se verifica: todo paquete con costo tiene actividades de quien cobra, y la suma de sus actividades es igual al costo del paquete. La regla tiene tres pasos:

1. Porcentaje pequeño y explícito por la forma de la actividad: {AUTOTXT}.
2. Pesos fijos según el recurso del elemento: {RULESTXT}.
3. El resto de cada elemento se reparte entre sus actividades de construcción en proporción a su duración, porque el listado no da cantidades de obra comparables entre actividades de distinta naturaleza (cimentación, estructura, instalaciones).

La supervisión técnica (V1) y el seguimiento del PGAS (V2) van a los dos contratos de supervisión (1.7.1 y 1.7.2) y se reparten antes entre los cuatro contratos según el costo de la obra que supervisa; el 2% de V1 que corresponde a las recepciones de obra (1.7.4) queda dentro del 4% del informe final de cada contrato. El escalamiento de cada elemento se lleva al punto medio ponderado de las actividades que lo ejecutan.'''
doc = f'''# Estimación de costos

Estimación propia del costo del programa ES-L1173 por paquete de trabajo de la EDT, asignado después a sus actividades, con las técnicas de estimación de costos (PMI, 2017, sección 7.2.2): estimación análoga, paramétrica, por índices, determinación de tarifas, ascendente y de tres puntos (PERT). No parte del presupuesto del préstamo: usa las cantidades de los documentos del proyecto y precios de referencia con fuente, salvadoreños siempre que existen, y solo al final se compara con los US$195 millones.

## Resultado

| Concepto | US$ M |
|---|---:|
| Estimación de los paquetes de trabajo (valor esperado PERT) | {m('total_E')} |
| Reserva de contingencia (percentil 80) | {m('contingencia')} |
| **Línea base de costos (BAC)** | **{m('linea_base')}** |
| Reserva de gestión (5% de la línea base) | {m('reserva_gestion')} |
| **Presupuesto del proyecto** | **{m('presupuesto')}** |
| Financiamiento autorizado (préstamo) | 195.0 |
| Margen frente al préstamo | {gap:,.1f} |

La línea base es la que reparte la curva S. La reserva de gestión queda fuera de la línea base y, junto con ella, forma el presupuesto del proyecto, como en los componentes del presupuesto del proyecto (PMI, 2017, sección 7.3). La sección 7 explica de dónde sale el margen y qué se hace con él.

## 1. Propósito, plan y características (pasos 1 a 3)

- **Propósito.** Obtener el costo de cada paquete de trabajo y de sus actividades para construir la línea base de costos, la curva S, los requisitos de financiamiento y los montos de la matriz de adquisiciones. Los destinatarios son la Gerencia General de CEPA y el BID, que revisan el Plan de Ejecución (PEP), los POA y el Plan de Adquisiciones.
- **Clase de estimado.** Por su nivel de definición corresponde a la clase 4 de la AACE (RP 18R-97): la terminal, las plataformas y la calle Foxtrot tienen diseños completos, pero el estacionamiento y el SSEI no tienen diseño. En los rangos de exactitud del PMBOK es un estimado de orden de magnitud (PMI, 2017, sección 7.2).
- **Plan de estimación.** En el programa, la estimación la prepara el especialista financiero de la UEP con el especialista en ingeniería aeroportuaria y el coordinador general de obra, durante la elaboración del PEP (paquete 3.2.1, en el primer semestre de 2026). La revisión independiente la hace el especialista de planificación y monitoreo, y la estimación se actualiza con cada POA. En este trabajo se investigaron tres frentes (precios de obra, servicios y honorarios, y distribución del costo en el tiempo) y la estimación tuvo dos revisiones independientes.
- **Características.** Las cantidades salen de los documentos del proyecto y del Plan de Adquisiciones de 2026: 18,555 m² y 6 puentes de abordaje de la terminal (la superficie sale de la solicitud de información de julio de 2026 y de la expresión de interés P00024 de 2026, que describen el proyecto que se licita; el EEO#3, de julio de 2025, usaba 16,303 m² para la Fase 2); las superficies de pavimento del cuadro 11 del EEO#3; 2,050 plazas en 4 niveles del estacionamiento licitado por CEPA en septiembre de 2026; 1,920 kWp del sistema solar (EAS-PGAS, tabla 2); los ocho puestos de la UEP (siete clave de la Propuesta de Préstamo y el técnico de apoyo del ROP) y los 21 procesos de su plantilla ampliada en el Plan de Adquisiciones 2026-2; y las duraciones y fechas del cronograma.

## 2. Técnicas por elemento y lista de verificación (paso 4)

| Técnica | Se usa en | Por qué |
|---|---|---|
| Análoga | Terminal, obras exteriores, sistemas de la terminal, Plan Estratégico, Plan Maestro, BIM, estudio de destinos, auditoría, evaluaciones y plantilla ampliada de la UEP (monto del Plan de Adquisiciones por mes de contrato) | Hay obras o contratos comparables con monto conocido; la terminal, con obras de CEPA en el mismo aeropuerto. |
| Paramétrica | Pavimentos, estacionamiento, sistema solar, SSEI, puentes, escáneres, supervisión y seguimiento del PGAS | Hay una cantidad medible (m², plazas, kWp, unidades o costo de la obra) y un costo unitario de referencia. |
| Por índices | Todas las obras | Los valores históricos se llevan a 2025 y luego a los años de ejecución con un índice compuesto de precios de CASALCO (materiales y mano de obra), como el EEO#3 hizo con los índices del BCR y CASALCO. |
| Determinación de tarifas | Capacitaciones, estudios de conectividad, separación de flujos y movilidad, y EDGE | Se dimensiona el equipo en meses-persona y se multiplica por la tarifa. |
| Ascendente | UEP | Se suman los honorarios de cada puesto por los meses que van de su contratación real al fin de la actividad 3.1.1-06, más los gastos operativos. |
| Tres puntos (PERT) | Todos los elementos | Cada elemento tiene un valor optimista (O), más probable (M) y pesimista (P). E = (O + 4M + P) / 6 y σ = (P − O) / 6. |

Quedan en costo cero, porque los ejecuta el personal de la UEP, CEPA, el BID o la AAC y su costo ya está en 3.1.1: las revisiones de diseños (1.1.x), las verificaciones de accesibilidad y EDGE en obra (1.2.5-01 a 04), el traslado del SSEI y su conformidad (1.6.2-01 a 04), la revisión del PGAS y las recepciones (1.7.3 y 1.7.4), el reglamento, el convenio y la cuenta (3.1.2 a 3.1.4), los planes (3.2.x), el sistema de gestión ambiental y social (3.3.1), el protocolo de la AAC (3.3.2), el mecanismo de quejas y los informes socioambientales (3.3.3 y 3.3.4), las contrataciones (3.4.x), los desembolsos (3.5.1) y el informe de terminación dentro del cierre (3.5.4). El diseño final de la fachada sur de la terminal (1.1.1-06 del contratista y 1.1.1-07 de la supervisión) tampoco lleva costo propio: el diseño del contratista se paga dentro del precio del contrato de obra, que es de diseño y construcción (T1), y su revisión dentro del contrato de supervisión (V1); que lo diseñe el contratista es una inferencia (S-I.8 del listado de actividades). El costo de la UEP lo lleva una sola actividad, 3.1.1-06 (administrar el programa desde la Unidad Ejecutora), de nivel de esfuerzo, del {PERIODO['inicio'][8:]}-{PERIODO['inicio'][5:7]}-{PERIODO['inicio'][:4]} al {PERIODO['fin'][8:]}-{PERIODO['fin'][5:7]}-{PERIODO['fin'][:4]}.

{RULEBLOCK}

Lista de verificación aplicada a cada elemento: tiene cantidad con fuente; tiene precio de referencia con fuente, año y moneda; se llevó a US$ de 2025; se indicó si incluye IVA, indirectos y equipamiento; tiene valores O, M y P; se asignó a paquetes de la EDT; se escaló al punto medio de su ejecución; y los supuestos sin fuente están declarados.

## 3. Reglas, supuestos y clasificación de los costos (paso 5)

- **Jerarquía de fuentes.** Primero, datos salvadoreños: obras de CEPA en el AIES, precios de CASALCO, honorarios publicados en el Portal de Transparencia y préstamos BID de El Salvador. Después, datos de Centroamérica. Solo donde no hay dato local se usa una referencia internacional ajustada, y se dice así: puentes de abordaje, escáneres, sistema solar, la referencia de mercado del estacionamiento y el escenario pesimista del Plan Maestro (Rionegro). Las tarifas de consultoría, la supervisión, la auditoría y las evaluaciones salen de contratos y préstamos en El Salvador. Las referencias de EE. UU. de la terminal y los pavimentos se usan solo como contraste.
- **Moneda e índices.** Todo se expresa en US$ de 2025 sin IVA y después se escala al punto medio de ejecución de cada elemento, ponderado por el peso de sus paquetes, con las fechas de las actividades que llevan el costo. Obras: 1.25% / 2.6% / 5.5% anual en O / M / P, según el índice compuesto de CASALCO (2021 a 2025 y 2024 a 2025) y el alza de los materiales del primer semestre de 2026. Servicios: 1.0% / 2.1% / 2.7%, según el IPC de El Salvador y la proyección del FMI.
- **Localización.** Solo se aplica a las referencias internacionales que se mantienen: equipos importados (puentes) 1.00 / 1.05 / 1.10 por la paridad de maquinaria del ICP del Banco Mundial (1.055); sistema solar 0.75; y la mediana de estacionamientos de WGI, 0.42, según la comparación de costos de construcción de Turner & Townsend (2026). El ICP da una paridad de construcción de 0.168 para El Salvador, pero mide una canasta de toda la construcción del país, en su mayoría vivienda; se usa solo como cota inferior.
- **Impuestos e indirectos.** Las referencias de obra incluyen indirectos y utilidad del contratista; a las obras se suma el IVA del 13% (Ley del IVA, art. 54). Los contratos salvadoreños de servicios que se usan como referencia incluyen el IVA del 13% (como el de la auditoría de PwC, que lo desglosa); los honorarios de la UEP se toman como figuran en el Plan de Adquisiciones. Si el contratista es extranjero, CEPA paga además el IVA del servicio de no domiciliados.
- **Supuestos sin fuente publicada.** Se declaran como supuestos del equipo: la partición del costo de la plataforma de 2016 entre concreto y asfalto (1.2 a 1.5 veces); el balizamiento más probable y pesimista (8 y 12% del pavimento); el 5% del SSEI para traslado y puesta en marcha; el escenario pesimista de los sistemas de la terminal (+50%) y el número de escáneres (0 / 2 / 4); el cálculo propio de O del estacionamiento con precios de CASALCO; los gastos operativos O y P de la UEP; el honorario del técnico de apoyo y del auditor EDGE; los meses-persona de cada estudio; los pesos por actividad de la regla de la sección 2 (porcentajes de movilización, pruebas e informe final, el 85% de la fabricación de los puentes y el 15% del acompañamiento EDGE); la plantilla ampliada de la UEP (mismo plazo de 56 meses del Plan de Adquisiciones y O y P de 0.85 y 1.15 veces); el reparto 70/30 de BIM y 85/15 de EDGE; y la correlación de 0.3 entre elementos.
- **Reparto de la terminal.** El costo del edificio se reparte entre sus paquetes con la estructura de capítulos del presupuesto de diseño de la Fase 2 (cuadro 2 del EEO#3): estructura y envolvente (1.2.1), acabados de salas (1.2.2), instalaciones (1.2.3), mobiliario (1.2.4) y transporte vertical y señalética para accesibilidad (1.2.5). De ese cuadro solo se usan las proporciones.
- **Clasificación de los costos.** Directos: obras, equipos, supervisión, consultorías, auditoría y evaluaciones ({obras_E / E['total_E'] * 1e6:.0%} de la estimación son obras). Indirectos: la UEP, su plantilla ampliada y sus gastos operativos, que sirven a todo el programa y se llevan en la actividad 3.1.1-06. Fijos: la UEP y sus gastos, que no dependen del volumen de obra. Variables: las obras y la supervisión, que crecen con las cantidades.
- **Costos hundidos.** Los diseños de la Fase 2 de la terminal (financiados con el préstamo ES-L1151) y el diseño de CEPA de 2022 para 700 plazas ya se pagaron y no se incluyen; solo se usan como información.
- **Costo de la calidad.** La supervisión, el seguimiento del PGAS, las auditorías y las evaluaciones son costos de prevención y evaluación que se incluyen; los costos de fallas (reparaciones y reclamos) quedan cubiertos por la reserva de contingencia.

## 4. Estimación puntual y de tres puntos (paso 6)

Valores en millones de US$ escalados al punto medio de ejecución, con IVA en las obras.

| Id | Elemento | Paquetes EDT | Técnica | Base de cálculo (O / M / P) | O | M | P | E | σ |
|---|---|---|---|---|---:|---:|---:|---:|---:|
{tabla}

En algunos elementos el escenario pesimista combina la cantidad máxima con el precio máximo (por ejemplo, el área y el costo por m² del SSEI), lo que agranda su σ; es una decisión conservadora. Alrededor del {local_E:.0%} de la estimación se apoya en datos salvadoreños.

Detalle de la UEP (honorario mensual en US$ de 2025, como consultores individuales sin prestaciones, y meses de contrato desde el inicio real de cada puesto hasta el fin de la actividad 3.1.1-06):

| Puesto | Inicio | Meses | O | M | P |
|---|---|---:|---:|---:|---:|
{uept}

El valor más probable son los honorarios reales de los siete consultores contratados por CEPA entre abril y mayo de 2026 (Plan de Adquisiciones 2026-2 del BID: contratos anuales de US$52,000 a 84,500). El optimista toma honorarios de otras unidades ejecutoras BID y Banco Mundial en El Salvador (MINSAL, MOP y ANDA, 2023 a 2026) y el pesimista suma 15% por renovaciones en cuatro años. El honorario del técnico de apoyo es un supuesto, y su inicio es la firma de su contrato en el cronograma. El ROP del programa es una adaptación de la plantilla del programa ES-L1157 (así figura en su encabezado), por lo que sus cifras se usan con cautela.

**Plantilla ampliada de la UEP (U3).** El Plan de Adquisiciones 2026-2 (15-jul-2026) tiene 21 procesos activos de consultores individuales (3CV, ex ante) para la plantilla ampliada que el PEP prevé (P00011 a P00041 sin el cancelado P00019 y sin P00014, que es el técnico de apoyo de U1), con un estimado de US${plan_pa:,.0f} y firmas estimadas de septiembre de 2026 a septiembre de 2027. Los montos del Plan de Adquisiciones no son anuales sino del plazo completo de cada proceso: en seis de los siete consultores clave el estimado es exactamente su contrato anual (columna "Contract Amount USD") por 56 / 12, es decir 56 meses desde abril de 2026, y el séptimo (P00005) se adjudicó 13% sobre su estimado. El plan no da el plazo de cada proceso nuevo, así que (supuesto) se toma el mismo plazo: el monto mensual implícito es el estimado dividido entre los meses que van de la firma estimada del PA al fin de esos 56 meses (diciembre de 2030), y se multiplica por los meses que van de la firma del cronograma al fin de 3.1.1-06. Así, el costo de la plantilla en el programa es de US${plan_m:,.0f} (valor más probable, sin escalamiento), US${plan_pa - plan_m:,.0f} menos que el estimado del PA porque el programa termina antes que el plazo supuesto por el plan. O y P son 0.85 y 1.15 veces ese valor (supuesto: el PA solo da un estimado).

| Proceso | Puesto | Monto del PA (US$) | Firma estimada del PA | Firma en el cronograma | Monto mensual implícito (US$) | Meses | Costo M (US$) |
|---|---|---:|---|---|---:|---:|---:|
{plant}

### Memoria de cálculo por elemento

| Id | Cómo se obtuvo | Fuentes |
|---|---|---|
{notas}

## 5. Análisis de sensibilidad (paso 7)

Efecto en la estimación PERT (US${m('total_E')} M) de cambiar un supuesto a la vez. Valores en millones de US$.

| Supuesto | Cambio | Estimación | Diferencia | Presupuesto |
|---|---|---:|---:|---:|
{sens}

Los supuestos que más mueven el resultado son los precios unitarios de las obras y el costo del estacionamiento: si el estacionamiento costara por plaza lo que el diseño de CEPA de 2022, la estimación subiría US${sens_cepa:.0f} millones. {'Ningún caso lleva el presupuesto por encima del préstamo.' if not over else 'Algún caso lleva el presupuesto por encima del préstamo.'}

## 6. Riesgo, incertidumbre y reservas (paso 8)

- **Rango.** La suma de los escenarios optimistas da US${m('total_O')} M y la de los pesimistas US${m('total_P')} M ({E['total_O'] / E['total_E'] - 1:+.0%} y {E['total_P'] / E['total_E'] - 1:+.0%} respecto de la estimación). No es un intervalo de confianza, porque suma extremos que no ocurrirían juntos, pero muestra que es un estimado de orden de magnitud.
- **Desviación del total.** Las obras comparten precios de insumos y escalamiento, así que sus desviaciones no son independientes, pero tampoco se mueven juntas en todo. Se usa una correlación uniforme de 0.3 entre elementos, en el rango de 0.25 a 0.3 que la GAO usa por defecto cuando no hay datos: σ del total = US${m('sigma_total')} M (con independencia total sería US${m('sigma_independiente')} M y con correlación total US${m('sigma_correlacionada')} M).
- **Reserva de contingencia.** Cubre hasta el percentil 80 del costo, el nivel que la GAO admite para programas de alto riesgo: 0.84 × σ = US${m('contingencia')} M, el {E['contingencia'] / E['total_E']:.1%} de la estimación y el {E['contingencia'] / E['presupuesto']:.1%} del presupuesto. Con otra correlación la reserva sería: 0.25, US${cr['0.25'] / 1e6:.1f} M; 0.5, US${cr['0.50'] / 1e6:.1f} M. Se asigna a cada paquete en proporción a su desviación.
- **Reserva de gestión.** 5% de la línea base (US${m('reserva_gestion')} M), para trabajo no previsto en el alcance. Según los componentes del presupuesto del proyecto (PMI, 2017, sección 7.3), queda fuera de la línea base y la libera la dirección del programa.
- **Riesgos de costo por elemento y respuesta.** Pasan a la matriz de riesgos:

| Elemento | Riesgo de costo | Respuesta |
|---|---|---|
| Estacionamiento (E1) | No hay diseño de 2,050 plazas; el costo por plaza puede ir de US$9,000 a 22,500. | Exigir el diseño en la licitación de 2026 y actualizar la estimación con las ofertas. |
| SSEI (S1) | Área y programa sin definir. | Definir la categoría OACI y el programa de necesidades antes de licitar. |
| Terminal (T1, T4) | Alcance de los sistemas de equipaje, uso común y escáneres. | Fijar el alcance tecnológico en las especificaciones y cotizar con proveedores. |
| Obras en general | Alza de acero y concreto (el concreto subió 7.4% en el primer semestre de 2026). | Cláusula de ajuste de precios con índices de CASALCO o del BCR. |
| Puentes y escáneres | Tipo de cambio y plazos de fabricación de equipos importados. | Comprarlos dentro del contrato de obra con fechas de entrega controladas. |

## 7. Comparación con el préstamo y presentación (paso 9)

Los montos del préstamo (EEO#3 y Anexo III) son valores de 2025 sin escalamiento e incluyen imprevistos del 9.39% en las obras. Por eso se comparan con la estimación más su reserva de contingencia en US$ de 2025, y el escalamiento se muestra aparte. Valores en millones de US$.

| Grupo | Estimación con reserva (US$ de 2025) | Préstamo (2025) | Diferencia a precios de 2025 | Escalamiento hasta la ejecución | Línea base |
|---|---:|---:|---:|---:|---:|
{grupos}

A precios de 2025 la estimación queda US${-flat_gap:,.1f} millones por debajo del préstamo. El escalamiento suma US${esc_tot:,.1f} millones y lleva la línea base a US${m('linea_base')} millones; con la reserva de gestión, el presupuesto queda US${gap:,.1f} millones por debajo del financiamiento.

- **Estacionamiento.** Es la diferencia principal (US${rf('Estacionamiento') - ff('Estacionamiento'):,.1f} M menos). El estudio del préstamo extrapoló a 2,000 plazas un diseño de 700 plazas (US$64.2 M, unos US$32,100 por plaza), y el Plan de Adquisiciones de 2026 conserva ese monto para la licitación de 2,050 plazas. Nuestra estimación más probable (US$12,600 por plaza sin IVA) sale de precios de CASALCO y de la referencia de mercado; el escenario pesimista toma el diseño de CEPA de 2022 (US$22,500). Es el supuesto que más conviene confirmar: las ofertas, cuya fecha límite de presentación fue el 16 de octubre de 2026, lo resolverán, y si se acercan al monto del préstamo la estimación subiría unos US${sens_pa:.0f} M (tabla de sensibilidad), todavía dentro del financiamiento.
- **Terminal.** A precios de 2025 la estimación es US${rf('Terminal') - ff('Terminal'):,.1f} M menor. El costo por m² sale de obras de CEPA en el mismo aeropuerto (2018 a 2025), que ya traen precios salvadoreños; los puentes y los sistemas se estiman aparte.
- **Lado aire y SSEI.** Quedan por debajo. Los pavimentos se basan en la plataforma de CEPA de 2016; el SSEI tiene el rango más amplio porque no tiene diseño.
- **Supervisión.** Es la segunda diferencia: el préstamo y el Plan de Adquisiciones usan 5% de la obra, y las supervisiones reales de edificios grandes en El Salvador (incluida la de las bandas de equipaje del AIES en 2025) cuestan entre 1.9 y 2.5%. Se toma 3% como más probable por la mezcla con obras del lado aire, que cuestan más de supervisar, y 5% como pesimista.
- **Componente II.** Con comparables salvadoreños y tarifas de El Salvador (honorario individual por un multiplicador de firma de 2.0 a 2.65, calculado con las cargas sociales salvadoreñas y la estructura del arancel del CFIA) da menos que los montos redondos del Anexo III.
- **Componente III.** La UEP se estima con los honorarios reales de los siete consultores contratados en 2026, el técnico de apoyo y la plantilla ampliada de 21 procesos del Plan de Adquisiciones 2026-2 (U3, US${float(el['U3']['M_usd']) / 1e6:.2f} M más probables con escalamiento). Los US$4.07 M del Anexo III salen del PEP, que prevé una plantilla de 19 plazas (además de las siete clave, un especialista legal, 7 administradores de contrato y 7 técnicos de apoyo) y US$800,000 de gastos operativos; el Plan de Adquisiciones desglosa la plantilla de otra forma (21 procesos, US$1.92 M), y la estimación sigue los procesos del plan.
- **Cómo se armó el presupuesto del préstamo.** La supervisión es exactamente el 5.000% de las obras, los componentes II y III son cifras redondas, y los imprevistos del 9.39% son el residuo que cierra en US$195 millones. Es la práctica normal al dimensionar un préstamo: se fija un techo y la contingencia absorbe el ajuste. El monto del préstamo no es lo que se va a pagar; los precios reales salen de las licitaciones.
- **Destino del margen.** Los US${gap:,.1f} millones no se asignan a ninguna obra: quedan como financiamiento disponible no comprometido. Si las ofertas superan la estimación, cubren el exceso; si no, pueden reasignarse a obras elegibles o cancelarse. Cualquier reasignación entre componentes o categorías de inversión requiere la no objeción del BID.

**Presentación y aprobación.** La estimación se presenta con el PEP: la UEP la prepara, la Gerencia General de CEPA la aprueba y el BID da su no objeción al PEP, al primer POA y al Plan de Adquisiciones. Una vez aprobada, la línea base de costos (curva S) solo cambia mediante el control de cambios del programa.

## Avance real a la fecha de corte (31 de octubre de 2026)

- **Préstamo.** Aprobado por el BID el 12 de noviembre de 2025, firmado el 13 de enero de 2026 y ratificado por la Asamblea el 29 de enero de 2026 (D.L. 505). Plazo de desembolsos: cinco años desde su vigencia.
- **UEP.** Los siete consultores clave empezaron entre el 16 de abril y el 4 de mayo de 2026, y el cronograma usa esas fechas (H01, 15 de mayo de 2026).
- **Adquisiciones.** El Aviso General de Adquisiciones se publicó el 5 de mayo de 2026. La supervisión del estacionamiento recibió expresiones de interés del 6 al 20 de mayo y la de la terminal hasta el 6 de octubre; el estacionamiento se licitó por LPI el 4 de septiembre de 2026 con ofertas el 16 de octubre, y la terminal el 8 de octubre con ofertas el 20 de noviembre. El cronograma reproduce esas fechas (3.2.3, 3.4.1 y 3.4.2). Las consultorías del Componente II no figuran en el Plan de Adquisiciones de 2026 y van atrasadas.
- **Presupuesto y ejecución.** La reforma a la Ley de Presupuesto 2026 incorporó US$30.3 M del préstamo (US$29.7 M para el estacionamiento y US$0.64 M para la UEP). Es una asignación presupuestaria, no ejecución: el BID no registra desembolsos publicados. El valor planificado a la fecha de corte es de US${PV_CORTE:.2f} M y es solo de la UEP; el costo real estimado a esa fecha es de US${R['costo_real_corte_musd']:.2f} M (honorarios mensuales de los siete contratos de la UEP en ejecución por los meses transcurridos), que es un costo incurrido estimado y no un desembolso del BID. Como el primer contrato de obra se firma en enero de 2027, esos US$29.7 M no se ejecutarán en 2026 y deben pasar al presupuesto de 2027; la comparación por semestre de los requisitos de financiamiento con los desembolsos previstos del préstamo está en la página 4 de la curva S.

## 8. Actualización y lecciones aprendidas (paso 10)

La estimación se actualiza cuando se aprueben los diseños (1.1.x), se conozcan las ofertas de las licitaciones (3.4.x) y en cada revisión del POA.

Lecciones aprendidas de esta estimación:

- Los datos salvadoreños existen, pero dispersos: obras anteriores de CEPA, precios de CASALCO y contratos en el Portal de Transparencia. Varios documentos del portal ya no están disponibles y se recuperaron con copias de archivo; en la ejecución real convendría pedirlos por la Ley de Acceso a la Información Pública.
- Las referencias internacionales sirven de contraste, pero el factor de localización es el supuesto más discutible y conviene evitarlo cuando hay datos locales.
- El elemento más incierto (el estacionamiento sin diseño) es también el que más pesa en la diferencia con el préstamo: definir su diseño antes de licitar reduce la mayor parte del riesgo de costo.

## Fuentes

{src}
'''
(PL.parent / 'docs' / 'estimacion-costos.md').write_text(doc, encoding='utf-8')
print('ok', doc.count(chr(8212)), round(flat_gap, 2), round(esc_tot, 2), round(local_E, 2))

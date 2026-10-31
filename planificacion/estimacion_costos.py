#!/usr/bin/env python3
"""Estimación independiente de costos del programa ES-L1173 por elemento y por paquete de trabajo de la EDT.

Aplica las técnicas de la clase 6: estimación paramétrica (costo unitario por cantidad), análoga (contratos comparables),
determinación de tarifas (meses-persona por tarifa), ascendente (puestos por honorario por meses) y tres puntos PERT,
E = (O + 4M + P) / 6 y sigma = (P - O) / 6. Los valores de referencia están en US$ de 2025 y salen de fuentes externas
(SOURCES); las cantidades salen de los documentos del proyecto. No parte de los montos del Anexo III ni del EEO#3:
se comparan al final; solo se toman de ellos los datos indicados en cada elemento (proporciones, el diseño de CEPA de 2022 y los gastos recurrentes del Anexo III). build_planificacion.py importa estimate() después de calcular el cronograma, porque el
escalamiento de precios se lleva al punto medio de cada elemento (ponderado por las actividades que lo ejecutan) y las
plazas de la UEP se cuentan desde su contratación real. allocate() reparte el costo de cada elemento entre las actividades de
quien cobra el contrato, con la regla de pesos documentada junto a RULES; write_outputs() escribe estimacion_costos.csv y
estimacion_costos.json.

Regla de pesos por actividad (clase 6: EDT, paquetes, actividades, recursos, cantidades y tarifas). Cada elemento de costo
llega a sus paquetes por su reparto (split) y, dentro de cada paquete, a las actividades de quien cobra el contrato
(contratista de obra, firma de supervisión, firma consultora, auditor externo). El costo indirecto de la UEP (U1, U2 y U3)
lo lleva solo la actividad de nivel de esfuerzo 3.1.1-06. Las actividades de la UEP, CEPA, el BID y la AAC no tienen costo
propio. Dentro de un paquete y de un elemento: 1) las actividades de movilización, de pruebas y de informe final reciben un
porcentaje pequeño y explícito (AUTO: 2 %, 2 % y 4 %); 2) una regla particular (RULES) fija el peso de las actividades cuyo
recurso es distinto (por ejemplo, en los puentes 85 % a la fabricación y 11 % a la instalación; los sistemas de la terminal,
a su instalación); 3) el resto se reparte entre las actividades de construcción en proporción a su duración, porque el listado
no da cantidades de obra comparables entre actividades de distinta naturaleza (cimentación, estructura, instalaciones).
allocate() verifica con assert que el costo de las actividades de cada paquete sea el del paquete y que ningún paquete con
costo carezca de actividades de quien cobra.
"""
from __future__ import annotations
import csv
import json
import math
from datetime import date, timedelta
from pathlib import Path

BASE_DATE = date(2025, 7, 1)  # US$ de 2025 (promedio anual)
# Escalamiento anual O / M / P. Obras: índice compuesto con precios de CASALCO (2021 a 2025: 1.25 %/año; 2024 a 2025: 2.6 %;
# 2026: concreto +7.4 % en el primer semestre, por eso P = 5.5 %). Servicios: IPC de El Salvador (oct-2025: 0.93 %; FMI 2026 a
# 2027: 2.1 a 2.7 %).
ESC = (0.0125, 0.026, 0.055)
ESC_SERV = (0.010, 0.021, 0.027)
IVA = 0.13  # Ley del IVA de El Salvador, art. 54
Z80 = 0.8416  # percentil 80 de la normal estándar
RHO = 0.3  # correlación uniforme entre elementos (GAO-20-195G, nota 36: 0.25 a 0.3 por defecto)
MGMT_RESERVE = 0.05  # reserva de gestión sobre la línea base (GAO-20-195G, p. 230: los programas suelen fijar 5 a 10 %)

SOURCES = {
    'MSP': 'Connico para Metropolitan Airports Commission, "Appendix E. MSP 2040 LTP Estimate", ROM rev. 2, 25-abr-2023, sin escalamiento (precios de 2023). Proyecto 3-2, Concourse G South Expansion (208,800 ft²), p. 77 y 78: sistemas A a D US$439.41/ft², mobiliario y equipo sin puentes US$9.52/ft², márgenes del contratista x1.288, evolución del diseño 25 %. https://www.mspairport.com/sites/default/files/2023-06/Appendix%20E-MSP%202040%20LTP%20Estimate.pdf',
    'PBB': 'Contratos de puentes de abordaje: Maryland BPW, 2-jul-2025 (BWI, 17 puentes, US$21.5 M); City of Savannah, 11-sep-2025 (5 puentes, US$8.50 M); Miami-Dade, memo 242117 de 2024 (MIA, 10 puentes, US$17.96 M). https://www.marylandcomptroller.gov/content/dam/mdcomp/md/meeting-briefs/2025/bpw-brief-07022025.pdf ; https://agenda.savannahga.gov/publishing/september-11-2025-city-council-regular-meeting/1524_11649.html ; https://www.miamidade.gov/govaction/legistarfiles/MinMatters/Y2024/242117min.pdf',
    'PAV': 'Precios de pavimento aeroportuario: MSP 2023, partida G2013 (plataforma PCC con base y subbase, US$275/yd²); licitaciones de Sidney OH (29-jun-2023) y Hagerstown MD (22-may-2024) para P-401 y P-209. https://www.sidneyoh.com/DocumentCenter/View/3094/BidTab23-10AirportParallelTaxiway ; https://washco-md.net/wp-content/uploads/purch-pur-1674-bidtab.pdf',
    'WGI': 'WGI, "Parking Structure Cost Outlook for 2024" (mediana US$29,900 por plaza, US$89.45/ft² de área bruta) y mediana de 2025 (US$31,400 por plaza), reportada en la nota de la NPA sobre el Outlook 2026. https://publications.wginc.com/hubfs/WGIs%20Parking%20Structure%20Cost%20Outlook%20for%202024.pdf ; https://www.parking-mobility.org/news/wgi-releases-2026-parking-structure-cost-outlook/',
    'PV': 'NREL/TP-7A40-92536, ene-2025, tabla A-1 (comercial, US$1.55 a 2.13/Wdc) e IRENA, "Renewable Power Generation Costs in 2024", tabla 3.1 (Centroamérica y Caribe, percentil 5: US$939/kW). https://docs.nlr.gov/docs/fy25osti/92536.pdf ; https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2025/Jul/IRENA_TEC_RPGC_in_2024_2025.pdf',
    'ARFF': 'FAA AC 150/5210-15A (dimensionamiento de estaciones ARFF) y estaciones recientes: Easterwood TX (TDLR TABS2024011129), DFW (TABS2024020164) y Monterey CA (Fire Apparatus Magazine, 12-jun-2024). https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_150_5210-15A.pdf ; https://www.tdlr.texas.gov/TABS/Search/Print/TABS2024011129 ; https://www.tdlr.texas.gov/TABS/Search/Print/TABS2024020164',
    'LOC': 'Factor de localización: Turner & Townsend, "Global Construction Market Intelligence 2026", costo promedio de construcción de Bogotá (US$1,274/m²), Santiago (1,753) y Monterrey (2,275) frente a Dallas (US$386/ft², unos 4,155/m²): 0.31 a 0.55. Banco Mundial, ICP 2021: PPP de construcción de El Salvador 0.168, usado como cota inferior. https://publications.turnerandtownsend.com/global-construction-market-intelligence-2026/latin-america ; https://publications.turnerandtownsend.com/global-construction-market-intelligence-2026/north-america ; https://api.worldbank.org/v2/sources/90/country/SLV/series/1501200/classification/PPPGlob/time/YR2021?format=json',
    'ESC': 'Escalamiento de servicios: FMI, consulta del Artículo IV 2025 de El Salvador (IPC). El escalamiento de obras usa CASALCO; ENR (BCI +4.5 % anual, jul-2026) y BLS PPI vía AGC (oferta de edificios no residenciales +5.4 %, oct-2026) quedan como contraste del escenario pesimista. https://www.imf.org/en/news/articles/2025/06/27/imf-concludes-2025-article-iv-consultation-and-first-review-under-the-eff-for-el-salvador ; https://www.enr.com/ext/resources/static_pages/Economics/2026/0706_CE_WK1.pdf ; https://www.agc.org/sites/default/files/users/user21902/PPI%20Tables%202026_09_v2.pdf',
    'IVA': 'Ley de Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios, D.L. 296 de 1992, art. 54 (13 %). https://www.jurisprudencia.ues.edu.sv/oajc/leyes/LegislacionTributaria/ley%20del%20Impuesto%20a%20la%20Tranferencia.pdf',
    'CPI': 'BLS, índice de precios al consumidor CPI-U (serie CUUR0000SA0), promedios anuales, para llevar valores históricos a US$ de 2025. https://api.bls.gov/publicAPI/v2/timeseries/data/CUUR0000SA0',
    'SUP': 'Supervisión en préstamos BID y Banco Mundial de la región: ES-L1155 (4.97 %), ES-L1151 (3.6 %), GU-L1170 (4.22 %), CR-L1032 (5.33 %), NI-L1092 (8.04 %), Banco Mundial P122007 (6.4 %) y P154275 (6.5 %); mediana 5.33 %. https://www.iadb.org/document.cfm?id=EZSHARE-397073461-141 ; https://www.iadb.org/document.cfm?id=EZSHARE-1607650465-26232 ; https://documents.worldbank.org/curated/en/161751491427758866/pdf/PAD1539-PAD-PUBLIC-Panama-PAD-main.pdf',
    'EAS': 'Gestión ambiental y social en préstamos de la región: GU-L1170 (0.33 %), NI-L1092 (0.34 %), CR-L1032 (1.1 %), Banco Mundial P122007 (1.8 %); mediana 0.72 %. https://www.iadb.org/document.cfm?id=EZSHARE-1434889300-109 ; https://www.iadb.org/document.cfm?id=EZSHARE-1939367940-17',
    'HON': 'Honorarios mensuales de consultores individuales en unidades ejecutoras BID y Banco Mundial en El Salvador (MINSAL, MOP y ANDA, 2023 a 2026), contratos publicados en el Portal de Transparencia. https://www.transparencia.gob.sv/mostrarDocContratacionesDescarga.php?id=MjExNDE4 (coordinador, US$6,400) y demás contratos citados en docs/estimacion-costos.md',
    'ROP': 'Reglamento Operativo del Programa (EEO#1), sección 5.4 (tipos de gastos operativos de la UEP). Documento del proyecto.',
    'PROP': 'Propuesta de Préstamo ES-L1173, condiciones previas al primer desembolso: siete puestos clave de la UEP. Documento del proyecto.',
    'ANX3': 'Propuesta de Préstamo ES-L1173, Anexo III, sección III: gastos recurrentes y de mantenimiento por US$200,000 durante toda la ejecución. Documento del proyecto.',
    'EEO3PAV': 'EEO#3, cuadro 18: señalización de plataformas US$242,753 de un costo directo de US$9,385,032 (2.6 %). Documento del proyecto; solo se usa la proporción.',
    'EEO3EST': 'EEO#3, cuadro 21: presupuesto por partidas del diseño de CEPA de 2022 para el edificio de estacionamiento (sistemas especiales 8.5 %, señalización 2.1 %). Documento del proyecto; solo se usan las proporciones.',
    'CEPA2018': 'CEPA, Portal de Transparencia, "Obras en ejecución": Ampliación de la terminal de pasajeros del AIES, etapa 1 (LA-10/2018, CAABSA), US$37,881,157 original y US$38,559,454.53 actualizado, 23,216 m² en 3 niveles; cuatro salas de espera 2016-2017, US$5,855,609.53 por 1,900 m²; plataforma de 2016. Capturas de Wayback: https://web.archive.org/web/20210921150851/https://www.transparencia.gob.sv/institutions/cepa/executing_works ; área: https://www.revistaeyn.com/centroamericaymundo/el-salvador-firma-mexicana-a-cargo-de-ampliacion-del-aeropuerto-internacional-BVEN1172232',
    'AIES2025': 'El Mundo: ampliación del check-in del AIES, unos US$12 M por 5,255 m² nuevos (15-12-2023 y 28-04-2025); terminal de bandas de equipaje, US$47.2 M por más de 17,000 m² (03-09-2025). https://diario.elmundo.sv/economia/cepa-invierte-12-millones-en-una-nueva-area-de-check-in-en-el-aeropuerto ; https://diario.elmundo.sv/ampArticle/cepa-invertira-47-2-millones-en-nueva-terminal-de-bandas-de-equipajes-en-aeropuerto-internacional-de-el-salvador?amp=1',
    'PLAT2016': 'Estrategia y Negocios, 30-11-2016: nueva plataforma del AIES para 5 posiciones, US$5.7 M por 43,600 m² (33,000 de concreto hidráulico y 10,600 de asfalto). https://www.revistaeyn.com/lasclavesdeldia/la-cepa-invierte-us10-millones-en-el-aeropuerto-internacional-el-salvador-EAEN1022372',
    'CASALCO': 'CASALCO, precios promedio de materiales y mano de obra, Área Metropolitana de San Salvador, 2019 a 2025 (concreto 210 US$135.35/m³, hierro, cemento, bloque, mezcla asfáltica US$97.34/t, obrero calificado US$17.41/día con prestaciones en dic-2025); El Mundo, 27-08-2026, alzas del primer semestre de 2026. https://www.casalco.org.sv/precios-promedio-materiales ; https://diario.elmundo.sv/economia/asfalto-cemento-bloques-y-otros-materiales-de-construccion-reportan-incrementos-entre-en-primer-semestre-del-ano',
    'CEPA2026': 'BID, Anuncio Específico de Adquisiciones IDB-6073OCES-P00001-SPN, 04-sep-2026: LPI de obras del edificio de estacionamiento (ofertas el 16-oct-2026); El Mundo, 07-09-2026: 4 niveles y 2,050 plazas, con US$29,662,050 en el presupuesto de 2026 (primer tramo, no el costo total). https://www.iadb.org/es/viewer/EZIDB0003440-1039777545-93 ; https://diario.elmundo.sv/economia/cepa-licita-construccion-de-nuevo-edificio-de-estacionamiento-en-el-aeropuerto',
    'SEICR': 'Delfino.cr, 12-11-2021: estación SEI del aeropuerto Juan Santamaría (Costa Rica), más de US$9 M por 2,630 m², 7 bahías. https://delfino.cr/2021/11/aeropuerto-internacional-juan-santamaria-estrena-nueva-estacion-de-bomberos',
    'PA2026': 'BID, Plan de Adquisiciones ES-L1173 2026-2 (15-jul-2026): contratos de los 7 consultores de la UEP (US$52,000 a 84,500 al año, abril a mayo de 2026), métodos y montos estimados de cada proceso, y los 21 procesos 3CV de la plantilla ampliada de la UEP (P00011 a P00041, US$1.92 M, firmas estimadas de septiembre de 2026 a septiembre de 2027). https://www.iadb.org/es/viewer/EZIDB0003440-1039777545-69',
    'PEP': 'BID, PEP/POA/PA (EER#3, nov-2025), hojas Payments y Payments Flow Output: plantilla de 19 plazas de la UEP (US$4.07 M) y pagos estimados por semestre. https://www.iadb.org/es/viewer/EZIDB0003440-654689410-14',
    'SUPSV': 'Contratos de supervisión en El Salvador (Portal de Transparencia): bandas de equipaje del AIES, US$1,131,905 por una obra de US$46,074,937 (Reg. 211014 y 211000, 2025); maternidad El Nido de MINSAL (Reg. 220102 y 214699); CENT (Reg. 199367 y 202701); pavimentos del AIES 2024-2025 (Reg. 205607, 215641 y 214286). Arancel del CFIA de Costa Rica (inspección 3 %, dirección técnica 5 %). https://www.transparencia.gob.sv/mostrarDocContratacionesDescarga.php?id=MjExMDE0&inst=211014 ; https://cfia.or.cr/site/wp-content/uploads/2024/pdf/descargas/reglamentos/ejercicio/arancel-de-servicios-profesionales-de-consultoria-para-edificaciones.pdf',
    'TARSV': 'Honorarios en El Salvador: UEP de ES-L1155 (US$3,000 a 3,900 al mes, Plan de Adquisiciones 5620/OC-ES 2026), coordinador de ES-L1151 (US$7,000), consultores de las CT ES-T1289, ES-T1314 y ES-T1315 (US$3,750 a 10,500), tarifas horarias de PwC en la auditoría de ES-L1155 (Reg. 214521). Multiplicador: cargas patronales salvadoreñas (ISSS 7.5 %, AFP 8.75 %, INCAF 1 %, aguinaldo y vacaciones) y estructura del arancel del CFIA (gastos generales y utilidad). https://www.iadb.org/document.cfm?id=EZIDB0000251-1515765089-1993 ; https://www.transparencia.gob.sv/mostrarDocContratacionesDescarga.php?id=MjE0NTIx&inst=214521',
    'AUDSV': 'Auditorías en El Salvador: PwC para ES-L1155, US$140,541 por 3 ejercicios con IVA (Reg. 214521, 2025); Cornejo & Umaña para CEPA (CAF), US$87,575 por 2 auditorías (Reg. 214288, 2025); presupuesto de auditoría de ES-L1151, US$400,000 a 5 años. https://www.transparencia.gob.sv/mostrarDocContratacionesDescarga.php?id=MjE0Mjg4&inst=214288 ; https://www.iadb.org/document.cfm?id=EZSHARE-1501734583-48',
    'EVALSV': 'Evaluaciones de préstamos BID en El Salvador: ES-L1151 (intermedia US$50,000, final US$100,000, plan de monitoreo y evaluación de 2022) y ES-L1075 (medio término y final US$72,500 cada una, 2014); evaluación final de un programa del MOPT (US$40,000, 2016). https://www.iadb.org/document.cfm?id=EZSHARE-1501734583-48 ; https://www.iadb.org/document.cfm?id=EZSHARE-1636930938-2',
    'PMSV': 'Plan maestro vigente del AIES: Kimley-Horn, cooperación USTDA de unos US$427,000, entregado en 2013 (La Prensa Gráfica, 4-may-2018, réplica en https://segundavueltasv.wordpress.com/tag/cepa/); actualización del plan maestro de Rionegro, COP 10,509 millones (El Colombiano, dic-2023). https://www.elcolombiano.com/antioquia/adjudican-contrato-del-plan-maestro-del-aeropuerto-jose-maria-cordova-EG23341126',
    'PEASV': 'Planes sectoriales: BID ES-T1289 (capítulo de transporte del Plan Maestro de Infraestructura, US$110,000, 2018), BID GY-T1134 (Plan Maestro Nacional de Aviación Civil de Guyana, US$500,000, 2016) y MOPT, Plan Director del Tren del Pacífico (Deloitte, US$1,900,000, 2023, Reg. 194908). https://www.iadb.org/document.cfm?id=EZSHARE-1484808944-22 ; https://www.iadb.org/document.cfm?id=EZSHARE-1445113869-20',
    'RUTASSV': 'Estudios en El Salvador: CORSATUR, perfil y gasto del visitante internacional (US$165,900 en 2025, Reg. 209042); topes de estudios con firma de las CT ES-T1315 (US$110,000) y ES-T1314 (US$250,000). https://www.iadb.org/document.cfm?id=EZSHARE-202171911-26 ; https://www.iadb.org/document.cfm?id=EZSHARE-1725942354-125',
    'TSA': 'British Aviation Group, "TSA Awards $1.3 Billion to Procure CT X-Ray Scanners for Airports", 17-abr-2023 (59 escáneres CT por US$42.9 M, año fiscal 2023). https://www.britishaviationgroup.co.uk/?p=20777',
    'EEO3EQ': 'EEO#3, capítulo 28 (equipamiento de la terminal): los sistemas FIDS, CUTE y SATE elevan el capítulo de US$7.2 M (puentes) a US$9.2 M de costo directo, con base en cotizaciones. Documento del proyecto; única referencia encontrada para estos sistemas.',
    'BIM': 'Implementación BIM pública: BID RG-T4814 (2025, firma para piloto BIM US$150,000; CT de US$500,000) y MEF Perú, Plan BIM (2022, S/734,040). https://ewsdata.rightsindevelopment.org/files/documents/14/IADB-RG-T4814_HMTw8o1.pdf ; https://mef.gob.pe/contenidos/ogip/procesos/0102-2022-CI-BID4428_TDR.pdf',
    'EDGE': 'GBCI / IFC, "EDGE Certification Pricing" (registro US$349; certificación US$0.29/m², mínimo US$2,900; US$0.24/m² entre 25,000 y 50,000 m²) e IFC, EDGE Certification Protocol 5.0. https://edgebuildings.com/about/edge-certification-pricing',
    'MEL': 'Plan de Monitoreo, Evaluación y Aprendizaje (EER#2), tabla 7: auditoría financiera US$160,000, evaluación de medio término US$50,000, evaluación ex post US$100,000. Documento del proyecto; se usa como contraste.',
    'GAO': 'GAO, "Cost Estimating and Assessment Guide", GAO-20-195G, marzo 2020 (p. 159: puede presupuestarse a un 70 u 80 % de confianza en programas de alto riesgo, sin un nivel único de buena práctica; nota 36: correlación por defecto de 0.25 a 0.3; p. 230: los programas suelen fijar una reserva de gestión de 5 a 10 %). https://www.gao.gov/assets/d20195G.pdf',
    'AACE': 'AACE International, RP 18R-97, rev. 2020 (clase 4: -15 a -30 % / +20 a +50 %; clase 3: -10 a -20 % / +10 a +30 %). https://web.aacei.org/docs/default-source/toc/toc_18r-97.pdf',
}

# Cantidades del proyecto
TERMINAL_M2 = 18_555  # solicitud de información de jul-2026 y expresión de interés P00024 (el EEO#3 usaba 16,303 m² en la Fase 2)
BRIDGES = 6  # una manga por sala de la Fase 2 (EEO#3)
PCC = {'1.3.1': 24_478.50, '1.3.2': 23_159.42}  # EEO#3, cuadro 11: plataformas de concreto hidráulico
ASPH_APRON = {'1.3.1': 4_119.34 + 9_159.44 + 4_360.17, '1.3.2': 3_210.53}  # rodaje entre plataformas, circulación y bordes
FOXTROT_M2 = 14_479.05 + 3_846.00 + 4_019.00  # calle F con intersección y hombros
PARKING_M2, PARKING_SPACES = 66_494 - 812.5, 2_050  # plazas: licitación de CEPA de sep-2026 (4 niveles); área de referencia: EEO#3, cuadro 20
# CEPA 2022, diseño de 700 plazas (cuadro 21 del EEO#3): directo US$13,547,362 para 739 plazas, indirectos 18 %, llevado a 2025
CEPA2022_PLAZA = 13_547_362 / 739 * 1.18 * 1.04
PV_KWP = 1_920.28  # EAS-PGAS, tabla 2

# Estructura de costos del presupuesto de la Fase 2 de la terminal (cuadro 2 del EEO#3, capítulos en US$ de 2017). Solo se
# usan las proporciones para repartir el costo del edificio entre los paquetes de la EDT; los montos no entran en la estimación.
TERMINAL_CHAPTERS = {
    '1.2.1': [181_029.16, 77_033.72, 225_718.09, 479_415.66, 4_426_759.34, 4_327_313.85, 515_719.60, 94_926.60],
    '1.2.2': [430_085.34, 1_570_155.21, 31_920.06, 649_507.11, 794_883.22, 209_262.61, 123_935.00, 499_967.16],
    '1.2.3': [5_138_223.49, 824_608.86, 286_010.64, 2_263_792.26, 1_238_678.36, 234_479.53],
    '1.2.4': [363_655.00],  # mobiliario; los puentes van como elemento propio
    '1.2.5': [102_500.00, 29_819.59],  # transporte vertical y señalética (accesibilidad universal)
}
_tc = {k: sum(v) for k, v in TERMINAL_CHAPTERS.items()}
TERMINAL_SPLIT = {k: v / sum(_tc.values()) for k, v in _tc.items()}

# Obras exteriores de la Fase 1 (as built de CEPA, cuadro 15 del EEO#3, US$ con IVA de 2017-2018) prorrateadas por área
# (18,555 / 21,673 m²), sin IVA y llevadas a 2025 con el CPI (1.282). O: redes de agua, colector y planta de tratamiento;
# P: incluye además la subestación eléctrica; M: punto medio (supuesto: la Fase 2 necesita la mitad de esa ampliación eléctrica).
_ext = (TERMINAL_M2 / 21_673) / 1.13 * 1.282
EXT_O = (603_424.99 + 902_062.31 + 1_306_070.19 + 76_832.52) * _ext
EXT_P = (EXT_O / _ext + 8_422_668.52) * _ext
EXT_M = (EXT_O + EXT_P) / 2

# Terminal: MSP 2023, (439.41 + 9.52) US$/ft² x 1.288 de márgenes x 10.7639 ft²/m² x 1.0566 (CPI 2023 a 2025)
MSP_M2 = (439.41 + 9.52) * 1.288 * 10.7639 * 1.0566

# Tarifas por mes-persona en US$ de 2025 (O, M, P)
# Honorario individual (El Salvador y BID en El Salvador) por el multiplicador de firma (cargas sociales salvadoreñas y
# estructura del arancel del CFIA: 2.0 / 2.35 / 2.65). Internacional: US$6,250 / 7,000 / 10,500; nacional: US$3,000 / 3,900 / 6,250.
MULT = (2.0, 2.35, 2.65)
INTL = tuple(round(h * f) for h, f in zip((6_250, 7_000, 10_500), MULT))
NAC = tuple(round(h * f) for h, f in zip((3_000, 3_900, 6_250), MULT))


def team(intl_mp, nac_mp):
    """Costo por determinación de tarifas: meses-persona internacionales y nacionales (O, M, P) por su tarifa."""
    return tuple(i * a + n * b for i, a, n, b in zip(intl_mp, INTL, nac_mp, NAC))


# UEP, ocho puestos: los siete clave de la condición previa al primer desembolso (Propuesta de Préstamo; EDT 3.1.1) y el técnico de
# apoyo administrativo del ROP 3.1.2. Honorario mensual (O, M, P) en US$ de 2025, sin prestaciones (consultores individuales), y
# fecha de inicio real del contrato (PA 2026-2, columna "Start Date Contract"; el técnico de apoyo firma según el cronograma).
UEP = [
    # O: otras unidades ejecutoras BID y Banco Mundial en El Salvador; M: contratos reales de la UEP de 2026 (Plan de
    # Adquisiciones 2026-2, monto anual / 12); P: M + 15 % por renovaciones y ajustes en cuatro años.
    ('Coordinador del Programa', (6_000, 7_042, 8_098), date(2026, 4, 16)),
    ('Coordinador general de obra', (4_000, 6_733, 7_743), date(2026, 4, 16)),
    ('Especialista de adquisiciones', (3_300, 5_509, 6_335), date(2026, 4, 23)),
    ('Especialista financiero', (3_000, 4_550, 5_233), date(2026, 5, 4)),
    ('Especialista de planificación y monitoreo', (3_000, 4_550, 5_233), date(2026, 4, 16)),
    ('Especialista en ingeniería aeroportuaria', (3_000, 5_417, 6_229), date(2026, 5, 4)),
    ('Especialista socioambiental', (3_200, 4_333, 4_983), date(2026, 5, 4)),
    ('Técnico en apoyo administrativo (ROP 3.1.2)', (1_200, 1_500, 2_000), None),  # supuesto: sin contrato comparable publicado
]
MONTH_DAYS = 30.4375  # días por mes (365.25 / 12) para convertir fechas en meses de contrato
# Gastos operativos: M = US$200,000 del Anexo III (gastos recurrentes y de mantenimiento de toda la ejecución); O y P, cálculo
# ascendente propio (US$1,500 y 4,000 al mes más equipo inicial de US$1,500 y 3,000 por puesto).
UEP_OPEX = (1_500, None, 4_000)
UEP_SETUP = (8 * 1_500, None, 8 * 3_000)
UEP_OPEX_M = 200_000

# Plantilla ampliada de la UEP: procesos 3CV activos del Plan de Adquisiciones 2026-2 (BID, 15-jul-2026; P00019 está cancelado y
# P00014, el asistente administrativo, es el técnico de apoyo de U1). Cada fila: proceso, puesto, monto estimado del proceso
# (columna "Estimated Amount") y firma estimada del PA (columna "Signed Contract Estimated Date"). Seis lotes, uno por
# solicitud de contratación del cronograma (3.4.4-45 a 3.4.4-74); la actividad que firma el lote es la indicada.
PLANTILLA = [
    (1, '3.4.4-49', [('P00011', 'Administrador 1 de Proyectos', 220_350.00, date(2026, 9, 7)), ('P00013', 'Especialista Legal', 114_833.33, date(2026, 9, 7)),
                     ('P00015', 'Ordenanza / Mensajero', 40_191.67, date(2026, 9, 7)), ('P00016', 'Analista en Adquisiciones', 86_125.00, date(2026, 9, 7)),
                     ('P00017', 'Analista Financiero', 86_125.00, date(2026, 9, 7)), ('P00018', 'Técnico en Planificación y Monitoreo', 78_000.00, date(2026, 9, 7)),
                     ('P00029', 'Ingeniero Estructurista', 85_800.00, date(2026, 9, 7)), ('P00030', 'Ingeniero Electricista', 85_800.00, date(2026, 9, 7)),
                     ('P00031', 'Ingeniero Hidráulico', 85_800.00, date(2026, 9, 7)),
                     ('P00032', 'Especialista en Seguridad Industrial y Salud Ocupacional', 97_500.00, date(2026, 9, 7))]),
    (2, '3.4.4-54', [('P00040', 'Pavimentos Aeroportuarios', 65_000.00, date(2026, 10, 1))]),
    (3, '3.4.4-59', [('P00033', 'Analista Social', 46_800.00, date(2026, 10, 15))]),
    (4, '3.4.4-64', [('P00012', 'Analista Técnico 1', 61_750.00, date(2027, 2, 9)), ('P00020', 'Gestor Documental', 52_000.00, date(2027, 2, 1)),
                     ('P00039', 'Arquitecto', 85_800.00, date(2027, 2, 9))]),
    (5, '3.4.4-69', [('P00034', 'Administrador 2 de Proyectos', 156_000.00, date(2027, 4, 16)), ('P00035', 'Analista Técnico 2', 58_500.00, date(2027, 4, 16)),
                     ('P00036', 'Administrador 3 de Proyectos', 156_000.00, date(2027, 4, 16)), ('P00037', 'Analista Técnico 3', 58_500.00, date(2027, 4, 16)),
                     ('P00038', 'Ingeniero Mecánico', 85_800.00, date(2027, 4, 16))]),
    (6, '3.4.4-74', [('P00041', 'Administrador 4 de Proyectos', 113_750.00, date(2027, 9, 23))]),
]
PLANTILLA_TOTAL = sum(p[2] for _, _, ps in PLANTILLA for p in ps)
assert abs(PLANTILLA_TOTAL - 1_920_425.00) < 0.5 and sum(len(ps) for _, _, ps in PLANTILLA) == 21
# Los montos del PA son por proceso y cubren todo su plazo, no un año: en los seis consultores clave cuyo contrato se firmó al
# monto estimado, el "Estimated Amount" es el monto anual del contrato (columna "Contract Amount USD") por 56 / 12. P00005 se
# adjudicó 13 % sobre su estimado y no entra en la prueba.
KEY_PA = [(394_333.33, 84_500), (254_800.00, 54_600), (308_490.00, 66_105), (254_800.00, 54_600), (303_333.33, 65_000), (242_666.67, 52_000)]
PA_MONTHS = 56
assert all(abs(d / q * 12 - PA_MONTHS) < 0.01 for d, q in KEY_PA)
PA_HORIZON = date(2026, 4, 16) + timedelta(days=PA_MONTHS * MONTH_DAYS)  # fin del plazo que supone el PA para los puestos de la UEP
PLANTILLA_O, PLANTILLA_P = 0.85, 1.15  # supuesto: O y P de la plantilla ampliada como fracción del monto mensual implícito del PA

# Elementos de estimación. tipo: 'obra' (lleva IVA y escalamiento), 'servicio' (escalamiento), 'pct' (porcentaje de las obras
# ya escaladas). split: reparto entre paquetes de la EDT. unit: costo unitario O/M/P (US$ 2025, sin IVA) o total si qty es None.
ELEMENTS = [
    dict(id='T1', name='Edificio de la terminal Fase 2', group='Terminal', tipo='obra', method='Paramétrica (US$/m²)',
         qty=TERMINAL_M2, unit_name='m²', unit=(1_700, 2_250, 2_900), split=TERMINAL_SPLIT, method_override='Análoga local (US$/m²)',
         src=['CEPA2018', 'AIES2025', 'CASALCO', 'MSP'],
         note=f'Obras de CEPA en el mismo aeropuerto, sin IVA y llevadas a 2025 con el índice de CASALCO: etapa 1 de 2018 (US$1,689/m²), check-in de 2025 (2,073), etapa 1 con su costo total reportado (2,452) y terminal de equipaje de 2025 (2,457); M es la mediana. P: cuatro salas de 2016-2017 y etapa 1 con mobiliario y supervisión (2,891 a 3,134). Contraste internacional: MSP 2023 ajustado a la región, US${MSP_M2 * 0.42:,.0f}/m². Superficie: {TERMINAL_M2:,} m², la de la solicitud de información de julio de 2026 y la expresión de interés P00024 (el EEO#3, de julio de 2025, usaba 16,303 m² para la Fase 2).'),

    dict(id='T2', name='Puentes de abordaje', group='Terminal', tipo='obra', method='Paramétrica (US$/unidad)',
         qty=BRIDGES, unit_name='puentes', unit=(1_265_000, 1_640_000, 2_410_000), split={'1.2.4': 1}, src=['PBB', 'MSP', 'LOC'],
         note='Equipo importado: factor de localización 1.00 / 1.05 / 1.10 (PPP de maquinaria del ICP: 1.055). M: promedio de MSP, BWI, Savannah y MIA.'),
    dict(id='T3', name='Obras exteriores de la terminal', group='Terminal', tipo='obra', method='Análoga (as built de la Fase 1)',
         qty=None, unit_name='global', unit=(EXT_O, EXT_M, EXT_P), split={'1.2.1': 1}, src=['CPI'],
         note='Costo real de las obras exteriores de la Fase 1 (CEPA), prorrateado por área (18,555 m² de la terminal frente a 21,673 m² de la Fase 1) y llevado a 2025. O sin subestación; P con subestación completa. Incluye la intervención y el traslado de redes (agua potable, aguas negras, contra incendio y eléctrica) que la Propuesta pide presupuestar como partida específica (tabla 5).'),
    dict(id='T4', name='Sistemas de la terminal (equipaje, uso común y escáneres)', group='Terminal', tipo='obra', method='Análoga y paramétrica',
         qty=None, unit_name='global', unit=(1_600_000, 2_000_000 * 1.3 + 2 * 768_000, 3_000_000 * 1.3 + 4 * 768_000), split={'1.2.4': 1},
         src=['EEO3EQ', 'TSA', 'CPI'],
         note='FIDS, CUTE y SATE: O US$1.6 M (los US$2.0 M de costo directo del EEO#3 sin la parte de pantallas y comunicaciones que ya trae el sistema D del MSP); M US$2.0 M con 30 % de indirectos; P +50 % (supuesto). Escáneres CT: 0 / 2 / 4 unidades a US$768,000 (TSA 2023, US$727,000, llevado a 2025).'),
    dict(id='A1', name='Plataformas de concreto hidráulico (35 cm)', group='Lado aire', tipo='obra', method='Paramétrica (US$/m²)',
         qty=sum(PCC.values()), unit_name='m²', unit=(130, 150, 190), split={k: v / sum(PCC.values()) for k, v in PCC.items()}, src=['PLAT2016', 'CASALCO', 'PAV'],
         note='Plataforma de CEPA de 2016 (US$5.7 M por 43,600 m²), separando concreto y asfalto con un supuesto de 1.2 a 1.5 veces el costo del asfalto, llevada a 2025 con CASALCO (1.112) y sin IVA: US$134 a 140/m². M (US$150) agrega el mayor espesor de 35 cm y el concreto de mayor módulo para aeronaves más grandes que las posiciones C y D de 2016 (supuesto). P: losas más gruesas, MR-45, demolición del asfalto existente y el alza del concreto de 2026. Contraste: sección PCC de MSP ajustada, US$210/m².'),
    dict(id='A2', name='Rodaje, circulación y bordes de plataforma en asfalto', group='Lado aire', tipo='obra', method='Paramétrica (US$/m²)',
         qty=sum(ASPH_APRON.values()), unit_name='m²', unit=(90, 105, 140), split={k: v / sum(ASPH_APRON.values()) for k, v in ASPH_APRON.items()}, src=['PLAT2016', 'CASALCO', 'PAV'],
         note='Parte asfáltica de la plataforma de CEPA de 2016 (US$95 a 114/m²), llevada a 2025 con la mezcla asfáltica de CASALCO (1.124) y sin IVA: US$94 a 113/m². P: sección para aeronaves clave E. Contraste: precios de EE. UU. ajustados, US$85/m².'),
    dict(id='A3', name='Calle de rodaje Foxtrot con hombros', group='Lado aire', tipo='obra', method='Paramétrica (US$/m²)',
         qty=FOXTROT_M2, unit_name='m²', unit=(90, 105, 140), split={'1.4.1': 1}, src=['PLAT2016', 'CASALCO'],
         note='Misma sección asfáltica; los hombros cuestan menos, lo que deja margen a favor.'),
    dict(id='A4', name='Señalización, balizamiento e iluminación de plataformas y Foxtrot', group='Lado aire', tipo='pct_lado_aire',
         method='Porcentaje del pavimento', qty=None, unit_name='% del pavimento', unit=(0.026, 0.08, 0.12),
         split=None, src=['EEO3PAV'], note='O: la señalización del presupuesto de plataformas del EEO#3 (cuadro 18) es 2.6 % del costo directo, sin luces de borde. M y P: supuesto del equipo que agrega el balizamiento y las torres de iluminación (8 y 12 %).'),
    dict(id='E1', name='Edificio de estacionamiento (2,050 plazas)', group='Estacionamiento', tipo='obra', method='Paramétrica (US$/plaza)',
         qty=PARKING_SPACES, unit_name='plazas', unit=(9_000, 12_600, round(CEPA2022_PLAZA)),
         split={'1.5.1': 0.894, '1.5.2': 0.106}, src=['CASALCO', 'WGI', 'LOC', 'EEO3EST', 'CEPA2026'],
         note=f'No hay un edificio de estacionamiento salvadoreño con monto publicado. Cálculo propio con precios de CASALCO (0.45 m³ de concreto y 50 kg de acero por m², materiales del 45 al 55 % del directo, 20 a 30 % de indirectos, instalaciones y rampas) que da US$300 / 400 / 550 por m² y, con unos 30 m² por plaza, US$9,000 / 12,000 / 16,500 por plaza. O: el extremo bajo de ese cálculo. M: promedio de su valor central (US$12,000) y de la mediana de WGI ajustada a la región (US$13,188). P: diseño de CEPA de 2022 para 700 plazas con sus indirectos, llevado a 2025 (US${CEPA2022_PLAZA:,.0f} por plaza). Contraste: el Plan de Adquisiciones de 2026 conserva el estimado del préstamo, US$64.2 M (US$31,318 por plaza). El 10.6 % para accesos, control de tráfico y locales (1.5.2) es el peso de los sistemas especiales y la señalización en el diseño de CEPA (cuadro 21 del EEO#3).'),

    dict(id='E2', name='Sistema fotovoltaico sobre cubierta (1,920 kWp)', group='Estacionamiento', tipo='obra', method='Paramétrica (US$/kWp)',
         qty=PV_KWP, unit_name='kWp', unit=(940, 1_160, 1_600), split={'1.5.3': 1}, src=['PV'],
         note='O: IRENA, percentil 5 de Centroamérica. M y P: NREL comercial 2024 y cubierta 2022 por 0.75.'),
    dict(id='S1', name='Edificio del SSEI y vías de acceso', group='SSEI', tipo='obra', method='Paramétrica (m² por US$/m²)',
         qty=None, unit_name='global', unit=(1_200 * 1_700, 1_600 * 2_100, 2_630 * 3_200), split={'1.6.1': 0.95, '1.6.2': 0.05}, src=['SEICR', 'CEPA2018', 'ARFF'],
         note='Área de 1,200 / 1,600 / 2,630 m² (4 a 5 bahías según la FAA AC 150/5210-15A; P: la estación de 7 bahías de Juan Santamaría) por US$1,700 / 2,100 / 3,200 por m² (O: terminal de 2018 del AIES; M: edificios públicos salvadoreños recientes; P: Juan Santamaría 2021 sin IVA). El 5 % de traslado y puesta en marcha (1.6.2) es supuesto.'),
    dict(id='V1', name='Supervisión técnica de las obras', group='Supervisión', tipo='pct_obras', method='Paramétrica (% de la obra)',
         qty=None, unit_name='% de la obra', unit=(0.020, 0.030, 0.050), split=None, src=['SUPSV', 'SUP'],
         note='Supervisiones reales en El Salvador: edificios grandes de 1.9 a 2.5 % (bandas de equipaje del AIES 2025, 2.46 %; maternidad El Nido 1.88 %; CENT 2.19 %) y pavimentos del AIES de 5.7 a 6.5 %. M: 3 %, la inspección del arancel del CFIA, por la mezcla de edificios y lado aire. P: 5 %, la dirección técnica del CFIA y el porcentaje que usa el Plan de Adquisiciones 2026.'),
    dict(id='V2', name='Seguimiento del PGAS de construcción', group='Gestión socioambiental', tipo='pct_obras', method='Paramétrica (% de la obra)',
         qty=None, unit_name='% de la obra', unit=(0.0033, 0.0072, 0.018), split=None, src=['EAS'],
         note='Mediana de cuatro préstamos de la región (0.72 %). Las medidas del PGAS las ejecuta el contratista dentro de su precio; este monto cubre su seguimiento dentro de los contratos de supervisión (1.7.1 y 1.7.2), repartido entre ellos como la supervisión técnica. La revisión del PGAS del contratista (1.7.3), el mecanismo de quejas y los informes socioambientales (3.3.3 y 3.3.4) los lleva el especialista socioambiental de la UEP, cuyo costo está en U1.'),
    dict(id='C1', name='Plan Estratégico del Sistema Aeronáutico', group='Componente II', tipo='servicio', method='Análoga',
         qty=None, unit_name='global', unit=(110_000, 500_000, 1_900_000), split={'2.1': 1}, src=['PEASV'],
         note='O: capítulo de transporte del Plan Maestro de Infraestructura (BID ES-T1289, 2018). M: Plan Maestro Nacional de Aviación Civil de Guyana (BID GY-T1134, 2016). P: Plan Director del Tren del Pacífico (MOPT, Deloitte, 2023).'),
    dict(id='C2', name='Actualización del Plan Maestro Aeroportuario', group='Componente II', tipo='servicio', method='Análoga',
         qty=None, unit_name='global', unit=(427_000, 1_065_000, 2_657_000), split={'2.2.1': 1}, src=['PMSV'],
         note='O: plan maestro vigente del AIES (Kimley-Horn, USTDA, 2012-2013). P: actualización del plan maestro de Rionegro, Colombia (2023). M: media geométrica de ambos.'),
    dict(id='C3', name='Capacitación de 21 funcionarios en planificación y operación', group='Componente II', tipo='servicio',
         method='Determinación de tarifas', qty=None, unit_name='global', unit=team((1, 1.5, 2), (0, 0, 0)), split={'2.2.2': 1}, src=['TARSV'],
         note='1 a 2 meses-persona de experto internacional.'),
    dict(id='C4', name='Estrategia y capacitación BIM', group='Componente II', tipo='servicio', method='Análoga',
         qty=None, unit_name='global', unit=(150_000, 209_000, 500_000), split={'2.3.1': 0.7, '2.3.2': 0.3}, src=['BIM'],
         note='O: firma del piloto BIM de RG-T4814; M: Plan BIM del MEF de Perú; P: CT completa de RG-T4814. El reparto 70/30 es supuesto.'),
    dict(id='C5', name='Estudio de conectividad terrestre', group='Componente II', tipo='servicio', method='Determinación de tarifas',
         qty=None, unit_name='global', unit=team((2, 3, 4), (10, 15, 20)), split={'2.4': 1}, src=['TARSV'],
         note='Equipo de 2 a 4 meses-persona internacionales y 10 a 20 nacionales en 7.5 meses.'),
    dict(id='C6', name='Estudio de diversificación de destinos', group='Componente II', tipo='servicio', method='Análoga',
         qty=None, unit_name='global', unit=(110_000, 165_000, 250_000), split={'2.5': 1}, src=['RUTASSV'],
         note='O: estudio con firma de la CT ES-T1315. M: estudio de perfil y gasto del visitante internacional de CORSATUR (2025-2026). P: tope de estudios con firma de la CT ES-T1314. No hay estudios de rutas publicados en Centroamérica.'),
    dict(id='C7', name='Auditoría y capacitación para la certificación EDGE', group='Componente II', tipo='servicio',
         method='Determinación de tarifas', qty=None, unit_name='global', unit=(349 + 2_900 + 2 * 2_600, 349 + 7_250 + 4 * 3_000, 349 + 12_000 + 6 * 3_500),
         split={'2.6.1': 0.85, '2.6.2': 0.15}, src=['EDGE', 'HON'],
         note='Tarifa publicada de GBCI más 2 a 6 meses-persona del auditor. El honorario del auditor no se publica: supuesto.'),
    dict(id='C8', name='Estudio de separación de flujos', group='Componente II', tipo='servicio', method='Determinación de tarifas',
         qty=None, unit_name='global', unit=team((1, 1.5, 2), (8, 12, 16)), split={'2.7': 1}, src=['TARSV'],
         note='Equipo de 1 a 2 meses-persona internacionales y 8 a 16 nacionales.'),
    dict(id='C9', name='Estudio de movilidad interna', group='Componente II', tipo='servicio', method='Determinación de tarifas',
         qty=None, unit_name='global', unit=team((1, 1.5, 2), (8, 12, 16)), split={'2.8': 1}, src=['TARSV'],
         note='Mismo equipo que el estudio de separación de flujos.'),
    dict(id='C10', name='Programa de igualdad e inclusión (300 funcionarios)', group='Componente II', tipo='servicio',
         method='Determinación de tarifas', qty=None, unit_name='global', unit=team((0, 0, 0), (2, 3, 4)), split={'2.9': 1}, src=['TARSV'],
         note='2 a 4 meses-persona de experto nacional.'),
    dict(id='U1', name='Personal de la Unidad Ejecutora (8 puestos)', group='Componente III', tipo='servicio', method='Ascendente (puestos × honorario × meses)',
         qty=None, unit_name='global', unit=None, split={'3.1.1': 1}, src=['PROP', 'PA2026', 'HON'],
         note='Siete puestos clave de la Propuesta de Préstamo, contratados entre abril y mayo de 2026, más el técnico de apoyo administrativo del ROP. Cada puesto se cuenta desde su contratación real hasta el fin de la actividad de nivel de esfuerzo 3.1.1-06. La plantilla ampliada que prevé el PEP (19 plazas, US$4.07 M) y que el Plan de Adquisiciones 2026-2 desglosa en 21 procesos está en U3.'),
    dict(id='U2', name='Gastos operativos de la Unidad Ejecutora', group='Componente III', tipo='servicio', method='Ascendente (mensual × meses)',
         qty=None, unit_name='global', unit=None, split={'3.1.1': 1}, src=['ROP', 'ANX3'],
         note='Servicios, oficina, combustible, pasajes y equipo (ROP 5.4). M: US$200,000 del Anexo III para gastos recurrentes de toda la ejecución; O y P: cálculo ascendente propio con montos mensuales supuestos.'),
    dict(id='U3', name='Plantilla ampliada de la Unidad Ejecutora (21 procesos del Plan de Adquisiciones 2026-2)', group='Componente III', tipo='servicio',
         method='Análoga (monto del Plan de Adquisiciones por mes de contrato)', qty=None, unit_name='global', unit=None, split={'3.1.1': 1}, src=['PA2026', 'PEP'],
         note='21 procesos 3CV activos del Plan de Adquisiciones 2026-2 (P00011 a P00041 sin P00019 cancelado ni P00014, que es el técnico de apoyo de U1), con firmas estimadas de septiembre de 2026 a septiembre de 2027 y un estimado de US$1.92 M. El "Estimated Amount" de cada proceso cubre todo su plazo, no un año (en los contratos clave es el monto anual por 56 / 12). Se divide entre los meses que van de la firma estimada del PA al fin del plazo que ese plan supone (56 meses desde abril de 2026) y se multiplica por los meses que van de la firma del cronograma al fin de 3.1.1-06. O y P: 0.85 y 1.15 veces ese monto mensual (supuesto: el PA solo da un estimado).'),
    dict(id='U4', name='Auditoría externa de los estados financieros', group='Componente III', tipo='servicio', method='Análoga',
         qty=None, unit_name='global', unit=(148_000, 191_000, 320_000), split={'3.5.2': 0.75, '3.5.4': 0.25}, src=['AUDSV', 'MEL'],
         note='Cuatro ejercicios: tres en 3.5.2 y los estados financieros finales en el cierre (3.5.4). Por ejercicio: O US$36,985 (PwC, ES-L1155, primer año), M US$47,783 (promedio de PwC y de Cornejo & Umaña para CEPA), P US$80,000 (presupuesto de ES-L1151); con IVA. El MEL y el PEP presupuestan US$160,000. El informe de terminación del cierre lo prepara la UEP.'),
    dict(id='U5', name='Evaluaciones de medio término y final', group='Componente III', tipo='servicio', method='Análoga',
         qty=None, unit_name='global', unit=(90_000, 150_000, 172_500), split={'3.5.3': 1}, src=['EVALSV', 'MEL'],
         note='O: intermedia de ES-L1151 (US$50,000) más la final de un programa del MOPT (US$40,000). M: intermedia y final de ES-L1151 (US$50,000 y 100,000). P: intermedia de ES-L1075 (US$72,500) más la final de ES-L1151. Se reparte entre las dos evaluaciones en 1/3 y 2/3, la proporción de M.'),
]

# Referencia del Anexo III / EEO#3 para comparar (no entra en la estimación), en US$
REFERENCE = {
    'Terminal': 78_992_537.10, 'Lado aire': 15_081_420.79 + 8_125_092.11, 'Estacionamiento': 64_202_613.69, 'SSEI': 9_473_574.43,
    'Supervisión': 8_793_761.91, 'Componente II': 5_000_000, 'Componente III': 5_331_000,
}


# ---- Reparto del costo entre las actividades de quien cobra (ver la regla en la cabecera) ----
PAYEES = {'Contratista de obra', 'Firma de supervisión', 'Firma consultora', 'Auditor externo'}
UEP_INDIRECT = '3.1.1-06'  # única actividad de la UEP con costo: el costo indirecto de U1, U2 y U3
UEP_ELEMENTS = ('U1', 'U2', 'U3')
# Contrato de supervisión de cada actividad (T terminal, E estacionamiento, P plataformas y Foxtrot, S SSEI) y obras que supervisa
SUP_CONTRACT = {'1.7.1-01': 'T', '1.7.1-02': 'T', '1.7.1-05': 'T', '1.7.1-03': 'E', '1.7.1-04': 'E', '1.7.1-06': 'E',
                '1.7.2-01': 'P', '1.7.2-02': 'P', '1.7.2-05': 'P', '1.7.2-03': 'S', '1.7.2-04': 'S', '1.7.2-06': 'S'}
SUP_WORKS = {'T': ('1.2.',), 'E': ('1.5.',), 'P': ('1.3.', '1.4.'), 'S': ('1.6.',)}
SUP_ELEMENTS = ('V1', 'V2')
# Porcentajes pequeños y explícitos por la forma de la actividad (inicio del nombre): movilización 2 %, pruebas 2 %, informe final
# de la supervisión 4 % (incluye el apoyo a las recepciones, que antes se cargaba al paquete 1.7.4).
AUTO = (('Movilizar', 0.02), ('Probar', 0.02), ('Realizar las pruebas', 0.02), ('Presentar el informe final', 0.04))
# Reglas particulares (elemento, paquete): fixed fija el peso de algunas actividades; rest limita el resto del reparto a esas
# actividades (por duración); auto=False desactiva los porcentajes de AUTO.
RULES = {
    ('T1', '1.2.4'): dict(fixed={'1.2.4-05': 0.03}, rest=['1.2.4-04']),  # mobiliario: se instala y se prueba
    ('T2', '1.2.4'): dict(fixed={'1.2.4-01': 0.02, '1.2.4-03': 0.11, '1.2.4-05': 0.02}, rest=['1.2.4-02']),  # puentes: 85 % fabricación y entrega
    ('T4', '1.2.4'): dict(fixed={'1.2.4-05': 0.03}, rest=['1.2.4-04']),  # sistemas: a su instalación
    ('A1', '1.3.2'): dict(rest=['1.3.2-01', '1.3.2-02', '1.3.2-03', '1.3.2-04']),  # el pavimento asfáltico (-05) lo lleva A2
    ('A2', '1.3.2'): dict(rest=['1.3.2-05']),
    ('C7', '2.6.1'): dict(fixed={'2.6.1-03': 0.15}),  # el acompañamiento dura 441 dl pero son pocas horas: 15 %
    ('U5', '3.5.3'): dict(fixed={'3.5.3-02': 1 / 3}, rest=['3.5.3-04']),  # intermedia US$50,000 y final US$100,000 (EVALSV)
    ('V2', '1.7.1'): dict(auto=False),
    ('V2', '1.7.2'): dict(auto=False),
}


def payees(ctx: dict, pkg: str) -> list[str]:
    return [c for c, a in ctx['acts'].items() if a['pkg'] == pkg and a['owner'] in PAYEES]


def act_weights(el: str, pkg: str, ctx: dict, subset: list[str] | None = None) -> dict[str, float]:
    """Peso de cada actividad que cobra en el costo del elemento el dentro del paquete pkg (suma 1)."""
    if el in UEP_ELEMENTS:
        assert pkg == '3.1.1' and UEP_INDIRECT in ctx['acts']
        return {UEP_INDIRECT: 1.0}
    acts = payees(ctx, pkg) if subset is None else subset
    assert acts, f'el paquete {pkg} tiene costo ({el}) pero ninguna actividad de quien cobra el contrato'
    rule = RULES.get((el, pkg), {})
    fixed = dict(rule.get('fixed', {}))
    cand = [c for c in rule.get('rest', acts) if c not in fixed]
    assert all(c in acts for c in list(fixed) + cand), (el, pkg)
    if rule.get('auto', True):
        for c in list(cand):
            share = next((x for pre, x in AUTO if ctx['acts'][c]['name'].startswith(pre)), None)
            if share is not None and len(cand) > 1:
                fixed[c] = share
                cand.remove(c)
    rest = 1 - sum(fixed.values())
    w = dict(fixed)
    if cand:
        tot = sum(ctx['acts'][c]['dur'] for c in cand)
        for c in cand:
            w[c] = rest * ctx['acts'][c]['dur'] / tot
    else:
        w = {c: x / sum(fixed.values()) for c, x in fixed.items()}
    assert abs(sum(w.values()) - 1) < 1e-9, (el, pkg, w)
    return w


def mid_ord(a: dict) -> float:
    return a['start'].toordinal() + (a['finish'] - a['start']).days / 2


def esc(mid: date, k: int, servicio: bool = False) -> float:
    rate = (ESC_SERV if servicio else ESC)[k]
    return (1 + rate) ** ((mid - BASE_DATE).days / 365.25)


def months_from(a: date, b: date) -> float:
    """Meses de contrato entre dos fechas (cero si b es anterior)."""
    return max(0.0, (b - a).days / MONTH_DAYS)


def uep_detail(ctx: dict) -> dict:
    """Puestos y procesos de la UEP con su inicio real y sus meses hasta el fin de 3.1.1-06 (ctx['uep'])."""
    u = ctx['uep']
    posts = []
    for name, rates, st in UEP:
        st = st or u['tech_start']
        posts.append({'puesto': name, 'O': rates[0], 'M': rates[1], 'P': rates[2], 'inicio': st, 'meses': months_from(st, u['end'])})
    lots = []
    for n, code, procs in PLANTILLA:
        sign = u['lot_sign'][code]
        for pid, name, amount, pa_sign in procs:
            monthly = amount / months_from(pa_sign, PA_HORIZON)
            lots.append({'lote': n, 'proceso': pid, 'puesto': name, 'monto_pa': amount, 'firma_pa': pa_sign, 'firma_modelo': sign,
                         'mensual': monthly, 'meses': months_from(sign, u['end'])})
    return {'posts': posts, 'lots': lots, 'start': u['start'], 'end': u['end']}


def uep_fraction(det: dict, d: date) -> dict[str, float]:
    """Fracción planificada de cada elemento de la UEP al cierre de la fecha d (costo mensual por puesto desde su inicio)."""
    out = {}
    tot = sum(p['M'] * p['meses'] for p in det['posts'])
    out['U1'] = sum(p['M'] * min(p['meses'], months_from(p['inicio'], d)) for p in det['posts']) / tot
    out['U2'] = min(1.0, months_from(det['start'], d) / months_from(det['start'], det['end']))
    tot3 = sum(x['mensual'] * x['meses'] for x in det['lots'])
    out['U3'] = sum(x['mensual'] * min(x['meses'], months_from(x['firma_modelo'], d)) for x in det['lots']) / tot3
    return out


def estimate(ctx: dict, escalate: bool = True) -> dict:
    """ctx: actividades del cronograma (ctx['acts']: código -> paquete, nombre, duración, inicio, fin, responsable) y fechas de la UEP
    (ctx['uep']). Devuelve elementos, costos por paquete y reservas (US$). Con escalate=False deja los valores en US$ de 2025
    (para compararlos con el estudio de costos del préstamo)."""
    det = uep_detail(ctx)
    els = []

    def mid_of(e):
        # punto medio ponderado por el peso de cada paquete y de cada actividad que ejecuta el elemento
        tot = sum(s * w * mid_ord(ctx['acts'][a]) for c, s in e['split'].items() for a, w in act_weights(e['id'], c, ctx).items())
        return date.fromordinal(round(tot / sum(e['split'].values())))

    obra_total = [0.0, 0.0, 0.0]
    for e in ELEMENTS:
        e = dict(e)
        if 'method_override' in e:
            e['method'] = e.pop('method_override')
        if e['id'] == 'U1':
            e['unit'] = tuple(sum(p[('O', 'M', 'P')[k]] * p['meses'] for p in det['posts']) for k in range(3))
            e['note'] += f' {sum(p["meses"] for p in det["posts"]) / len(det["posts"]):.1f} meses en promedio por puesto; total mensual US${sum(p["M"] for p in det["posts"]):,} (M).'
        if e['id'] == 'U2':
            n = months_from(det['start'], det['end'])
            e['unit'] = (UEP_OPEX[0] * n + UEP_SETUP[0], UEP_OPEX_M, UEP_OPEX[2] * n + UEP_SETUP[2])
        if e['id'] == 'U3':
            m = sum(x['mensual'] * x['meses'] for x in det['lots'])
            e['unit'] = (PLANTILLA_O * m, m, PLANTILLA_P * m)
            e['note'] += f' Resultado: US${m / 1e6:.2f} M frente a US${PLANTILLA_TOTAL / 1e6:.2f} M del PA.'
        if e['tipo'] in ('pct_obras', 'pct_lado_aire'):
            els.append(e)
            continue
        if e['id'] == 'U3':
            tot3 = sum(x['mensual'] * x['meses'] for x in det['lots'])
            mid = date.fromordinal(round(sum(x['mensual'] * x['meses'] * (x['firma_modelo'].toordinal() + (det['end'] - x['firma_modelo']).days / 2)
                                              for x in det['lots']) / tot3))
        elif e['id'] in UEP_ELEMENTS:
            mid = det['start'] + (det['end'] - det['start']) / 2
        else:
            mid = mid_of(e)
        base = [(e['qty'] or 1) * e['unit'][k] for k in range(3)]
        tax = 1 + IVA if e['tipo'] == 'obra' else 1
        e['mid'] = mid
        e['esc'] = [esc(mid, k, e['tipo'] != 'obra') if escalate else 1.0 for k in range(3)]
        e['omp'] = [base[k] * tax * e['esc'][k] for k in range(3)]
        if e['tipo'] == 'obra':
            for k in range(3):
                obra_total[k] += e['omp'][k]
        els.append(e)

    # Señalización y balizamiento: porcentaje del pavimento ya escalado, repartido entre plataformas y Foxtrot.
    pav = {e['id']: e for e in els if e['id'] in ('A1', 'A2', 'A3')}
    for e in els:
        if e['tipo'] != 'pct_lado_aire':
            continue
        apron = [pav['A1']['omp'][k] + pav['A2']['omp'][k] for k in range(3)]
        fox = pav['A3']['omp']
        e['omp'] = [(apron[k] + fox[k]) * e['unit'][k] for k in range(3)]
        e['split'] = {'1.3.3': apron[1] / (apron[1] + fox[1]), '1.4.2': fox[1] / (apron[1] + fox[1])}
        for k in range(3):
            obra_total[k] += e['omp'][k]

    obra_E = sum((e['omp'][0] + 4 * e['omp'][1] + e['omp'][2]) / 6 for e in els if e['tipo'] in ('obra', 'pct_lado_aire'))
    land = sum((e['omp'][0] + 4 * e['omp'][1] + e['omp'][2]) / 6 for e in els if e['group'] in ('Terminal', 'Estacionamiento'))
    for e in els:
        if e['tipo'] != 'pct_obras':
            continue
        e['omp'] = [obra_E * e['unit'][k] for k in range(3)]
        # supervisión (V1) y seguimiento del PGAS (V2): ambos van a los contratos de supervisión, repartidos según la obra
        # supervisada (terminal y estacionamiento en 1.7.1; plataformas, Foxtrot y SSEI en 1.7.2)
        e['split'] = {'1.7.1': land / obra_E, '1.7.2': 1 - land / obra_E}

    for e in els:
        o, m, p = e['omp']
        e['E'] = (o + 4 * m + p) / 6
        e['sigma'] = (p - o) / 6

    total_E = sum(e['E'] for e in els)
    sig_ind = math.sqrt(sum(e['sigma'] ** 2 for e in els))
    sig_cor = sum(e['sigma'] for e in els)
    # Los elementos de obra comparten precios de insumos y el escalamiento, así que no son independientes, pero tampoco se
    # mueven juntos en todo: se usa una correlación uniforme explícita (RHO) y se informa la reserva para otros valores.
    # Con correlación uniforme rho: sigma_total^2 = suma(sigma_i^2) + rho * suma_{i != j}(sigma_i * sigma_j)
    def sig_rho(rho):
        return math.sqrt(sig_ind ** 2 + rho * (sig_cor ** 2 - sig_ind ** 2))
    sigma_total = sig_rho(RHO)
    rho = RHO
    contingency = Z80 * sigma_total
    reserve_by_rho = {f'{x:.2f}': Z80 * sig_rho(x) for x in (0.0, 0.25, 0.3, 0.5, 1.0)}
    pkg, pkg_res = {}, {}
    for e in els:
        share_res = contingency * e['sigma'] / sig_cor  # la reserva se asigna en proporción a la incertidumbre de cada elemento
        for c, s in e['split'].items():
            pkg[c] = pkg.get(c, 0.0) + e['E'] * s
            pkg_res[c] = pkg_res.get(c, 0.0) + share_res * s
        e['reserve'] = share_res
    baseline = total_E + contingency
    return {
        'elements': els, 'packages': pkg, 'package_reserve': pkg_res, 'total_E': total_E, 'sigma_independiente': sig_ind,
        'sigma_correlacionada': sig_cor, 'sigma_total': sigma_total, 'rho': rho, 'contingencia_por_rho': reserve_by_rho, 'contingencia': contingency, 'linea_base': baseline,
        'reserva_gestion': baseline * MGMT_RESERVE, 'presupuesto': baseline * (1 + MGMT_RESERVE), 'uep': det,
        'total_O': sum(e['omp'][0] for e in els), 'total_M': sum(e['omp'][1] for e in els), 'total_P': sum(e['omp'][2] for e in els),
        'obras_E': obra_E,
    }


def allocate(res: dict, ctx: dict) -> dict:
    """Reparte el costo de cada elemento entre las actividades de quien cobra. Devuelve, por actividad, la estimación (base), la
    contingencia y los elementos que la forman. Verifica con assert que el costo de las actividades de cada paquete sea el del
    paquete y que solo cobren los pagadores y el costo indirecto de la UEP."""
    pk = res['packages']
    works = {g: sum(v for c, v in pk.items() if c.startswith(pre)) for g, pre in SUP_WORKS.items()}
    base, cont, parts = {}, {}, {}
    for e in res['elements']:
        for c, s in e['split'].items():
            if e['id'] in SUP_ELEMENTS:
                pay = payees(ctx, c)
                groups = sorted({SUP_CONTRACT[a] for a in pay})
                tot = sum(works[g] for g in groups)
                w = {}
                for g in groups:
                    for a, x in act_weights(e['id'], c, ctx, [a for a in pay if SUP_CONTRACT[a] == g]).items():
                        w[a] = works[g] / tot * x
            else:
                w = act_weights(e['id'], c, ctx)
            assert abs(sum(w.values()) - 1) < 1e-9
            for a, x in w.items():
                base[a] = base.get(a, 0.0) + e['E'] * s * x
                cont[a] = cont.get(a, 0.0) + e['reserve'] * s * x
                parts.setdefault(a, {})
                parts[a][e['id']] = parts[a].get(e['id'], 0.0) + e['E'] * s * x
    for a in base:
        assert ctx['acts'][a]['owner'] in PAYEES or a == UEP_INDIRECT, f'{a} no debería tener costo'
    for c in pk:
        sub = [a for a in base if ctx['acts'][a]['pkg'] == c]
        assert abs(sum(base[a] for a in sub) - pk[c]) < 1e-3, c
        assert abs(sum(cont[a] for a in sub) - res['package_reserve'][c]) < 1e-3, c
    assert abs(sum(base.values()) - res['total_E']) < 1e-2 and abs(sum(cont.values()) - res['contingencia']) < 1e-2
    return {'base': base, 'cont': cont, 'parts': parts}


def sensitivity(ctx) -> list[dict]:
    """Paso 7: cambia un supuesto a la vez y devuelve la estimación PERT y el presupuesto resultantes (US$)."""
    global ESC
    base = estimate(ctx)
    cases = []

    def run(label, change, mutate):
        global ESC
        saved_el, saved_esc = [dict(e) for e in ELEMENTS], ESC
        mutate()
        r = estimate(ctx)
        ELEMENTS[:] = saved_el
        ESC = saved_esc
        cases.append({'supuesto': label, 'cambio': change, 'estimacion': r['total_E'], 'diferencia': r['total_E'] - base['total_E'],
                      'presupuesto': r['presupuesto']})

    def set_unit(i, k, v):
        for e in ELEMENTS:
            if e['id'] == i:
                u = list(e['unit']); u[k] = v; e['unit'] = tuple(u)

    def scale_obras(f):
        for e in ELEMENTS:
            if e['tipo'] == 'obra' and e['id'] not in ('T3', 'T4'):
                e['unit'] = tuple(x * f for x in e['unit'])

    def set_esc(m):
        global ESC
        ESC = (ESC[0], m, ESC[2])

    run('Precios unitarios de las obras', '+10%', lambda: scale_obras(1.1))
    run('Precios unitarios de las obras', '−10%', lambda: scale_obras(0.9))
    run('Escalamiento de obras más probable', '5.5% anual', lambda: set_esc(0.055))
    run('Escalamiento de obras más probable', '1.25% anual', lambda: set_esc(0.0125))
    run('Costo más probable de la terminal', 'US$2,900/m²', lambda: set_unit('T1', 1, 2_900))
    run('Estacionamiento más probable', 'US$31,318 por plaza (estimado del Plan de Adquisiciones 2026)', lambda: set_unit('E1', 1, 31_318 / 1.13))
    run('Estacionamiento más probable', f'US${round(CEPA2022_PLAZA):,} por plaza (diseño de CEPA 2022)', lambda: set_unit('E1', 1, round(CEPA2022_PLAZA)))
    run('Supervisión más probable', '5% (Plan de Adquisiciones 2026)', lambda: set_unit('V1', 1, 0.05))
    return cases


def write_outputs(res: dict, out: Path, ctx=None) -> None:
    fields = ['id', 'grupo', 'elemento', 'metodo', 'cantidad', 'unidad', 'unit_O', 'unit_M', 'unit_P', 'punto_medio', 'esc_M',
              'O_usd', 'M_usd', 'P_usd', 'E_usd', 'sigma_usd', 'reserva_usd', 'paquetes', 'fuentes', 'nota']
    with (out / 'estimacion_costos.csv').open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(fields)
        for e in res['elements']:
            w.writerow([e['id'], e['group'], e['name'], e['method'], e['qty'] if e['qty'] else '', e['unit_name'],
                        *(round(x, 4) for x in e['unit']), e.get('mid', ''), round(e['esc'][1], 4) if 'esc' in e else '',
                        *(round(x) for x in e['omp']), round(e['E']), round(e['sigma']), round(e['reserve']),
                        '; '.join(f'{c} {s:.1%}' for c, s in e['split'].items()), ', '.join(e['src']), e['note']])
    summary = {k: v for k, v in res.items() if k not in ('elements', 'packages', 'package_reserve', 'uep')}
    summary['por_grupo'] = {}
    for e in res['elements']:
        g = summary['por_grupo'].setdefault(e['group'], {'O': 0, 'M': 0, 'P': 0, 'E': 0, 'reserva': 0, 'referencia': REFERENCE.get(e['group'])})
        for k, v in zip('OMP', e['omp']):
            g[k] += v
        g['E'] += e['E']
        g['reserva'] += e['reserve']
    summary['paquetes'] = {c: {'E': res['packages'][c], 'reserva': res['package_reserve'][c]} for c in sorted(res['packages'], key=lambda c: [int(p) for p in c.split('.')])}
    det = res['uep']
    summary['uep'] = [{**p, 'inicio': str(p['inicio'])} for p in det['posts']]
    summary['plantilla'] = [{**x, 'firma_pa': str(x['firma_pa']), 'firma_modelo': str(x['firma_modelo'])} for x in det['lots']]
    summary['uep_periodo'] = {'inicio': str(det['start']), 'fin': str(det['end'])}
    if ctx is not None:
        flat = estimate(ctx, escalate=False)
        summary['sin_escalamiento'] = {
            'total_E': flat['total_E'], 'contingencia': flat['contingencia'], 'linea_base': flat['linea_base'],
            'por_grupo': {g: sum(e['E'] + e['reserve'] for e in flat['elements'] if e['group'] == g) for g in summary['por_grupo']}}
        summary['sensibilidad'] = sensitivity(ctx)
    summary['fuentes'] = SOURCES
    summary['supuestos'] = {'base': str(BASE_DATE), 'escalamiento_OMP': ESC, 'iva': IVA, 'z80': Z80, 'reserva_gestion': MGMT_RESERVE,
                            'tarifa_internacional_mp': INTL, 'tarifa_nacional_mp': NAC, 'reparto_terminal': TERMINAL_SPLIT,
                            'plantilla_OP': (PLANTILLA_O, PLANTILLA_P), 'horizonte_pa': str(PA_HORIZON)}
    (out / 'estimacion_costos.json').write_text(json.dumps(summary, ensure_ascii=False, indent=1, default=str), encoding='utf-8')

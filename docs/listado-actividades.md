# Listado de actividades del cronograma

Este documento descompone los 54 paquetes de trabajo de la EDT en 449 actividades y es el insumo del cronograma del Programa de Modernización del Aeropuerto Internacional de El Salvador (ES-L1173). Para cada actividad indica la fase, el entregable (paquete de trabajo) al que pertenece, el responsable y la estimación de su duración por tres valores (PERT). Al final están la tabla de dependencias, las restricciones de fecha, las actividades de nivel de esfuerzo y los hitos. El cronograma toma de aquí las duraciones y las precedencias; las fechas, la ruta crítica y las holguras se calculan en él.

## 1. Cómo se obtuvo el listado

La EDT termina en paquetes de trabajo, que son entregables; las actividades se definen en el cronograma, al descomponer cada paquete en las acciones que lo producen (PMI, 2017, sección 6.2). El desglose sigue tres pasos:

1. **Identificar las actividades necesarias.** Para cada paquete se listaron las acciones que producen su entregable, a partir del diccionario de la EDT (sección 5) y de los documentos del programa: el Reglamento Operativo (ROP), el contrato de préstamo, el Plan de Ejecución (PEP), el Plan de Adquisiciones 2026-2, los avisos de licitación, el análisis de costos (EEO#3), la evaluación y el plan de gestión ambiental y social (PGAS) y el plan de monitoreo y evaluación (MEL).
2. **Usar verbos de acción.** Cada actividad empieza con un verbo en infinitivo y nombra un objeto concreto ("Construir la estructura de concreto de los niveles 1 a 3 de la terminal", "Obtener la no objeción del BID a los documentos de licitación del SSEI").
3. **Verificar que cada actividad se pueda estimar, secuenciar, asignar y controlar.** Cada una tiene un solo responsable, un resultado verificable, una duración estimada y al menos una relación de precedencia. La duración más probable va de 5 a 130 días laborables; los trabajos más largos se dividieron en etapas o frentes.

Criterios adicionales:

- **Actividades recurrentes por periodo.** Los planes operativos anuales, los informes semestrales, las solicitudes de desembolso y las auditorías se desglosan por año o por semestre.
- **Adquisiciones por contrato.** Cada contratación tiene sus propias actividades (preparar documentos, obtener la no objeción del BID, publicar y recibir ofertas o propuestas, evaluar, adjudicar y firmar). Por eso los paquetes 3.4.1 a 3.4.4 tienen más actividades que el resto.
- **Actividades de terceros.** Las no objeciones del BID y las aprobaciones de la AAC son actividades con su propia duración y con el tercero como responsable, porque consumen tiempo del cronograma aunque la UEP no las ejecute.
- **Responsables.** Los puestos de la Unidad Ejecutora (UEP) del diccionario de la EDT, CEPA, los contratistas de obra, las firmas de supervisión y consultoría, el auditor externo, el BID y la AAC.

### Fases

Cada actividad se asigna a una de cinco fases, que siguen los grupos de procesos de la dirección de proyectos (PMI, 2017): inicio, planificación, ejecución, monitoreo y control, y cierre.

| Fase | Qué incluye | Actividades |
|---|---|---:|
| Inicio | Condiciones de arranque del programa: conformar la UEP, aprobar el ROP, suscribir el convenio de transferencia y abrir la cuenta especial. | 19 |
| Planificación | Planes (PEP, POA, Plan de Adquisiciones), revisión de diseños, sistemas de gestión ambiental y social, documentos de licitación y términos de referencia. | 126 |
| Ejecución | Conducir las adquisiciones (publicar, evaluar, adjudicar y firmar), construir, instalar, elaborar estudios y capacitar. | 224 |
| Monitoreo y control | Supervisar las obras, dar seguimiento al PGAS, informar al BID, auditar, evaluar a medio término y revisar productos. | 45 |
| Cierre | Recibir las obras, aprobar productos finales, evaluar al cierre, liquidar contratos, presentar los estados financieros finales y el informe de terminación. | 35 |
| **Total** | | **449** |

## 2. Estimación de las duraciones

Todas las duraciones están en días laborables (dl), de lunes a viernes, sin feriados; un mes equivale a unos 21.7 dl. Cada actividad tiene tres valores, según la estimación por tres valores (PMI, 2017, sección 6.4.2.4):

- **O (optimista):** la duración si todo sale bien.
- **M (más probable):** la duración en condiciones normales.
- **P (pesimista):** la duración si se presentan los problemas razonables de ese tipo de trabajo (lluvias, revisiones adicionales, reprocesos).
- **Estimada (De):** De = (O + 4M + P) / 6. El cronograma usa De redondeada al día laborable entero.

El análisis de reservas agrega además una reserva de contingencia (PMI, 2017, sección 6.4.2.6). No se agrega a cada actividad: con O y P se obtiene la desviación de cada actividad, σ = (P − O) / 6, y el cronograma fija con la desviación de la ruta crítica una reserva de tiempo explícita para el programa.

Los tres valores se fijaron con las técnicas de estimación de la duración (PMI, 2017, sección 6.4.2). La columna "Técnica" de cada actividad indica cuál se usó y la columna "Fuente" su fundamento:

| Técnica | Cuándo se usó | Actividades |
|---|---|---:|
| Dato del programa | La duración o la fecha sale de un documento del propio programa: plazos del ROP y del contrato de préstamo, fechas del Plan de Adquisiciones 2026-2 y de los avisos de licitación, plazos de contrato del PEP. | 111 |
| Calibrada | La duración se dedujo de dos fechas documentadas del programa (inicio del proceso o apertura de ofertas y firma estimada en el Plan de Adquisiciones 2026-2 o en el PEP), repartiendo el intervalo entre las etapas del proceso. O y P se fijaron un 20% por debajo y por encima. | 22 |
| Análoga | Plazos reales de proyectos similares: ampliaciones de terminales, estacionamientos de varios niveles, puentes de abordaje y consultorías equivalentes. | 11 |
| Paramétrica | Cantidad de obra por rendimiento: m² de pavimento por mes con el aeropuerto en operación, m² de estructura por mes, cantidades del EEO#3 y del PGAS. | 22 |
| Juicio de expertos | Pasos administrativos y técnicos sin dato publicado (revisiones internas, aprobaciones de CEPA, pruebas); la fuente explica el razonamiento. | 270 |
| Nivel de esfuerzo | Actividades de acompañamiento (supervisión, seguimiento del PGAS, mecanismo de quejas, informes socioambientales, desembolsos) que no tienen duración propia: empiezan con sus predecesoras y terminan con las actividades que acompañan (sección 6, "Actividades de nivel de esfuerzo"). Se marcan con NE. | 13 |

## 3. Dependencias

La tabla de dependencias (sección 7) tiene una fila por cada par de actividades relacionadas. Usa los tipos de relación del método de diagramación por precedencia y las clases de dependencia (PMI, 2017, secciones 6.3.2.1 y 6.3.2.2):

- **Tipo de relación:** FI, fin a inicio (618); II, inicio a inicio (38); FF, fin a fin (21); IF, inicio a fin (0). El desfase está en días laborables; un desfase positivo es una espera y uno negativo, un adelanto. Las relaciones II con desfase permiten superponer etapas de obra, como las instalaciones con la estructura.
- **Clase:** obligatoria (550), cuando la impone la lógica técnica, el contrato o la norma; discrecional (57), cuando la decide el equipo; externa (70), cuando depende de un tercero (BID, AAC u otra autoridad).
- **Restricciones de fecha:** 43 actividades no pueden comenzar antes de una fecha documentada (sección 6, "Restricciones de fecha"): los avisos de licitación publicados, el inicio de los procesos según el Plan de Adquisiciones 2026-2, la incorporación real de los consultores de la UEP y los periodos que fija el contrato (ejercicios fiscales y semestres).
- **Condiciones del contrato de préstamo que se reflejan como dependencias:** ninguna obra empieza sin el Plan de Gestión del Riesgo de Desastres y Cambio Climático final presentado al BID (cláusula 4.06); ninguna obra del lado aire empieza sin el protocolo de seguridad operacional aprobado por la AAC; y la plataforma de posiciones remotas no empieza hasta que el SSEI esté reubicado y en funcionamiento (Propuesta de Préstamo, párrafo 4.6).
- **Un vínculo por par.** Entre dos actividades hay una sola relación, para que la red se pueda exportar a MS Project y Open Planner. Las actividades sin predecesora son las primeras del programa (Plan de Adquisiciones inicial y contratación de la UEP), y toda actividad sin otra sucesora termina antes del cierre administrativo (3.5.4-06).

## 4. Criterios de desglose por contrato

- Cada actividad tiene su propia estimación PERT con su fundamento; no se usan duraciones únicas por paquete.
- La licitación de obras (3.4.1) se divide en cuatro licitaciones públicas internacionales, una por obra (estacionamiento, terminal, SSEI y plataformas con calle Foxtrot), con las fechas de los avisos publicados y las firmas estimadas en el Plan de Adquisiciones 2026-2. Ninguna tiene precalificación: el plan y los avisos son licitación directa.
- La supervisión (3.4.2 y 1.7.1 a 1.7.2) tiene cuatro contratos, uno por obra, como en el Plan de Adquisiciones 2026-2. La recepción definitiva (1.7.4) también es por contrato, de modo que cada obra se recibe sin esperar a las demás.
- El Aviso General de Adquisiciones (5 de mayo de 2026) precede a todos los procesos, y el diseño de la fachada sur lo elabora el contratista de la terminal con la revisión de la supervisión (avisos de 2026).
- El Plan de Gestión del Riesgo de Desastres y Cambio Climático final (3.3.1) es una actividad del listado, porque el contrato lo exige antes del inicio de las obras.
- La evaluación de medio término se contrata al firmarse el contrato de obra y el de supervisión del SSEI, para que su informe quede antes del plazo de 60 días posterior al 50% del tiempo de ejecución planificado (S-III.10), y la evaluación final con el fin de la terminal; no se usan las fechas del PEP de noviembre de 2025. El último desembolso incluye el pago de la evaluación final.
- Las consultorías del Componente II (3.4.3) se contratan por separado, una por producto del PEP. Como no figuran en el Plan de Adquisiciones 2026-2, sus procesos empiezan después de incluirlas en una revisión del plan posterior al 31 de octubre de 2026.
- Todas las contrataciones del Componente II (3.4.3), las evaluaciones y las auditorías (3.4.4) tienen revisión ex ante del BID (Anexo III.i, 2.5; Plan de Adquisiciones 2026-2), con sus no objeciones como actividades del BID. La estrategia y capacitación BIM (2.3.1 y 2.3.2) va por lista corta internacional porque su contrato supera los US$200,000 de la tabla 10 del ROP.
- El listado incluye la plantilla ampliada de la UEP del Plan de Adquisiciones 2026-2 (21 procesos de consultores individuales, en seis lotes de fechas, 3.4.4-45 a 3.4.4-74) y la actividad de nivel de esfuerzo que administra el programa desde la UEP (3.1.1-06).
- Los paquetes 1.2.5 (accesibilidad y medidas EDGE de la terminal) y 1.6.2 (equipamiento del SSEI) tienen actividades del contratista de obra que ejecutan el trabajo; las de la UEP, CEPA y la supervisión verifican, trasladan o prueban.
- Las auditorías (3.4.4 y 3.5.2) son contratos anuales; la auditoría del último ejercicio queda dentro de la auditoría de los estados financieros finales del cierre (3.5.4).
- Los plazos de obra se estimaron por etapas y se contrastaron con los avisos de licitación, el sondeo de mercado de la terminal, el PEP y obras análogas.

## 5. Resumen

| Componente | Paquetes | Actividades | Inicio | Planificación | Ejecución | Monitoreo y control | Cierre |
|---|---:|---:|---:|---:|---:|---:|---:|
| Componente I. Obras y adecuaciones | 23 | 121 | 0 | 25 | 73 | 10 | 13 |
| Componente II. Fortalecimiento institucional | 12 | 66 | 0 | 12 | 30 | 11 | 13 |
| Administración, evaluación y auditorías | 19 | 262 | 19 | 89 | 121 | 24 | 9 |
| **Total** | **54** | **449** | **19** | **126** | **224** | **45** | **35** |

## 6. Listado de actividades

Las actividades se agrupan por entregable (paquete de trabajo de la EDT). El código de cada actividad es el del paquete seguido de un correlativo. O, M, P y Estimada están en días laborables.

### Componente I. Obras y adecuaciones

#### 1.1.1 Diseños de la terminal revisados y aprobados

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.1.1-01 | Revisar técnicamente el expediente de diseño de la terminal (planos, especificaciones y cantidades) | Planificación | Especialista en ingeniería aeroportuaria | 20 | 30 | 45 | 30.8 | Juicio de expertos | RFI-T sec 2: proyecto ejecutivo completo de 18,555 m2 en 3 niveles; 6 semanas para verificar el 80% del costo y actualizar el contexto de 2026 |
| 1.1.1-02 | Ajustar los diseños y el presupuesto de la terminal con la firma diseñadora (FIDS, CUTE, puentes de abordaje y observaciones de la revisión) | Planificación | Firma consultora | 20 | 30 | 50 | 31.7 | Juicio de expertos | EEO3 Cuadro 12: faltaban FIDS, CUTE y SATE y los puentes estaban subvaluados; 6 semanas de ajuste |
| 1.1.1-03 | Revisar la coordinación del modelo BIM de la terminal con los planos y las especificaciones | Planificación | Especialista en ingeniería aeroportuaria | 10 | 15 | 25 | 15.8 | Juicio de expertos | RFI-T sec 2: la terminal debe desarrollarse con metodología BIM; 3 semanas de revisión de interferencias |
| 1.1.1-04 | Aprobar el expediente de diseño de la terminal | Planificación | CEPA | 5 | 10 | 20 | 10.8 | Juicio de expertos | Aprobación interna de CEPA; 2 semanas |
| 1.1.1-05 | Emitir la no objeción del BID a las especificaciones técnicas y los planos de la licitación de la terminal | Planificación | BID | 3 | 5 | 10 | 5.5 | Dato del programa | ROP anexo 7.1 (p. 43): 5 días para la no objeción a los documentos de licitación |
| 1.1.1-06 | Elaborar el diseño final de la fachada sur de la terminal (tres salas de espera y sus puentes de abordaje) en el modelo BIM | Ejecución | Contratista de obra | 40 | 60 | 90 | 61.7 | Juicio de expertos | Inferencia (S-I.8), no un dato explícito: la EOI-T (P00024) solo contrata la supervisión del diseño de la fachada sur (3 salas y puentes) a integrar con la fachada norte, y el Anexo III.i (2.4) prevé contratos FIDIC amarillo, de diseño y construcción por el contratista; unos 3 meses de diseño de detalle |
| 1.1.1-07 | Revisar con la supervisión el diseño de la fachada sur y validar su integración con el diseño de la fachada norte | Monitoreo y control | Firma de supervisión | 10 | 15 | 25 | 15.8 | Juicio de expertos | Inferencia (S-I.8), no un dato explícito: según la EOI-T (P00024) la supervisión revisa y valida el diseño de las fachadas sur y norte; una ronda de revisión de 3 semanas |
| 1.1.1-08 | Aprobar el diseño de la fachada sur de la terminal | Planificación | CEPA | 3 | 5 | 8 | 5.2 | Juicio de expertos | Inferencia (S-I.8), no un dato explícito: aprobación de CEPA a propuesta de la supervisión; 1 semana |

#### 1.1.2 Diseños de plataformas y calle Foxtrot revisados y aprobados

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.1.2-01 | Realizar sondeos geotécnicos en las tres posiciones remotas y verificar el diseño de pavimentos | Planificación | Firma consultora | 20 | 30 | 50 | 31.7 | Juicio de expertos | EEO3 sec 4.2 recomienda un sondeo por posición remota; 6 semanas entre contratación, campo y ensayos |
| 1.1.2-02 | Revisar técnicamente los diseños de plataformas, calle Foxtrot, drenaje y ayudas visuales | Planificación | Especialista en ingeniería aeroportuaria | 20 | 30 | 45 | 30.8 | Juicio de expertos | EEO3 Cuadro 11 y 17: unos 68,500 m2 de plataformas y 18,400 m2 de Foxtrot (PGAS 2.4.3); 6 semanas |
| 1.1.2-03 | Revisar con la AAC la geometría del lado aire y el plan de fases de las obras | Planificación | AAC | 10 | 20 | 40 | 21.7 | Juicio de expertos | EDT 1.1.2: diseños compatibles con el protocolo de la AAC; 4 semanas de trámite externo |
| 1.1.2-04 | Ajustar los diseños y el presupuesto de plataformas y calle Foxtrot con la firma diseñadora | Planificación | Firma consultora | 15 | 25 | 40 | 25.8 | Juicio de expertos | 5 semanas de ajuste por observaciones técnicas, de la AAC y del sondeo |
| 1.1.2-05 | Aprobar los diseños de plataformas y calle Foxtrot | Planificación | CEPA | 5 | 10 | 20 | 10.8 | Juicio de expertos | Aprobación interna de CEPA; 2 semanas |
| 1.1.2-06 | Emitir la no objeción del BID a las especificaciones técnicas y los planos de la licitación de plataformas y Foxtrot | Planificación | BID | 3 | 5 | 10 | 5.5 | Dato del programa | ROP anexo 7.1 (p. 43): 5 días |

#### 1.1.3 Diseños del estacionamiento y del sistema solar revisados y aprobados

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.1.3-01 | Revisar técnicamente el expediente de diseño del estacionamiento (estructura, circulaciones y accesibilidad universal) | Planificación | Especialista en ingeniería aeroportuaria | 25 | 30 | 45 | 31.7 | Juicio de expertos | EEO3 sec 3.3 y 4.3: diseño de 700 plazas extrapolado a 2,000; 6 semanas por el mayor tamaño |
| 1.1.3-02 | Revisar el diseño del sistema fotovoltaico y su conexión eléctrica | Planificación | Especialista en ingeniería aeroportuaria | 8 | 12 | 20 | 12.7 | Juicio de expertos | PGAS sec 2.4.5: 3,166,804 kWh/año en cubierta; 2 a 3 semanas de revisión |
| 1.1.3-03 | Ajustar los diseños y el presupuesto del estacionamiento con la firma diseñadora | Planificación | Firma consultora | 15 | 20 | 35 | 21.7 | Juicio de expertos | 4 semanas de ajuste por observaciones |
| 1.1.3-04 | Aprobar el expediente de diseño del estacionamiento | Planificación | CEPA | 5 | 10 | 20 | 10.8 | Juicio de expertos | Aprobación interna de CEPA; 2 semanas |
| 1.1.3-05 | Emitir la no objeción del BID a las especificaciones técnicas y los planos de la licitación del estacionamiento | Planificación | BID | 3 | 5 | 10 | 5.5 | Dato del programa | ROP anexo 7.1 (p. 43): 5 días |

#### 1.1.4 Diseños del SSEI revisados y aprobados

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.1.4-01 | Revisar técnicamente el diseño del edificio del SSEI y de sus vías de acceso | Planificación | Especialista en ingeniería aeroportuaria | 15 | 20 | 30 | 20.8 | Juicio de expertos | Edificio menor (US$9.5 millones, PEP); 4 semanas de revisión |
| 1.1.4-02 | Validar con el SSEI y la AAC el emplazamiento, los tiempos de respuesta y la continuidad del servicio | Planificación | AAC | 8 | 15 | 30 | 16.3 | Juicio de expertos | EDT 1.1.4 y 1.6.2: servicio cubierto durante el traslado; 3 semanas con la AAC |
| 1.1.4-03 | Ajustar el diseño del SSEI con la firma diseñadora | Planificación | Firma consultora | 10 | 15 | 25 | 15.8 | Juicio de expertos | 3 semanas de ajuste |
| 1.1.4-04 | Aprobar el diseño del SSEI | Planificación | CEPA | 5 | 10 | 20 | 10.8 | Juicio de expertos | Aprobación interna de CEPA; 2 semanas |
| 1.1.4-05 | Emitir la no objeción del BID a las especificaciones técnicas y los planos de la licitación del SSEI | Planificación | BID | 3 | 5 | 10 | 5.5 | Dato del programa | ROP anexo 7.1 (p. 43): 5 días |

#### 1.2.1 Estructura y envolvente de la terminal construidas

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.2.1-01 | Movilizar al contratista e instalar cerramientos, accesos y obras provisionales con la terminal en operación | Ejecución | Contratista de obra | 20 | 30 | 45 | 30.8 | Juicio de expertos | RFI-T sec 2 (obra con el aeropuerto en operación); 6 semanas de movilización y plan de seguridad operacional |
| 1.2.1-02 | Ejecutar la demolición, el movimiento de tierra y la cimentación de la terminal | Ejecución | Contratista de obra | 55 | 75 | 110 | 77.5 | Paramétrica | RFI-T sec 2: huella de 5,868 m2 (nivel 1); rendimiento supuesto de unos 90 m2/dl con dos frentes |
| 1.2.1-03 | Construir la estructura de concreto de los niveles 1 a 3 de la terminal | Ejecución | Contratista de obra | 105 | 130 | 170 | 132.5 | Paramétrica | RFI-T sec 2: 18,555 m2 en 3 niveles; 2 frentes (norte y sur) a unos 1,500 m2/mes por frente (rendimiento supuesto) |
| 1.2.1-04 | Montar la estructura metálica y la cubierta de la terminal | Ejecución | Contratista de obra | 55 | 75 | 105 | 76.7 | Paramétrica | RFI-T sec 2: cubierta de doble altura sobre el nivel 2 (7,639 m2); rendimiento supuesto de unos 100 m2/dl con dos cuadrillas |
| 1.2.1-05 | Instalar las fachadas de vidrio y los cerramientos exteriores de la terminal | Ejecución | Contratista de obra | 60 | 80 | 110 | 81.7 | Paramétrica | RFI-T sec 2: fachada de vidrio hacia la plataforma; rendimiento supuesto de unos 50 m de fachada por semana por frente |

#### 1.2.2 Salas de espera, circulación y áreas de apoyo terminadas

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.2.2-01 | Construir las divisiones, la mampostería liviana y los cielos de los tres niveles | Ejecución | Contratista de obra | 70 | 95 | 125 | 95.8 | Paramétrica | RFI-T sec 2: 18,555 m2; rendimiento supuesto de unos 220 m2/dl con tres cuadrillas |
| 1.2.2-02 | Aplicar los acabados de pisos y paredes de las seis salas de espera, los pasillos, los locales y el salón VIP | Ejecución | Contratista de obra | 80 | 105 | 140 | 106.7 | Paramétrica | RFI-T sec 2: seis salas, área comercial y VIP; rendimiento supuesto de unos 1,000 m2/mes por frente con 4 frentes |
| 1.2.2-03 | Integrar la ampliación con la terminal de la Etapa 1 y habilitar las circulaciones de pasajeros | Ejecución | Contratista de obra | 25 | 45 | 70 | 45.8 | Juicio de expertos | RFI-T sec 1 y 2: integración funcional con la Etapa 1 en operación; ventanas de cierre parcial |

#### 1.2.3 Instalaciones eléctricas, hidráulicas, climatización y contra incendio recibidas

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.2.3-01 | Instalar las redes eléctricas, de agua, de drenaje y los ductos de climatización por nivel | Ejecución | Contratista de obra | 85 | 115 | 150 | 115.8 | Paramétrica | EEO3 sec 3.1 (capítulos eléctrico e hidráulico); 3 niveles a unos 35 dl por nivel con sistemas en paralelo (supuesto) |
| 1.2.3-02 | Instalar la subestación, los tableros, la planta de emergencia y los equipos de climatización | Ejecución | Contratista de obra | 55 | 75 | 110 | 77.5 | Juicio de expertos | Equipos de largo plazo de entrega comprados desde el inicio; 15 semanas de montaje y conexión |
| 1.2.3-03 | Instalar la detección y supresión de incendios, la voz y datos y el control de acceso | Ejecución | Contratista de obra | 50 | 70 | 100 | 71.7 | Juicio de expertos | EEO3 sec 3.1: sistema contra incendios y señales débiles; 14 semanas |
| 1.2.3-04 | Realizar las pruebas, el balanceo y la puesta en marcha de las instalaciones de la terminal | Ejecución | Contratista de obra | 30 | 50 | 80 | 51.7 | Juicio de expertos | Pruebas de aceptación por sistema (eléctrico, climatización, incendio, hidráulico); 8 semanas |

#### 1.2.4 Puentes de abordaje, mobiliario y equipos instalados

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.2.4-01 | Elaborar y aprobar los planos de taller de los seis puentes de abordaje | Ejecución | Contratista de obra | 25 | 40 | 65 | 41.7 | Juicio de expertos | Los puentes se ajustan a la geometría construida; 8 semanas con la supervisión |
| 1.2.4-02 | Fabricar y entregar en sitio los seis puentes de abordaje | Ejecución | Contratista de obra | 100 | 130 | 170 | 131.7 | Análoga | A-PBB: Santiago de Compostela, 4 puentes en 7 meses; Shannon, 1 puente en 9 meses (A-TED) |
| 1.2.4-03 | Instalar y conectar los seis puentes de abordaje a la terminal y a la plataforma | Ejecución | Contratista de obra | 35 | 50 | 75 | 51.7 | Análoga | Unas 2 semanas por puente con dos cuadrillas (supuesto); A-PBB |
| 1.2.4-04 | Instalar el mobiliario, los escáneres de seguridad y los sistemas de información de vuelo | Ejecución | Contratista de obra | 25 | 35 | 55 | 36.7 | Juicio de expertos | RFI-T sec 2 y EEO3 Cuadro 12: FIDS, CUTE, escáneres y mobiliario; 7 semanas |
| 1.2.4-05 | Probar los equipos, capacitar al personal de CEPA y entregar los manuales | Ejecución | Contratista de obra | 20 | 30 | 45 | 30.8 | Juicio de expertos | EDT 1.2.4: equipos probados y entregados con sus manuales; 5 semanas |
| 1.2.4-06 | Realizar las pruebas integradas de operación de la terminal con las aerolíneas y las autoridades | Ejecución | CEPA | 10 | 20 | 35 | 20.8 | Juicio de expertos | Práctica de preparación operacional de terminales (ORAT); 3 semanas |

#### 1.2.5 Accesibilidad universal, movilidad del cuidado y criterios de sostenibilidad incorporados

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.2.5-01 | Verificar en los planos aprobados los recorridos de accesibilidad universal y de movilidad del cuidado | Planificación | Especialista socioambiental | 10 | 15 | 25 | 15.8 | Juicio de expertos | EDT 1.2.5; lista de verificación de 3 semanas sobre los 3 niveles |
| 1.2.5-02 | Verificar en el diseño aprobado las metas EDGE Advanced de energía, agua y carbono incorporado | Planificación | Especialista socioambiental | 10 | 15 | 25 | 15.8 | Juicio de expertos | RFI-T sec 2: ahorro de 40% de energía, 20% de agua y 20% de carbono incorporado; 3 semanas |
| 1.2.5-03 | Verificar en obra la ejecución de los recorridos accesibles y de los espacios de movilidad del cuidado | Ejecución | Especialista socioambiental | 15 | 20 | 30 | 20.8 | Juicio de expertos | Verificación durante los acabados; 4 semanas; verifica la obra del contratista (1.2.5-05) |
| 1.2.5-04 | Verificar en obra las medidas de eficiencia y reunir las evidencias para la auditoría EDGE | Ejecución | Especialista socioambiental | 12 | 18 | 28 | 18.7 | Juicio de expertos | La auditoría EDGE corresponde al paquete 2.6.1; 3 a 4 semanas; verifica la obra del contratista (1.2.5-06) |
| 1.2.5-05 | Instalar el transporte vertical accesible y la señalética de los recorridos accesibles y habilitar los espacios de movilidad del cuidado de la terminal | Ejecución | Contratista de obra | 45 | 60 | 85 | 61.7 | Juicio de expertos | EDT 1.2.5; EEO3 cuadro 2: el capítulo de accesibilidad universal de la terminal es transporte vertical y señalética; RFI-T sec 2: accesibilidad universal y movilidad del cuidado; 12 semanas por juicio de expertos, contrastadas con los 105 dl de los acabados (1.2.2-02) |
| 1.2.5-06 | Instalar y poner en marcha las medidas de eficiencia EDGE de la terminal (iluminación, griferías y accesorios de bajo consumo, aislamiento y control solar) | Ejecución | Contratista de obra | 30 | 45 | 65 | 45.8 | Juicio de expertos | EDT 1.2.5; RFI-T sec 2: EDGE Advanced con ahorro de 40% de energía, 20% de agua y 20% de carbono incorporado; 9 semanas por juicio de expertos, después de las fachadas y con los equipos |

#### 1.3.1 Plataforma de posiciones de contacto construida

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.3.1-01 | Movilizar al contratista de plataformas y Foxtrot e instalar el cerramiento y los accesos del lado aire | Ejecución | Contratista de obra | 20 | 30 | 45 | 30.8 | Juicio de expertos | PP 4.6: protocolo de la AAC antes de obras del lado aire; 6 semanas |
| 1.3.1-02 | Construir la terracería, el drenaje y la base de la fase 1 de la plataforma de contacto | Ejecución | Contratista de obra | 40 | 50 | 70 | 51.7 | Paramétrica | EEO3 Cuadro 11: unos 42,100 m2 de contacto en dos fases de 21,000 m2; base y drenaje en 9 semanas |
| 1.3.1-03 | Colar el pavimento de concreto de la fase 1 de la plataforma de contacto y sellar las juntas | Ejecución | Contratista de obra | 65 | 85 | 115 | 86.7 | Paramétrica | 21,000 m2 a unos 5,300 m2/mes con la plataforma en operación (A-GRR, A-BRU) |
| 1.3.1-04 | Construir la terracería, el drenaje y la base de la fase 2 de la plataforma de contacto | Ejecución | Contratista de obra | 40 | 50 | 70 | 51.7 | Juicio de expertos | Fase 2 solo cuando la fase 1 reabre a las aeronaves; igual que la fase 1 |
| 1.3.1-05 | Colar el pavimento de concreto de la fase 2 de la plataforma de contacto y sellar las juntas | Ejecución | Contratista de obra | 65 | 85 | 115 | 86.7 | Paramétrica | 21,000 m2 a unos 5,300 m2/mes (A-GRR, A-BRU) |
| 1.3.1-06 | Instalar los ductos y los servicios de apoyo a aeronaves de la plataforma de contacto | Ejecución | Contratista de obra | 18 | 25 | 40 | 26.3 | Juicio de expertos | EDT 1.3.1 (pavimento, drenaje y servicios); 5 semanas con apertura de zanjas por fase |

#### 1.3.2 Plataforma de posiciones remotas construida

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.3.2-01 | Demoler el SSEI antiguo y despejar la huella de la plataforma remota | Ejecución | Contratista de obra | 12 | 20 | 35 | 21.2 | Juicio de expertos | PP 4.6 y EEO3 Cuadro 23: el SSEI actual queda afectado por la plataforma remota; 4 semanas |
| 1.3.2-02 | Ejecutar la terracería y la capa de suelo cemento de 30 cm de la plataforma remota | Ejecución | Contratista de obra | 30 | 40 | 60 | 41.7 | Paramétrica | PGAS sec 2.4.4: 28,200 m2 con suelo cemento de 30 cm; rendimiento supuesto de unos 15,000 m2/mes en área aislada |
| 1.3.2-03 | Modificar los canales existentes y construir el drenaje y las obras de paso de la plataforma remota | Ejecución | Contratista de obra | 20 | 30 | 45 | 30.8 | Juicio de expertos | PGAS sec 2.4.4: modificación de canales y obras de paso para equipos de salvamento; 6 semanas |
| 1.3.2-04 | Colar el pavimento de concreto de 34 cm de la plataforma remota y sellar las juntas | Ejecución | Contratista de obra | 40 | 55 | 90 | 58.3 | Paramétrica | PGAS sec 2.4.4: 23,100 m2; unos 11,000 m2/mes sin fases (supuesto, doble de A-GRR); lluvias de mayo a octubre |
| 1.3.2-05 | Construir el pavimento asfáltico de los márgenes y las zonas de apoyo terrestre de la plataforma remota | Ejecución | Contratista de obra | 18 | 25 | 40 | 26.3 | Paramétrica | PGAS sec 2.4.4: 5,100 m2 de asfalto de 8 cm; rendimiento supuesto de unos 5,000 m2/semana más preparación |

#### 1.3.3 Señalización, luces y torres de iluminación de plataforma instaladas

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.3.3-01 | Instalar los ductos, las torres de iluminación y las luces de la plataforma de contacto | Ejecución | Contratista de obra | 28 | 40 | 60 | 41.3 | Juicio de expertos | PGAS sec 2.4.2: señalización, luces y torres de iluminación; 8 semanas por las dos fases |
| 1.3.3-02 | Instalar las luces de borde y las torres de iluminación de la plataforma remota | Ejecución | Contratista de obra | 25 | 35 | 50 | 35.8 | Juicio de expertos | PGAS sec 2.4.4: luces de borde de plataforma; 7 semanas |
| 1.3.3-03 | Pintar la señalización horizontal de las plataformas nuevas | Ejecución | Contratista de obra | 8 | 12 | 20 | 12.7 | Juicio de expertos | Pintura tras el curado del concreto (28 días); 2 a 3 semanas |
| 1.3.3-04 | Probar las luces y la señalización de las plataformas nuevas | Ejecución | Contratista de obra | 6 | 10 | 18 | 10.7 | Juicio de expertos | Pruebas fotométricas y eléctricas; 2 semanas |
| 1.3.3-05 | Autorizar la puesta en servicio de las plataformas nuevas | Ejecución | AAC | 5 | 10 | 25 | 11.7 | Juicio de expertos | Supuesto: inspección de la AAC antes de operar; 2 semanas |

#### 1.4.1 Pavimento y hombros de la calle Foxtrot construidos

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.4.1-01 | Ejecutar la terracería, la base granular y el drenaje de la calle Foxtrot | Ejecución | Contratista de obra | 35 | 50 | 75 | 51.7 | Paramétrica | PGAS sec 2.4.3: 18,400 m2 con terracería completa; rendimiento supuesto de unos 8,000 m2/mes de base y drenaje |
| 1.4.1-02 | Pavimentar con concreto asfáltico la calle Foxtrot y los hombros | Ejecución | Contratista de obra | 22 | 30 | 45 | 31.2 | Paramétrica | PGAS sec 2.4.3: 13,400 m2 de calle y 5,000 m2 de hombros; rendimiento supuesto de unos 12,000 m2/mes |
| 1.4.1-03 | Construir la intersección de Foxtrot con la calle de rodaje Alfa en ventanas de cierre nocturnas | Ejecución | Contratista de obra | 20 | 30 | 50 | 31.7 | Juicio de expertos | EEO3 Cuadro 11: 2,786 m2 de intersección; solo con cierres nocturnos de la calle Alfa |

#### 1.4.2 Señalización y balizamiento de la calle Foxtrot instalados

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.4.2-01 | Instalar los ductos, el cableado y las luces de borde y de los puntos de espera de la calle Foxtrot | Ejecución | Contratista de obra | 22 | 30 | 45 | 31.2 | Juicio de expertos | PGAS sec 2.4.3: balizamiento e iluminación de borde; 6 semanas |
| 1.4.2-02 | Pintar la señalización horizontal de la calle Foxtrot | Ejecución | Contratista de obra | 6 | 10 | 15 | 10.2 | Juicio de expertos | 2 semanas, tras el pavimento asfáltico |
| 1.4.2-03 | Probar el balizamiento y la iluminación de la calle Foxtrot | Ejecución | Contratista de obra | 6 | 10 | 18 | 10.7 | Juicio de expertos | Pruebas fotométricas y eléctricas; 2 semanas |
| 1.4.2-04 | Autorizar la puesta en servicio de la calle Foxtrot | Ejecución | AAC | 5 | 10 | 25 | 11.7 | Juicio de expertos | Supuesto: inspección de la AAC antes de operar; 2 semanas |

#### 1.5.1 Edificio de estacionamiento construido

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.5.1-01 | Movilizar al contratista e instalar los cerramientos y las obras provisionales del sitio del estacionamiento | Ejecución | Contratista de obra | 20 | 30 | 45 | 30.8 | Juicio de expertos | SPN-E: LPI de obra civil; 6 semanas de movilización |
| 1.5.1-02 | Construir la cimentación del edificio de estacionamiento | Ejecución | Contratista de obra | 55 | 70 | 95 | 71.7 | Paramétrica | EEO3 Cuadro 20 y PGAS 2.4.1: huella de unos 21,400 a 22,500 m2 por nivel; rendimiento supuesto de unos 315 m2/dl con tres frentes |
| 1.5.1-03 | Construir la estructura de los niveles 1 y 2 del estacionamiento | Ejecución | Contratista de obra | 100 | 125 | 160 | 126.7 | Paramétrica | EEO3 Cuadro 20: niveles 1 y 2 de 22,506 y 21,994 m2 (unos 44,500 m2); rendimiento supuesto de unos 8,000 m2/mes con tres frentes |
| 1.5.1-04 | Construir la estructura del nivel superior, la cubierta y las rampas del estacionamiento | Ejecución | Contratista de obra | 50 | 65 | 95 | 67.5 | Paramétrica | EEO3 Cuadro 20: nivel superior de 21,994 m2 (66,494 m2 en total); 8,000 m2/mes más rampas y cubierta (unas 3 semanas) |
| 1.5.1-05 | Instalar las redes eléctricas, de iluminación, de drenaje y de protección contra incendios del estacionamiento | Ejecución | Contratista de obra | 80 | 110 | 145 | 110.8 | Juicio de expertos | EEO3 Cuadro 21: incendios y eléctrica son partidas mayores; 4 niveles a unos 25 dl por nivel y sistema (supuesto) |
| 1.5.1-06 | Construir los acabados, los ascensores, las rutas accesibles y la señalización vial del estacionamiento | Ejecución | Contratista de obra | 75 | 105 | 135 | 105.0 | Juicio de expertos | SPN-E: accesibilidad universal para PcD; 17 semanas con solape por nivel |

#### 1.5.2 Sistemas de acceso, tráfico y áreas de alquiler instalados

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.5.2-01 | Instalar el control de acceso, las barreras, el cobro y la guía de plazas del estacionamiento | Ejecución | Contratista de obra | 35 | 50 | 75 | 51.7 | Juicio de expertos | EDT 1.5.2; 10 semanas de instalación para 2,050 plazas |
| 1.5.2-02 | Habilitar las áreas de alquiler de vehículos y la gestión del tráfico interno | Ejecución | Contratista de obra | 25 | 40 | 60 | 40.8 | Juicio de expertos | EDT 1.5.2; 8 semanas |
| 1.5.2-03 | Probar los sistemas de acceso y tráfico y capacitar al personal de operación | Ejecución | Contratista de obra | 12 | 20 | 30 | 20.3 | Juicio de expertos | EDT 1.5.2: sistemas probados; 4 semanas |

#### 1.5.3 Sistema de generación solar instalado

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.5.3-01 | Tramitar la autorización de interconexión del sistema solar con la red de distribución | Ejecución | CEPA | 20 | 35 | 70 | 38.3 | Juicio de expertos | Trámite externo con el regulador y la distribuidora; el marco de autoconsumo cambió en 2026 (A-PVM) |
| 1.5.3-02 | Instalar las estructuras de soporte y los paneles fotovoltaicos en la cubierta del estacionamiento | Ejecución | Contratista de obra | 30 | 45 | 65 | 45.8 | Paramétrica | PGAS sec 2.4.5: 3,166,804 kWh/año, unos 2 MWp; rendimiento supuesto de unos 40 kWp/dl con tres cuadrillas |
| 1.5.3-03 | Instalar los inversores, el cableado, los tableros y los medidores del sistema solar | Ejecución | Contratista de obra | 20 | 30 | 45 | 30.8 | Juicio de expertos | EDT 1.5.3; 6 semanas, solapado con los paneles |
| 1.5.3-04 | Probar y energizar el sistema solar y entregar el estacionamiento con sus manuales | Ejecución | Contratista de obra | 15 | 25 | 40 | 25.8 | Juicio de expertos | EDT 1.5.3: sistema instalado, probado y entregado; 5 semanas |

#### 1.6.1 Edificio del SSEI y vías de acceso construidos

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.6.1-01 | Movilizar al contratista e instalar los cerramientos y los accesos del sitio del SSEI | Ejecución | Contratista de obra | 12 | 20 | 30 | 20.3 | Juicio de expertos | Obra menor (PEP: 200 días calendario); 3 semanas |
| 1.6.1-02 | Construir la cimentación y la estructura del edificio del SSEI | Ejecución | Contratista de obra | 35 | 50 | 70 | 50.8 | Juicio de expertos | PEP: contrato de 200 días calendario (143 dl) para toda la obra; 9 semanas |
| 1.6.1-03 | Construir la cubierta, los cerramientos y las instalaciones del edificio del SSEI | Ejecución | Contratista de obra | 40 | 55 | 75 | 55.8 | Juicio de expertos | PEP: 143 dl de contrato; solapado con la estructura |
| 1.6.1-04 | Construir las vías de acceso y de salida a la plataforma del SSEI | Ejecución | Contratista de obra | 28 | 40 | 55 | 40.5 | Juicio de expertos | EDT 1.6.1; vías cortas pavimentadas con la plataforma en operación (supuesto) |
| 1.6.1-05 | Instalar los acabados, los sistemas de alarma y comunicaciones y probar el edificio del SSEI | Ejecución | Contratista de obra | 28 | 40 | 55 | 40.5 | Juicio de expertos | EDT 1.6.1: requisitos del servicio de salvamento; 7 semanas |

#### 1.6.2 SSEI en funcionamiento en la nueva ubicación

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.6.2-01 | Preparar el plan de traslado y de cobertura del servicio durante el traslado del SSEI | Planificación | CEPA | 12 | 20 | 35 | 21.2 | Juicio de expertos | PP 4.6 y EEO3 Cuadro 23 (traslado); 4 semanas, en paralelo con la obra |
| 1.6.2-02 | Dar la conformidad a la cobertura de protección contra incendios durante el traslado del SSEI | Ejecución | AAC | 5 | 10 | 20 | 10.8 | Juicio de expertos | Trámite de la AAC sobre categoría y tiempos de respuesta; 2 semanas |
| 1.6.2-03 | Trasladar al personal y los vehículos del SSEI al edificio nuevo ya equipado | Ejecución | CEPA | 5 | 8 | 15 | 8.7 | Juicio de expertos | Juicio de expertos: una semana de traslado de personal, vehículos y archivos; el equipamiento pasó a 1.6.2-05 y 1.6.2-06 (contratista) |
| 1.6.2-04 | Realizar las pruebas de tiempo de respuesta y declarar en operación el SSEI nuevo | Ejecución | CEPA | 5 | 10 | 20 | 10.8 | Juicio de expertos | PP 4.6: SSEI reubicado y en total funcionamiento; 2 semanas |
| 1.6.2-05 | Suministrar e instalar el equipamiento del edificio nuevo del SSEI (equipos de rescate y de comunicaciones, mobiliario y talleres) | Ejecución | Contratista de obra | 20 | 30 | 45 | 30.8 | Juicio de expertos | Estimación de costos S1: el 5% del edificio del SSEI corresponde al equipamiento, el traslado y la puesta en marcha (supuesto); 6 semanas de suministro e instalación por juicio de expertos |
| 1.6.2-06 | Probar el equipamiento del SSEI, capacitar al personal en su uso y entregar los manuales | Ejecución | Contratista de obra | 8 | 12 | 20 | 12.7 | Juicio de expertos | EDT 1.6.2: pruebas y puesta en operación del SSEI; 2 a 3 semanas por juicio de expertos |

#### 1.7.1 Supervisión de la terminal y del estacionamiento ejecutada

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.7.1-01 | Movilizar a la firma de supervisión de la terminal | Ejecución | Firma de supervisión | 7 | 10 | 18 | 10.8 | Juicio de expertos | Equipo, oficina y revisión del plan de trabajo antes de la orden de inicio; 2 semanas |
| 1.7.1-02 | Supervisar la construcción de la terminal | Monitoreo y control | Firma de supervisión | NE | NE | NE | NE | Nivel de esfuerzo | PEP: supervisión de 1,170 días calendario para los procesos 1 y 3 |
| 1.7.1-03 | Movilizar a la firma de supervisión del estacionamiento | Ejecución | Firma de supervisión | 7 | 10 | 18 | 10.8 | Juicio de expertos | Equipo, oficina y revisión del plan de trabajo; 2 semanas |
| 1.7.1-04 | Supervisar la construcción del estacionamiento y del sistema solar | Monitoreo y control | Firma de supervisión | NE | NE | NE | NE | Nivel de esfuerzo | PA 2026-2: contrato de supervisión del estacionamiento (P00002) |
| 1.7.1-05 | Presentar el informe final de supervisión de la terminal | Cierre | Firma de supervisión | 10 | 15 | 25 | 15.8 | Juicio de expertos | Informe final y saldo de supervisión; 3 semanas |
| 1.7.1-06 | Presentar el informe final de supervisión del estacionamiento | Cierre | Firma de supervisión | 10 | 15 | 25 | 15.8 | Juicio de expertos | Informe final y saldo de supervisión; 3 semanas |

#### 1.7.2 Supervisión de plataformas, calle Foxtrot y SSEI ejecutada

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.7.2-01 | Movilizar a la firma de supervisión de plataformas y calle Foxtrot | Ejecución | Firma de supervisión | 7 | 10 | 18 | 10.8 | Juicio de expertos | Equipo, oficina y revisión del plan de fases; 2 semanas |
| 1.7.2-02 | Supervisar la construcción de plataformas y de la calle Foxtrot | Monitoreo y control | Firma de supervisión | NE | NE | NE | NE | Nivel de esfuerzo | PEP: supervisión de 650 días calendario (proceso 2) |
| 1.7.2-03 | Movilizar a la firma de supervisión del SSEI | Ejecución | Firma de supervisión | 5 | 8 | 15 | 8.7 | Juicio de expertos | Obra menor; 2 semanas |
| 1.7.2-04 | Supervisar la construcción del edificio del SSEI | Monitoreo y control | Firma de supervisión | NE | NE | NE | NE | Nivel de esfuerzo | PEP: supervisión de 330 días calendario (proceso 4) |
| 1.7.2-05 | Presentar el informe final de supervisión de plataformas y calle Foxtrot | Cierre | Firma de supervisión | 10 | 15 | 25 | 15.8 | Juicio de expertos | Informe final y saldo de supervisión; 3 semanas |
| 1.7.2-06 | Presentar el informe final de supervisión del SSEI | Cierre | Firma de supervisión | 8 | 12 | 20 | 12.7 | Juicio de expertos | Informe final y saldo de supervisión; 2 a 3 semanas |

#### 1.7.3 PGAS de construcción implementado

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.7.3-01 | Revisar y aprobar el PGAS de construcción del contratista del estacionamiento | Monitoreo y control | Especialista socioambiental | 8 | 12 | 20 | 12.7 | Juicio de expertos | PGAS (informe trimestral del contratista y plan de construcción); 2 a 3 semanas |
| 1.7.3-02 | Revisar y aprobar el PGAS de construcción del contratista de la terminal | Monitoreo y control | Especialista socioambiental | 10 | 15 | 25 | 15.8 | Juicio de expertos | Obra mayor con el aeropuerto en operación; 3 semanas |
| 1.7.3-03 | Revisar y aprobar el PGAS de construcción del contratista del SSEI | Monitoreo y control | Especialista socioambiental | 5 | 8 | 15 | 8.7 | Juicio de expertos | Obra menor; 1 a 2 semanas |
| 1.7.3-04 | Revisar y aprobar el PGAS de construcción del contratista de plataformas y Foxtrot | Monitoreo y control | Especialista socioambiental | 8 | 12 | 20 | 12.7 | Juicio de expertos | Obra del lado aire; 2 a 3 semanas |
| 1.7.3-05 | Dar seguimiento al cumplimiento del PGAS durante las obras | Monitoreo y control | Especialista socioambiental | NE | NE | NE | NE | Nivel de esfuerzo | PGAS: informe trimestral del contratista; seguimiento hasta las recepciones provisionales |
| 1.7.3-06 | Verificar el cierre de las instalaciones temporales y la restauración de los sitios de obra | Cierre | Especialista socioambiental | 10 | 15 | 25 | 15.8 | Juicio de expertos | EDT 1.7.3: cierre de instalaciones temporales; 3 semanas |

#### 1.7.4 Planos de obra ejecutada y actas de recepción aprobados

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1.7.4-01 | Realizar la recepción provisional de la terminal y levantar la lista de pendientes | Cierre | Coordinador general de obra | 12 | 20 | 35 | 21.2 | Juicio de expertos | Inspección conjunta por sistema y nivel; 4 semanas |
| 1.7.4-02 | Realizar la recepción provisional del estacionamiento y del sistema solar y levantar la lista de pendientes | Cierre | Coordinador general de obra | 8 | 12 | 22 | 13.0 | Juicio de expertos | Inspección de un edificio de estructura repetitiva; 2 a 3 semanas |
| 1.7.4-03 | Realizar la recepción provisional de las plataformas y de la calle Foxtrot y levantar la lista de pendientes | Cierre | Coordinador general de obra | 8 | 12 | 22 | 13.0 | Juicio de expertos | Inspección de pavimentos y ayudas visuales; 2 a 3 semanas |
| 1.7.4-04 | Realizar la recepción provisional del edificio del SSEI y levantar la lista de pendientes | Cierre | Coordinador general de obra | 5 | 8 | 15 | 8.7 | Juicio de expertos | Obra menor; 1 a 2 semanas |
| 1.7.4-05 | Verificar la subsanación de pendientes, recibir los planos de obra ejecutada y firmar el acta de recepción definitiva de la terminal | Cierre | Coordinador general de obra | 40 | 55 | 85 | 57.5 | Juicio de expertos | Planos y modelo BIM como construido (RFI-T sec 2); unas 8 semanas de subsanación y 3 de actas, por contrato |
| 1.7.4-06 | Verificar la subsanación de pendientes, recibir los planos de obra ejecutada y firmar el acta de recepción definitiva del estacionamiento y el sistema solar | Cierre | Coordinador general de obra | 30 | 40 | 60 | 41.7 | Juicio de expertos | Planos y modelo BIM como construido (RFI-T sec 2); unas 8 semanas de subsanación y 3 de actas, por contrato |
| 1.7.4-07 | Verificar la subsanación de pendientes, recibir los planos de obra ejecutada y firmar el acta de recepción definitiva de las plataformas y la calle Foxtrot | Cierre | Coordinador general de obra | 30 | 40 | 60 | 41.7 | Juicio de expertos | Planos y modelo BIM como construido (RFI-T sec 2); unas 8 semanas de subsanación y 3 de actas, por contrato |
| 1.7.4-08 | Verificar la subsanación de pendientes, recibir los planos de obra ejecutada y firmar el acta de recepción definitiva del edificio del SSEI | Cierre | Coordinador general de obra | 20 | 30 | 45 | 30.8 | Juicio de expertos | Planos y modelo BIM como construido (RFI-T sec 2); unas 8 semanas de subsanación y 3 de actas, por contrato |

### Componente II. Fortalecimiento institucional

#### 2.1 Plan estratégico del sistema aeronáutico aprobado

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 2.1-01 | Elaborar el plan de trabajo y el informe inicial del plan estratégico | Planificación | Firma consultora | 8 | 10 | 15 | 10.5 | Juicio de expertos | TDR-ANA; PEP-C2 (plazo 180 d cal = 129 dl para todo el contrato) |
| 2.1-02 | Elaborar el diagnóstico del sistema aeronáutico, su marco normativo y su infraestructura | Ejecución | Firma consultora | 25 | 35 | 50 | 35.8 | Juicio de expertos | PEP-C2; ToC (P2.1); diagnóstico documental y entrevistas con actores del sector, sin trabajo de campo extenso |
| 2.1-03 | Formular la visión, los lineamientos y el plan de acción y redactar el borrador del plan estratégico | Ejecución | Firma consultora | 30 | 40 | 55 | 40.8 | Juicio de expertos | PEP-C2; EDT 5.2 (infraestructura, operación, normativa y sostenibilidad) |
| 2.1-04 | Revisar el borrador del plan estratégico y consolidar las observaciones de CEPA y del BID | Monitoreo y control | Especialista de planificación y monitoreo | 10 | 12 | 20 | 13.0 | Juicio de expertos | ROP (la UEP aprueba productos y entregables); la copia al BID es supuesto S-II.4 |
| 2.1-05 | Incorporar las observaciones y entregar la versión final del plan estratégico | Ejecución | Firma consultora | 8 | 10 | 15 | 10.5 | Juicio de expertos | TDR-ANA |
| 2.1-06 | Aprobar el plan estratégico final y remitirlo al BID | Cierre | CEPA | 5 | 7 | 12 | 7.5 | Juicio de expertos | EDT 5.2 criterio de aceptación de 2.1; MEL (P2.1: producto aprobado como anexo del informe semestral) |

#### 2.2.1 Plan Maestro Aeroportuario actualizado y aprobado

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 2.2.1-01 | Elaborar el plan de trabajo y el informe inicial del Plan Maestro | Planificación | Firma consultora | 10 | 15 | 20 | 15.0 | Análoga | FAA-AC (alcance y programa del estudio); PEP-C2 |
| 2.2.1-02 | Elaborar el inventario, el diagnóstico de instalaciones y el pronóstico de demanda | Ejecución | Firma consultora | 60 | 75 | 100 | 76.7 | Análoga | FAA-AC (inventario, pronósticos, requerimientos); ICAO-LB (la actualización de un plan maestro tomó cerca de un año); PEP-C2 (730 d cal incluye la capacitación 2.2.2) |
| 2.2.1-03 | Determinar los requerimientos, evaluar alternativas y redactar el borrador del Plan Maestro con su plan de implementación y financiero | Ejecución | Firma consultora | 85 | 110 | 130 | 109.2 | Análoga | FAA-AC (alternativas, plan de desarrollo, implementación y financiero); ICAO-LB |
| 2.2.1-04 | Revisar el borrador del Plan Maestro y consolidar las observaciones de CEPA, la AAC y el BID | Monitoreo y control | Especialista de planificación y monitoreo | 20 | 25 | 40 | 26.7 | Juicio de expertos | ROP; documento voluminoso con varias áreas de CEPA; revisión de la AAC es supuesto S-II.5 |
| 2.2.1-05 | Incorporar las observaciones y las recomendaciones del estudio de conectividad y entregar la versión final del Plan Maestro | Ejecución | Firma consultora | 15 | 20 | 30 | 20.8 | Juicio de expertos | TDR-ANA; ToC (2.4 aporta recomendaciones al Plan Maestro) |
| 2.2.1-06 | Aprobar el Plan Maestro actualizado y entregarlo al BID | Cierre | CEPA | 5 | 10 | 20 | 10.8 | Juicio de expertos | EDT 5.2 criterio de aceptación de 2.2.1; MEL (P2.2) |

#### 2.2.2 Funcionarios capacitados en planificación, gestión y operación

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 2.2.2-01 | Preparar el programa, los materiales y la lista de participantes de la capacitación en planificación, gestión y operación | Planificación | Firma consultora | 15 | 20 | 30 | 20.8 | Juicio de expertos | MEL (R2.1: áreas de ingeniería, planificación, proyectos estratégicos y gerencia aeroportuaria); PEP-C2 |
| 2.2.2-02 | Impartir los cursos de planificación, gestión y operación aeroportuaria al menos a 21 funcionarios | Ejecución | Firma consultora | 30 | 40 | 60 | 41.7 | Paramétrica | MEL (R2.1 meta 21 funcionarios, énfasis en el Plan Maestro); estimación de 8 a 10 módulos de 4 sesiones (supuesto S-II.6) |
| 2.2.2-03 | Aplicar las evaluaciones y los talleres de cierre a los participantes | Monitoreo y control | Firma consultora | 5 | 7 | 10 | 7.2 | Juicio de expertos | MEL (R2.1: asistencia mínima y puntaje en exámenes o talleres) |
| 2.2.2-04 | Certificar a los funcionarios aprobados y registrar el indicador R2.1 | Cierre | Especialista de planificación y monitoreo | 5 | 7 | 10 | 7.2 | Juicio de expertos | MEL (R2.1, informe semestral) |

#### 2.3.1 Estrategia BIM aprobada

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 2.3.1-01 | Elaborar el plan de trabajo y el informe inicial de la estrategia BIM | Planificación | Firma consultora | 8 | 10 | 15 | 10.5 | Juicio de expertos | TDR-ANA; PEP-C2 (760 d cal = 543 dl para estrategia y capacitación) |
| 2.3.1-02 | Diagnosticar la madurez BIM de CEPA, sus procesos de diseño y sus herramientas | Ejecución | Firma consultora | 15 | 20 | 30 | 20.8 | Juicio de expertos | PEP-C2; ToC (P2.3) |
| 2.3.1-03 | Formular la estrategia BIM (usos, roles, entorno común de datos y requisitos de información) y redactar el borrador | Ejecución | Firma consultora | 20 | 30 | 40 | 30.0 | Juicio de expertos | EDT 5.2 (arreglo de datos y roles definidos) |
| 2.3.1-04 | Revisar el borrador de la estrategia BIM y consolidar las observaciones de CEPA | Monitoreo y control | Especialista en ingeniería aeroportuaria | 8 | 10 | 15 | 10.5 | Juicio de expertos | ROP |
| 2.3.1-05 | Incorporar las observaciones y entregar la versión final de la estrategia BIM | Ejecución | Firma consultora | 6 | 8 | 12 | 8.3 | Juicio de expertos | TDR-ANA |
| 2.3.1-06 | Aprobar la estrategia BIM final | Cierre | CEPA | 5 | 7 | 10 | 7.2 | Juicio de expertos | EDT 5.2 criterio de aceptación de 2.3.1 |

#### 2.3.2 Personal de ingeniería capacitado en BIM

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 2.3.2-01 | Preparar el programa y los materiales de la capacitación en BIM | Planificación | Firma consultora | 10 | 15 | 20 | 15.0 | Juicio de expertos | PEP-C2; EDT 5.2 (2.3.2) |
| 2.3.2-02 | Impartir los cursos de BIM al personal de ingeniería de CEPA | Ejecución | Firma consultora | 25 | 35 | 50 | 35.8 | Paramétrica | Curso de unas 100 a 120 horas (supuesto S-II.6), a razón de 3 a 4 horas diarias en jornada compartida con el trabajo |
| 2.3.2-03 | Evaluar a los participantes en BIM | Monitoreo y control | Firma consultora | 5 | 7 | 10 | 7.2 | Juicio de expertos | EDT 5.2 (2.3.2) |
| 2.3.2-04 | Entregar los materiales y el registro de la capacitación en BIM | Cierre | Especialista en ingeniería aeroportuaria | 5 | 7 | 10 | 7.2 | Juicio de expertos | EDT 5.2 criterio de aceptación de 2.3.2 |

#### 2.4 Estudio de conectividad terrestre entregado

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 2.4-01 | Elaborar el plan de trabajo y el informe inicial del estudio de conectividad terrestre | Planificación | Firma consultora | 8 | 10 | 15 | 10.5 | Juicio de expertos | TDR-ANA; PEP-C2 |
| 2.4-02 | Diagnosticar el acceso terrestre al AIES con aforos, encuestas y análisis de los modos de transporte | Ejecución | Firma consultora | 30 | 40 | 55 | 40.8 | Juicio de expertos | TDR-ANA (estudios de tráfico y movilidad con conteos y encuestas); EDT 5.2 |
| 2.4-03 | Evaluar alternativas de acceso hacia San Salvador y los destinos turísticos y redactar el borrador del estudio | Ejecución | Firma consultora | 35 | 45 | 60 | 45.8 | Juicio de expertos | EDT 5.2 (criterios de sostenibilidad e inclusión); PEP-C2 |
| 2.4-04 | Revisar el borrador del estudio de conectividad y consolidar las observaciones de CEPA | Monitoreo y control | Especialista de planificación y monitoreo | 10 | 12 | 20 | 13.0 | Juicio de expertos | ROP |
| 2.4-05 | Incorporar las observaciones y entregar el informe final del estudio de conectividad | Ejecución | Firma consultora | 8 | 10 | 15 | 10.5 | Juicio de expertos | TDR-ANA |
| 2.4-06 | Aprobar el informe final del estudio de conectividad | Cierre | CEPA | 5 | 7 | 12 | 7.5 | Juicio de expertos | EDT 5.2 criterio de aceptación de 2.4 |

#### 2.5 Estudio de diversificación de destinos entregado

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 2.5-01 | Elaborar el plan de trabajo y el informe inicial del estudio de diversificación de destinos | Planificación | Firma consultora | 8 | 10 | 15 | 10.5 | Juicio de expertos | TDR-ANA; PEP-C2 |
| 2.5-02 | Diagnosticar el mercado actual del AIES (tráfico, aerolíneas, rutas y zona de influencia) | Ejecución | Firma consultora | 25 | 35 | 45 | 35.0 | Juicio de expertos | TDR-ANA (estudios de mercado aéreo); EDT 5.2 |
| 2.5-03 | Analizar los mercados de origen y destino y las aerolíneas potenciales, priorizarlos y redactar el borrador del estudio | Ejecución | Firma consultora | 35 | 45 | 60 | 45.8 | Juicio de expertos | EDT 5.2 (mercados y destinos priorizados, sin apertura de rutas); PEP-C2 |
| 2.5-04 | Revisar el borrador del estudio de diversificación y consolidar las observaciones de CEPA | Monitoreo y control | Especialista de planificación y monitoreo | 10 | 12 | 20 | 13.0 | Juicio de expertos | ROP |
| 2.5-05 | Incorporar las observaciones y entregar el informe final del estudio de diversificación | Ejecución | Firma consultora | 8 | 10 | 15 | 10.5 | Juicio de expertos | TDR-ANA |
| 2.5-06 | Aprobar el informe final del estudio de diversificación | Cierre | CEPA | 5 | 7 | 12 | 7.5 | Juicio de expertos | EDT 5.2 criterio de aceptación de 2.5 |

#### 2.6.1 Auditoría para la certificación EDGE realizada

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 2.6.1-01 | Registrar los proyectos de terminal y estacionamiento en EDGE y elaborar la autoevaluación | Planificación | Firma consultora | 15 | 20 | 30 | 20.8 | Juicio de expertos | EDGE-P secciones 4 y 5 (autoevaluación en la aplicación EDGE y registro con el proveedor de certificación) |
| 2.6.1-02 | Realizar la auditoría de diseño y obtener el certificado preliminar EDGE | Ejecución | Firma consultora | 25 | 35 | 50 | 35.8 | Análoga | EDGE-P 6.2 (auditoría de diseño sin visita, al menos una resubmisión); GBCSA (revisión de 4 semanas en la ronda 1 y 3 en la ronda 2, unos 35 dl) |
| 2.6.1-03 | Acompañar a CEPA y a los contratistas para conservar las medidas EDGE durante la construcción | Monitoreo y control | Firma consultora | NE | NE | NE | NE | Nivel de esfuerzo | EDT 5.2 (auditoría y acompañamiento); EDGE-P 6.3 inciso c (cambios de diseño exigen autoevaluación actualizada) |
| 2.6.1-04 | Realizar la auditoría en sitio de las medidas EDGE de la terminal y del estacionamiento terminados | Ejecución | Firma consultora | 20 | 25 | 35 | 25.8 | Análoga | EDGE-P 6.3 (verificación de las medidas instaladas, un nuevo intento si hay incumplimientos); dos edificios en un mismo sitio |
| 2.6.1-05 | Atender las observaciones del proveedor de certificación y presentar el informe de auditoría | Ejecución | Firma consultora | 20 | 25 | 35 | 25.8 | Análoga | GBCSA (ronda 1 de 4 semanas y ronda 2 de 3 semanas, unos 35 dl); EDGE-P 6.3 (control de calidad independiente) |
| 2.6.1-06 | Recibir el certificado EDGE final y el informe de auditoría | Cierre | CEPA | 5 | 5 | 10 | 5.8 | Juicio de expertos | EDT 5.2 criterio de aceptación de 2.6.1; EDGE-P 6.3 |

#### 2.6.2 Personal capacitado en certificación EDGE

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 2.6.2-01 | Preparar el programa y los materiales de la capacitación en EDGE | Planificación | Firma consultora | 8 | 10 | 15 | 10.5 | Juicio de expertos | EDT 5.2 (2.6.2); PEP-C2 |
| 2.6.2-02 | Impartir el curso de EDGE al personal previsto | Ejecución | Firma consultora | 10 | 15 | 25 | 15.8 | Paramétrica | Curso de 2 a 3 semanas (supuesto S-II.6) |
| 2.6.2-03 | Evaluar y certificar a los participantes en EDGE | Monitoreo y control | Firma consultora | 5 | 7 | 10 | 7.2 | Juicio de expertos | EDT 5.2 (2.6.2) |
| 2.6.2-04 | Entregar el registro de la capacitación en EDGE | Cierre | Especialista en ingeniería aeroportuaria | 5 | 5 | 8 | 5.5 | Juicio de expertos | EDT 5.2 criterio de aceptación de 2.6.2 |

#### 2.7 Estudio de separación de flujos entregado

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 2.7-01 | Elaborar el plan de trabajo y el informe inicial del estudio de separación de flujos | Planificación | Firma consultora | 8 | 10 | 15 | 10.5 | Juicio de expertos | TDR-ANA; PEP-C2 (200 d cal = 143 dl) |
| 2.7-02 | Diagnosticar los flujos de llegadas y salidas de la terminal antigua mediante levantamiento y observación | Ejecución | Firma consultora | 15 | 20 | 30 | 20.8 | Juicio de expertos | PEP-C2; EDT 5.2 (2.7) |
| 2.7-03 | Identificar y priorizar las intervenciones de separación de flujos y redactar el borrador del estudio | Ejecución | Firma consultora | 20 | 30 | 40 | 30.0 | Juicio de expertos | EDT 5.2 (intervenciones identificadas y priorizadas, sin ejecutarlas) |
| 2.7-04 | Revisar el borrador del estudio de separación de flujos y consolidar las observaciones de CEPA | Monitoreo y control | Especialista en ingeniería aeroportuaria | 8 | 10 | 15 | 10.5 | Juicio de expertos | ROP |
| 2.7-05 | Incorporar las observaciones y entregar el informe final del estudio de separación de flujos | Ejecución | Firma consultora | 5 | 8 | 12 | 8.2 | Juicio de expertos | TDR-ANA |
| 2.7-06 | Aprobar el informe final del estudio de separación de flujos | Cierre | CEPA | 5 | 7 | 10 | 7.2 | Juicio de expertos | EDT 5.2 criterio de aceptación de 2.7 |

#### 2.8 Estudio de movilidad interna entregado

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 2.8-01 | Elaborar el plan de trabajo y el informe inicial del estudio de movilidad interna | Planificación | Firma consultora | 8 | 10 | 15 | 10.5 | Juicio de expertos | TDR-ANA; PEP-C2 (180 d cal = 129 dl) |
| 2.8-02 | Diagnosticar el tráfico de las vías internas con aforos en horas pico y en el dejar y recoger pasajeros | Ejecución | Firma consultora | 20 | 30 | 40 | 30.0 | Juicio de expertos | TDR-ANA (aforos vehiculares y análisis de capacidad vial); EDT 5.2 (2.8) |
| 2.8-03 | Analizar los puntos de conflicto, definir las medidas y redactar el borrador del estudio | Ejecución | Firma consultora | 25 | 35 | 50 | 35.8 | Juicio de expertos | EDT 5.2 (acceso al nuevo estacionamiento) |
| 2.8-04 | Revisar el borrador del estudio de movilidad interna y consolidar las observaciones de CEPA | Monitoreo y control | Especialista en ingeniería aeroportuaria | 8 | 10 | 15 | 10.5 | Juicio de expertos | ROP |
| 2.8-05 | Incorporar las observaciones y entregar el informe final del estudio de movilidad interna | Ejecución | Firma consultora | 5 | 8 | 12 | 8.2 | Juicio de expertos | TDR-ANA |
| 2.8-06 | Aprobar el informe final del estudio de movilidad interna | Cierre | CEPA | 5 | 7 | 10 | 7.2 | Juicio de expertos | EDT 5.2 criterio de aceptación de 2.8 |

#### 2.9 Programa de igualdad e inclusión ejecutado

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 2.9-01 | Elaborar el diagnóstico de necesidades, el programa y los materiales de capacitación en igualdad e inclusión | Planificación | Firma consultora | 20 | 30 | 40 | 30.0 | Juicio de expertos | EDT 5.2 (2.9: igualdad, prevención de violencia y acoso, discapacidad y comunicación no sexista); MEL (T2) |
| 2.9-02 | Impartir la capacitación a la primera cohorte de 100 funcionarios y evaluarla | Ejecución | Firma consultora | 25 | 35 | 45 | 35.0 | Juicio de expertos | MEL tabla de metas anuales (T2: 100 funcionarios por año, 300 en total); duración del curso supuesto S-II.7 |
| 2.9-03 | Impartir la capacitación a la segunda cohorte de 100 funcionarios y evaluarla | Ejecución | Firma consultora | 25 | 35 | 45 | 35.0 | Juicio de expertos | MEL tabla de metas anuales (T2) |
| 2.9-04 | Impartir la capacitación a la tercera cohorte de 100 funcionarios y evaluarla | Ejecución | Firma consultora | 25 | 35 | 45 | 35.0 | Juicio de expertos | MEL tabla de metas anuales (T2) |
| 2.9-05 | Emitir las constancias de los 300 funcionarios aprobados y entregar el informe final del programa | Cierre | Firma consultora | 8 | 10 | 15 | 10.5 | Juicio de expertos | MEL (T2: culminar el curso y rendir evaluación satisfactoria) |
| 2.9-06 | Aprobar el informe final y registrar el indicador T2 en el informe semestral | Cierre | Especialista socioambiental | 5 | 7 | 10 | 7.2 | Juicio de expertos | EDT 5.2 criterio de aceptación de 2.9; MEL (P2.9, T2) |

### Administración, evaluación y auditorías

#### 3.1.1 Unidad ejecutora conformada y en funciones

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.1.1-01 | Incorporar al Coordinador del Programa, al Coordinador general de obra y al Especialista de planificación y monitoreo | Inicio | CEPA | 4 | 5 | 6 | 5.0 | Dato del programa | PA 2026-2 filas P00004, P00005, P00007 (inicio de contrato 16-abr-2026) |
| 3.1.1-02 | Incorporar al Especialista de adquisiciones | Inicio | CEPA | 4 | 5 | 6 | 5.0 | Dato del programa | PA 2026-2 fila P00008 (inicio de contrato 23-abr-2026) |
| 3.1.1-03 | Incorporar al Especialista en ingeniería aeroportuaria, al Especialista financiero y al Especialista socioambiental | Inicio | CEPA | 4 | 5 | 6 | 5.0 | Dato del programa | PA 2026-2 filas P00006, P00009, P00010 (inicio de contrato 4-may-2026) |
| 3.1.1-04 | Registrar las firmas autorizadas del programa ante el BID | Inicio | Especialista financiero | 4 | 5 | 6 | 5.0 | Juicio de expertos | Contrato 6073/OC-ES, cláusula 3.01(a). Trámite documental de una semana |
| 3.1.1-05 | Documentar ante el BID la conformación de la UEP con dedicación exclusiva | Inicio | Coordinador del Programa | 4 | 5 | 6 | 5.0 | Juicio de expertos | Contrato 6073/OC-ES, cláusula 3.01(b). Expediente con contratos y TdR de los siete puestos |
| 3.1.1-06 | Administrar el programa desde la Unidad Ejecutora | Monitoreo y control | Coordinador del Programa | NE | NE | NE | NE | Nivel de esfuerzo | Contratos de los siete consultores clave (PA 2026-2, P00004 a P00010; inicio de contrato 16-abr a 4-may-2026), anuales y renovables hasta el cierre; la UEP trabaja durante todo el programa |

#### 3.1.2 Reglamento operativo vigente

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.1.2-01 | Ajustar el borrador del ROP acordado con el BID a la estructura de la UEP y a las cifras del PA | Inicio | Coordinador del Programa | 12 | 15 | 18 | 15.0 | Juicio de expertos | Contrato cláusula 3.01(c) (ROP en términos previamente acordados); EEO1 ROP es el borrador de preparación |
| 3.1.2-02 | Obtener la no objeción del BID al ROP ajustado | Inicio | BID | 5 | 10 | 15 | 10.0 | Juicio de expertos | Contrato cláusula 4.05 (consentimiento del BID a cambios del ROP); ROP anexo 7.1 usa 5 días por revisión, documento extenso |
| 3.1.2-03 | Aprobar el ROP en CEPA mediante resolución de la autoridad superior | Inicio | CEPA | 4 | 5 | 6 | 5.0 | Juicio de expertos | EDT 3.1.2 (ROP con no objeción del BID y aprobación de CEPA) |

#### 3.1.3 Convenio de transferencia de recursos vigente

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.1.3-01 | Redactar el convenio de transferencia de recursos entre la República y CEPA | Inicio | Coordinador del Programa | 16 | 20 | 24 | 20.0 | Juicio de expertos | Contrato cláusula 3.01(d); convenio de obligaciones de ejecución, cuatro semanas |
| 3.1.3-02 | Obtener la no objeción del BID al texto del convenio | Inicio | BID | 3 | 5 | 7 | 5.0 | Dato del programa | Contrato cláusula 3.01(d) (términos acordados con el Banco); ROP anexo 7.1 (5 días por revisión) |
| 3.1.3-03 | Suscribir el convenio y ponerlo en vigencia | Inicio | CEPA | 8 | 10 | 12 | 10.0 | Juicio de expertos | Firma de dos partes (Hacienda y CEPA) y formalización; dos semanas |

#### 3.1.4 Cuenta especial aperturada

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.1.4-01 | Solicitar a la Dirección General de Tesorería la apertura de la cuenta especial en el BCR | Inicio | Especialista financiero | 8 | 10 | 12 | 10.0 | Juicio de expertos | EDT 3.1.4 (cuenta en el BCR gestionada con la DGT); trámite bancario de dos semanas |
| 3.1.4-02 | Abrir y habilitar la cuenta especial para recibir desembolsos | Inicio | CEPA | 8 | 10 | 12 | 10.0 | Juicio de expertos | EDT 3.1.4 criterio de aceptación; dos semanas |
| 3.1.4-03 | Registrar la cuenta especial ante el BID | Inicio | Especialista financiero | 4 | 5 | 6 | 5.0 | Juicio de expertos | Contrato cláusula 3.01(a) y Normas Generales art. 4.07 (Anticipo de Fondos) |

#### 3.2.1 Plan de ejecución plurianual aprobado

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.2.1-01 | Actualizar la EDT, el cronograma y el presupuesto del PEP de noviembre de 2025 con las fechas reales del préstamo | Planificación | Especialista de planificación y monitoreo | 16 | 20 | 24 | 20.0 | Juicio de expertos | PEP nov-2025 (eer3.txt) como base; contrato cláusula 5.01(a)(ii). Actualización de un plan existente |
| 3.2.1-02 | Integrar al PEP el calendario de adquisiciones, hitos y desembolsos por componente | Planificación | Especialista de planificación y monitoreo | 8 | 10 | 12 | 10.0 | Juicio de expertos | Contrato cláusula 5.01(a)(i)-(ii) (el POA y el PEP incluyen plan de adquisiciones y proyecciones de desembolso) |
| 3.2.1-03 | Aprobar el PEP en CEPA y presentarlo al BID | Planificación | Coordinador del Programa | 4 | 5 | 6 | 5.0 | Juicio de expertos | EDT 3.2.1 criterio de aceptación (aprobado por CEPA y presentado al BID) |

#### 3.2.2 Planes operativos anuales aprobados

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.2.2-01 | Elaborar el POA 2027 con metas, cronograma físico y financiero y presupuesto por producto | Planificación | Especialista de planificación y monitoreo | 16 | 20 | 24 | 20.0 | Juicio de expertos | Contrato cláusula 5.01(a)(i) (contenido del POA); cuatro semanas |
| 3.2.2-02 | Aprobar el POA 2027 en CEPA y presentarlo al BID antes del inicio del año | Planificación | Coordinador del Programa | 4 | 5 | 6 | 5.0 | Juicio de expertos | EDT 3.2.2 (POA aprobado antes del periodo que cubre) |
| 3.2.2-03 | Elaborar el POA 2028 con metas, cronograma físico y financiero y presupuesto por producto | Planificación | Especialista de planificación y monitoreo | 16 | 20 | 24 | 20.0 | Juicio de expertos | Contrato cláusula 5.01(a)(i) (contenido del POA); cuatro semanas |
| 3.2.2-04 | Aprobar el POA 2028 en CEPA y presentarlo al BID antes del inicio del año | Planificación | Coordinador del Programa | 4 | 5 | 6 | 5.0 | Juicio de expertos | EDT 3.2.2 (POA aprobado antes del periodo que cubre) |
| 3.2.2-05 | Elaborar el POA 2029 con metas, cronograma físico y financiero y presupuesto por producto | Planificación | Especialista de planificación y monitoreo | 16 | 20 | 24 | 20.0 | Juicio de expertos | Contrato cláusula 5.01(a)(i) (contenido del POA); cuatro semanas |
| 3.2.2-06 | Aprobar el POA 2029 en CEPA y presentarlo al BID antes del inicio del año | Planificación | Coordinador del Programa | 4 | 5 | 6 | 5.0 | Juicio de expertos | EDT 3.2.2 (POA aprobado antes del periodo que cubre) |
| 3.2.2-07 | Elaborar el POA 2030 con metas, cronograma físico y financiero y presupuesto por producto | Planificación | Especialista de planificación y monitoreo | 16 | 20 | 24 | 20.0 | Juicio de expertos | Contrato cláusula 5.01(a)(i) (contenido del POA); cuatro semanas |
| 3.2.2-08 | Aprobar el POA 2030 en CEPA y presentarlo al BID antes del inicio del año | Planificación | Coordinador del Programa | 4 | 5 | 6 | 5.0 | Juicio de expertos | EDT 3.2.2 (POA aprobado antes del periodo que cubre) |

#### 3.2.3 Plan de adquisiciones aprobado

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.2.3-01 | Elaborar el Plan de Adquisiciones inicial 2026-1 con estacionamiento, su supervisión, la UEP y la auditoría del año 1 | Planificación | CEPA | 20 | 30 | 40 | 30.0 | Juicio de expertos | PA 2026-1 (cobertura desde 14-abr-2026). Plan base heredado de la preparación, 6 semanas |
| 3.2.3-02 | Obtener la no objeción del BID al Plan de Adquisiciones 2026-1 | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 (BID emite no objeción en 5 días); PA 2026-1 cobertura 14-abr-2026 |
| 3.2.3-03 | Actualizar el Plan de Adquisiciones a la versión 2026-2 con terminal, SSEI, plataformas y las tres supervisiones restantes | Planificación | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | Diferencia entre PA 2026-1 y 2026-2 (cuatro obras y tres supervisiones nuevas), 4 semanas |
| 3.2.3-04 | Obtener la no objeción del BID al Plan de Adquisiciones 2026-2 | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | PA 2026-2, cobertura desde 14-jul-2026; ROP anexo 7.1 |
| 3.2.3-05 | Mantener el Plan de Adquisiciones actualizado en el sistema del BID cada vez que cambie un proceso | Monitoreo y control | Especialista de adquisiciones | NE | NE | NE | NE | Nivel de esfuerzo | Contrato 6073/OC-ES, cláusula 4.04 y EDT 3.2.3 |
| 3.2.3-06 | Publicar el Aviso General de Adquisiciones del programa en el portal del BID | Ejecución | Especialista de adquisiciones | 4 | 5 | 6 | 5.0 | Dato del programa | SPN-E y SPN-T, numeral 1: Aviso General de Adquisiciones publicado el 5-may-2026; una semana de preparación y publicación |

#### 3.3.1 Sistema de gestión ambiental y social y plan de acción vigentes

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.3.1-01 | Revisar el PAAS del 8 de octubre de 2025 y ajustar el SGAS a la organización de la UEP | Planificación | Especialista socioambiental | 12 | 15 | 18 | 15.0 | Juicio de expertos | Contrato cláusula 4.06(b) (PAAS 8-oct-2025); EAS-PGAS v2. Los instrumentos ya existen, solo se ajustan |
| 3.3.1-02 | Elaborar los procedimientos y formatos del SGAS: selección de obra, reporte de incidentes e informe de cumplimiento | Planificación | Especialista socioambiental | 16 | 20 | 24 | 20.0 | Juicio de expertos | EAS-PGAS v2 sec. 6.7 y Anexo 3 (modelo de informe); cuatro semanas |
| 3.3.1-03 | Obtener la no objeción del BID al SGAS y al PAAS actualizados | Planificación | BID | 5 | 10 | 15 | 10.0 | Juicio de expertos | Contrato cláusula 4.05 (cambios al PAAS requieren consentimiento del BID); ROP anexo 7.1 usa 5 días por revisión, se duplica por ser dos instrumentos |
| 3.3.1-04 | Incorporar el SGAS y el PAAS como anexos del ROP aprobado | Planificación | Especialista socioambiental | 4 | 5 | 6 | 5.0 | Juicio de expertos | Contrato cláusula 3.01(c) (ROP con SGAS y PAAS como anexos); trámite documental |
| 3.3.1-05 | Elaborar el Plan de Gestión del Riesgo de Desastres y Cambio Climático final con los diseños aprobados | Planificación | Especialista socioambiental | 20 | 30 | 45 | 30.8 | Juicio de expertos | Contrato cláusula 4.06 (presentar el plan final previo al inicio de las obras); actualiza el plan preliminar con los diseños finales, 6 semanas |
| 3.3.1-06 | Presentar al BID el Plan de Gestión del Riesgo de Desastres y Cambio Climático final | Planificación | Coordinador del Programa | 3 | 5 | 10 | 5.5 | Juicio de expertos | Contrato cláusula 4.06; remisión y atención de observaciones, 1 semana |

#### 3.3.2 Protocolo de seguridad operacional aprobado por la AAC

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.3.2-01 | Evaluar el riesgo operacional y definir las fases de trabajo del lado aire junto con la operación aeroportuaria | Planificación | Especialista en ingeniería aeroportuaria | 16 | 20 | 24 | 20.0 | Juicio de expertos | Anexo III (justificación de licitaciones) sec. 3.2: SMS y evaluación previa de riesgos; FAA AC 150/5370-2G; 4 semanas |
| 3.3.2-02 | Elaborar el protocolo de seguridad operacional para obras del lado aire, de uso de contratistas y supervisión | Planificación | Coordinador general de obra | 24 | 30 | 36 | 30.0 | Análoga | Análogo al Construction Safety and Phasing Plan de FAA AC 150/5370-2G (https://www.faa.gov/documentLibrary/media/Advisory_Circular/150-5370-2G.pdf); contrato cláusula 4.08(i) |
| 3.3.2-03 | Presentar el protocolo a la AAC y atender sus observaciones | Planificación | Coordinador general de obra | 12 | 15 | 18 | 15.0 | Juicio de expertos | Anexo III sec. 3.2 (autorización tramitada por CEPA); dos a tres semanas de ida y vuelta |
| 3.3.2-04 | Aprobar el protocolo de seguridad operacional de las obras del lado aire | Planificación | AAC | 10 | 20 | 40 | 21.7 | Juicio de expertos | Contrato cláusula 4.08(i) (protocolo aprobado por la AAC antes de obras del lado aire); plazo de un tercero, 4 semanas |

#### 3.3.3 Mecanismo de quejas y reclamos en operación

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.3.3-01 | Diseñar el procedimiento del mecanismo de quejas y reclamos: canales, plazos de respuesta y registro de casos | Planificación | Especialista socioambiental | 12 | 15 | 18 | 15.0 | Juicio de expertos | Contrato cláusula 4.06 (mecanismo de quejas, numeral iii); EAS-PGAS v2 sec. de participación y reclamos |
| 3.3.3-02 | Instalar y difundir los canales del mecanismo entre trabajadores, usuarios, arrendatarios, aerolíneas y comunidades | Ejecución | Especialista socioambiental | 16 | 20 | 24 | 20.0 | Juicio de expertos | Contrato cláusula 4.06 (mecanismo de quejas, numeral iii) (accesible y publicitado); EDT 3.3.3, 4 semanas |
| 3.3.3-03 | Operar el mecanismo, registrar los casos y dar respuesta durante las obras | Monitoreo y control | Especialista socioambiental | NE | NE | NE | NE | Nivel de esfuerzo | EDT 3.3.3 (registro de casos); contrato cláusula 4.06 (mecanismo de quejas, numeral iii) |

#### 3.3.4 Informes de cumplimiento socioambiental presentados

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.3.4-01 | Acordar con el BID el formato del informe de cumplimiento ambiental y social semestral | Planificación | Especialista socioambiental | 8 | 10 | 12 | 10.0 | Juicio de expertos | Contrato cláusula 5.01 (forma y contenido acordados con el Banco); EAS-PGAS v2 Anexo 3 (modelo de informe) |
| 3.3.4-02 | Presentar los informes semestrales de cumplimiento ambiental y social junto con el informe de progreso | Monitoreo y control | Especialista socioambiental | NE | NE | NE | NE | Nivel de esfuerzo | Contrato cláusula 5.01; EAS-PGAS v2 (CEPA a BID, semestral) |
| 3.3.4-03 | Presentar al BID el informe final ambiental y social del programa | Cierre | Especialista socioambiental | 12 | 15 | 18 | 15.0 | Juicio de expertos | EAS-PGAS v2 (informe final ambiental y social al terminar cada obra, CEPA a BID); 3 semanas |

#### 3.4.1 Contratos de obras del Componente I firmados

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.4.1-01 | Preparar los documentos de licitación del estacionamiento y el sistema solar | Planificación | Especialista de adquisiciones | 35 | 45 | 55 | 45.0 | Dato del programa | ROP anexo 7.1, LPI paso 2 (45 días para documentos de la solicitud y bases) |
| 3.4.1-02 | Obtener la no objeción del BID a los documentos de licitación del estacionamiento y el sistema solar | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1, LPI pasos 5 y 6 (no objeción en 5 días); Anexo III sec. 2.5 (supervisión ex ante) |
| 3.4.1-03 | Publicar el aviso específico de adquisiciones del estacionamiento y el sistema solar y recibir ofertas hasta la apertura | Ejecución | Especialista de adquisiciones | 31 | 31 | 31 | 31.0 | Dato del programa | SPN IDB-6073OCES-P00001-SPN: aviso 4-sep-2026, ofertas 16-oct-2026 |
| 3.4.1-04 | Evaluar las ofertas del estacionamiento y el sistema solar y elaborar el informe de evaluación | Ejecución | Especialista de adquisiciones | 23 | 29 | 35 | 29.0 | Calibrada | Calibrado a la firma del PA (PA 2026-2 P00001: firma 27-ene-2027). ROP anexo 7.1 estima 15 dl de evaluación |
| 3.4.1-05 | Obtener la no objeción del BID a la evaluación y a la recomendación de adjudicación del estacionamiento y el sistema solar | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1, LPI paso 16 (5 días); Anexo III sec. 2.5 |
| 3.4.1-06 | Adjudicar y firmar el contrato de obra del estacionamiento y el sistema solar | Ejecución | CEPA | 31 | 39 | 47 | 39.0 | Calibrada | Calibrado a la firma del PA (PA 2026-2 P00001: firma 27-ene-2027). ROP anexo 7.1 pasos 17 a 22: notificación, plazo suspensivo de 10 días, resolución de adjudicación (10 días), contrato y garantías |
| 3.4.1-07 | Preparar los documentos de licitación de la terminal de pasajeros | Planificación | Especialista de adquisiciones | 35 | 45 | 55 | 45.0 | Dato del programa | ROP anexo 7.1, LPI paso 2 (45 días para documentos de la solicitud y bases) |
| 3.4.1-08 | Obtener la no objeción del BID a los documentos de licitación de la terminal de pasajeros | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1, LPI pasos 5 y 6 (no objeción en 5 días); Anexo III sec. 2.5 (supervisión ex ante) |
| 3.4.1-09 | Publicar el aviso específico de adquisiciones de la terminal de pasajeros y recibir ofertas hasta la apertura | Ejecución | Especialista de adquisiciones | 32 | 32 | 32 | 32.0 | Dato del programa | SPN IDB-6073OCES-P00023-SPN: aviso 8-oct-2026, ofertas 20-nov-2026 |
| 3.4.1-10 | Evaluar las ofertas de la terminal de pasajeros y elaborar el informe de evaluación | Ejecución | Especialista de adquisiciones | 35 | 44 | 53 | 44.0 | Calibrada | Calibrado a la firma del PA (PA 2026-2 P00023: firma 24-abr-2027 (sábado, se modela el viernes 23)). ROP anexo 7.1 estima 15 dl de evaluación |
| 3.4.1-11 | Obtener la no objeción del BID a la evaluación y a la recomendación de adjudicación de la terminal de pasajeros | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1, LPI paso 16 (5 días); Anexo III sec. 2.5 |
| 3.4.1-12 | Adjudicar y firmar el contrato de obra de la terminal de pasajeros | Ejecución | CEPA | 49 | 61 | 73 | 61.0 | Calibrada | Calibrado a la firma del PA (PA 2026-2 P00023: firma 24-abr-2027 (sábado, se modela el viernes 23)). ROP anexo 7.1 pasos 17 a 22: notificación, plazo suspensivo de 10 días, resolución de adjudicación (10 días), contrato y garantías |
| 3.4.1-13 | Preparar los documentos de licitación del SSEI | Planificación | Especialista de adquisiciones | 35 | 45 | 55 | 45.0 | Dato del programa | ROP anexo 7.1, LPI paso 2 (45 días para documentos de la solicitud y bases) |
| 3.4.1-14 | Obtener la no objeción del BID a los documentos de licitación del SSEI | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1, LPI pasos 5 y 6 (no objeción en 5 días); Anexo III sec. 2.5 (supervisión ex ante) |
| 3.4.1-15 | Publicar el aviso específico de adquisiciones del SSEI y recibir ofertas hasta la apertura | Ejecución | Especialista de adquisiciones | 25 | 31 | 37 | 31.0 | Análoga | Periodo de ofertas del aviso del estacionamiento (SPN-E, 31 dl), con una semana de margen hacia cada lado; el ROP anexo 7.1 estima 42 dl |
| 3.4.1-16 | Evaluar las ofertas del SSEI y elaborar el informe de evaluación | Ejecución | Especialista de adquisiciones | 22 | 28 | 34 | 28.0 | Calibrada | Calibrado a la firma del PA (PA 2026-2 P00025: firma 27-may-2027). ROP anexo 7.1 estima 15 dl de evaluación |
| 3.4.1-17 | Obtener la no objeción del BID a la evaluación y a la recomendación de adjudicación del SSEI | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1, LPI paso 16 (5 días); Anexo III sec. 2.5 |
| 3.4.1-18 | Adjudicar y firmar el contrato de obra del SSEI | Ejecución | CEPA | 30 | 38 | 46 | 38.0 | Calibrada | Calibrado a la firma del PA (PA 2026-2 P00025: firma 27-may-2027). ROP anexo 7.1 pasos 17 a 22: notificación, plazo suspensivo de 10 días, resolución de adjudicación (10 días), contrato y garantías |
| 3.4.1-19 | Preparar los documentos de licitación de las plataformas y la calle Foxtrot | Planificación | Especialista de adquisiciones | 35 | 45 | 55 | 45.0 | Dato del programa | ROP anexo 7.1, LPI paso 2 (45 días para documentos de la solicitud y bases) |
| 3.4.1-20 | Obtener la no objeción del BID a los documentos de licitación de las plataformas y la calle Foxtrot | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1, LPI pasos 5 y 6 (no objeción en 5 días); Anexo III sec. 2.5 (supervisión ex ante) |
| 3.4.1-21 | Publicar el aviso específico de adquisiciones de las plataformas y la calle Foxtrot y recibir ofertas hasta la apertura | Ejecución | Especialista de adquisiciones | 25 | 31 | 37 | 31.0 | Análoga | Periodo de ofertas del aviso del estacionamiento (SPN-E, 31 dl), con una semana de margen hacia cada lado; el ROP anexo 7.1 estima 42 dl |
| 3.4.1-22 | Evaluar las ofertas de las plataformas y la calle Foxtrot y elaborar el informe de evaluación | Ejecución | Especialista de adquisiciones | 20 | 25 | 30 | 25.0 | Calibrada | Calibrado a la firma del PA (PA 2026-2 P00027: firma 22-jul-2027). ROP anexo 7.1 estima 15 dl de evaluación |
| 3.4.1-23 | Obtener la no objeción del BID a la evaluación y a la recomendación de adjudicación de las plataformas y la calle Foxtrot | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1, LPI paso 16 (5 días); Anexo III sec. 2.5 |
| 3.4.1-24 | Adjudicar y firmar el contrato de obra de las plataformas y la calle Foxtrot | Ejecución | CEPA | 27 | 34 | 41 | 34.0 | Calibrada | Calibrado a la firma del PA (PA 2026-2 P00027: firma 22-jul-2027). ROP anexo 7.1 pasos 17 a 22: notificación, plazo suspensivo de 10 días, resolución de adjudicación (10 días), contrato y garantías |

#### 3.4.2 Contrato de supervisión firmado

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.4.2-01 | Preparar los términos de referencia, la solicitud de expresiones de interés y la lista corta de la supervisión del estacionamiento y el sistema solar | Planificación | Especialista de adquisiciones | 14 | 17 | 20 | 17.0 | Dato del programa | EOI-E: expresiones de interés del 6 al 20-may-2026 (CEPA-EOI y aviso P00002); lista corta de 5 a 8 firmas en unos 6 dl más |
| 3.4.2-02 | Obtener la no objeción del BID a los términos de referencia y a la lista corta de la supervisión del estacionamiento y el sistema solar | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP sec. de revisión ex ante de firmas (etapa i: documentos y lista corta); ROP anexo 7.1 (5 días por revisión) |
| 3.4.2-03 | Invitar a las firmas de la lista corta y recibir las propuestas de la supervisión del estacionamiento y el sistema solar | Ejecución | Especialista de adquisiciones | 30 | 40 | 50 | 40.0 | Juicio de expertos | GN-2350-15 exige plazo suficiente; 6 a 8 semanas con aclaraciones y enmiendas a la solicitud de propuestas |
| 3.4.2-04 | Evaluar las propuestas técnicas y económicas y negociar el contrato de la supervisión del estacionamiento y el sistema solar | Ejecución | Especialista de adquisiciones | 99 | 124 | 149 | 124.0 | Calibrada | Calibrado a la firma del PA (PA 2026-2 P00002: firma 3-feb-2027, proceso en curso desde la solicitud de expresiones de interés del 6-may-2026) |
| 3.4.2-05 | Obtener la no objeción del BID al informe de evaluación combinado y al contrato negociado de la supervisión del estacionamiento y el sistema solar | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP sec. de revisión ex ante de firmas (etapa iii); ROP anexo 7.1 (5 días) |
| 3.4.2-06 | Firmar el contrato de supervisión del estacionamiento y el sistema solar | Ejecución | CEPA | 3 | 5 | 7 | 5.0 | Juicio de expertos | PA 2026-2 P00002: inicio 1-nov-2026 (domingo), firma 3-feb-2027, estado Proceso en curso. Firma y garantías de una a dos semanas |
| 3.4.2-07 | Publicar la solicitud de expresiones de interés de la supervisión de la terminal y conformar la lista corta | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Dato del programa | EOI-T: expresiones de interés hasta el 6-oct-2026, método SBCC, lista corta de 5 a 8 firmas; publicación supuesta 10 dl antes, como el estacionamiento |
| 3.4.2-08 | Obtener la no objeción del BID a los términos de referencia y a la lista corta de la supervisión de la terminal | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP sec. de revisión ex ante de firmas (etapa i: documentos y lista corta); ROP anexo 7.1 (5 días por revisión) |
| 3.4.2-09 | Invitar a las firmas de la lista corta y recibir las propuestas de la supervisión de la terminal | Ejecución | Especialista de adquisiciones | 24 | 30 | 36 | 30.0 | Juicio de expertos | GN-2350-15 exige plazo suficiente; 30 dl (6 semanas) es la práctica común |
| 3.4.2-10 | Evaluar las propuestas técnicas y económicas y negociar el contrato de la supervisión de la terminal | Ejecución | Especialista de adquisiciones | 83 | 104 | 125 | 104.0 | Calibrada | Calibrado a la firma del PA (PA 2026-2 P00024: firma 19-may-2027) desde el cierre de expresiones de interés del 6-oct-2026 (EOI-T); incluye la supervisión del diseño en los TdR |
| 3.4.2-11 | Obtener la no objeción del BID al informe de evaluación combinado y al contrato negociado de la supervisión de la terminal | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP sec. de revisión ex ante de firmas (etapa iii); ROP anexo 7.1 (5 días) |
| 3.4.2-12 | Firmar el contrato de supervisión de la terminal | Ejecución | CEPA | 6 | 8 | 10 | 8.0 | Juicio de expertos | PA 2026-2 P00024: firma 19-may-2027. Firma y garantías de una a dos semanas |
| 3.4.2-13 | Preparar los términos de referencia, la solicitud de expresiones de interés y la lista corta de la supervisión del SSEI | Planificación | Especialista de adquisiciones | 38 | 47 | 56 | 47.0 | Calibrada | Calibrado al inicio y firma del PA. PA 2026-2 P00026: inicio 11-nov-2026, firma 10-jun-2027 |
| 3.4.2-14 | Obtener la no objeción del BID a los términos de referencia y a la lista corta de la supervisión del SSEI | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP sec. de revisión ex ante de firmas (etapa i: documentos y lista corta); ROP anexo 7.1 (5 días por revisión) |
| 3.4.2-15 | Invitar a las firmas de la lista corta y recibir las propuestas de la supervisión del SSEI | Ejecución | Especialista de adquisiciones | 24 | 30 | 36 | 30.0 | Juicio de expertos | GN-2350-15 exige plazo suficiente; 30 dl (6 semanas) es la práctica común |
| 3.4.2-16 | Evaluar las propuestas técnicas y económicas y negociar el contrato de la supervisión del SSEI | Ejecución | Especialista de adquisiciones | 46 | 57 | 68 | 57.0 | Calibrada | Calibrado a la firma del PA. PA 2026-2 P00026: inicio 11-nov-2026, firma 10-jun-2027. ROP etapas ii y iii de revisión de firmas |
| 3.4.2-17 | Obtener la no objeción del BID al informe de evaluación combinado y al contrato negociado de la supervisión del SSEI | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP sec. de revisión ex ante de firmas (etapa iii); ROP anexo 7.1 (5 días) |
| 3.4.2-18 | Firmar el contrato de supervisión del SSEI | Ejecución | CEPA | 6 | 8 | 10 | 8.0 | Juicio de expertos | PA 2026-2 P00026: inicio 11-nov-2026, firma 10-jun-2027. Firma y garantías de una a dos semanas |
| 3.4.2-19 | Preparar los términos de referencia, la solicitud de expresiones de interés y la lista corta de la supervisión de las plataformas y la calle Foxtrot | Planificación | Especialista de adquisiciones | 32 | 40 | 48 | 40.0 | Calibrada | Calibrado al inicio y firma del PA. PA 2026-2 P00028: inicio 19-ene-2027, firma 28-jul-2027 |
| 3.4.2-20 | Obtener la no objeción del BID a los términos de referencia y a la lista corta de la supervisión de las plataformas y la calle Foxtrot | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP sec. de revisión ex ante de firmas (etapa i: documentos y lista corta); ROP anexo 7.1 (5 días por revisión) |
| 3.4.2-21 | Invitar a las firmas de la lista corta y recibir las propuestas de la supervisión de las plataformas y la calle Foxtrot | Ejecución | Especialista de adquisiciones | 24 | 30 | 36 | 30.0 | Juicio de expertos | GN-2350-15 exige plazo suficiente; 30 dl (6 semanas) es la práctica común |
| 3.4.2-22 | Evaluar las propuestas técnicas y económicas y negociar el contrato de la supervisión de las plataformas y la calle Foxtrot | Ejecución | Especialista de adquisiciones | 39 | 49 | 59 | 49.0 | Calibrada | Calibrado a la firma del PA. PA 2026-2 P00028: inicio 19-ene-2027, firma 28-jul-2027. ROP etapas ii y iii de revisión de firmas |
| 3.4.2-23 | Obtener la no objeción del BID al informe de evaluación combinado y al contrato negociado de la supervisión de las plataformas y la calle Foxtrot | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP sec. de revisión ex ante de firmas (etapa iii); ROP anexo 7.1 (5 días) |
| 3.4.2-24 | Firmar el contrato de supervisión de las plataformas y la calle Foxtrot | Ejecución | CEPA | 6 | 8 | 10 | 8.0 | Juicio de expertos | PA 2026-2 P00028: inicio 19-ene-2027, firma 28-jul-2027. Firma y garantías de una a dos semanas |

#### 3.4.3 Contratos de consultorías del Componente II firmados

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.4.3-01 | Incluir las consultorías del Componente II en el Plan de Adquisiciones | Planificación | Especialista de adquisiciones | 10 | 15 | 20 | 15.0 | Juicio de expertos | PA 2026-2 no contiene ningún proceso del Componente II; supuesto: se incluyen en una revisión del PA posterior al corte del 31-oct-2026 |
| 3.4.3-02 | Obtener la no objeción del BID a la actualización del PA con el Componente II | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 (5 días por revisión); contrato cláusula 4.04 |
| 3.4.3-03 | Preparar los términos de referencia, la solicitud de expresiones de interés y la lista corta para el plan estratégico del sistema aeronáutico (producto 2.1) | Planificación | Especialista de adquisiciones | 32 | 40 | 48 | 40.0 | Juicio de expertos | ROP anexo 7.1 3CV (TdR 10 días) y ROP tabla 10 (SBCC con lista corta internacional si monto ≥ US$200,000). Juicio: EOI de 2 semanas, evaluación de lista corta de 2 semanas, TdR de 3 semanas |
| 3.4.3-04 | Obtener la no objeción del BID a los términos de referencia y a la lista corta del plan estratégico del sistema aeronáutico (producto 2.1) | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 (5 días por revisión del BID) |
| 3.4.3-05 | Invitar a las firmas de la lista corta y recibir las propuestas para el plan estratégico del sistema aeronáutico (producto 2.1) | Ejecución | Especialista de adquisiciones | 24 | 30 | 36 | 30.0 | Juicio de expertos | GN-2350-15; juicio de expertos: 6 semanas de plazo de propuestas |
| 3.4.3-06 | Evaluar las propuestas y negociar el contrato para el plan estratégico del sistema aeronáutico (producto 2.1) | Ejecución | Especialista de adquisiciones | 28 | 35 | 42 | 35.0 | Juicio de expertos | Juicio de expertos: evaluación técnica, apertura económica y negociación, 7 semanas |
| 3.4.3-07 | Obtener la no objeción del BID al informe de evaluación y al contrato negociado del plan estratégico del sistema aeronáutico (producto 2.1) | Ejecución | BID | 5 | 7 | 9 | 7.0 | Juicio de expertos | ROP anexo 7.1 (5 días); se amplía a 7 por ser informe combinado y contrato |
| 3.4.3-08 | Firmar el contrato de consultoría para el plan estratégico del sistema aeronáutico (producto 2.1) | Ejecución | CEPA | 8 | 10 | 12 | 10.0 | Juicio de expertos | Juicio de expertos: firma y garantías, 2 semanas |
| 3.4.3-09 | Preparar los términos de referencia, la solicitud de expresiones de interés y la lista corta para la actualización del Plan Maestro y la capacitación (productos 2.2.1 y 2.2.2) | Planificación | Especialista de adquisiciones | 32 | 40 | 48 | 40.0 | Juicio de expertos | ROP anexo 7.1 3CV (TdR 10 días) y ROP tabla 10 (SBCC con lista corta internacional si monto ≥ US$200,000). Juicio: EOI de 2 semanas, evaluación de lista corta de 2 semanas, TdR de 3 semanas |
| 3.4.3-10 | Obtener la no objeción del BID a los términos de referencia y a la lista corta de la actualización del Plan Maestro y la capacitación (productos 2.2.1 y 2.2.2) | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 (5 días por revisión del BID) |
| 3.4.3-11 | Invitar a las firmas de la lista corta y recibir las propuestas para la actualización del Plan Maestro y la capacitación (productos 2.2.1 y 2.2.2) | Ejecución | Especialista de adquisiciones | 24 | 30 | 36 | 30.0 | Juicio de expertos | GN-2350-15; juicio de expertos: 6 semanas de plazo de propuestas |
| 3.4.3-12 | Evaluar las propuestas y negociar el contrato para la actualización del Plan Maestro y la capacitación (productos 2.2.1 y 2.2.2) | Ejecución | Especialista de adquisiciones | 28 | 35 | 42 | 35.0 | Juicio de expertos | Juicio de expertos: evaluación técnica, apertura económica y negociación, 7 semanas |
| 3.4.3-13 | Obtener la no objeción del BID al informe de evaluación y al contrato negociado de la actualización del Plan Maestro y la capacitación (productos 2.2.1 y 2.2.2) | Ejecución | BID | 5 | 7 | 9 | 7.0 | Juicio de expertos | ROP anexo 7.1 (5 días); se amplía a 7 por ser informe combinado y contrato |
| 3.4.3-14 | Firmar el contrato de consultoría para la actualización del Plan Maestro y la capacitación (productos 2.2.1 y 2.2.2) | Ejecución | CEPA | 8 | 10 | 12 | 10.0 | Juicio de expertos | Juicio de expertos: firma y garantías, 2 semanas |
| 3.4.3-15 | Preparar los términos de referencia y la solicitud de expresiones de interés para la estrategia y capacitación BIM (productos 2.3.1 y 2.3.2) | Planificación | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | ROP anexo 7.1 3CV (TdR 10 días), ampliado por juicio a 4 semanas; el contrato de BIM (unos US$259,000) supera los US$200,000 de la tabla 10 del ROP: SBCC con lista corta internacional y revisión ex ante (Anexo III.i, 2.5) |
| 3.4.3-16 | Publicar la solicitud de expresiones de interés y conformar la lista corta internacional para la estrategia y capacitación BIM (productos 2.3.1 y 2.3.2) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | Juicio de expertos: EOI de 2 semanas y evaluación de 2 semanas; ROP tabla 10 (lista corta con llamado internacional para contratos desde US$200,000) |
| 3.4.3-17 | Invitar a las firmas de la lista corta y recibir las propuestas para la estrategia y capacitación BIM (productos 2.3.1 y 2.3.2) | Ejecución | Especialista de adquisiciones | 24 | 30 | 36 | 30.0 | Juicio de expertos | GN-2350-15; juicio de expertos: 6 semanas de plazo de propuestas de firmas internacionales, igual que los otros procesos SBCC (3.4.3-05) |
| 3.4.3-18 | Evaluar las propuestas y negociar el contrato para la estrategia y capacitación BIM (productos 2.3.1 y 2.3.2) | Ejecución | Especialista de adquisiciones | 28 | 35 | 42 | 35.0 | Juicio de expertos | Juicio de expertos: evaluación técnica, apertura económica y negociación, 7 semanas, igual que los otros procesos SBCC (3.4.3-06) |
| 3.4.3-19 | Adjudicar y firmar el contrato de consultoría para la estrategia y capacitación BIM (productos 2.3.1 y 2.3.2) | Ejecución | CEPA | 8 | 10 | 12 | 10.0 | Juicio de expertos | Juicio de expertos: resolución de adjudicación y firma, 2 semanas |
| 3.4.3-20 | Preparar los términos de referencia, la solicitud de expresiones de interés y la lista corta para el estudio de conectividad terrestre (producto 2.4) | Planificación | Especialista de adquisiciones | 32 | 40 | 48 | 40.0 | Juicio de expertos | ROP anexo 7.1 3CV (TdR 10 días) y ROP tabla 10 (SBCC con lista corta internacional si monto ≥ US$200,000). Juicio: EOI de 2 semanas, evaluación de lista corta de 2 semanas, TdR de 3 semanas |
| 3.4.3-21 | Obtener la no objeción del BID a los términos de referencia y a la lista corta del estudio de conectividad terrestre (producto 2.4) | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 (5 días por revisión del BID) |
| 3.4.3-22 | Invitar a las firmas de la lista corta y recibir las propuestas para el estudio de conectividad terrestre (producto 2.4) | Ejecución | Especialista de adquisiciones | 24 | 30 | 36 | 30.0 | Juicio de expertos | GN-2350-15; juicio de expertos: 6 semanas de plazo de propuestas |
| 3.4.3-23 | Evaluar las propuestas y negociar el contrato para el estudio de conectividad terrestre (producto 2.4) | Ejecución | Especialista de adquisiciones | 28 | 35 | 42 | 35.0 | Juicio de expertos | Juicio de expertos: evaluación técnica, apertura económica y negociación, 7 semanas |
| 3.4.3-24 | Obtener la no objeción del BID al informe de evaluación y al contrato negociado del estudio de conectividad terrestre (producto 2.4) | Ejecución | BID | 5 | 7 | 9 | 7.0 | Juicio de expertos | ROP anexo 7.1 (5 días); se amplía a 7 por ser informe combinado y contrato |
| 3.4.3-25 | Firmar el contrato de consultoría para el estudio de conectividad terrestre (producto 2.4) | Ejecución | CEPA | 8 | 10 | 12 | 10.0 | Juicio de expertos | Juicio de expertos: firma y garantías, 2 semanas |
| 3.4.3-26 | Preparar los términos de referencia y la solicitud de expresiones de interés para el estudio de diversificación de destinos (producto 2.5) | Planificación | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | ROP anexo 7.1 3CV (TdR 10 días), ampliado por juicio a 4 semanas; consultoría < US$200,000 va por lista corta nacional (ROP tabla 10), con revisión ex ante porque el Anexo III.i (2.5) y el PA 2026-2 sujetan todos los procesos a ella, aunque la tabla 10 del ROP prevé ex post para firmas por menos de US$200,000 |
| 3.4.3-27 | Publicar la solicitud de expresiones de interés y conformar la lista corta nacional para el estudio de diversificación de destinos (producto 2.5) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | Juicio de expertos: EOI de 2 semanas y evaluación de 2 semanas; ROP tabla 10 (lista corta con llamado nacional) |
| 3.4.3-28 | Invitar a las firmas de la lista corta y recibir las propuestas para el estudio de diversificación de destinos (producto 2.5) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | GN-2350-15; juicio de expertos: 4 semanas de plazo de propuestas |
| 3.4.3-29 | Evaluar las propuestas y negociar el contrato para el estudio de diversificación de destinos (producto 2.5) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | Juicio de expertos: 4 semanas de evaluación y negociación |
| 3.4.3-30 | Adjudicar y firmar el contrato de consultoría para el estudio de diversificación de destinos (producto 2.5) | Ejecución | CEPA | 8 | 10 | 12 | 10.0 | Juicio de expertos | Juicio de expertos: resolución de adjudicación y firma, 2 semanas |
| 3.4.3-31 | Preparar los términos de referencia y la solicitud de expresiones de interés para la auditoría y capacitación para la certificación EDGE (productos 2.6.1 y 2.6.2) | Planificación | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | ROP anexo 7.1 3CV (TdR 10 días), ampliado por juicio a 4 semanas; consultoría < US$200,000 va por lista corta nacional (ROP tabla 10), con revisión ex ante porque el Anexo III.i (2.5) y el PA 2026-2 sujetan todos los procesos a ella, aunque la tabla 10 del ROP prevé ex post para firmas por menos de US$200,000 |
| 3.4.3-32 | Publicar la solicitud de expresiones de interés y conformar la lista corta nacional para la auditoría y capacitación para la certificación EDGE (productos 2.6.1 y 2.6.2) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | Juicio de expertos: EOI de 2 semanas y evaluación de 2 semanas; ROP tabla 10 (lista corta con llamado nacional) |
| 3.4.3-33 | Invitar a las firmas de la lista corta y recibir las propuestas para la auditoría y capacitación para la certificación EDGE (productos 2.6.1 y 2.6.2) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | GN-2350-15; juicio de expertos: 4 semanas de plazo de propuestas |
| 3.4.3-34 | Evaluar las propuestas y negociar el contrato para la auditoría y capacitación para la certificación EDGE (productos 2.6.1 y 2.6.2) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | Juicio de expertos: 4 semanas de evaluación y negociación |
| 3.4.3-35 | Adjudicar y firmar el contrato de consultoría para la auditoría y capacitación para la certificación EDGE (productos 2.6.1 y 2.6.2) | Ejecución | CEPA | 8 | 10 | 12 | 10.0 | Juicio de expertos | Juicio de expertos: resolución de adjudicación y firma, 2 semanas |
| 3.4.3-36 | Preparar los términos de referencia y la solicitud de expresiones de interés para el estudio de separación de flujos (producto 2.7) | Planificación | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | ROP anexo 7.1 3CV (TdR 10 días), ampliado por juicio a 4 semanas; consultoría < US$200,000 va por lista corta nacional (ROP tabla 10), con revisión ex ante porque el Anexo III.i (2.5) y el PA 2026-2 sujetan todos los procesos a ella, aunque la tabla 10 del ROP prevé ex post para firmas por menos de US$200,000 |
| 3.4.3-37 | Publicar la solicitud de expresiones de interés y conformar la lista corta nacional para el estudio de separación de flujos (producto 2.7) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | Juicio de expertos: EOI de 2 semanas y evaluación de 2 semanas; ROP tabla 10 (lista corta con llamado nacional) |
| 3.4.3-38 | Invitar a las firmas de la lista corta y recibir las propuestas para el estudio de separación de flujos (producto 2.7) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | GN-2350-15; juicio de expertos: 4 semanas de plazo de propuestas |
| 3.4.3-39 | Evaluar las propuestas y negociar el contrato para el estudio de separación de flujos (producto 2.7) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | Juicio de expertos: 4 semanas de evaluación y negociación |
| 3.4.3-40 | Adjudicar y firmar el contrato de consultoría para el estudio de separación de flujos (producto 2.7) | Ejecución | CEPA | 8 | 10 | 12 | 10.0 | Juicio de expertos | Juicio de expertos: resolución de adjudicación y firma, 2 semanas |
| 3.4.3-41 | Preparar los términos de referencia y la solicitud de expresiones de interés para el estudio de movilidad interna (producto 2.8) | Planificación | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | ROP anexo 7.1 3CV (TdR 10 días), ampliado por juicio a 4 semanas; consultoría < US$200,000 va por lista corta nacional (ROP tabla 10), con revisión ex ante porque el Anexo III.i (2.5) y el PA 2026-2 sujetan todos los procesos a ella, aunque la tabla 10 del ROP prevé ex post para firmas por menos de US$200,000 |
| 3.4.3-42 | Publicar la solicitud de expresiones de interés y conformar la lista corta nacional para el estudio de movilidad interna (producto 2.8) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | Juicio de expertos: EOI de 2 semanas y evaluación de 2 semanas; ROP tabla 10 (lista corta con llamado nacional) |
| 3.4.3-43 | Invitar a las firmas de la lista corta y recibir las propuestas para el estudio de movilidad interna (producto 2.8) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | GN-2350-15; juicio de expertos: 4 semanas de plazo de propuestas |
| 3.4.3-44 | Evaluar las propuestas y negociar el contrato para el estudio de movilidad interna (producto 2.8) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | Juicio de expertos: 4 semanas de evaluación y negociación |
| 3.4.3-45 | Adjudicar y firmar el contrato de consultoría para el estudio de movilidad interna (producto 2.8) | Ejecución | CEPA | 8 | 10 | 12 | 10.0 | Juicio de expertos | Juicio de expertos: resolución de adjudicación y firma, 2 semanas |
| 3.4.3-46 | Preparar los términos de referencia y la solicitud de expresiones de interés para el programa de igualdad e inclusión (producto 2.9) | Planificación | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | ROP anexo 7.1 3CV (TdR 10 días), ampliado por juicio a 4 semanas; consultoría < US$200,000 va por lista corta nacional (ROP tabla 10), con revisión ex ante porque el Anexo III.i (2.5) y el PA 2026-2 sujetan todos los procesos a ella, aunque la tabla 10 del ROP prevé ex post para firmas por menos de US$200,000 |
| 3.4.3-47 | Publicar la solicitud de expresiones de interés y conformar la lista corta nacional para el programa de igualdad e inclusión (producto 2.9) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | Juicio de expertos: EOI de 2 semanas y evaluación de 2 semanas; ROP tabla 10 (lista corta con llamado nacional) |
| 3.4.3-48 | Invitar a las firmas de la lista corta y recibir las propuestas para el programa de igualdad e inclusión (producto 2.9) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | GN-2350-15; juicio de expertos: 4 semanas de plazo de propuestas |
| 3.4.3-49 | Evaluar las propuestas y negociar el contrato para el programa de igualdad e inclusión (producto 2.9) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | Juicio de expertos: 4 semanas de evaluación y negociación |
| 3.4.3-50 | Adjudicar y firmar el contrato de consultoría para el programa de igualdad e inclusión (producto 2.9) | Ejecución | CEPA | 8 | 10 | 12 | 10.0 | Juicio de expertos | Juicio de expertos: resolución de adjudicación y firma, 2 semanas |
| 3.4.3-51 | Obtener la no objeción del BID a los términos de referencia y a la lista corta para la estrategia y capacitación BIM (productos 2.3.1 y 2.3.2) | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 (5 días por revisión del BID); revisión ex ante de todos los procesos (Anexo III.i, 2.5; PA 2026-2) |
| 3.4.3-52 | Obtener la no objeción del BID al informe de evaluación y al contrato negociado para la estrategia y capacitación BIM (productos 2.3.1 y 2.3.2) | Ejecución | BID | 5 | 7 | 9 | 7.0 | Juicio de expertos | ROP anexo 7.1 (5 días); se amplía a 7 por ser informe combinado y contrato; revisión ex ante (Anexo III.i, 2.5) |
| 3.4.3-53 | Obtener la no objeción del BID a los términos de referencia y a la lista corta para el estudio de diversificación de destinos (producto 2.5) | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 (5 días por revisión del BID); revisión ex ante de todos los procesos (Anexo III.i, 2.5; PA 2026-2) |
| 3.4.3-54 | Obtener la no objeción del BID al informe de evaluación y al contrato negociado para el estudio de diversificación de destinos (producto 2.5) | Ejecución | BID | 5 | 7 | 9 | 7.0 | Juicio de expertos | ROP anexo 7.1 (5 días); se amplía a 7 por ser informe combinado y contrato; revisión ex ante (Anexo III.i, 2.5) |
| 3.4.3-55 | Obtener la no objeción del BID a los términos de referencia y a la lista corta para la auditoría y capacitación para la certificación EDGE (productos 2.6.1 y 2.6.2) | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 (5 días por revisión del BID); revisión ex ante de todos los procesos (Anexo III.i, 2.5; PA 2026-2) |
| 3.4.3-56 | Obtener la no objeción del BID al informe de evaluación y al contrato negociado para la auditoría y capacitación para la certificación EDGE (productos 2.6.1 y 2.6.2) | Ejecución | BID | 5 | 7 | 9 | 7.0 | Juicio de expertos | ROP anexo 7.1 (5 días); se amplía a 7 por ser informe combinado y contrato; revisión ex ante (Anexo III.i, 2.5) |
| 3.4.3-57 | Obtener la no objeción del BID a los términos de referencia y a la lista corta para el estudio de separación de flujos (producto 2.7) | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 (5 días por revisión del BID); revisión ex ante de todos los procesos (Anexo III.i, 2.5; PA 2026-2) |
| 3.4.3-58 | Obtener la no objeción del BID al informe de evaluación y al contrato negociado para el estudio de separación de flujos (producto 2.7) | Ejecución | BID | 5 | 7 | 9 | 7.0 | Juicio de expertos | ROP anexo 7.1 (5 días); se amplía a 7 por ser informe combinado y contrato; revisión ex ante (Anexo III.i, 2.5) |
| 3.4.3-59 | Obtener la no objeción del BID a los términos de referencia y a la lista corta para el estudio de movilidad interna (producto 2.8) | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 (5 días por revisión del BID); revisión ex ante de todos los procesos (Anexo III.i, 2.5; PA 2026-2) |
| 3.4.3-60 | Obtener la no objeción del BID al informe de evaluación y al contrato negociado para el estudio de movilidad interna (producto 2.8) | Ejecución | BID | 5 | 7 | 9 | 7.0 | Juicio de expertos | ROP anexo 7.1 (5 días); se amplía a 7 por ser informe combinado y contrato; revisión ex ante (Anexo III.i, 2.5) |
| 3.4.3-61 | Obtener la no objeción del BID a los términos de referencia y a la lista corta para el programa de igualdad e inclusión (producto 2.9) | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 (5 días por revisión del BID); revisión ex ante de todos los procesos (Anexo III.i, 2.5; PA 2026-2) |
| 3.4.3-62 | Obtener la no objeción del BID al informe de evaluación y al contrato negociado para el programa de igualdad e inclusión (producto 2.9) | Ejecución | BID | 5 | 7 | 9 | 7.0 | Juicio de expertos | ROP anexo 7.1 (5 días); se amplía a 7 por ser informe combinado y contrato; revisión ex ante (Anexo III.i, 2.5) |

#### 3.4.4 Contratos de la unidad ejecutora, evaluación y auditoría firmados

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.4.4-01 | Preparar los términos de referencia y la convocatoria de los siete consultores clave de la UEP | Inicio | CEPA | 14 | 18 | 22 | 18.0 | Dato del programa | PA 2026-2 filas P00004 a P00010 (firma 15-abr-2026); ROP anexo 7.1 3CV (TdR 10 días más revisión) |
| 3.4.4-02 | Obtener la no objeción del BID a los términos de referencia de los siete consultores clave | Inicio | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (5 días) |
| 3.4.4-03 | Recibir los currículos, evaluar y seleccionar a los siete consultores clave | Inicio | CEPA | 16 | 20 | 24 | 20.0 | Dato del programa | ROP anexo 7.1 3CV (15 días de recepción de CV más 3 de evaluación e informe) |
| 3.4.4-04 | Obtener la no objeción del BID a la selección de los siete consultores clave | Inicio | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (5 días) |
| 3.4.4-05 | Firmar los contratos de los siete consultores clave de la UEP | Inicio | CEPA | 3 | 5 | 7 | 5.0 | Dato del programa | PA 2026-2 filas P00004 a P00010: firma 15-abr-2026 y estado Contrato en ejecución |
| 3.4.4-06 | Preparar los términos de referencia y la convocatoria del técnico de apoyo administrativo | Planificación | Especialista de adquisiciones | 8 | 10 | 12 | 10.0 | Dato del programa | PA 2026-2 fila P00014 (Asistente Administrativo, inicio 14-jul-2026, firma 15-ago-2026, estado Previsto); ROP anexo 7.1 3CV |
| 3.4.4-07 | Obtener la no objeción del BID a los términos de referencia del técnico de apoyo | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (5 días) |
| 3.4.4-08 | Recibir los currículos, evaluar y seleccionar al técnico de apoyo | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Dato del programa | ROP anexo 7.1 3CV (15 + 3 días e informe) |
| 3.4.4-09 | Obtener la no objeción del BID a la selección del técnico de apoyo | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (5 días) |
| 3.4.4-10 | Firmar el contrato del técnico de apoyo administrativo | Ejecución | CEPA | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (contrato y registro) |
| 3.4.4-11 | Preparar los términos de referencia y la lista corta de la auditoría externa año 1 | Planificación | Especialista de adquisiciones | 3 | 5 | 7 | 5.0 | Dato del programa | PA 2026-2 P00003 (inicio 1-abr-2027, firma 5-may-2027). Estructura reducida para respetar las fechas del PA (25 dl en total) |
| 3.4.4-12 | Obtener la no objeción del BID a los términos de referencia de la auditoría año 1 | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | PA 2026-2 P00003 (inicio 1-abr-2027, firma 5-may-2027). Estructura reducida para respetar las fechas del PA (25 dl en total) |
| 3.4.4-13 | Invitar a las firmas, recibir y evaluar las propuestas de la auditoría año 1 por menor costo | Ejecución | Especialista de adquisiciones | 3 | 5 | 7 | 5.0 | Dato del programa | PA 2026-2 P00003 (inicio 1-abr-2027, firma 5-may-2027). Estructura reducida para respetar las fechas del PA (25 dl en total) |
| 3.4.4-14 | Obtener la no objeción del BID a la recomendación de adjudicación de la auditoría año 1 | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | PA 2026-2 P00003 (inicio 1-abr-2027, firma 5-may-2027). Estructura reducida para respetar las fechas del PA (25 dl en total) |
| 3.4.4-15 | Firmar el contrato de la auditoría externa año 1 | Ejecución | CEPA | 3 | 5 | 7 | 5.0 | Dato del programa | PA 2026-2 P00003 (inicio 1-abr-2027, firma 5-may-2027). Estructura reducida para respetar las fechas del PA (25 dl en total) |
| 3.4.4-16 | Preparar los términos de referencia y la lista corta de la auditoría externa año 2 | Planificación | Especialista de adquisiciones | 24 | 30 | 36 | 30.0 | Juicio de expertos | PEP nov-2025 (eer3.txt) auditoría año 2: proceso 1-may-2027, contrato 12-dic-2027. SBMC con lista corta nacional, ex ante (ROP tabla 10: contrato menor a US$200,000; PA 2026-2); duraciones por juicio con ROP anexo 7.1 |
| 3.4.4-17 | Obtener la no objeción del BID a los términos de referencia de la auditoría año 2 | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | PEP nov-2025 (eer3.txt) auditoría año 2: proceso 1-may-2027, contrato 12-dic-2027. SBMC con lista corta nacional, ex ante (ROP tabla 10: contrato menor a US$200,000; PA 2026-2); duraciones por juicio con ROP anexo 7.1 |
| 3.4.4-18 | Invitar a las firmas, recibir y evaluar las propuestas de la auditoría año 2 por menor costo | Ejecución | Especialista de adquisiciones | 20 | 25 | 30 | 25.0 | Juicio de expertos | PEP nov-2025 (eer3.txt) auditoría año 2: proceso 1-may-2027, contrato 12-dic-2027. SBMC con lista corta nacional, ex ante (ROP tabla 10: contrato menor a US$200,000; PA 2026-2); duraciones por juicio con ROP anexo 7.1 |
| 3.4.4-19 | Obtener la no objeción del BID a la recomendación de adjudicación de la auditoría año 2 | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | PEP nov-2025 (eer3.txt) auditoría año 2: proceso 1-may-2027, contrato 12-dic-2027. SBMC con lista corta nacional, ex ante (ROP tabla 10: contrato menor a US$200,000; PA 2026-2); duraciones por juicio con ROP anexo 7.1 |
| 3.4.4-20 | Firmar el contrato de la auditoría externa año 2 | Ejecución | CEPA | 6 | 8 | 10 | 8.0 | Juicio de expertos | PEP nov-2025 (eer3.txt) auditoría año 2: proceso 1-may-2027, contrato 12-dic-2027. SBMC con lista corta nacional, ex ante (ROP tabla 10: contrato menor a US$200,000; PA 2026-2); duraciones por juicio con ROP anexo 7.1 |
| 3.4.4-21 | Preparar los términos de referencia y la lista corta de la auditoría externa año 3 | Planificación | Especialista de adquisiciones | 24 | 30 | 36 | 30.0 | Juicio de expertos | PEP nov-2025 (eer3.txt) auditoría año 3: proceso 1-may-2028, contrato 12-dic-2028. SBMC con lista corta nacional, ex ante (ROP tabla 10: contrato menor a US$200,000; PA 2026-2); duraciones por juicio con ROP anexo 7.1 |
| 3.4.4-22 | Obtener la no objeción del BID a los términos de referencia de la auditoría año 3 | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | PEP nov-2025 (eer3.txt) auditoría año 3: proceso 1-may-2028, contrato 12-dic-2028. SBMC con lista corta nacional, ex ante (ROP tabla 10: contrato menor a US$200,000; PA 2026-2); duraciones por juicio con ROP anexo 7.1 |
| 3.4.4-23 | Invitar a las firmas, recibir y evaluar las propuestas de la auditoría año 3 por menor costo | Ejecución | Especialista de adquisiciones | 20 | 25 | 30 | 25.0 | Juicio de expertos | PEP nov-2025 (eer3.txt) auditoría año 3: proceso 1-may-2028, contrato 12-dic-2028. SBMC con lista corta nacional, ex ante (ROP tabla 10: contrato menor a US$200,000; PA 2026-2); duraciones por juicio con ROP anexo 7.1 |
| 3.4.4-24 | Obtener la no objeción del BID a la recomendación de adjudicación de la auditoría año 3 | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | PEP nov-2025 (eer3.txt) auditoría año 3: proceso 1-may-2028, contrato 12-dic-2028. SBMC con lista corta nacional, ex ante (ROP tabla 10: contrato menor a US$200,000; PA 2026-2); duraciones por juicio con ROP anexo 7.1 |
| 3.4.4-25 | Firmar el contrato de la auditoría externa año 3 | Ejecución | CEPA | 6 | 8 | 10 | 8.0 | Juicio de expertos | PEP nov-2025 (eer3.txt) auditoría año 3: proceso 1-may-2028, contrato 12-dic-2028. SBMC con lista corta nacional, ex ante (ROP tabla 10: contrato menor a US$200,000; PA 2026-2); duraciones por juicio con ROP anexo 7.1 |
| 3.4.4-26 | Preparar los términos de referencia y la lista corta de la auditoría externa año 4 | Planificación | Especialista de adquisiciones | 24 | 30 | 36 | 30.0 | Juicio de expertos | PEP nov-2025 (eer3.txt) auditoría año 4: proceso 1-dic-2028, contrato 14-jul-2029. SBMC con lista corta nacional, ex ante (ROP tabla 10: contrato menor a US$200,000; PA 2026-2); duraciones por juicio con ROP anexo 7.1 |
| 3.4.4-27 | Obtener la no objeción del BID a los términos de referencia de la auditoría año 4 | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | PEP nov-2025 (eer3.txt) auditoría año 4: proceso 1-dic-2028, contrato 14-jul-2029. SBMC con lista corta nacional, ex ante (ROP tabla 10: contrato menor a US$200,000; PA 2026-2); duraciones por juicio con ROP anexo 7.1 |
| 3.4.4-28 | Invitar a las firmas, recibir y evaluar las propuestas de la auditoría año 4 por menor costo | Ejecución | Especialista de adquisiciones | 20 | 25 | 30 | 25.0 | Juicio de expertos | PEP nov-2025 (eer3.txt) auditoría año 4: proceso 1-dic-2028, contrato 14-jul-2029. SBMC con lista corta nacional, ex ante (ROP tabla 10: contrato menor a US$200,000; PA 2026-2); duraciones por juicio con ROP anexo 7.1 |
| 3.4.4-29 | Obtener la no objeción del BID a la recomendación de adjudicación de la auditoría año 4 | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | PEP nov-2025 (eer3.txt) auditoría año 4: proceso 1-dic-2028, contrato 14-jul-2029. SBMC con lista corta nacional, ex ante (ROP tabla 10: contrato menor a US$200,000; PA 2026-2); duraciones por juicio con ROP anexo 7.1 |
| 3.4.4-30 | Firmar el contrato de la auditoría externa año 4 | Ejecución | CEPA | 6 | 8 | 10 | 8.0 | Juicio de expertos | PEP nov-2025 (eer3.txt) auditoría año 4: proceso 1-dic-2028, contrato 14-jul-2029. SBMC con lista corta nacional, ex ante (ROP tabla 10: contrato menor a US$200,000; PA 2026-2); duraciones por juicio con ROP anexo 7.1 |
| 3.4.4-31 | Preparar los términos de referencia y la solicitud de expresiones de interés de la evaluación de medio término | Planificación | Especialista de adquisiciones | 12 | 15 | 18 | 15.0 | Dato del programa | PEP nov-2025 evaluación de medio término: proceso 15-jul-2027, contrato 27-nov-2027 (matriz: oct-2027 a dic-2027). SCC con lista corta nacional y revisión ex ante (Anexo III.i, 2.5; ROP tabla 10) |
| 3.4.4-32 | Publicar la solicitud de expresiones de interés y conformar la lista corta nacional de la evaluación de medio término | Ejecución | Especialista de adquisiciones | 12 | 15 | 18 | 15.0 | Calibrada | Calibrado al contrato del PEP (97 dl entre el inicio del proceso y el contrato, 135 días calendario); reparto 15/15/5/17/28/7/10 dl con las dos no objeciones del BID de la revisión ex ante (Anexo III.i, 2.5); método SCC (GN-2350-15) |
| 3.4.4-33 | Invitar a las firmas de la lista corta y recibir las propuestas de la evaluación de medio término | Ejecución | Especialista de adquisiciones | 14 | 17 | 20 | 17.0 | Calibrada | Calibrado al contrato del PEP (97 dl entre el inicio del proceso y el contrato, 135 días calendario); reparto 15/15/5/17/28/7/10 dl con las dos no objeciones del BID de la revisión ex ante (Anexo III.i, 2.5); método SCC (GN-2350-15) |
| 3.4.4-34 | Evaluar las propuestas y negociar el contrato de la evaluación de medio término | Ejecución | Especialista de adquisiciones | 22 | 28 | 34 | 28.0 | Calibrada | Calibrado al contrato del PEP (97 dl entre el inicio del proceso y el contrato, 135 días calendario); reparto 15/15/5/17/28/7/10 dl con las dos no objeciones del BID de la revisión ex ante (Anexo III.i, 2.5); método SCC (GN-2350-15) |
| 3.4.4-35 | Adjudicar y firmar el contrato de la evaluación de medio término | Ejecución | CEPA | 8 | 10 | 12 | 10.0 | Calibrada | Calibrado al contrato del PEP (97 dl entre el inicio del proceso y el contrato, 135 días calendario); reparto 15/15/5/17/28/7/10 dl con las dos no objeciones del BID de la revisión ex ante (Anexo III.i, 2.5); método SCC (GN-2350-15) |
| 3.4.4-36 | Preparar los términos de referencia y la solicitud de expresiones de interés de la evaluación final | Planificación | Especialista de adquisiciones | 12 | 15 | 18 | 15.0 | Dato del programa | PEP nov-2025 evaluación de cierre: proceso 15-ene-2029, contrato 30-may-2029 (matriz: mar-2029 a may-2029). SCC con lista corta nacional y revisión ex ante (Anexo III.i, 2.5; ROP tabla 10) |
| 3.4.4-37 | Publicar la solicitud de expresiones de interés y conformar la lista corta nacional de la evaluación final | Ejecución | Especialista de adquisiciones | 12 | 15 | 18 | 15.0 | Calibrada | Calibrado al contrato del PEP (98 dl entre el inicio del proceso y el contrato, 135 días calendario); reparto 15/15/5/17/29/7/10 dl con las dos no objeciones del BID de la revisión ex ante (Anexo III.i, 2.5); método SCC (GN-2350-15) |
| 3.4.4-38 | Invitar a las firmas de la lista corta y recibir las propuestas de la evaluación final | Ejecución | Especialista de adquisiciones | 14 | 17 | 20 | 17.0 | Calibrada | Calibrado al contrato del PEP (98 dl entre el inicio del proceso y el contrato, 135 días calendario); reparto 15/15/5/17/29/7/10 dl con las dos no objeciones del BID de la revisión ex ante (Anexo III.i, 2.5); método SCC (GN-2350-15) |
| 3.4.4-39 | Evaluar las propuestas y negociar el contrato de la evaluación final | Ejecución | Especialista de adquisiciones | 23 | 29 | 35 | 29.0 | Calibrada | Calibrado al contrato del PEP (98 dl entre el inicio del proceso y el contrato, 135 días calendario); reparto 15/15/5/17/29/7/10 dl con las dos no objeciones del BID de la revisión ex ante (Anexo III.i, 2.5); método SCC (GN-2350-15) |
| 3.4.4-40 | Adjudicar y firmar el contrato de la evaluación final | Ejecución | CEPA | 8 | 10 | 12 | 10.0 | Calibrada | Calibrado al contrato del PEP (98 dl entre el inicio del proceso y el contrato, 135 días calendario); reparto 15/15/5/17/29/7/10 dl con las dos no objeciones del BID de la revisión ex ante (Anexo III.i, 2.5); método SCC (GN-2350-15) |
| 3.4.4-41 | Obtener la no objeción del BID a los términos de referencia y a la lista corta de la evaluación de medio término | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 (5 días por revisión del BID); revisión ex ante (Anexo III.i, 2.5) |
| 3.4.4-42 | Obtener la no objeción del BID al informe de evaluación y al contrato negociado de la evaluación de medio término | Ejecución | BID | 5 | 7 | 9 | 7.0 | Juicio de expertos | ROP anexo 7.1 (5 días); se amplía a 7 por ser informe combinado y contrato; revisión ex ante (Anexo III.i, 2.5) |
| 3.4.4-43 | Obtener la no objeción del BID a los términos de referencia y a la lista corta de la evaluación final | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 (5 días por revisión del BID); revisión ex ante (Anexo III.i, 2.5) |
| 3.4.4-44 | Obtener la no objeción del BID al informe de evaluación y al contrato negociado de la evaluación final | Ejecución | BID | 5 | 7 | 9 | 7.0 | Juicio de expertos | ROP anexo 7.1 (5 días); se amplía a 7 por ser informe combinado y contrato; revisión ex ante (Anexo III.i, 2.5) |
| 3.4.4-45 | Preparar los términos de referencia y la convocatoria de los consultores individuales del lote 1 de la plantilla ampliada de la UEP (diez puestos, agosto de 2026) | Planificación | Especialista de adquisiciones | 8 | 10 | 12 | 10.0 | Dato del programa | PA 2026-2 filas P00011, P00013, P00015, P00016, P00017, P00018, P00029, P00030, P00031, P00032 (3CV, ex ante, estado Previsto): inicio de proceso 14-ago-2026, firma estimada 7-sep-2026; ROP anexo 7.1 3CV (50 dl); decisión de incluir la plantilla ampliada (S-III.14) |
| 3.4.4-46 | Obtener la no objeción del BID a los términos de referencia del lote 1 de la plantilla ampliada de la UEP (diez puestos, agosto de 2026) | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (5 días); revisión ex ante (PA 2026-2) |
| 3.4.4-47 | Recibir los currículos, comparar las calificaciones y seleccionar a los consultores del lote 1 de la plantilla ampliada de la UEP (diez puestos, agosto de 2026) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Dato del programa | ROP anexo 7.1 3CV (15 + 3 días e informe) |
| 3.4.4-48 | Obtener la no objeción del BID a la selección de los consultores del lote 1 de la plantilla ampliada de la UEP (diez puestos, agosto de 2026) | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (5 días); revisión ex ante (PA 2026-2) |
| 3.4.4-49 | Firmar los contratos de los consultores individuales del lote 1 de la plantilla ampliada de la UEP (diez puestos, agosto de 2026) | Ejecución | CEPA | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (contrato y registro) |
| 3.4.4-50 | Preparar los términos de referencia y la convocatoria de los consultores individuales del lote 2 de la plantilla ampliada de la UEP (pavimentos aeroportuarios, septiembre de 2026) | Planificación | Especialista de adquisiciones | 8 | 10 | 12 | 10.0 | Dato del programa | PA 2026-2 filas P00040 (3CV, ex ante, estado Previsto): inicio de proceso 4-sep-2026, firma estimada 1-oct-2026; ROP anexo 7.1 3CV (50 dl); decisión de incluir la plantilla ampliada (S-III.14) |
| 3.4.4-51 | Obtener la no objeción del BID a los términos de referencia del lote 2 de la plantilla ampliada de la UEP (pavimentos aeroportuarios, septiembre de 2026) | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (5 días); revisión ex ante (PA 2026-2) |
| 3.4.4-52 | Recibir los currículos, comparar las calificaciones y seleccionar a los consultores del lote 2 de la plantilla ampliada de la UEP (pavimentos aeroportuarios, septiembre de 2026) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Dato del programa | ROP anexo 7.1 3CV (15 + 3 días e informe) |
| 3.4.4-53 | Obtener la no objeción del BID a la selección de los consultores del lote 2 de la plantilla ampliada de la UEP (pavimentos aeroportuarios, septiembre de 2026) | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (5 días); revisión ex ante (PA 2026-2) |
| 3.4.4-54 | Firmar los contratos de los consultores individuales del lote 2 de la plantilla ampliada de la UEP (pavimentos aeroportuarios, septiembre de 2026) | Ejecución | CEPA | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (contrato y registro) |
| 3.4.4-55 | Preparar los términos de referencia y la convocatoria de los consultores individuales del lote 3 de la plantilla ampliada de la UEP (analista social, septiembre de 2026) | Planificación | Especialista de adquisiciones | 8 | 10 | 12 | 10.0 | Dato del programa | PA 2026-2 filas P00033 (3CV, ex ante, estado Previsto): inicio de proceso 16-sep-2026, firma estimada 15-oct-2026; ROP anexo 7.1 3CV (50 dl); decisión de incluir la plantilla ampliada (S-III.14) |
| 3.4.4-56 | Obtener la no objeción del BID a los términos de referencia del lote 3 de la plantilla ampliada de la UEP (analista social, septiembre de 2026) | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (5 días); revisión ex ante (PA 2026-2) |
| 3.4.4-57 | Recibir los currículos, comparar las calificaciones y seleccionar a los consultores del lote 3 de la plantilla ampliada de la UEP (analista social, septiembre de 2026) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Dato del programa | ROP anexo 7.1 3CV (15 + 3 días e informe) |
| 3.4.4-58 | Obtener la no objeción del BID a la selección de los consultores del lote 3 de la plantilla ampliada de la UEP (analista social, septiembre de 2026) | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (5 días); revisión ex ante (PA 2026-2) |
| 3.4.4-59 | Firmar los contratos de los consultores individuales del lote 3 de la plantilla ampliada de la UEP (analista social, septiembre de 2026) | Ejecución | CEPA | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (contrato y registro) |
| 3.4.4-60 | Preparar los términos de referencia y la convocatoria de los consultores individuales del lote 4 de la plantilla ampliada de la UEP (tres puestos, enero de 2027) | Planificación | Especialista de adquisiciones | 8 | 10 | 12 | 10.0 | Dato del programa | PA 2026-2 filas P00012, P00020, P00039 (3CV, ex ante, estado Previsto): inicio de proceso 14-ene-2027 (P00020) y 15-ene-2027, firma estimada 1-feb-2027 y 9-feb-2027; ROP anexo 7.1 3CV (50 dl); decisión de incluir la plantilla ampliada (S-III.14) |
| 3.4.4-61 | Obtener la no objeción del BID a los términos de referencia del lote 4 de la plantilla ampliada de la UEP (tres puestos, enero de 2027) | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (5 días); revisión ex ante (PA 2026-2) |
| 3.4.4-62 | Recibir los currículos, comparar las calificaciones y seleccionar a los consultores del lote 4 de la plantilla ampliada de la UEP (tres puestos, enero de 2027) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Dato del programa | ROP anexo 7.1 3CV (15 + 3 días e informe) |
| 3.4.4-63 | Obtener la no objeción del BID a la selección de los consultores del lote 4 de la plantilla ampliada de la UEP (tres puestos, enero de 2027) | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (5 días); revisión ex ante (PA 2026-2) |
| 3.4.4-64 | Firmar los contratos de los consultores individuales del lote 4 de la plantilla ampliada de la UEP (tres puestos, enero de 2027) | Ejecución | CEPA | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (contrato y registro) |
| 3.4.4-65 | Preparar los términos de referencia y la convocatoria de los consultores individuales del lote 5 de la plantilla ampliada de la UEP (cinco puestos, marzo de 2027) | Planificación | Especialista de adquisiciones | 8 | 10 | 12 | 10.0 | Dato del programa | PA 2026-2 filas P00034, P00035, P00036, P00037, P00038 (3CV, ex ante, estado Previsto): inicio de proceso 23-mar-2027, firma estimada 16-abr-2027; ROP anexo 7.1 3CV (50 dl); decisión de incluir la plantilla ampliada (S-III.14) |
| 3.4.4-66 | Obtener la no objeción del BID a los términos de referencia del lote 5 de la plantilla ampliada de la UEP (cinco puestos, marzo de 2027) | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (5 días); revisión ex ante (PA 2026-2) |
| 3.4.4-67 | Recibir los currículos, comparar las calificaciones y seleccionar a los consultores del lote 5 de la plantilla ampliada de la UEP (cinco puestos, marzo de 2027) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Dato del programa | ROP anexo 7.1 3CV (15 + 3 días e informe) |
| 3.4.4-68 | Obtener la no objeción del BID a la selección de los consultores del lote 5 de la plantilla ampliada de la UEP (cinco puestos, marzo de 2027) | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (5 días); revisión ex ante (PA 2026-2) |
| 3.4.4-69 | Firmar los contratos de los consultores individuales del lote 5 de la plantilla ampliada de la UEP (cinco puestos, marzo de 2027) | Ejecución | CEPA | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (contrato y registro) |
| 3.4.4-70 | Preparar los términos de referencia y la convocatoria de los consultores individuales del lote 6 de la plantilla ampliada de la UEP (Administrador 4 de Proyectos, agosto de 2027) | Planificación | Especialista de adquisiciones | 8 | 10 | 12 | 10.0 | Dato del programa | PA 2026-2 filas P00041 (3CV, ex ante, estado Previsto): inicio de proceso 30-ago-2027, firma estimada 23-sep-2027; ROP anexo 7.1 3CV (50 dl); decisión de incluir la plantilla ampliada (S-III.14) |
| 3.4.4-71 | Obtener la no objeción del BID a los términos de referencia del lote 6 de la plantilla ampliada de la UEP (Administrador 4 de Proyectos, agosto de 2027) | Planificación | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (5 días); revisión ex ante (PA 2026-2) |
| 3.4.4-72 | Recibir los currículos, comparar las calificaciones y seleccionar a los consultores del lote 6 de la plantilla ampliada de la UEP (Administrador 4 de Proyectos, agosto de 2027) | Ejecución | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Dato del programa | ROP anexo 7.1 3CV (15 + 3 días e informe) |
| 3.4.4-73 | Obtener la no objeción del BID a la selección de los consultores del lote 6 de la plantilla ampliada de la UEP (Administrador 4 de Proyectos, agosto de 2027) | Ejecución | BID | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (5 días); revisión ex ante (PA 2026-2) |
| 3.4.4-74 | Firmar los contratos de los consultores individuales del lote 6 de la plantilla ampliada de la UEP (Administrador 4 de Proyectos, agosto de 2027) | Ejecución | CEPA | 3 | 5 | 7 | 5.0 | Dato del programa | ROP anexo 7.1 3CV (contrato y registro) |

#### 3.5.1 Desembolsos justificados e informes financieros presentados

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.5.1-01 | Solicitar el primer desembolso por Anticipo de Fondos con las condiciones previas cumplidas | Ejecución | Especialista financiero | 8 | 10 | 12 | 10.0 | Juicio de expertos | Contrato cláusula 3.01 y Normas Generales art. 4.07 (Anticipo de Fondos); expediente de dos semanas |
| 3.5.1-02 | Elaborar y presentar al BID el informe semestral de progreso del semestre S2 de 2026 con la solicitud de desembolso | Monitoreo y control | Especialista de planificación y monitoreo | 15 | 20 | 21 | 19.3 | Dato del programa | Contrato cláusula 5.01(a)(iii) (informe 30 días después de cada semestre calendario, unos 21 dl); incluye POA y PEP de los dos semestres siguientes |
| 3.5.1-03 | Elaborar y presentar al BID el informe semestral de progreso del semestre S1 de 2027 con la solicitud de desembolso | Monitoreo y control | Especialista de planificación y monitoreo | 15 | 20 | 21 | 19.3 | Dato del programa | Contrato cláusula 5.01(a)(iii) (informe 30 días después de cada semestre calendario, unos 21 dl); incluye POA y PEP de los dos semestres siguientes |
| 3.5.1-04 | Elaborar y presentar al BID el informe semestral de progreso del semestre S2 de 2027 con la solicitud de desembolso | Monitoreo y control | Especialista de planificación y monitoreo | 15 | 20 | 21 | 19.3 | Dato del programa | Contrato cláusula 5.01(a)(iii) (informe 30 días después de cada semestre calendario, unos 21 dl); incluye POA y PEP de los dos semestres siguientes |
| 3.5.1-05 | Elaborar y presentar al BID el informe semestral de progreso del semestre S1 de 2028 con la solicitud de desembolso | Monitoreo y control | Especialista de planificación y monitoreo | 15 | 20 | 21 | 19.3 | Dato del programa | Contrato cláusula 5.01(a)(iii) (informe 30 días después de cada semestre calendario, unos 21 dl); incluye POA y PEP de los dos semestres siguientes |
| 3.5.1-06 | Elaborar y presentar al BID el informe semestral de progreso del semestre S2 de 2028 con la solicitud de desembolso | Monitoreo y control | Especialista de planificación y monitoreo | 15 | 20 | 21 | 19.3 | Dato del programa | Contrato cláusula 5.01(a)(iii) (informe 30 días después de cada semestre calendario, unos 21 dl); incluye POA y PEP de los dos semestres siguientes |
| 3.5.1-07 | Elaborar y presentar al BID el informe semestral de progreso del semestre S1 de 2029 con la solicitud de desembolso | Monitoreo y control | Especialista de planificación y monitoreo | 15 | 20 | 21 | 19.3 | Dato del programa | Contrato cláusula 5.01(a)(iii) (informe 30 días después de cada semestre calendario, unos 21 dl); incluye POA y PEP de los dos semestres siguientes |
| 3.5.1-08 | Justificar los gastos y tramitar las solicitudes de desembolso del año 2027 | Monitoreo y control | Especialista financiero | NE | NE | NE | NE | Nivel de esfuerzo | Normas Generales art. 4.06 (reembolsos dentro de 60 días tras cada semestre) y art. 4.07 (justificar al menos 80% del anticipo anterior) |
| 3.5.1-09 | Justificar los gastos y tramitar las solicitudes de desembolso del año 2028 | Monitoreo y control | Especialista financiero | NE | NE | NE | NE | Nivel de esfuerzo | Normas Generales art. 4.06 (reembolsos dentro de 60 días tras cada semestre) y art. 4.07 (justificar al menos 80% del anticipo anterior) |
| 3.5.1-10 | Justificar los gastos y tramitar las solicitudes de desembolso del año 2029 | Monitoreo y control | Especialista financiero | NE | NE | NE | NE | Nivel de esfuerzo | Normas Generales art. 4.06 (reembolsos dentro de 60 días tras cada semestre) y art. 4.07 (justificar al menos 80% del anticipo anterior) |

#### 3.5.2 Auditorías externas emitidas

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.5.2-01 | Preparar los estados financieros del programa del ejercicio 2026 | Monitoreo y control | Especialista financiero | 15 | 20 | 25 | 20.0 | Juicio de expertos | Contrato cláusula 5.02(a)(i) y (b) (ejercicio de 1 de enero a 31 de diciembre); 4 semanas de cierre contable |
| 3.5.2-02 | Auditar los estados financieros del programa del ejercicio 2026 | Monitoreo y control | Auditor externo | 20 | 30 | 40 | 30.0 | Juicio de expertos | Contrato cláusula 5.02(a)(i); auditoría anual de un programa de monto medio, 6 semanas |
| 3.5.2-03 | Presentar al BID los estados financieros auditados del ejercicio 2026 | Monitoreo y control | Especialista financiero | 3 | 5 | 7 | 5.0 | Dato del programa | Contrato cláusula 5.02(a)(i) y Normas Generales art. 7.03 (120 días después del cierre de cada ejercicio) |
| 3.5.2-04 | Preparar los estados financieros del programa del ejercicio 2027 | Monitoreo y control | Especialista financiero | 15 | 20 | 25 | 20.0 | Juicio de expertos | Contrato cláusula 5.02(a)(i) y (b) (ejercicio de 1 de enero a 31 de diciembre); 4 semanas de cierre contable |
| 3.5.2-05 | Auditar los estados financieros del programa del ejercicio 2027 | Monitoreo y control | Auditor externo | 20 | 30 | 40 | 30.0 | Juicio de expertos | Contrato cláusula 5.02(a)(i); auditoría anual de un programa de monto medio, 6 semanas |
| 3.5.2-06 | Presentar al BID los estados financieros auditados del ejercicio 2027 | Monitoreo y control | Especialista financiero | 3 | 5 | 7 | 5.0 | Dato del programa | Contrato cláusula 5.02(a)(i) y Normas Generales art. 7.03 (120 días después del cierre de cada ejercicio) |
| 3.5.2-07 | Preparar los estados financieros del programa del ejercicio 2028 | Monitoreo y control | Especialista financiero | 15 | 20 | 25 | 20.0 | Juicio de expertos | Contrato cláusula 5.02(a)(i) y (b) (ejercicio de 1 de enero a 31 de diciembre); 4 semanas de cierre contable |
| 3.5.2-08 | Auditar los estados financieros del programa del ejercicio 2028 | Monitoreo y control | Auditor externo | 20 | 30 | 40 | 30.0 | Juicio de expertos | Contrato cláusula 5.02(a)(i); auditoría anual de un programa de monto medio, 6 semanas |
| 3.5.2-09 | Presentar al BID los estados financieros auditados del ejercicio 2028 | Monitoreo y control | Especialista financiero | 3 | 5 | 7 | 5.0 | Dato del programa | Contrato cláusula 5.02(a)(i) y Normas Generales art. 7.03 (120 días después del cierre de cada ejercicio) |

#### 3.5.3 Evaluaciones de medio término y de cierre realizadas

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.5.3-01 | Proyectar con los contratos de obra firmados la fecha del hito de medio término (50% del tiempo de ejecución planificado o 50% de los recursos desembolsados, lo que ocurra primero) | Planificación | Especialista de planificación y monitoreo | 3 | 5 | 7 | 5.0 | Juicio de expertos | Contrato cláusula 5.03(a): informe a más tardar 60 días después de que se desembolse el 50% de los recursos o transcurra el 50% del tiempo de ejecución planificado, lo que ocurra primero; vigencia desde la plena validez jurídica (cláusula 6.01, S-III.20); anticipos de fondos (Normas Generales, art. 4.07, S-III.19); MEL |
| 3.5.3-02 | Ejecutar la evaluación de medio término: avance físico y financiero y medición temprana de resultados | Monitoreo y control | Firma consultora | 65 | 86 | 100 | 84.8 | Dato del programa | PEP nov-2025 evaluación de medio término: contrato de 120 días calendario, equivalentes a 86 dl; contrato cláusula 5.03(a) |
| 3.5.3-03 | Revisar el informe de evaluación de medio término y presentarlo al BID | Monitoreo y control | Especialista de planificación y monitoreo | 8 | 10 | 12 | 10.0 | Juicio de expertos | EDT 3.5.3 (informe aceptado); contrato cláusula 5.03(a) |
| 3.5.3-04 | Ejecutar la evaluación final de efectividad sin atribución empírica | Cierre | Firma consultora | 100 | 129 | 140 | 126.0 | Dato del programa | PEP nov-2025 evaluación de cierre: contrato de 180 días calendario, equivalentes a 129 dl; MEL sec. IV.B y contrato cláusula 5.03(b) |
| 3.5.3-05 | Revisar el informe de evaluación final y presentarlo al BID | Cierre | Especialista de planificación y monitoreo | 8 | 10 | 12 | 10.0 | Juicio de expertos | EDT 3.5.3 (informe aceptado); contrato cláusula 5.03(b) |

#### 3.5.4 Informe de terminación y cierre administrativo del programa

| Código | Actividad | Fase | Responsable | O | M | P | Estimada | Técnica | Fuente |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 3.5.4-01 | Liquidar los contratos de obra, supervisión y consultoría | Cierre | Especialista de adquisiciones | 16 | 20 | 24 | 20.0 | Juicio de expertos | EDT 3.5.4 (contratos liquidados); 4 semanas para los 52 contratos del programa: 23 de obras, supervisión, consultorías, evaluaciones y auditorías, y 29 de personal de la UEP, cuya liquidación es un finiquito de honorarios (duración por juicio, sin cambio) |
| 3.5.4-02 | Justificar los anticipos pendientes y tramitar el último desembolso | Cierre | Especialista financiero | 16 | 20 | 24 | 20.0 | Juicio de expertos | Normas Generales art. 4.03(a) (última solicitud de desembolso 30 días antes del vencimiento del plazo) y art. 4.14 (periodo de cierre); 4 semanas |
| 3.5.4-03 | Auditar y presentar al BID los estados financieros finales del programa | Cierre | Auditor externo | 30 | 40 | 60 | 41.7 | Juicio de expertos | Contrato Normas Generales art. 7.03(a) (120 días tras el último desembolso); 8 semanas |
| 3.5.4-04 | Preparar y entregar al BID los insumos de la UEP para el informe de terminación del programa, con las lecciones aprendidas | Cierre | Coordinador del Programa | 20 | 25 | 30 | 25.0 | Juicio de expertos | EDT 3.5.4; contrato cláusula 5.03(c) (el BID prepara el PCR con insumos de la UEP); 5 semanas |
| 3.5.4-05 | Devolver los saldos no justificados al BID y cerrar la cuenta especial | Cierre | Especialista financiero | 12 | 15 | 18 | 15.0 | Juicio de expertos | Normas Generales art. 4.07 (devolución de Anticipo de Fondos no justificado); 3 semanas |
| 3.5.4-06 | Cerrar el expediente administrativo del programa y archivar los documentos | Cierre | Técnico de apoyo administrativo | 8 | 10 | 12 | 10.0 | Juicio de expertos | Normas Generales art. 6.01(c) (conservación de documentos y registros); EDT 3.5.4; 2 semanas |

### Restricciones de fecha

| Código | Actividad | No comenzar antes de | Fundamento |
|---|---|---|---|
| 3.1.1-01 | Incorporar al Coordinador del Programa, al Coordinador general de obra y al Especialista de planificación y monitoreo | 16-04-2026 | Fecha real de inicio 16-abr-2026 |
| 3.1.1-02 | Incorporar al Especialista de adquisiciones | 23-04-2026 | Fecha real de inicio 23-abr-2026 |
| 3.1.1-03 | Incorporar al Especialista en ingeniería aeroportuaria, al Especialista financiero y al Especialista socioambiental | 04-05-2026 | Fecha real de inicio 4-may-2026 |
| 3.2.2-01 | Elaborar el POA 2027 con metas, cronograma físico y financiero y presupuesto por producto | 02-11-2026 | Ancla de calendario por juicio: elaboración en nov-dic para tenerlo aprobado antes del 1 de enero (EDT 3.2.2) |
| 3.2.2-03 | Elaborar el POA 2028 con metas, cronograma físico y financiero y presupuesto por producto | 01-11-2027 | Ancla de calendario por juicio: elaboración en nov-dic para tenerlo aprobado antes del 1 de enero (EDT 3.2.2) |
| 3.2.2-05 | Elaborar el POA 2029 con metas, cronograma físico y financiero y presupuesto por producto | 01-11-2028 | Ancla de calendario por juicio: elaboración en nov-dic para tenerlo aprobado antes del 1 de enero (EDT 3.2.2) |
| 3.2.2-07 | Elaborar el POA 2030 con metas, cronograma físico y financiero y presupuesto por producto | 01-11-2029 | Ancla de calendario por juicio: elaboración en nov-dic para tenerlo aprobado antes del 1 de enero (EDT 3.2.2) |
| 3.2.3-02 | Obtener la no objeción del BID al Plan de Adquisiciones 2026-1 | 07-04-2026 | Termina el 13-abr-2026 para regir desde el 14-abr-2026 |
| 3.2.3-04 | Obtener la no objeción del BID al Plan de Adquisiciones 2026-2 | 08-07-2026 | Termina el 14-jul-2026 |
| 3.2.3-06 | Publicar el Aviso General de Adquisiciones del programa en el portal del BID | 29-04-2026 | Publicado el 5-may-2026 |
| 3.4.1-03 | Publicar el aviso específico de adquisiciones del estacionamiento y el sistema solar y recibir ofertas hasta la apertura | 04-09-2026 | Apertura de ofertas el 2026-10-16 |
| 3.4.1-09 | Publicar el aviso específico de adquisiciones de la terminal de pasajeros y recibir ofertas hasta la apertura | 08-10-2026 | Apertura de ofertas el 2026-11-20 |
| 3.4.1-15 | Publicar el aviso específico de adquisiciones del SSEI y recibir ofertas hasta la apertura | 06-01-2027 | Apertura de ofertas el 2027-02-17 |
| 3.4.1-21 | Publicar el aviso específico de adquisiciones de las plataformas y la calle Foxtrot y recibir ofertas hasta la apertura | 12-03-2027 | Apertura de ofertas el 2027-04-23 |
| 3.4.2-01 | Preparar los términos de referencia, la solicitud de expresiones de interés y la lista corta de la supervisión del estacionamiento y el sistema solar | 06-05-2026 | El PA 2026-2 registra el proceso como "en curso" con inicio el 1-nov-2026 |
| 3.4.2-07 | Publicar la solicitud de expresiones de interés de la supervisión de la terminal y conformar la lista corta | 22-09-2026 | El PA 2026-2 registra el inicio del proceso el 13-oct-2026, después del cierre de las expresiones de interés |
| 3.4.2-13 | Preparar los términos de referencia, la solicitud de expresiones de interés y la lista corta de la supervisión del SSEI | 11-11-2026 | Duración calibrada con las fechas del PA |
| 3.4.2-19 | Preparar los términos de referencia, la solicitud de expresiones de interés y la lista corta de la supervisión de las plataformas y la calle Foxtrot | 19-01-2027 | Duración calibrada con las fechas del PA |
| 3.4.3-01 | Incluir las consultorías del Componente II en el Plan de Adquisiciones | 02-11-2026 | Supuesto: revisión del PA tras el corte del 31-oct-2026 |
| 3.4.4-01 | Preparar los términos de referencia y la convocatoria de los siete consultores clave de la UEP | 02-02-2026 | Inicio tras la ratificación del préstamo el 29-ene-2026 |
| 3.4.4-06 | Preparar los términos de referencia y la convocatoria del técnico de apoyo administrativo | 14-07-2026 | Inicio de proceso del PA |
| 3.4.4-11 | Preparar los términos de referencia y la lista corta de la auditoría externa año 1 | 01-04-2027 | PA 2026-2 P00003 (inicio 1-abr-2027, firma 5-may-2027). Estructura reducida para respetar las fechas del PA (25 dl en total) |
| 3.4.4-16 | Preparar los términos de referencia y la lista corta de la auditoría externa año 2 | 13-09-2027 | Inicio fijado para firmar en la fecha del PEP (2027-12-13) sin espera entre el proceso y la firma |
| 3.4.4-21 | Preparar los términos de referencia y la lista corta de la auditoría externa año 3 | 12-09-2028 | Inicio fijado para firmar en la fecha del PEP (2028-12-12) sin espera entre el proceso y la firma |
| 3.4.4-26 | Preparar los términos de referencia y la lista corta de la auditoría externa año 4 | 16-04-2029 | Inicio fijado para firmar en la fecha del PEP (2029-07-16) sin espera entre el proceso y la firma |
| 3.4.4-45 | Preparar los términos de referencia y la convocatoria de los consultores individuales del lote 1 de la plantilla ampliada de la UEP (diez puestos, agosto de 2026) | 14-08-2026 | Procesos P00011, P00013, P00015, P00016, P00017, P00018, P00029, P00030, P00031, P00032: P00011 Administrador 1 de Proyectos; P00013 Especialista Legal; P00015 Ordenanza / Mensajero; P00016 Analista en Adquisiciones; P00017 Analista Financiero; P00018 Técnico en Planificación y Monitoreo; P00029 Ingeniero Estructurista; P00030 Ingeniero Electricista; P00031 Ingeniero Hidráulico; P00032 Especialista en Seguridad Industrial y Salud Ocupacional. Monto estimado total US$980,525. Inicio de proceso del PA 14-ago-2026 |
| 3.4.4-50 | Preparar los términos de referencia y la convocatoria de los consultores individuales del lote 2 de la plantilla ampliada de la UEP (pavimentos aeroportuarios, septiembre de 2026) | 04-09-2026 | Procesos P00040: P00040 Pavimentos Aeroportuarios. Monto estimado total US$65,000. Inicio de proceso del PA 4-sep-2026 |
| 3.4.4-55 | Preparar los términos de referencia y la convocatoria de los consultores individuales del lote 3 de la plantilla ampliada de la UEP (analista social, septiembre de 2026) | 16-09-2026 | Procesos P00033: P00033 Analista Social. Monto estimado total US$46,800. Inicio de proceso del PA 16-sep-2026 |
| 3.4.4-60 | Preparar los términos de referencia y la convocatoria de los consultores individuales del lote 4 de la plantilla ampliada de la UEP (tres puestos, enero de 2027) | 14-01-2027 | Procesos P00012, P00020, P00039: P00012 Analista Técnico 1; P00020 Gestor Documental; P00039 Arquitecto. Monto estimado total US$199,550. Inicio de proceso del PA 14-ene-2027 (P00020) y 15-ene-2027 |
| 3.4.4-65 | Preparar los términos de referencia y la convocatoria de los consultores individuales del lote 5 de la plantilla ampliada de la UEP (cinco puestos, marzo de 2027) | 23-03-2027 | Procesos P00034, P00035, P00036, P00037, P00038: P00034 Administrador 2 de Proyectos; P00035 Analista Técnico 2; P00036 Administrador 3 de Proyectos; P00037 Analista Técnico 3; P00038 Ingeniero Mecánico. Monto estimado total US$514,800. Inicio de proceso del PA 23-mar-2027 |
| 3.4.4-70 | Preparar los términos de referencia y la convocatoria de los consultores individuales del lote 6 de la plantilla ampliada de la UEP (Administrador 4 de Proyectos, agosto de 2027) | 30-08-2027 | Procesos P00041: P00041 Administrador 4 de Proyectos. Monto estimado total US$113,750. Inicio de proceso del PA 30-ago-2027 |
| 3.5.1-02 | Elaborar y presentar al BID el informe semestral de progreso del semestre S2 de 2026 con la solicitud de desembolso | 01-01-2027 | Plazo contractual de 30 días calendario tras el cierre del semestre |
| 3.5.1-03 | Elaborar y presentar al BID el informe semestral de progreso del semestre S1 de 2027 con la solicitud de desembolso | 01-07-2027 | Plazo contractual de 30 días calendario tras el cierre del semestre |
| 3.5.1-04 | Elaborar y presentar al BID el informe semestral de progreso del semestre S2 de 2027 con la solicitud de desembolso | 03-01-2028 | Plazo contractual de 30 días calendario tras el cierre del semestre |
| 3.5.1-05 | Elaborar y presentar al BID el informe semestral de progreso del semestre S1 de 2028 con la solicitud de desembolso | 03-07-2028 | Plazo contractual de 30 días calendario tras el cierre del semestre |
| 3.5.1-06 | Elaborar y presentar al BID el informe semestral de progreso del semestre S2 de 2028 con la solicitud de desembolso | 01-01-2029 | Plazo contractual de 30 días calendario tras el cierre del semestre |
| 3.5.1-07 | Elaborar y presentar al BID el informe semestral de progreso del semestre S1 de 2029 con la solicitud de desembolso | 02-07-2029 | Plazo contractual de 30 días calendario tras el cierre del semestre |
| 3.5.1-08 | Justificar los gastos y tramitar las solicitudes de desembolso del año 2027 | 01-01-2027 | Acompaña todo el año hasta el informe del semestre S2 |
| 3.5.1-09 | Justificar los gastos y tramitar las solicitudes de desembolso del año 2028 | 03-01-2028 | Acompaña todo el año hasta el informe del semestre S2 |
| 3.5.1-10 | Justificar los gastos y tramitar las solicitudes de desembolso del año 2029 | 01-01-2029 | Acompaña los pagos hasta la liquidación de los contratos |
| 3.5.2-01 | Preparar los estados financieros del programa del ejercicio 2026 | 01-01-2027 | Ancla: cierre del ejercicio |
| 3.5.2-04 | Preparar los estados financieros del programa del ejercicio 2027 | 03-01-2028 | Ancla: cierre del ejercicio |
| 3.5.2-07 | Preparar los estados financieros del programa del ejercicio 2028 | 01-01-2029 | Ancla: cierre del ejercicio |

### Actividades de nivel de esfuerzo

| Código | Actividad | Empieza después de | Termina con |
|---|---|---|---|
| 1.7.1-02 | Supervisar la construcción de la terminal | 1.7.1-01 | 1.7.4-01 |
| 1.7.1-04 | Supervisar la construcción del estacionamiento y del sistema solar | 1.7.1-03 | 1.7.4-02 |
| 1.7.2-02 | Supervisar la construcción de plataformas y de la calle Foxtrot | 1.7.2-01 | 1.7.4-03 |
| 1.7.2-04 | Supervisar la construcción del edificio del SSEI | 1.7.2-03 | 1.7.4-04 |
| 1.7.3-05 | Dar seguimiento al cumplimiento del PGAS durante las obras | 1.7.3-01 | 1.7.4-01, 1.7.4-02, 1.7.4-03, 1.7.4-04 |
| 2.6.1-03 | Acompañar a CEPA y a los contratistas para conservar las medidas EDGE durante la construcción | 2.6.1-02 | 1.2.4-06, 1.5.3-04 |
| 3.1.1-06 | Administrar el programa desde la Unidad Ejecutora | 3.1.1-01 | 3.5.4-04 |
| 3.2.3-05 | Mantener el Plan de Adquisiciones actualizado en el sistema del BID cada vez que cambie un proceso | 3.2.3-04 | 3.4.1-06, 3.4.1-12, 3.4.1-18, 3.4.1-24, 3.4.2-06, 3.4.2-12, 3.4.2-18, 3.4.2-24, 3.4.3-08, 3.4.3-14, 3.4.3-19, 3.4.3-25, 3.4.3-30, 3.4.3-35, 3.4.3-40, 3.4.3-45, 3.4.3-50, 3.4.4-05, 3.4.4-10, 3.4.4-15, 3.4.4-20, 3.4.4-25, 3.4.4-30, 3.4.4-35, 3.4.4-40 |
| 3.3.3-03 | Operar el mecanismo, registrar los casos y dar respuesta durante las obras | 3.3.3-02 | 1.2.4-06, 1.3.3-05, 1.4.2-04, 1.5.3-04, 1.6.2-04 |
| 3.3.4-02 | Presentar los informes semestrales de cumplimiento ambiental y social junto con el informe de progreso | 1.5.1-01, 3.3.4-01 | 1.2.4-06, 1.3.3-05, 1.4.2-04, 1.5.3-04, 1.6.2-04 |
| 3.5.1-08 | Justificar los gastos y tramitar las solicitudes de desembolso del año 2027 | 3.5.1-01 | 3.5.1-04 |
| 3.5.1-09 | Justificar los gastos y tramitar las solicitudes de desembolso del año 2028 | 3.5.1-01 | 3.5.1-06 |
| 3.5.1-10 | Justificar los gastos y tramitar las solicitudes de desembolso del año 2029 | 3.5.1-01 | 3.5.4-01 |

## 7. Tabla de dependencias

| Sucesora | Predecesora | Tipo | Desfase (dl) | Clase | Justificación |
|---|---|---|---:|---|---|
| 1.1.1-01 | 3.1.1-05 | FI | 0 | Obligatoria | El especialista en ingeniería aeroportuaria debe estar contratado para revisar |
| 1.1.1-02 | 1.1.1-01 | FI | 0 | Obligatoria | Los ajustes responden a las observaciones de la revisión |
| 1.1.1-03 | 1.1.1-01 | II | 10 | Discrecional | La revisión BIM arranca con la revisión técnica avanzada |
| 1.1.1-03 | 1.1.1-02 | FF | 0 | Discrecional | La revisión BIM termina con los ajustes |
| 1.1.1-04 | 1.1.1-02 | FI | 0 | Obligatoria | Se aprueba el diseño ya ajustado |
| 1.1.1-04 | 1.1.1-03 | FI | 0 | Obligatoria | Se aprueba con el modelo BIM coordinado |
| 1.1.1-04 | 1.2.5-01 | FI | 0 | Discrecional | Accesibilidad verificada antes de aprobar (EDT 1.2.5) |
| 1.1.1-04 | 1.2.5-02 | FI | 0 | Discrecional | Metas EDGE verificadas antes de aprobar (EDT 1.2.5) |
| 1.1.1-05 | 1.1.1-04 | FI | 0 | Obligatoria | El BID revisa lo aprobado por CEPA (ROP anexo 7.1) |
| 1.1.1-06 | 3.4.1-12 | FI | 10 | Obligatoria | El contratista diseña desde la orden de inicio del contrato de obra |
| 1.1.1-07 | 1.1.1-06 | FI | 0 | Obligatoria | Se revisa el diseño terminado |
| 1.1.1-07 | 1.7.1-01 | FI | 0 | Obligatoria | La supervisión del diseño la hace la firma de supervisión de la terminal ya movilizada |
| 1.1.1-08 | 1.1.1-07 | FI | 0 | Obligatoria | Se aprueba el diseño revisado |
| 1.1.2-01 | 3.1.1-05 | FI | 0 | Obligatoria | Servicio contratado por la UEP |
| 1.1.2-02 | 1.1.1-01 | FI | 0 | Discrecional | Mismo especialista en ingeniería aeroportuaria: primero la terminal |
| 1.1.2-02 | 3.1.1-05 | FI | 0 | Obligatoria | El especialista en ingeniería aeroportuaria debe estar contratado |
| 1.1.2-03 | 1.1.2-02 | FI | 0 | Obligatoria | La AAC revisa la geometría ya revisada por CEPA |
| 1.1.2-04 | 1.1.2-01 | FI | 0 | Obligatoria | El sondeo alimenta el diseño de pavimentos |
| 1.1.2-04 | 1.1.2-03 | FI | 0 | Obligatoria | Se incorporan observaciones de la AAC |
| 1.1.2-05 | 1.1.2-04 | FI | 0 | Obligatoria | Se aprueba el diseño ajustado |
| 1.1.2-06 | 1.1.2-05 | FI | 0 | Obligatoria | El BID revisa lo aprobado por CEPA (ROP anexo 7.1) |
| 1.1.3-01 | 3.1.1-05 | FI | 0 | Obligatoria | El especialista en ingeniería aeroportuaria debe estar contratado |
| 1.1.3-02 | 1.1.3-01 | II | 10 | Discrecional | La revisión fotovoltaica arranca con la revisión técnica avanzada |
| 1.1.3-03 | 1.1.3-01 | FI | 0 | Obligatoria | Los ajustes responden a las observaciones |
| 1.1.3-03 | 1.1.3-02 | FI | 0 | Obligatoria | Los ajustes incluyen el sistema fotovoltaico |
| 1.1.3-04 | 1.1.3-03 | FI | 0 | Obligatoria | Se aprueba el diseño ajustado |
| 1.1.3-05 | 1.1.3-04 | FI | 0 | Obligatoria | El BID revisa lo aprobado por CEPA (ROP anexo 7.1) |
| 1.1.4-01 | 1.1.3-01 | FI | 0 | Discrecional | Mismo especialista en ingeniería aeroportuaria: primero el estacionamiento |
| 1.1.4-01 | 3.1.1-05 | FI | 0 | Obligatoria | El especialista en ingeniería aeroportuaria debe estar contratado |
| 1.1.4-02 | 1.1.4-01 | FI | 0 | Obligatoria | La AAC valida el diseño ya revisado |
| 1.1.4-03 | 1.1.4-02 | FI | 0 | Obligatoria | Se incorporan observaciones de la AAC |
| 1.1.4-04 | 1.1.4-03 | FI | 0 | Obligatoria | Se aprueba el diseño ajustado |
| 1.1.4-05 | 1.1.4-04 | FI | 0 | Obligatoria | El BID revisa lo aprobado por CEPA (ROP anexo 7.1) |
| 1.2.1-01 | 1.1.1-05 | FI | 0 | Obligatoria | Diseño aprobado antes de construir |
| 1.2.1-01 | 1.7.1-01 | II | 5 | Obligatoria | La supervisión debe estar movilizada antes de la orden de inicio |
| 1.2.1-01 | 1.7.3-02 | FI | 0 | Obligatoria | PGAS de construcción aprobado antes de movilizar |
| 1.2.1-01 | 3.3.1-06 | FI | 0 | Obligatoria | El contrato exige presentar el plan final previo al inicio de las obras (cláusula 4.06) |
| 1.2.1-01 | 3.3.2-04 | FI | 0 | Obligatoria | PP 4.6: protocolo aprobado antes de obras del lado aire |
| 1.2.1-01 | 3.4.1-12 | FI | 10 | Obligatoria | Garantías, anticipo y orden de inicio tras la firma |
| 1.2.1-01 | 3.4.2-12 | FI | 0 | Obligatoria | La firma de supervisión ocurre antes o junto con el inicio de su obra (EDT 3.4.2: firma en condiciones de iniciar con las obras) |
| 1.2.1-02 | 1.2.1-01 | FI | 0 | Obligatoria | Se cimenta con el sitio movilizado |
| 1.2.1-03 | 1.2.1-02 | II | 40 | Obligatoria | La estructura inicia al terminar las primeras zapatas |
| 1.2.1-04 | 1.2.1-03 | II | 95 | Obligatoria | La cubierta se monta al completar la losa del nivel 2 |
| 1.2.1-05 | 1.1.1-08 | FI | 0 | Obligatoria | Las fachadas se instalan con el diseño aprobado de la fachada sur |
| 1.2.1-05 | 1.2.1-04 | II | 30 | Obligatoria | Las fachadas inician con la cubierta montada en un frente |
| 1.2.2-01 | 1.2.1-04 | II | 40 | Obligatoria | Las divisiones inician bajo cubierta |
| 1.2.2-02 | 1.2.1-05 | II | 30 | Obligatoria | Acabados con la envolvente cerrada |
| 1.2.2-02 | 1.2.2-01 | II | 50 | Discrecional | Los acabados siguen las divisiones por frentes |
| 1.2.2-03 | 1.2.2-02 | FF | 5 | Obligatoria | La integración no termina antes que los acabados |
| 1.2.3-01 | 1.2.1-03 | II | 60 | Obligatoria | Redes por nivel con la estructura de ese nivel terminada |
| 1.2.3-01 | 1.2.2-01 | FF | 10 | Discrecional | Las redes terminan con las divisiones |
| 1.2.3-02 | 1.2.1-04 | FI | 0 | Obligatoria | Equipos en cuartos técnicos y cubierta ya cubiertos |
| 1.2.3-02 | 1.2.3-01 | II | 40 | Discrecional | Equipos tras avanzar las redes |
| 1.2.3-03 | 1.2.2-01 | FF | 20 | Obligatoria | Se completan una vez cerrados los cielos |
| 1.2.3-03 | 1.2.3-01 | II | 50 | Discrecional | Sistemas especiales tras avanzar las redes |
| 1.2.3-04 | 1.2.2-02 | II | 80 | Obligatoria | Pruebas con los acabados avanzados |
| 1.2.3-04 | 1.2.3-02 | FI | 0 | Obligatoria | Se prueba lo instalado |
| 1.2.3-04 | 1.2.3-03 | FI | 0 | Obligatoria | Se prueba lo instalado |
| 1.2.4-01 | 1.1.1-08 | FI | 0 | Obligatoria | Los planos de taller de los puentes de abordaje dependen del diseño aprobado de la fachada sur |
| 1.2.4-01 | 1.2.1-01 | FI | 30 | Obligatoria | Planos de taller con el contrato en marcha |
| 1.2.4-02 | 1.2.4-01 | FI | 0 | Obligatoria | Se fabrica con planos aprobados |
| 1.2.4-03 | 1.2.1-05 | FI | 0 | Obligatoria | Puentes conectados a una fachada terminada |
| 1.2.4-03 | 1.2.4-02 | FI | 0 | Obligatoria | Se instala lo entregado |
| 1.2.4-03 | 1.3.1-05 | FI | 0 | Obligatoria | Puentes sobre la plataforma de contacto pavimentada |
| 1.2.4-04 | 1.2.2-02 | FF | 25 | Obligatoria | Los equipos se instalan al cierre de los acabados |
| 1.2.4-05 | 1.2.3-04 | FI | 0 | Obligatoria | Equipos probados con las instalaciones en marcha |
| 1.2.4-05 | 1.2.4-03 | FI | 0 | Obligatoria | Se prueba lo instalado |
| 1.2.4-05 | 1.2.4-04 | FI | 0 | Obligatoria | Se prueba lo instalado |
| 1.2.4-06 | 1.2.2-03 | FI | 0 | Obligatoria | La terminal debe estar conectada con la Etapa 1 |
| 1.2.4-06 | 1.2.4-05 | FI | 0 | Obligatoria | Las pruebas integradas siguen a las pruebas de equipos |
| 1.2.4-06 | 1.2.5-03 | FI | 0 | Obligatoria | Accesibilidad verificada antes de operar |
| 1.2.4-06 | 1.2.5-04 | FI | 0 | Obligatoria | Evidencias de eficiencia reunidas |
| 1.2.4-06 | 1.3.1-06 | FI | 0 | Obligatoria | Servicios de la plataforma de contacto listos |
| 1.2.5-01 | 1.1.1-02 | FI | 0 | Obligatoria | Se verifica el diseño ajustado |
| 1.2.5-02 | 1.1.1-02 | FI | 0 | Obligatoria | Se verifica el diseño ajustado |
| 1.2.5-03 | 1.2.2-01 | II | 30 | Discrecional | Verificación por frentes |
| 1.2.5-03 | 1.2.5-05 | FF | 5 | Obligatoria | Se verifica al terminar la construcción de los recorridos y los espacios |
| 1.2.5-04 | 1.2.3-04 | FF | 5 | Obligatoria | Se verifica con las instalaciones en marcha |
| 1.2.5-04 | 1.2.5-06 | FI | 0 | Obligatoria | Se verifican las medidas ya instaladas |
| 1.2.5-05 | 1.2.2-01 | II | 30 | Discrecional | Se construyen por frentes al avanzar las divisiones y los cielos |
| 1.2.5-05 | 1.2.2-02 | FF | 5 | Obligatoria | Los recorridos terminan con los acabados de los pasillos y las salas |
| 1.2.5-05 | 1.2.5-01 | FI | 0 | Obligatoria | Los recorridos se construyen según el diseño verificado |
| 1.2.5-06 | 1.2.1-05 | FI | 0 | Obligatoria | El control solar y el aislamiento se instalan sobre las fachadas ya montadas |
| 1.2.5-06 | 1.2.3-02 | II | 20 | Discrecional | Iluminación, griferías y controles se instalan con los equipos de las instalaciones |
| 1.2.5-06 | 1.2.5-02 | FI | 0 | Obligatoria | Se instalan las medidas del diseño verificado |
| 1.3.1-01 | 1.1.2-06 | FI | 0 | Obligatoria | Diseño aprobado antes de construir |
| 1.3.1-01 | 1.7.2-01 | II | 5 | Obligatoria | La supervisión debe estar movilizada antes de la orden de inicio |
| 1.3.1-01 | 1.7.3-04 | FI | 0 | Obligatoria | PGAS de construcción aprobado antes de movilizar |
| 1.3.1-01 | 3.3.1-06 | FI | 0 | Obligatoria | El contrato exige presentar el plan final previo al inicio de las obras (cláusula 4.06) |
| 1.3.1-01 | 3.3.2-04 | FI | 0 | Obligatoria | PP 4.6: protocolo aprobado antes de obras del lado aire |
| 1.3.1-01 | 3.4.1-24 | FI | 10 | Obligatoria | Garantías, anticipo y orden de inicio tras la firma |
| 1.3.1-01 | 3.4.2-24 | FI | 0 | Obligatoria | La firma de supervisión ocurre antes o junto con el inicio de su obra (EDT 3.4.2: firma en condiciones de iniciar con las obras) |
| 1.3.1-02 | 1.3.1-01 | FI | 0 | Obligatoria | Obra tras movilizar |
| 1.3.1-03 | 1.3.1-02 | FI | 0 | Obligatoria | Pavimento sobre la base terminada |
| 1.3.1-04 | 1.3.1-03 | FI | 5 | Obligatoria | Fase 2 solo cuando la fase 1 reabre a las aeronaves |
| 1.3.1-05 | 1.3.1-04 | FI | 0 | Obligatoria | Pavimento sobre la base terminada |
| 1.3.1-06 | 1.3.1-05 | FF | 5 | Obligatoria | Los servicios no terminan antes que el pavimento |
| 1.3.2-01 | 1.3.1-01 | FI | 0 | Obligatoria | Contratista ya movilizado |
| 1.3.2-01 | 1.6.2-04 | FI | 0 | Obligatoria | PP 4.6: SSEI reubicado y operando antes de obras en la plataforma remota |
| 1.3.2-02 | 1.3.2-01 | FI | 0 | Obligatoria | Terracería sobre la huella despejada |
| 1.3.2-03 | 1.3.2-02 | II | 20 | Discrecional | Drenaje en paralelo con la terracería |
| 1.3.2-04 | 1.3.2-02 | FI | 0 | Obligatoria | Pavimento sobre la base terminada |
| 1.3.2-04 | 1.3.2-03 | FI | 0 | Obligatoria | Pavimento con el drenaje terminado |
| 1.3.2-05 | 1.3.2-04 | FF | 5 | Obligatoria | Los márgenes no terminan antes que el concreto |
| 1.3.3-01 | 1.3.1-05 | FF | 20 | Obligatoria | Las luces terminan tras el pavimento de la fase 2 |
| 1.3.3-02 | 1.3.2-04 | FF | 10 | Obligatoria | Las luces terminan tras el pavimento |
| 1.3.3-03 | 1.3.1-05 | FI | 25 | Obligatoria | Curado del concreto de 28 días antes de pintar |
| 1.3.3-03 | 1.3.2-05 | FI | 0 | Obligatoria | La pintura va tras el pavimento |
| 1.3.3-04 | 1.3.3-01 | FI | 0 | Obligatoria | Se prueba lo instalado |
| 1.3.3-04 | 1.3.3-02 | FI | 0 | Obligatoria | Se prueba lo instalado |
| 1.3.3-04 | 1.3.3-03 | FI | 0 | Obligatoria | Se prueba lo instalado |
| 1.3.3-05 | 1.3.3-04 | FI | 0 | Obligatoria | La AAC autoriza lo probado |
| 1.4.1-01 | 1.3.1-01 | FI | 0 | Obligatoria | Mismo contratista ya movilizado |
| 1.4.1-01 | 1.3.1-03 | FI | 0 | Discrecional | Un segundo frente solo tras reabrir la fase 1 de la plataforma |
| 1.4.1-02 | 1.4.1-01 | FI | 0 | Obligatoria | Pavimento sobre la base terminada |
| 1.4.1-03 | 1.4.1-02 | II | 20 | Discrecional | Intersección con Alfa al avanzar el pavimento |
| 1.4.2-01 | 1.4.1-02 | II | 10 | Discrecional | Ductos y luces al avanzar el pavimento |
| 1.4.2-01 | 1.4.1-03 | FI | 0 | Obligatoria | Luces de la intersección tras construirla |
| 1.4.2-02 | 1.4.1-03 | FI | 0 | Obligatoria | La pintura va tras el pavimento |
| 1.4.2-03 | 1.4.2-01 | FI | 0 | Obligatoria | Se prueba lo instalado |
| 1.4.2-03 | 1.4.2-02 | FI | 0 | Obligatoria | Se prueba lo instalado |
| 1.4.2-04 | 1.4.2-03 | FI | 0 | Obligatoria | La AAC autoriza lo probado |
| 1.5.1-01 | 1.1.3-05 | FI | 0 | Obligatoria | Diseño aprobado antes de construir |
| 1.5.1-01 | 1.7.1-03 | II | 5 | Obligatoria | La supervisión debe estar movilizada antes de la orden de inicio |
| 1.5.1-01 | 1.7.3-01 | FI | 0 | Obligatoria | PGAS de construcción aprobado antes de movilizar |
| 1.5.1-01 | 3.3.1-06 | FI | 0 | Obligatoria | El contrato exige presentar el plan final previo al inicio de las obras (cláusula 4.06) |
| 1.5.1-01 | 3.4.1-06 | FI | 10 | Obligatoria | Garantías, anticipo y orden de inicio tras la firma |
| 1.5.1-01 | 3.4.2-06 | FI | 0 | Obligatoria | La firma de supervisión ocurre antes o junto con el inicio de su obra (EDT 3.4.2: firma en condiciones de iniciar con las obras) |
| 1.5.1-02 | 1.5.1-01 | FI | 0 | Obligatoria | Se cimenta con el sitio movilizado |
| 1.5.1-03 | 1.5.1-02 | II | 30 | Obligatoria | La estructura inicia al terminar las primeras zapatas |
| 1.5.1-04 | 1.5.1-03 | II | 85 | Obligatoria | Niveles superiores al completar zonas de los niveles 1 y 2 |
| 1.5.1-05 | 1.5.1-03 | II | 55 | Discrecional | Instalaciones por nivel tras la estructura de ese nivel |
| 1.5.1-05 | 1.5.1-04 | FF | 15 | Obligatoria | Las redes terminan tras la estructura |
| 1.5.1-06 | 1.5.1-04 | II | 45 | Discrecional | Acabados por nivel tras la estructura |
| 1.5.1-06 | 1.5.1-05 | FF | 15 | Obligatoria | Los acabados terminan tras las redes |
| 1.5.2-01 | 1.5.1-06 | II | 15 | Discrecional | Equipos de acceso cuando los niveles inferiores están listos |
| 1.5.2-02 | 1.5.1-06 | II | 10 | Discrecional | Áreas de alquiler cuando el nivel de calle está listo |
| 1.5.2-03 | 1.5.2-01 | FI | 0 | Obligatoria | Se prueba lo instalado |
| 1.5.2-03 | 1.5.2-02 | FI | 0 | Obligatoria | Se prueba lo habilitado |
| 1.5.3-01 | 1.5.1-01 | II | 60 | Discrecional | El trámite se gestiona con el contrato ya en marcha |
| 1.5.3-02 | 1.5.1-04 | II | 50 | Obligatoria | Paneles cuando la cubierta superior tiene losa |
| 1.5.3-02 | 1.5.1-06 | FF | 5 | Discrecional | Los paneles se terminan con los acabados |
| 1.5.3-03 | 1.5.3-02 | FF | 10 | Obligatoria | Terminan tras los paneles |
| 1.5.3-04 | 1.5.1-06 | FI | 0 | Obligatoria | Se entrega con el edificio terminado |
| 1.5.3-04 | 1.5.2-03 | FI | 0 | Obligatoria | Se entrega con los sistemas de acceso probados |
| 1.5.3-04 | 1.5.3-01 | FI | 0 | Externa | No se energiza sin autorización de interconexión |
| 1.5.3-04 | 1.5.3-03 | FI | 0 | Obligatoria | Se prueba lo instalado |
| 1.6.1-01 | 1.1.4-05 | FI | 0 | Obligatoria | Diseño aprobado antes de construir |
| 1.6.1-01 | 1.7.2-03 | II | 5 | Obligatoria | La supervisión debe estar movilizada antes de la orden de inicio |
| 1.6.1-01 | 1.7.3-03 | FI | 0 | Obligatoria | PGAS de construcción aprobado antes de movilizar |
| 1.6.1-01 | 3.3.1-06 | FI | 0 | Obligatoria | El contrato exige presentar el plan final previo al inicio de las obras (cláusula 4.06) |
| 1.6.1-01 | 3.3.2-04 | FI | 0 | Obligatoria | PP 4.6: protocolo aprobado antes de obras del lado aire (vías de salida a la plataforma) |
| 1.6.1-01 | 3.4.1-18 | FI | 10 | Obligatoria | Garantías, anticipo y orden de inicio tras la firma |
| 1.6.1-01 | 3.4.2-18 | FI | 0 | Obligatoria | La firma de supervisión ocurre antes o junto con el inicio de su obra (EDT 3.4.2: firma en condiciones de iniciar con las obras) |
| 1.6.1-02 | 1.6.1-01 | FI | 0 | Obligatoria | Se construye con el sitio movilizado |
| 1.6.1-03 | 1.6.1-02 | II | 30 | Discrecional | Cubierta al avanzar la estructura |
| 1.6.1-04 | 1.6.1-02 | II | 20 | Discrecional | Vías con un segundo frente |
| 1.6.1-05 | 1.6.1-03 | FI | -10 | Discrecional | Acabados al cerrar la cubierta |
| 1.6.1-05 | 1.6.1-04 | FI | 0 | Obligatoria | Probar con vías de salida construidas |
| 1.6.2-01 | 1.6.1-03 | II | 0 | Discrecional | Planificar el traslado con la obra avanzada |
| 1.6.2-02 | 1.6.2-01 | FI | 0 | Externa | La AAC revisa el plan presentado |
| 1.6.2-03 | 1.6.2-02 | FI | 0 | Externa | Traslado con cobertura conforme de la AAC |
| 1.6.2-03 | 1.6.2-06 | FI | 0 | Obligatoria | El traslado requiere el equipamiento probado |
| 1.6.2-03 | 1.7.4-04 | FI | 0 | Obligatoria | El traslado requiere el edificio recibido |
| 1.6.2-04 | 1.6.2-03 | FI | 0 | Obligatoria | Se prueba tras trasladar |
| 1.6.2-05 | 1.6.1-05 | II | 20 | Discrecional | El equipamiento se instala al avanzar los acabados y los sistemas del edificio |
| 1.6.2-06 | 1.6.1-05 | FI | 0 | Obligatoria | Se prueba con el edificio ya probado |
| 1.6.2-06 | 1.6.2-05 | FI | 0 | Obligatoria | Se prueba lo instalado |
| 1.7.1-01 | 3.4.2-12 | FI | 0 | Obligatoria | La supervisión se moviliza tras firmar |
| 1.7.1-02 | 1.7.1-01 | FI | 0 | Obligatoria | Supervisión tras movilizar |
| 1.7.1-03 | 3.4.2-06 | FI | 0 | Obligatoria | La supervisión se moviliza tras firmar |
| 1.7.1-04 | 1.7.1-03 | FI | 0 | Obligatoria | Supervisión tras movilizar |
| 1.7.1-05 | 1.7.4-05 | FI | 0 | Obligatoria | El informe final de la supervisión incluye la recepción definitiva y los planos de obra ejecutada |
| 1.7.1-06 | 1.7.4-06 | FI | 0 | Obligatoria | El informe final de la supervisión incluye la recepción definitiva y los planos de obra ejecutada |
| 1.7.2-01 | 3.4.2-24 | FI | 0 | Obligatoria | La supervisión se moviliza tras firmar |
| 1.7.2-02 | 1.7.2-01 | FI | 0 | Obligatoria | Supervisión tras movilizar |
| 1.7.2-03 | 3.4.2-18 | FI | 0 | Obligatoria | La supervisión se moviliza tras firmar |
| 1.7.2-04 | 1.7.2-03 | FI | 0 | Obligatoria | Supervisión tras movilizar |
| 1.7.2-05 | 1.7.4-07 | FI | 0 | Obligatoria | El informe final de la supervisión incluye la recepción definitiva y los planos de obra ejecutada |
| 1.7.2-06 | 1.7.4-08 | FI | 0 | Obligatoria | El informe final de la supervisión incluye la recepción definitiva y los planos de obra ejecutada |
| 1.7.3-01 | 3.3.1-04 | FI | 0 | Obligatoria | El SGAS rige los PGAS de construcción |
| 1.7.3-01 | 3.4.1-06 | FI | 0 | Obligatoria | El contratista presenta su PGAS tras firmar |
| 1.7.3-02 | 3.3.1-04 | FI | 0 | Obligatoria | El SGAS rige los PGAS de construcción |
| 1.7.3-02 | 3.4.1-12 | FI | 0 | Obligatoria | El contratista presenta su PGAS tras firmar |
| 1.7.3-03 | 3.3.1-04 | FI | 0 | Obligatoria | El SGAS rige los PGAS de construcción |
| 1.7.3-03 | 3.4.1-18 | FI | 0 | Obligatoria | El contratista presenta su PGAS tras firmar |
| 1.7.3-04 | 3.3.1-04 | FI | 0 | Obligatoria | El SGAS rige los PGAS de construcción |
| 1.7.3-04 | 3.4.1-24 | FI | 0 | Obligatoria | El contratista presenta su PGAS tras firmar |
| 1.7.3-05 | 1.7.3-01 | FI | 0 | Obligatoria | Seguimiento desde el primer PGAS aprobado |
| 1.7.3-06 | 1.7.4-01 | FI | 0 | Obligatoria | Cierre tras las recepciones provisionales |
| 1.7.3-06 | 1.7.4-02 | FI | 0 | Obligatoria | Cierre tras las recepciones provisionales |
| 1.7.3-06 | 1.7.4-03 | FI | 0 | Obligatoria | Cierre tras las recepciones provisionales |
| 1.7.3-06 | 1.7.4-04 | FI | 0 | Obligatoria | Cierre tras las recepciones provisionales |
| 1.7.4-01 | 1.2.4-06 | FI | 0 | Obligatoria | Se recibe la obra terminada |
| 1.7.4-01 | 1.3.3-05 | FI | 0 | Obligatoria | La terminal opera con las plataformas autorizadas |
| 1.7.4-02 | 1.5.3-04 | FI | 0 | Obligatoria | Se recibe la obra terminada |
| 1.7.4-03 | 1.3.3-05 | FI | 0 | Obligatoria | Se recibe la obra terminada |
| 1.7.4-03 | 1.4.2-04 | FI | 0 | Obligatoria | Se recibe la obra terminada |
| 1.7.4-04 | 1.6.1-05 | FI | 0 | Obligatoria | Se recibe la obra terminada |
| 1.7.4-05 | 1.7.4-01 | FI | 0 | Obligatoria | La recepción definitiva sigue a la provisional y a la lista de pendientes del mismo contrato |
| 1.7.4-06 | 1.7.4-02 | FI | 0 | Obligatoria | La recepción definitiva sigue a la provisional y a la lista de pendientes del mismo contrato |
| 1.7.4-07 | 1.7.4-03 | FI | 0 | Obligatoria | La recepción definitiva sigue a la provisional y a la lista de pendientes del mismo contrato |
| 1.7.4-08 | 1.7.4-04 | FI | 0 | Obligatoria | La recepción definitiva sigue a la provisional y a la lista de pendientes del mismo contrato |
| 2.1-01 | 3.4.3-08 | FI | 0 | Obligatoria | Contractual: el consultor inicia con el contrato firmado |
| 2.1-02 | 2.1-01 | FI | 0 | Obligatoria | El diagnóstico sigue al plan de trabajo aprobado |
| 2.1-03 | 2.1-02 | FI | 0 | Obligatoria | La propuesta parte del diagnóstico |
| 2.1-04 | 2.1-03 | FI | 0 | Obligatoria | Se revisa el borrador entregado |
| 2.1-05 | 2.1-04 | FI | 0 | Obligatoria | Se incorporan las observaciones recibidas |
| 2.1-06 | 2.1-05 | FI | 0 | Obligatoria | Se aprueba la versión final entregada |
| 2.2.1-01 | 3.4.3-14 | FI | 0 | Obligatoria | Contractual: el consultor inicia con el contrato firmado |
| 2.2.1-02 | 2.2.1-01 | FI | 0 | Obligatoria | El inventario sigue al plan de trabajo |
| 2.2.1-03 | 2.1-03 | FI | 0 | Discrecional | El borrador del plan estratégico orienta las alternativas del Plan Maestro; se acepta el borrador y no la aprobación para no frenar el plan maestro |
| 2.2.1-03 | 2.2.1-02 | FI | 0 | Obligatoria | Los requerimientos y alternativas parten del diagnóstico y la demanda |
| 2.2.1-04 | 2.2.1-03 | FI | 0 | Obligatoria | Se revisa el borrador entregado |
| 2.2.1-05 | 2.2.1-04 | FI | 0 | Obligatoria | Se incorporan las observaciones recibidas |
| 2.2.1-05 | 2.4-05 | FI | 0 | Discrecional | El informe final de conectividad aporta recomendaciones utilizables en el Plan Maestro (ToC y EDT 5.2, 2.4) |
| 2.2.1-06 | 2.1-06 | FF | 10 | Discrecional | El Plan Maestro no se aprueba antes que el plan estratégico que lo orienta; 10 dl para alinear su texto con el plan aprobado |
| 2.2.1-06 | 2.2.1-05 | FI | 0 | Obligatoria | Se aprueba la versión final entregada |
| 2.2.2-01 | 2.2.1-03 | FI | 0 | Discrecional | El programa se diseña cuando el borrador del Plan Maestro ya define su contenido |
| 2.2.2-02 | 2.2.1-06 | FI | 0 | Obligatoria | La capacitación se centra en implementar el Plan Maestro aprobado (MEL R2.1) |
| 2.2.2-02 | 2.2.2-01 | FI | 0 | Obligatoria | Los cursos requieren el programa y la lista de participantes |
| 2.2.2-03 | 2.2.2-02 | FI | 0 | Obligatoria | Se evalúa al terminar los cursos |
| 2.2.2-04 | 2.2.2-03 | FI | 0 | Obligatoria | Se certifica a quienes aprueban la evaluación |
| 2.3.1-01 | 3.4.3-19 | FI | 0 | Obligatoria | Contractual: el consultor inicia con el contrato firmado |
| 2.3.1-02 | 2.3.1-01 | FI | 0 | Obligatoria | El diagnóstico sigue al plan de trabajo |
| 2.3.1-03 | 2.3.1-02 | FI | 0 | Obligatoria | La estrategia parte del diagnóstico |
| 2.3.1-04 | 2.3.1-03 | FI | 0 | Obligatoria | Se revisa el borrador entregado |
| 2.3.1-05 | 2.3.1-04 | FI | 0 | Obligatoria | Se incorporan las observaciones recibidas |
| 2.3.1-06 | 2.3.1-05 | FI | 0 | Obligatoria | Se aprueba la versión final entregada |
| 2.3.2-01 | 2.3.1-05 | FI | 0 | Discrecional | El programa se prepara con la estrategia final entregada |
| 2.3.2-02 | 2.3.1-06 | FI | 0 | Obligatoria | La capacitación aplica la estrategia BIM ya aprobada (EDT 5.2, 2.3.2) |
| 2.3.2-02 | 2.3.2-01 | FI | 0 | Obligatoria | Los cursos requieren programa y materiales |
| 2.3.2-03 | 2.3.2-02 | FI | 0 | Obligatoria | Se evalúa al terminar los cursos |
| 2.3.2-04 | 2.3.2-03 | FI | 0 | Obligatoria | El registro se entrega con las evaluaciones |
| 2.4-01 | 3.4.3-25 | FI | 0 | Obligatoria | Contractual: el consultor inicia con el contrato firmado |
| 2.4-02 | 2.4-01 | FI | 0 | Obligatoria | El diagnóstico sigue al plan de trabajo |
| 2.4-03 | 2.4-02 | FI | 0 | Obligatoria | Las alternativas parten del diagnóstico |
| 2.4-04 | 2.4-03 | FI | 0 | Obligatoria | Se revisa el borrador entregado |
| 2.4-05 | 2.4-04 | FI | 0 | Obligatoria | Se incorporan las observaciones recibidas |
| 2.4-06 | 2.4-05 | FI | 0 | Obligatoria | Se aprueba la versión final entregada |
| 2.5-01 | 3.4.3-30 | FI | 0 | Obligatoria | Contractual: el consultor inicia con el contrato firmado |
| 2.5-02 | 2.5-01 | FI | 0 | Obligatoria | El diagnóstico sigue al plan de trabajo |
| 2.5-03 | 2.5-02 | FI | 0 | Obligatoria | El análisis de mercados parte del diagnóstico |
| 2.5-04 | 2.5-03 | FI | 0 | Obligatoria | Se revisa el borrador entregado |
| 2.5-05 | 2.5-04 | FI | 0 | Obligatoria | Se incorporan las observaciones recibidas |
| 2.5-06 | 2.5-05 | FI | 0 | Obligatoria | Se aprueba la versión final entregada |
| 2.6.1-01 | 1.1.1-05 | FI | 0 | Obligatoria | La autoevaluación EDGE se hace sobre el diseño aprobado de la terminal |
| 2.6.1-01 | 1.1.3-05 | FI | 0 | Obligatoria | La autoevaluación EDGE se hace sobre el diseño aprobado del estacionamiento |
| 2.6.1-01 | 3.4.3-35 | FI | 0 | Obligatoria | Contractual: el auditor inicia con el contrato firmado |
| 2.6.1-02 | 2.6.1-01 | FI | 0 | Obligatoria | EDGE-P 6.2: la auditoría de diseño parte de la autoevaluación y el registro |
| 2.6.1-03 | 2.6.1-02 | FI | 0 | Discrecional | El acompañamiento en obra parte del certificado preliminar |
| 2.6.1-04 | 1.2.4-06 | FI | 0 | Obligatoria | EDGE-P 6.3: el auditor verifica medidas instaladas en el edificio terminado |
| 2.6.1-04 | 1.5.3-04 | FI | 0 | Obligatoria | EDGE-P 6.3: el auditor verifica medidas instaladas en el edificio terminado |
| 2.6.1-04 | 2.6.1-03 | FI | 0 | Obligatoria | La auditoría en sitio sigue al acompañamiento |
| 2.6.1-05 | 2.6.1-04 | FI | 0 | Obligatoria | La revisión del proveedor sigue a la auditoría en sitio |
| 2.6.1-06 | 2.6.1-05 | FI | 0 | Obligatoria | El certificado se emite tras la revisión del proveedor |
| 2.6.2-01 | 2.6.1-02 | FI | 0 | Discrecional | El material se prepara con los criterios EDGE ya verificados en el diseño |
| 2.6.2-02 | 2.6.1-04 | FI | 0 | Discrecional | El curso se imparte con las medidas ya verificadas en sitio como caso real |
| 2.6.2-02 | 2.6.2-01 | FI | 0 | Obligatoria | Los cursos requieren programa y materiales |
| 2.6.2-03 | 2.6.2-02 | FI | 0 | Obligatoria | Se evalúa al terminar el curso |
| 2.6.2-04 | 2.6.2-03 | FI | 0 | Obligatoria | El registro se entrega con las evaluaciones |
| 2.7-01 | 3.4.3-40 | FI | 0 | Obligatoria | Contractual: el consultor inicia con el contrato firmado |
| 2.7-02 | 2.7-01 | FI | 0 | Obligatoria | El diagnóstico sigue al plan de trabajo |
| 2.7-03 | 1.1.1-05 | FI | 0 | Obligatoria | La separación de flujos en la terminal antigua debe ser compatible con el diseño aprobado de la nueva terminal |
| 2.7-03 | 2.7-02 | FI | 0 | Obligatoria | Las intervenciones parten del diagnóstico |
| 2.7-04 | 2.7-03 | FI | 0 | Obligatoria | Se revisa el borrador entregado |
| 2.7-05 | 2.7-04 | FI | 0 | Obligatoria | Se incorporan las observaciones recibidas |
| 2.7-06 | 2.7-05 | FI | 0 | Obligatoria | Se aprueba la versión final entregada |
| 2.8-01 | 3.4.3-45 | FI | 0 | Obligatoria | Contractual: el consultor inicia con el contrato firmado |
| 2.8-02 | 2.8-01 | FI | 0 | Obligatoria | El diagnóstico sigue al plan de trabajo |
| 2.8-03 | 1.1.3-05 | FI | 0 | Obligatoria | El estudio enfatiza el acceso al nuevo estacionamiento, cuyo diseño aprobado fija accesos y circulaciones |
| 2.8-03 | 2.8-02 | FI | 0 | Obligatoria | Las medidas parten del diagnóstico |
| 2.8-04 | 2.8-03 | FI | 0 | Obligatoria | Se revisa el borrador entregado |
| 2.8-05 | 2.8-04 | FI | 0 | Obligatoria | Se incorporan las observaciones recibidas |
| 2.8-06 | 2.8-05 | FI | 0 | Obligatoria | Se aprueba la versión final entregada |
| 2.9-01 | 3.4.3-50 | FI | 0 | Obligatoria | Contractual: el consultor inicia con el contrato firmado |
| 2.9-02 | 2.9-01 | FI | 0 | Obligatoria | La primera cohorte requiere el programa y los materiales |
| 2.9-03 | 2.9-02 | II | 260 | Discrecional | MEL: metas anuales de 100 funcionarios (una cohorte cada año de 260 dl) |
| 2.9-04 | 2.9-03 | II | 260 | Discrecional | MEL: metas anuales de 100 funcionarios (una cohorte cada año de 260 dl) |
| 2.9-05 | 2.9-04 | FI | 0 | Obligatoria | Las constancias de los 300 se emiten al terminar la última cohorte |
| 2.9-06 | 2.9-05 | FI | 0 | Obligatoria | Se aprueba el informe final entregado |
| 3.1.1-01 | 3.4.4-05 | FI | 0 | Obligatoria | Contrato 3CV firmado antes de que el consultor inicie |
| 3.1.1-02 | 3.4.4-05 | FI | 0 | Obligatoria | Contrato 3CV firmado antes de que el consultor inicie |
| 3.1.1-03 | 3.4.4-05 | FI | 0 | Obligatoria | Contrato 3CV firmado antes de que el consultor inicie |
| 3.1.1-04 | 3.1.1-01 | FI | 0 | Obligatoria | Firmas autorizadas incluyen al Coordinador |
| 3.1.1-05 | 3.1.1-01 | FI | 0 | Obligatoria | El expediente cubre los siete puestos y las firmas |
| 3.1.1-05 | 3.1.1-02 | FI | 0 | Obligatoria | El expediente cubre los siete puestos y las firmas |
| 3.1.1-05 | 3.1.1-03 | FI | 0 | Obligatoria | El expediente cubre los siete puestos y las firmas |
| 3.1.1-05 | 3.1.1-04 | FI | 0 | Obligatoria | El expediente cubre los siete puestos y las firmas |
| 3.1.1-06 | 3.1.1-01 | II | 0 | Obligatoria | La administración del programa empieza con la incorporación real del personal clave |
| 3.1.2-01 | 3.1.1-01 | FI | 0 | Obligatoria | Coordinador en funciones |
| 3.1.2-01 | 3.3.1-01 | FI | 0 | Obligatoria | El ROP lleva el SGAS ajustado como anexo |
| 3.1.2-02 | 3.1.2-01 | FI | 0 | Externa | No objeción del BID sobre el texto ajustado |
| 3.1.2-03 | 3.1.2-02 | FI | 0 | Obligatoria | CEPA aprueba con la no objeción |
| 3.1.3-01 | 3.1.1-05 | FI | 0 | Discrecional | La UEP conformada redacta el convenio en paralelo con el ROP |
| 3.1.3-02 | 3.1.3-01 | FI | 0 | Externa | No objeción del BID |
| 3.1.3-03 | 3.1.3-02 | FI | 0 | Obligatoria | Se suscribe el texto aceptado |
| 3.1.4-01 | 3.1.1-04 | FI | 0 | Obligatoria | Firmas autorizadas necesarias para abrir la cuenta |
| 3.1.4-02 | 3.1.4-01 | FI | 0 | Obligatoria | Se abre tras la solicitud |
| 3.1.4-03 | 3.1.4-02 | FI | 0 | Obligatoria | Se registra la cuenta abierta |
| 3.2.1-01 | 3.1.1-01 | FI | 0 | Obligatoria | Especialista de planificación en funciones |
| 3.2.1-02 | 3.2.1-01 | FI | 0 | Obligatoria | Se integra sobre el PEP actualizado |
| 3.2.1-02 | 3.2.3-02 | FI | 0 | Obligatoria | Requiere el PA aprobado |
| 3.2.1-03 | 3.2.1-02 | FI | 0 | Obligatoria | Se aprueba el PEP completo |
| 3.2.2-01 | 3.2.1-03 | FI | 0 | Obligatoria | El POA se deriva del PEP aprobado |
| 3.2.2-02 | 3.2.2-01 | FI | 0 | Obligatoria | Se aprueba el POA elaborado |
| 3.2.2-03 | 3.2.2-02 | FI | 0 | Discrecional | El siguiente POA parte del anterior aprobado |
| 3.2.2-04 | 3.2.2-03 | FI | 0 | Obligatoria | Se aprueba el POA elaborado |
| 3.2.2-05 | 3.2.2-04 | FI | 0 | Discrecional | El siguiente POA parte del anterior aprobado |
| 3.2.2-06 | 3.2.2-05 | FI | 0 | Obligatoria | Se aprueba el POA elaborado |
| 3.2.2-07 | 3.2.2-06 | FI | 0 | Discrecional | El siguiente POA parte del anterior aprobado |
| 3.2.2-08 | 3.2.2-07 | FI | 0 | Obligatoria | Se aprueba el POA elaborado |
| 3.2.3-02 | 3.2.3-01 | FI | 0 | Obligatoria | El BID revisa el plan ya elaborado |
| 3.2.3-03 | 3.2.3-02 | FI | 0 | Obligatoria | Se actualiza sobre la versión aprobada |
| 3.2.3-04 | 3.2.3-03 | FI | 0 | Obligatoria | Revisión del BID sobre el plan actualizado |
| 3.2.3-05 | 3.2.3-04 | FI | 0 | Obligatoria | Se actualiza tras la última versión aprobada |
| 3.2.3-06 | 3.2.3-02 | FI | 0 | Obligatoria | El aviso general resume el Plan de Adquisiciones aprobado |
| 3.3.1-01 | 3.1.1-03 | FI | 0 | Obligatoria | Especialista socioambiental en funciones |
| 3.3.1-02 | 3.3.1-01 | FI | 0 | Obligatoria | Procedimientos sobre el SGAS ajustado |
| 3.3.1-03 | 3.3.1-02 | FI | 0 | Externa | No objeción del BID sobre los instrumentos terminados |
| 3.3.1-04 | 3.1.2-03 | FI | 0 | Obligatoria | Se anexan al ROP ya aprobado |
| 3.3.1-04 | 3.3.1-03 | FI | 0 | Obligatoria | Se incorporan los instrumentos con no objeción |
| 3.3.1-05 | 1.1.1-05 | FI | 0 | Obligatoria | El plan final se elabora con los diseños aprobados de las obras |
| 3.3.1-05 | 1.1.2-06 | FI | 0 | Obligatoria | El plan final se elabora con los diseños aprobados de las obras |
| 3.3.1-05 | 1.1.3-05 | FI | 0 | Obligatoria | El plan final se elabora con los diseños aprobados de las obras |
| 3.3.1-05 | 1.1.4-05 | FI | 0 | Obligatoria | El plan final se elabora con los diseños aprobados de las obras |
| 3.3.1-05 | 3.3.1-04 | FI | 0 | Obligatoria | El plan se integra al sistema de gestión ambiental y social vigente |
| 3.3.1-06 | 3.3.1-05 | FI | 0 | Obligatoria | Se presenta el plan terminado |
| 3.3.2-01 | 1.1.2-06 | FI | 0 | Obligatoria | El riesgo y las fases dependen de la geometría del lado aire (EDT 1.1.2) |
| 3.3.2-01 | 3.3.1-04 | FI | 0 | Obligatoria | El protocolo se apoya en el SGAS vigente |
| 3.3.2-02 | 3.3.2-01 | FI | 0 | Obligatoria | El protocolo recoge el análisis de riesgo |
| 3.3.2-03 | 3.3.2-02 | FI | 0 | Obligatoria | Se presenta el protocolo terminado |
| 3.3.2-04 | 3.3.2-03 | FI | 0 | Externa | Aprobación de la AAC |
| 3.3.3-01 | 3.3.1-04 | FI | 0 | Obligatoria | El mecanismo es parte del SGAS vigente |
| 3.3.3-02 | 3.3.3-01 | FI | 0 | Obligatoria | Se instala el procedimiento diseñado |
| 3.3.3-03 | 3.3.3-02 | FI | 0 | Obligatoria | Se opera el mecanismo instalado |
| 3.3.4-01 | 3.3.1-04 | FI | 0 | Obligatoria | El informe se basa en el SGAS vigente |
| 3.3.4-02 | 1.5.1-01 | II | 0 | Obligatoria | Los informes comienzan con la primera obra |
| 3.3.4-02 | 3.3.4-01 | FI | 0 | Obligatoria | Formato acordado |
| 3.3.4-03 | 1.7.4-05 | FI | 0 | Obligatoria | Requiere las cuatro obras recibidas |
| 3.3.4-03 | 1.7.4-06 | FI | 0 | Obligatoria | Requiere las cuatro obras recibidas |
| 3.3.4-03 | 1.7.4-07 | FI | 0 | Obligatoria | Requiere las cuatro obras recibidas |
| 3.3.4-03 | 1.7.4-08 | FI | 0 | Obligatoria | Requiere las cuatro obras recibidas |
| 3.3.4-03 | 3.3.4-02 | FI | 0 | Obligatoria | El informe final cierra la serie semestral |
| 3.4.1-01 | 1.1.3-05 | FF | 0 | Discrecional | Los documentos se preparan en paralelo con la revisión del diseño y cierran con su aprobación |
| 3.4.1-01 | 3.1.1-02 | FI | 0 | Obligatoria | Especialista de adquisiciones en funciones |
| 3.4.1-01 | 3.2.3-02 | FI | 0 | Obligatoria | El proceso debe estar en el PA aprobado (ROP anexo 7.1 paso 3) |
| 3.4.1-02 | 3.3.1-04 | FI | 0 | Obligatoria | Documentos con cláusulas del SGAS (contrato cláusula 4.06(d)) |
| 3.4.1-02 | 3.4.1-01 | FI | 0 | Obligatoria | Documentos completos antes de enviarlos |
| 3.4.1-03 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige el proceso |
| 3.4.1-03 | 3.2.3-06 | FI | 0 | Obligatoria | Todo aviso específico y toda solicitud de expresiones de interés siguen al Aviso General de Adquisiciones (GN-2349-15 y GN-2350-15) |
| 3.4.1-03 | 3.4.1-02 | FI | 0 | Externa | Publicación tras no objeción del BID |
| 3.4.1-04 | 3.4.1-03 | FI | 0 | Obligatoria | Se evalúa tras la apertura |
| 3.4.1-05 | 3.4.1-04 | FI | 0 | Externa | No objeción a la evaluación |
| 3.4.1-06 | 3.4.1-05 | FI | 0 | Obligatoria | Adjudicación tras no objeción |
| 3.4.1-07 | 1.1.1-05 | FF | 0 | Discrecional | Los documentos se preparan en paralelo con la revisión del diseño y cierran con su aprobación |
| 3.4.1-07 | 3.1.1-02 | FI | 0 | Obligatoria | Especialista de adquisiciones en funciones |
| 3.4.1-07 | 3.2.3-04 | FI | 0 | Obligatoria | El proceso debe estar en el PA aprobado (ROP anexo 7.1 paso 3) |
| 3.4.1-08 | 3.3.1-04 | FI | 0 | Obligatoria | Documentos con cláusulas del SGAS (contrato cláusula 4.06(d)) |
| 3.4.1-08 | 3.4.1-07 | FI | 0 | Obligatoria | Documentos completos antes de enviarlos |
| 3.4.1-09 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige el proceso |
| 3.4.1-09 | 3.2.3-06 | FI | 0 | Obligatoria | Todo aviso específico y toda solicitud de expresiones de interés siguen al Aviso General de Adquisiciones (GN-2349-15 y GN-2350-15) |
| 3.4.1-09 | 3.4.1-08 | FI | 0 | Externa | Publicación tras no objeción del BID |
| 3.4.1-10 | 3.4.1-09 | FI | 0 | Obligatoria | Se evalúa tras la apertura |
| 3.4.1-11 | 3.4.1-10 | FI | 0 | Externa | No objeción a la evaluación |
| 3.4.1-12 | 3.4.1-11 | FI | 0 | Obligatoria | Adjudicación tras no objeción |
| 3.4.1-13 | 1.1.4-05 | FF | 0 | Discrecional | Los documentos se preparan en paralelo con la revisión del diseño y cierran con su aprobación |
| 3.4.1-13 | 3.1.1-02 | FI | 0 | Obligatoria | Especialista de adquisiciones en funciones |
| 3.4.1-13 | 3.2.3-04 | FI | 0 | Obligatoria | El proceso debe estar en el PA aprobado (ROP anexo 7.1 paso 3) |
| 3.4.1-14 | 3.3.1-04 | FI | 0 | Obligatoria | Documentos con cláusulas del SGAS (contrato cláusula 4.06(d)) |
| 3.4.1-14 | 3.4.1-13 | FI | 0 | Obligatoria | Documentos completos antes de enviarlos |
| 3.4.1-15 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige el proceso |
| 3.4.1-15 | 3.2.3-06 | FI | 0 | Obligatoria | Todo aviso específico y toda solicitud de expresiones de interés siguen al Aviso General de Adquisiciones (GN-2349-15 y GN-2350-15) |
| 3.4.1-15 | 3.4.1-14 | FI | 0 | Externa | Publicación tras no objeción del BID |
| 3.4.1-16 | 3.4.1-15 | FI | 0 | Obligatoria | Se evalúa tras la apertura |
| 3.4.1-17 | 3.4.1-16 | FI | 0 | Externa | No objeción a la evaluación |
| 3.4.1-18 | 3.4.1-17 | FI | 0 | Obligatoria | Adjudicación tras no objeción |
| 3.4.1-19 | 1.1.2-06 | FF | 0 | Discrecional | Los documentos se preparan en paralelo con la revisión del diseño y cierran con su aprobación |
| 3.4.1-19 | 3.1.1-02 | FI | 0 | Obligatoria | Especialista de adquisiciones en funciones |
| 3.4.1-19 | 3.2.3-04 | FI | 0 | Obligatoria | El proceso debe estar en el PA aprobado (ROP anexo 7.1 paso 3) |
| 3.4.1-20 | 3.3.1-04 | FI | 0 | Obligatoria | Documentos con cláusulas del SGAS (contrato cláusula 4.06(d)) |
| 3.4.1-20 | 3.4.1-19 | FI | 0 | Obligatoria | Documentos completos antes de enviarlos |
| 3.4.1-21 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige el proceso |
| 3.4.1-21 | 3.2.3-06 | FI | 0 | Obligatoria | Todo aviso específico y toda solicitud de expresiones de interés siguen al Aviso General de Adquisiciones (GN-2349-15 y GN-2350-15) |
| 3.4.1-21 | 3.4.1-20 | FI | 0 | Externa | Publicación tras no objeción del BID |
| 3.4.1-22 | 3.4.1-21 | FI | 0 | Obligatoria | Se evalúa tras la apertura |
| 3.4.1-23 | 3.4.1-22 | FI | 0 | Externa | No objeción a la evaluación |
| 3.4.1-24 | 3.4.1-23 | FI | 0 | Obligatoria | Adjudicación tras no objeción |
| 3.4.2-01 | 3.2.3-02 | FI | 0 | Obligatoria | El proceso debe estar en el PA aprobado |
| 3.4.2-01 | 3.2.3-06 | FI | 0 | Obligatoria | Todo aviso específico y toda solicitud de expresiones de interés siguen al Aviso General de Adquisiciones (GN-2349-15 y GN-2350-15) |
| 3.4.2-02 | 3.4.2-01 | FI | 0 | Externa | Secuencia del proceso SBCC |
| 3.4.2-03 | 3.4.2-02 | FI | 0 | Obligatoria | Secuencia del proceso SBCC |
| 3.4.2-04 | 3.4.2-03 | FI | 0 | Obligatoria | Secuencia del proceso SBCC |
| 3.4.2-05 | 3.4.2-04 | FI | 0 | Externa | Secuencia del proceso SBCC |
| 3.4.2-06 | 3.4.2-05 | FI | 0 | Obligatoria | Secuencia del proceso SBCC |
| 3.4.2-07 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige la selección de firmas |
| 3.4.2-07 | 3.2.3-04 | FI | 0 | Obligatoria | El proceso debe estar en el PA aprobado |
| 3.4.2-07 | 3.2.3-06 | FI | 0 | Obligatoria | Todo aviso específico y toda solicitud de expresiones de interés siguen al Aviso General de Adquisiciones (GN-2349-15 y GN-2350-15) |
| 3.4.2-07 | 3.3.1-04 | FI | 0 | Obligatoria | Los TdR incluyen la supervisión del SGAS (EDT 1.7.3) |
| 3.4.2-08 | 3.4.2-07 | FI | 0 | Externa | Secuencia del proceso SBCC |
| 3.4.2-09 | 3.4.2-08 | FI | 0 | Obligatoria | Secuencia del proceso SBCC |
| 3.4.2-10 | 3.4.2-09 | FI | 0 | Obligatoria | Secuencia del proceso SBCC |
| 3.4.2-11 | 3.4.2-10 | FI | 0 | Externa | Secuencia del proceso SBCC |
| 3.4.2-12 | 3.4.2-11 | FI | 0 | Obligatoria | Secuencia del proceso SBCC |
| 3.4.2-13 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige la selección de firmas |
| 3.4.2-13 | 3.2.3-04 | FI | 0 | Obligatoria | El proceso debe estar en el PA aprobado |
| 3.4.2-13 | 3.2.3-06 | FI | 0 | Obligatoria | Todo aviso específico y toda solicitud de expresiones de interés siguen al Aviso General de Adquisiciones (GN-2349-15 y GN-2350-15) |
| 3.4.2-13 | 3.3.1-04 | FI | 0 | Obligatoria | Los TdR incluyen la supervisión del SGAS (EDT 1.7.3) |
| 3.4.2-14 | 3.4.2-13 | FI | 0 | Externa | Secuencia del proceso SBCC |
| 3.4.2-15 | 3.4.2-14 | FI | 0 | Obligatoria | Secuencia del proceso SBCC |
| 3.4.2-16 | 3.4.2-15 | FI | 0 | Obligatoria | Secuencia del proceso SBCC |
| 3.4.2-17 | 3.4.2-16 | FI | 0 | Externa | Secuencia del proceso SBCC |
| 3.4.2-18 | 3.4.2-17 | FI | 0 | Obligatoria | Secuencia del proceso SBCC |
| 3.4.2-19 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige la selección de firmas |
| 3.4.2-19 | 3.2.3-04 | FI | 0 | Obligatoria | El proceso debe estar en el PA aprobado |
| 3.4.2-19 | 3.2.3-06 | FI | 0 | Obligatoria | Todo aviso específico y toda solicitud de expresiones de interés siguen al Aviso General de Adquisiciones (GN-2349-15 y GN-2350-15) |
| 3.4.2-19 | 3.3.1-04 | FI | 0 | Obligatoria | Los TdR incluyen la supervisión del SGAS (EDT 1.7.3) |
| 3.4.2-20 | 3.4.2-19 | FI | 0 | Externa | Secuencia del proceso SBCC |
| 3.4.2-21 | 3.4.2-20 | FI | 0 | Obligatoria | Secuencia del proceso SBCC |
| 3.4.2-22 | 3.4.2-21 | FI | 0 | Obligatoria | Secuencia del proceso SBCC |
| 3.4.2-23 | 3.4.2-22 | FI | 0 | Externa | Secuencia del proceso SBCC |
| 3.4.2-24 | 3.4.2-23 | FI | 0 | Obligatoria | Secuencia del proceso SBCC |
| 3.4.3-01 | 3.2.3-04 | FI | 0 | Obligatoria | Se actualiza sobre el PA 2026-2 |
| 3.4.3-02 | 3.4.3-01 | FI | 0 | Externa | No objeción del BID |
| 3.4.3-03 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige la selección |
| 3.4.3-03 | 3.4.3-02 | FI | 0 | Obligatoria | El proceso debe estar en el PA aprobado (ROP anexo 7.1 paso 3) |
| 3.4.3-04 | 3.4.3-03 | FI | 0 | Externa | Secuencia del proceso |
| 3.4.3-05 | 3.4.3-04 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-06 | 3.4.3-05 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-07 | 3.4.3-06 | FI | 0 | Externa | Secuencia del proceso |
| 3.4.3-08 | 3.4.3-07 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-09 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige la selección |
| 3.4.3-09 | 3.4.3-02 | FI | 0 | Obligatoria | El proceso debe estar en el PA aprobado (ROP anexo 7.1 paso 3) |
| 3.4.3-10 | 3.4.3-09 | FI | 0 | Externa | Secuencia del proceso |
| 3.4.3-11 | 3.4.3-10 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-12 | 3.4.3-11 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-13 | 3.4.3-12 | FI | 0 | Externa | Secuencia del proceso |
| 3.4.3-14 | 3.4.3-13 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-15 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige la selección |
| 3.4.3-15 | 3.4.3-02 | FI | 0 | Obligatoria | El proceso debe estar en el PA aprobado (ROP anexo 7.1 paso 3) |
| 3.4.3-16 | 3.2.3-06 | FI | 0 | Obligatoria | Todo aviso específico y toda solicitud de expresiones de interés siguen al Aviso General de Adquisiciones (GN-2349-15 y GN-2350-15) |
| 3.4.3-16 | 3.4.3-15 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-17 | 3.4.3-51 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-18 | 3.4.3-17 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-19 | 3.4.3-52 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-20 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige la selección |
| 3.4.3-20 | 3.4.3-02 | FI | 0 | Obligatoria | El proceso debe estar en el PA aprobado (ROP anexo 7.1 paso 3) |
| 3.4.3-21 | 3.4.3-20 | FI | 0 | Externa | Secuencia del proceso |
| 3.4.3-22 | 3.4.3-21 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-23 | 3.4.3-22 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-24 | 3.4.3-23 | FI | 0 | Externa | Secuencia del proceso |
| 3.4.3-25 | 3.4.3-24 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-26 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige la selección |
| 3.4.3-26 | 3.4.3-02 | FI | 0 | Obligatoria | El proceso debe estar en el PA aprobado (ROP anexo 7.1 paso 3) |
| 3.4.3-27 | 3.2.3-06 | FI | 0 | Obligatoria | Todo aviso específico y toda solicitud de expresiones de interés siguen al Aviso General de Adquisiciones (GN-2349-15 y GN-2350-15) |
| 3.4.3-27 | 3.4.3-26 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-28 | 3.4.3-53 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-29 | 3.4.3-28 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-30 | 3.4.3-54 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-31 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige la selección |
| 3.4.3-31 | 3.4.3-02 | FI | 0 | Obligatoria | El proceso debe estar en el PA aprobado (ROP anexo 7.1 paso 3) |
| 3.4.3-32 | 3.2.3-06 | FI | 0 | Obligatoria | Todo aviso específico y toda solicitud de expresiones de interés siguen al Aviso General de Adquisiciones (GN-2349-15 y GN-2350-15) |
| 3.4.3-32 | 3.4.3-31 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-33 | 3.4.3-55 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-34 | 3.4.3-33 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-35 | 3.4.3-56 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-36 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige la selección |
| 3.4.3-36 | 3.4.3-02 | FI | 0 | Obligatoria | El proceso debe estar en el PA aprobado (ROP anexo 7.1 paso 3) |
| 3.4.3-37 | 3.2.3-06 | FI | 0 | Obligatoria | Todo aviso específico y toda solicitud de expresiones de interés siguen al Aviso General de Adquisiciones (GN-2349-15 y GN-2350-15) |
| 3.4.3-37 | 3.4.3-36 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-38 | 3.4.3-57 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-39 | 3.4.3-38 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-40 | 3.4.3-58 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-41 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige la selección |
| 3.4.3-41 | 3.4.3-02 | FI | 0 | Obligatoria | El proceso debe estar en el PA aprobado (ROP anexo 7.1 paso 3) |
| 3.4.3-42 | 3.2.3-06 | FI | 0 | Obligatoria | Todo aviso específico y toda solicitud de expresiones de interés siguen al Aviso General de Adquisiciones (GN-2349-15 y GN-2350-15) |
| 3.4.3-42 | 3.4.3-41 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-43 | 3.4.3-59 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-44 | 3.4.3-43 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-45 | 3.4.3-60 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-46 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige la selección |
| 3.4.3-46 | 3.4.3-02 | FI | 0 | Obligatoria | El proceso debe estar en el PA aprobado (ROP anexo 7.1 paso 3) |
| 3.4.3-47 | 3.2.3-06 | FI | 0 | Obligatoria | Todo aviso específico y toda solicitud de expresiones de interés siguen al Aviso General de Adquisiciones (GN-2349-15 y GN-2350-15) |
| 3.4.3-47 | 3.4.3-46 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-48 | 3.4.3-61 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-49 | 3.4.3-48 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-50 | 3.4.3-62 | FI | 0 | Obligatoria | Secuencia del proceso |
| 3.4.3-51 | 3.4.3-16 | FI | 0 | Externa | No objeción del BID (revisión ex ante) |
| 3.4.3-52 | 3.4.3-18 | FI | 0 | Externa | No objeción del BID (revisión ex ante) |
| 3.4.3-53 | 3.4.3-27 | FI | 0 | Externa | No objeción del BID (revisión ex ante) |
| 3.4.3-54 | 3.4.3-29 | FI | 0 | Externa | No objeción del BID (revisión ex ante) |
| 3.4.3-55 | 3.4.3-32 | FI | 0 | Externa | No objeción del BID (revisión ex ante) |
| 3.4.3-56 | 3.4.3-34 | FI | 0 | Externa | No objeción del BID (revisión ex ante) |
| 3.4.3-57 | 3.4.3-37 | FI | 0 | Externa | No objeción del BID (revisión ex ante) |
| 3.4.3-58 | 3.4.3-39 | FI | 0 | Externa | No objeción del BID (revisión ex ante) |
| 3.4.3-59 | 3.4.3-42 | FI | 0 | Externa | No objeción del BID (revisión ex ante) |
| 3.4.3-60 | 3.4.3-44 | FI | 0 | Externa | No objeción del BID (revisión ex ante) |
| 3.4.3-61 | 3.4.3-47 | FI | 0 | Externa | No objeción del BID (revisión ex ante) |
| 3.4.3-62 | 3.4.3-49 | FI | 0 | Externa | No objeción del BID (revisión ex ante) |
| 3.4.4-02 | 3.4.4-01 | FI | 0 | Externa | Secuencia 3CV del ROP |
| 3.4.4-03 | 3.4.4-02 | FI | 0 | Obligatoria | Secuencia 3CV del ROP |
| 3.4.4-04 | 3.4.4-03 | FI | 0 | Externa | Secuencia 3CV del ROP |
| 3.4.4-05 | 3.4.4-04 | FI | 0 | Obligatoria | Secuencia 3CV del ROP |
| 3.4.4-06 | 3.1.1-02 | FI | 0 | Obligatoria | El Especialista de adquisiciones conduce el proceso |
| 3.4.4-06 | 3.2.3-04 | FI | 0 | Obligatoria | Proceso en el PA aprobado |
| 3.4.4-07 | 3.4.4-06 | FI | 0 | Externa | Secuencia 3CV del ROP |
| 3.4.4-08 | 3.4.4-07 | FI | 0 | Obligatoria | Secuencia 3CV del ROP |
| 3.4.4-09 | 3.4.4-08 | FI | 0 | Externa | Secuencia 3CV del ROP |
| 3.4.4-10 | 3.4.4-09 | FI | 0 | Obligatoria | Secuencia 3CV del ROP |
| 3.4.4-11 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige la selección |
| 3.4.4-11 | 3.2.3-02 | FI | 0 | Obligatoria | Proceso en el PA aprobado |
| 3.4.4-12 | 3.4.4-11 | FI | 0 | Externa | Secuencia SBMC |
| 3.4.4-13 | 3.4.4-12 | FI | 0 | Obligatoria | Secuencia SBMC |
| 3.4.4-14 | 3.4.4-13 | FI | 0 | Externa | Secuencia SBMC |
| 3.4.4-15 | 3.4.4-14 | FI | 0 | Obligatoria | Secuencia SBMC |
| 3.4.4-16 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige la selección |
| 3.4.4-16 | 3.2.3-04 | FI | 0 | Obligatoria | Proceso en el PA aprobado |
| 3.4.4-17 | 3.4.4-16 | FI | 0 | Externa | Secuencia SBMC |
| 3.4.4-18 | 3.4.4-17 | FI | 0 | Obligatoria | Secuencia SBMC |
| 3.4.4-19 | 3.4.4-18 | FI | 0 | Externa | Secuencia SBMC |
| 3.4.4-20 | 3.4.4-19 | FI | 0 | Obligatoria | Secuencia SBMC |
| 3.4.4-21 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige la selección |
| 3.4.4-21 | 3.2.3-04 | FI | 0 | Obligatoria | Proceso en el PA aprobado |
| 3.4.4-22 | 3.4.4-21 | FI | 0 | Externa | Secuencia SBMC |
| 3.4.4-23 | 3.4.4-22 | FI | 0 | Obligatoria | Secuencia SBMC |
| 3.4.4-24 | 3.4.4-23 | FI | 0 | Externa | Secuencia SBMC |
| 3.4.4-25 | 3.4.4-24 | FI | 0 | Obligatoria | Secuencia SBMC |
| 3.4.4-26 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige la selección |
| 3.4.4-26 | 3.2.3-04 | FI | 0 | Obligatoria | Proceso en el PA aprobado |
| 3.4.4-27 | 3.4.4-26 | FI | 0 | Externa | Secuencia SBMC |
| 3.4.4-28 | 3.4.4-27 | FI | 0 | Obligatoria | Secuencia SBMC |
| 3.4.4-29 | 3.4.4-28 | FI | 0 | Externa | Secuencia SBMC |
| 3.4.4-30 | 3.4.4-29 | FI | 0 | Obligatoria | Secuencia SBMC |
| 3.4.4-31 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige la selección |
| 3.4.4-31 | 3.2.3-04 | FI | 0 | Obligatoria | Proceso en el PA aprobado |
| 3.4.4-31 | 3.5.3-01 | FI | 0 | Obligatoria | La contratación se inicia con el hito proyectado |
| 3.4.4-32 | 3.2.3-06 | FI | 0 | Obligatoria | Todo aviso específico y toda solicitud de expresiones de interés siguen al Aviso General de Adquisiciones (GN-2349-15 y GN-2350-15) |
| 3.4.4-32 | 3.4.4-31 | FI | 0 | Obligatoria | Secuencia SCC |
| 3.4.4-33 | 3.4.4-41 | FI | 0 | Obligatoria | Secuencia SCC |
| 3.4.4-34 | 3.4.4-33 | FI | 0 | Obligatoria | Secuencia SCC |
| 3.4.4-35 | 3.4.4-42 | FI | 0 | Obligatoria | Secuencia SCC |
| 3.4.4-36 | 1.2.4-06 | FI | -60 | Discrecional | La evaluación final se contrata para empezar al terminar la terminal, cuando el desembolso se acerca al 95% (contrato, cláusula 5.03) |
| 3.4.4-36 | 3.1.2-03 | FI | 0 | Obligatoria | El ROP vigente rige la selección |
| 3.4.4-36 | 3.2.3-04 | FI | 0 | Obligatoria | Proceso en el PA aprobado |
| 3.4.4-37 | 3.2.3-06 | FI | 0 | Obligatoria | Todo aviso específico y toda solicitud de expresiones de interés siguen al Aviso General de Adquisiciones (GN-2349-15 y GN-2350-15) |
| 3.4.4-37 | 3.4.4-36 | FI | 0 | Obligatoria | Secuencia SCC |
| 3.4.4-38 | 3.4.4-43 | FI | 0 | Obligatoria | Secuencia SCC |
| 3.4.4-39 | 3.4.4-38 | FI | 0 | Obligatoria | Secuencia SCC |
| 3.4.4-40 | 3.4.4-44 | FI | 0 | Obligatoria | Secuencia SCC |
| 3.4.4-41 | 3.4.4-32 | FI | 0 | Externa | No objeción del BID (revisión ex ante) |
| 3.4.4-42 | 3.4.4-34 | FI | 0 | Externa | No objeción del BID (revisión ex ante) |
| 3.4.4-43 | 3.4.4-37 | FI | 0 | Externa | No objeción del BID (revisión ex ante) |
| 3.4.4-44 | 3.4.4-39 | FI | 0 | Externa | No objeción del BID (revisión ex ante) |
| 3.4.4-45 | 3.1.1-02 | FI | 0 | Obligatoria | El Especialista de adquisiciones conduce el proceso |
| 3.4.4-45 | 3.2.3-04 | FI | 0 | Obligatoria | Proceso en el PA aprobado |
| 3.4.4-46 | 3.4.4-45 | FI | 0 | Externa | Secuencia 3CV del ROP |
| 3.4.4-47 | 3.4.4-46 | FI | 0 | Obligatoria | Secuencia 3CV del ROP |
| 3.4.4-48 | 3.4.4-47 | FI | 0 | Externa | Secuencia 3CV del ROP |
| 3.4.4-49 | 3.4.4-48 | FI | 0 | Obligatoria | Secuencia 3CV del ROP |
| 3.4.4-50 | 3.1.1-02 | FI | 0 | Obligatoria | El Especialista de adquisiciones conduce el proceso |
| 3.4.4-50 | 3.2.3-04 | FI | 0 | Obligatoria | Proceso en el PA aprobado |
| 3.4.4-51 | 3.4.4-50 | FI | 0 | Externa | Secuencia 3CV del ROP |
| 3.4.4-52 | 3.4.4-51 | FI | 0 | Obligatoria | Secuencia 3CV del ROP |
| 3.4.4-53 | 3.4.4-52 | FI | 0 | Externa | Secuencia 3CV del ROP |
| 3.4.4-54 | 3.4.4-53 | FI | 0 | Obligatoria | Secuencia 3CV del ROP |
| 3.4.4-55 | 3.1.1-02 | FI | 0 | Obligatoria | El Especialista de adquisiciones conduce el proceso |
| 3.4.4-55 | 3.2.3-04 | FI | 0 | Obligatoria | Proceso en el PA aprobado |
| 3.4.4-56 | 3.4.4-55 | FI | 0 | Externa | Secuencia 3CV del ROP |
| 3.4.4-57 | 3.4.4-56 | FI | 0 | Obligatoria | Secuencia 3CV del ROP |
| 3.4.4-58 | 3.4.4-57 | FI | 0 | Externa | Secuencia 3CV del ROP |
| 3.4.4-59 | 3.4.4-58 | FI | 0 | Obligatoria | Secuencia 3CV del ROP |
| 3.4.4-60 | 3.1.1-02 | FI | 0 | Obligatoria | El Especialista de adquisiciones conduce el proceso |
| 3.4.4-60 | 3.2.3-04 | FI | 0 | Obligatoria | Proceso en el PA aprobado |
| 3.4.4-61 | 3.4.4-60 | FI | 0 | Externa | Secuencia 3CV del ROP |
| 3.4.4-62 | 3.4.4-61 | FI | 0 | Obligatoria | Secuencia 3CV del ROP |
| 3.4.4-63 | 3.4.4-62 | FI | 0 | Externa | Secuencia 3CV del ROP |
| 3.4.4-64 | 3.4.4-63 | FI | 0 | Obligatoria | Secuencia 3CV del ROP |
| 3.4.4-65 | 3.1.1-02 | FI | 0 | Obligatoria | El Especialista de adquisiciones conduce el proceso |
| 3.4.4-65 | 3.2.3-04 | FI | 0 | Obligatoria | Proceso en el PA aprobado |
| 3.4.4-66 | 3.4.4-65 | FI | 0 | Externa | Secuencia 3CV del ROP |
| 3.4.4-67 | 3.4.4-66 | FI | 0 | Obligatoria | Secuencia 3CV del ROP |
| 3.4.4-68 | 3.4.4-67 | FI | 0 | Externa | Secuencia 3CV del ROP |
| 3.4.4-69 | 3.4.4-68 | FI | 0 | Obligatoria | Secuencia 3CV del ROP |
| 3.4.4-70 | 3.1.1-02 | FI | 0 | Obligatoria | El Especialista de adquisiciones conduce el proceso |
| 3.4.4-70 | 3.2.3-04 | FI | 0 | Obligatoria | Proceso en el PA aprobado |
| 3.4.4-71 | 3.4.4-70 | FI | 0 | Externa | Secuencia 3CV del ROP |
| 3.4.4-72 | 3.4.4-71 | FI | 0 | Obligatoria | Secuencia 3CV del ROP |
| 3.4.4-73 | 3.4.4-72 | FI | 0 | Externa | Secuencia 3CV del ROP |
| 3.4.4-74 | 3.4.4-73 | FI | 0 | Obligatoria | Secuencia 3CV del ROP |
| 3.5.1-01 | 3.1.1-05 | FI | 0 | Obligatoria | Condición previa al primer desembolso (contrato cláusula 3.01) |
| 3.5.1-01 | 3.1.2-03 | FI | 0 | Obligatoria | Condición previa al primer desembolso (contrato cláusula 3.01) |
| 3.5.1-01 | 3.1.3-03 | FI | 0 | Obligatoria | Condición previa al primer desembolso (contrato cláusula 3.01) |
| 3.5.1-01 | 3.1.4-03 | FI | 0 | Obligatoria | Condición previa al primer desembolso (contrato cláusula 3.01) |
| 3.5.1-01 | 3.3.1-04 | FI | 0 | Obligatoria | Condición previa al primer desembolso (contrato cláusula 3.01) |
| 3.5.1-02 | 3.5.1-01 | FI | 0 | Obligatoria | Informe tras el primer desembolso |
| 3.5.1-03 | 3.5.1-02 | FI | 0 | Discrecional | Un informe a la vez |
| 3.5.1-04 | 3.5.1-03 | FI | 0 | Discrecional | Un informe a la vez |
| 3.5.1-05 | 3.5.1-04 | FI | 0 | Discrecional | Un informe a la vez |
| 3.5.1-06 | 3.5.1-05 | FI | 0 | Discrecional | Un informe a la vez |
| 3.5.1-07 | 3.5.1-06 | FI | 0 | Discrecional | Un informe a la vez |
| 3.5.1-08 | 3.5.1-01 | FI | 0 | Obligatoria | Se requiere el primer desembolso |
| 3.5.1-09 | 3.5.1-01 | FI | 0 | Obligatoria | Se requiere el primer desembolso |
| 3.5.1-10 | 3.5.1-01 | FI | 0 | Obligatoria | Se requiere el primer desembolso |
| 3.5.2-01 | 3.1.4-03 | FI | 0 | Obligatoria | Los estados financieros del programa parten de la cuenta especial |
| 3.5.2-02 | 3.4.4-15 | FI | 0 | Obligatoria | El auditor debe tener contrato firmado |
| 3.5.2-02 | 3.5.2-01 | FI | 0 | Obligatoria | Se audita sobre los estados preparados |
| 3.5.2-03 | 3.5.2-02 | FI | 0 | Obligatoria | Se presenta el dictamen emitido |
| 3.5.2-04 | 3.5.2-03 | FI | 0 | Discrecional | Un ejercicio auditado a la vez |
| 3.5.2-05 | 3.4.4-20 | FI | 0 | Obligatoria | El auditor debe tener contrato firmado |
| 3.5.2-05 | 3.5.2-04 | FI | 0 | Obligatoria | Se audita sobre los estados preparados |
| 3.5.2-06 | 3.5.2-05 | FI | 0 | Obligatoria | Se presenta el dictamen emitido |
| 3.5.2-07 | 3.5.2-06 | FI | 0 | Discrecional | Un ejercicio auditado a la vez |
| 3.5.2-08 | 3.4.4-25 | FI | 0 | Obligatoria | El auditor debe tener contrato firmado |
| 3.5.2-08 | 3.5.2-07 | FI | 0 | Obligatoria | Se audita sobre los estados preparados |
| 3.5.2-09 | 3.5.2-08 | FI | 0 | Obligatoria | Se presenta el dictamen emitido |
| 3.5.3-01 | 3.4.1-18 | FI | 0 | Discrecional | Con los contratos de obra del estacionamiento, la terminal y el SSEI firmados (87% del monto de las obras) se proyecta cuándo se cumple el 50% del tiempo de ejecución y del desembolso, a tiempo para presentar el informe antes del plazo |
| 3.5.3-01 | 3.4.2-18 | FI | 0 | Discrecional | Con la supervisión del SSEI firmada ya están los cronogramas de las tres primeras obras para proyectar el hito |
| 3.5.3-02 | 3.4.4-35 | FI | 0 | Obligatoria | La firma consultora requiere contrato firmado |
| 3.5.3-03 | 3.5.3-02 | FI | 0 | Obligatoria | Se revisa el informe terminado |
| 3.5.3-04 | 3.4.4-40 | FI | 0 | Obligatoria | La firma consultora requiere contrato firmado |
| 3.5.3-04 | 3.5.3-03 | FI | 0 | Obligatoria | La evaluación final parte de la de medio término |
| 3.5.3-05 | 1.7.4-05 | FI | 0 | Obligatoria | Requiere las cuatro obras recibidas |
| 3.5.3-05 | 1.7.4-06 | FI | 0 | Obligatoria | Requiere las cuatro obras recibidas |
| 3.5.3-05 | 1.7.4-07 | FI | 0 | Obligatoria | Requiere las cuatro obras recibidas |
| 3.5.3-05 | 1.7.4-08 | FI | 0 | Obligatoria | Requiere las cuatro obras recibidas |
| 3.5.3-05 | 3.5.3-04 | FI | 0 | Obligatoria | Se revisa el informe terminado |
| 3.5.4-01 | 1.7.4-05 | FI | 0 | Obligatoria | Requiere las cuatro obras recibidas |
| 3.5.4-01 | 1.7.4-06 | FI | 0 | Obligatoria | Requiere las cuatro obras recibidas |
| 3.5.4-01 | 1.7.4-07 | FI | 0 | Obligatoria | Requiere las cuatro obras recibidas |
| 3.5.4-01 | 1.7.4-08 | FI | 0 | Obligatoria | Requiere las cuatro obras recibidas |
| 3.5.4-01 | 2.1-06 | FI | 0 | Obligatoria | No se liquida antes de recibir las obras y los productos del Componente II |
| 3.5.4-01 | 2.2.1-06 | FI | 0 | Obligatoria | No se liquida antes de recibir las obras y los productos del Componente II |
| 3.5.4-01 | 2.2.2-04 | FI | 0 | Obligatoria | No se liquida antes de recibir las obras y los productos del Componente II |
| 3.5.4-01 | 2.3.1-06 | FI | 0 | Obligatoria | No se liquida antes de recibir las obras y los productos del Componente II |
| 3.5.4-01 | 2.3.2-04 | FI | 0 | Obligatoria | No se liquida antes de recibir las obras y los productos del Componente II |
| 3.5.4-01 | 2.4-06 | FI | 0 | Obligatoria | No se liquida antes de recibir las obras y los productos del Componente II |
| 3.5.4-01 | 2.5-06 | FI | 0 | Obligatoria | No se liquida antes de recibir las obras y los productos del Componente II |
| 3.5.4-01 | 2.6.1-06 | FI | 0 | Obligatoria | No se liquida antes de recibir las obras y los productos del Componente II |
| 3.5.4-01 | 2.6.2-04 | FI | 0 | Obligatoria | No se liquida antes de recibir las obras y los productos del Componente II |
| 3.5.4-01 | 2.7-06 | FI | 0 | Obligatoria | No se liquida antes de recibir las obras y los productos del Componente II |
| 3.5.4-01 | 2.8-06 | FI | 0 | Obligatoria | No se liquida antes de recibir las obras y los productos del Componente II |
| 3.5.4-01 | 2.9-06 | FI | 0 | Obligatoria | No se liquida antes de recibir las obras y los productos del Componente II |
| 3.5.4-02 | 3.5.3-05 | FI | 0 | Obligatoria | El último desembolso incluye el pago de la evaluación final |
| 3.5.4-02 | 3.5.4-01 | FI | 0 | Obligatoria | Se justifica lo liquidado |
| 3.5.4-03 | 3.4.4-30 | FI | 0 | Obligatoria | El auditor del año 4 emite los estados finales |
| 3.5.4-03 | 3.5.2-09 | FI | 0 | Obligatoria | Los estados financieros finales parten del último ejercicio auditado |
| 3.5.4-03 | 3.5.4-02 | FI | 0 | Obligatoria | Estados finales tras el último desembolso |
| 3.5.4-04 | 3.3.4-03 | FI | 0 | Obligatoria | Incluye el informe final ambiental y social |
| 3.5.4-04 | 3.5.1-07 | FI | 0 | Obligatoria | El informe de terminación recoge el último informe semestral |
| 3.5.4-04 | 3.5.3-05 | FI | 0 | Obligatoria | El informe de terminación incorpora los resultados de la evaluación final |
| 3.5.4-04 | 3.5.4-03 | FI | 0 | Obligatoria | Informe tras estados finales |
| 3.5.4-05 | 3.5.4-03 | FI | 0 | Obligatoria | Se devuelven saldos tras los estados finales |
| 3.5.4-06 | 1.7.1-02 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 1.7.1-04 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 1.7.1-05 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 1.7.1-06 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 1.7.2-02 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 1.7.2-04 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 1.7.2-05 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 1.7.2-06 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 1.7.3-05 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 1.7.3-06 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 3.2.2-08 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 3.2.3-05 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 3.3.3-03 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 3.4.4-10 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 3.4.4-49 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 3.4.4-54 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 3.4.4-59 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 3.4.4-64 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 3.4.4-69 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 3.4.4-74 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 3.5.1-08 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 3.5.1-09 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 3.5.1-10 | FI | 0 | Obligatoria | El cierre administrativo requiere todo el trabajo del programa terminado |
| 3.5.4-06 | 3.5.4-04 | FI | 0 | Obligatoria | Cierre administrativo tras el informe |
| 3.5.4-06 | 3.5.4-05 | FI | 0 | Obligatoria | Cierre administrativo tras cerrar la cuenta |

## 8. Hitos

Los hitos tienen duración cero y se cumplen cuando terminan las actividades indicadas.

| Hito | Nombre | Se cumple al terminar |
|---|---|---|
| H01 | Unidad Ejecutora conformada | 3.1.1-05 |
| H02 | Condiciones previas al primer desembolso cumplidas (ROP, convenio, cuenta) | 3.1.2-03, 3.1.3-03, 3.1.4-03 |
| H03 | Contratos de obra y de supervisión firmados | 3.4.1-06, 3.4.1-12, 3.4.1-18, 3.4.1-24, 3.4.2-06, 3.4.2-12, 3.4.2-18, 3.4.2-24 |
| H04 | Protocolo de seguridad operacional aprobado por la AAC | 3.3.2-04 |
| H05 | SSEI reubicado y en funcionamiento | 1.6.2-04 |
| H06 | Plataforma de posiciones remotas concluida | 1.3.2-05 |
| H07 | Terminal ampliada concluida y equipada | 1.2.4-06, 1.2.5-04 |
| H08 | Estacionamiento con sistema solar concluido | 1.5.2-03, 1.5.3-04 |
| H09 | Obras recibidas (planos de obra ejecutada y actas aprobados) | 1.7.4-05, 1.7.4-06, 1.7.4-07, 1.7.4-08 |
| H10 | Cierre administrativo del programa | 3.5.4-06 |

## 9. Supuestos

Lo que no tiene fuente documental se declara aquí. La columna "Fuente" del listado remite a estos supuestos cuando corresponde.

### Componente I. Obras y adecuaciones

- **S-I.1.** Las cuatro revisiones de diseño (1.1.1 a 1.1.4) empiezan cuando el especialista en ingeniería aeroportuaria de la UEP está contratado y se hacen en serie, porque la EDT asigna un solo especialista en ingeniería aeroportuaria. Los ingenieros de apoyo que el Plan de Adquisiciones 2026-2 prevé contratar entre septiembre y octubre de 2026 llegan cuando las revisiones del estacionamiento y de la terminal ya terminaron. El diseño de cada obra lo hizo una firma contratada por CEPA fuera del programa; la UEP lo revisa, lo ajusta y obtiene la no objeción del BID antes de licitar.
- **S-I.2.** Los sondeos geotécnicos de las posiciones remotas (1.1.2-01) son un servicio menor de CEPA fuera del Plan de Adquisiciones, como recomienda el EEO#3. Si ya se hicieron, la actividad se elimina.
- **S-I.3.** La plataforma de posiciones remotas ocupa el sitio del SSEI actual, por lo que incluye su demolición (1.3.2-01).
- **S-I.4.** La autorización de la AAC para poner en servicio las plataformas y la calle Foxtrot (1.3.3-05 y 1.4.2-04) y las pruebas integradas de operación de la terminal (1.2.4-06) son práctica aeronáutica, sin un documento del programa que las fije.
- **S-I.5.** La recepción definitiva (1.7.4-06) es el acta posterior a subsanar pendientes y recibir los planos de obra ejecutada; el periodo de garantía de defectos no se modela como actividad.
- **S-I.6.** Los rendimientos marcados como "supuesto" en la columna "Fuente" son estimaciones propias contrastadas con plataformas análogas (A-GRR y A-BRU).
- **S-I.7.** Plazos de obra: la terminal suma unos 20 meses de construcción con los valores estimados (aviso de licitación, 18 meses; sondeo de mercado, 24; PEP, 1,080 días calendario) y el estacionamiento unos 16 meses (aviso, 15; PEP, 750 días calendario; estacionamientos análogos, 18 a 20). Se dio más peso al aviso de licitación por ser el documento más reciente.
- **S-I.8.** El diseño final de la fachada sur (tres salas de espera y sus puentes de abordaje) se modela a cargo del contratista de la terminal, con revisión de la supervisión junto con la fachada norte (1.1.1-06 a 1.1.1-08). Es una inferencia, no un dato explícito: la solicitud de expresiones de interés de la supervisión de la terminal (EOI-T, P00024) solo contrata la "supervisión del diseño" de la fachada sur, el aviso de la terminal (SPN-T, P00023) no menciona diseño, y el Anexo III.i prevé contratos FIDIC amarillo, de diseño y construcción por el contratista. Si el diseño lo hiciera CEPA u otra firma, 1.1.1-06 cambiaría de responsable y su inicio ya no dependería de la orden de inicio de la obra. En las demás obras el diseño final lo contrató o lo hizo CEPA antes de licitar (Anexo III.i, sección 3). Costo: 1.1.1-06 y 1.1.1-07 no llevan costo propio; el diseño del contratista se paga dentro del precio del contrato de obra, de diseño y construcción (T1), y su revisión dentro del contrato de supervisión (V1), como declaran la estimación de costos y la curva S.

### Adquisiciones y administración del programa

- **S-III.1.** En las cuatro licitaciones de obra, las etapas posteriores a la apertura de ofertas (evaluar, no objeción del BID, adjudicar y firmar) se calibraron para reproducir la firma estimada del Plan de Adquisiciones 2026-2. Resultan más largas que los 15 + 5 + 10 dl que estima el ROP.
- **S-III.2.** El SSEI y las plataformas con Foxtrot no tienen aviso publicado al 31 de octubre de 2026: se toma como fecha de publicación el inicio de proceso del Plan de Adquisiciones 2026-2 y un periodo de ofertas de 31 dl, igual al del estacionamiento.
- **S-III.3.** Ninguna licitación de obra tiene precalificación: los dos avisos publicados son una Solicitud de Ofertas por licitación pública internacional con los requisitos de calificación dentro del documento de licitación (SPN-E, numeral 5; SPN-T, numeral 5), aunque el Anexo III.i (2.1 y 2.4) la preveía. Todos los procesos se licitan con revisión ex ante del BID (Anexo III.i, 2.5).
- **S-III.4.** La supervisión del estacionamiento empezó con la solicitud de expresiones de interés que CEPA publicó el 6 de mayo de 2026 y que cerró el 20 de mayo (CEPA-EOI y EOI-E), aunque el Plan de Adquisiciones 2026-2 le asigna como inicio el 1 de noviembre de 2026 y la marca "en curso". Como la firma estimada es el 3 de febrero de 2027, la evaluación y negociación se calibró para absorber ese intervalo.
- **S-III.5.** Las consultorías del Componente II no figuran en el Plan de Adquisiciones 2026-2. Se supone una revisión del plan después del 31 de octubre de 2026 (3.4.3-01) y nueve contratos, uno por producto del PEP, todos con revisión ex ante del BID, como fija el Anexo III.i (2.5) para todos los procesos y como aplica el Plan de Adquisiciones 2026-2 a todos los suyos (incluso P00003, de US$40,000), aunque la tabla 10 del ROP prevé ex post para firmas consultoras por menos de US$200,000. Métodos: SBCC con lista corta internacional para 2.1, 2.2 y 2.4 y para BIM (2.3.1 y 2.3.2, unos US$259,000, que supera el umbral de US$200,000 de la tabla 10); SBCC con lista corta nacional para 2.5 (US$177,000); SCC con lista corta nacional para 2.6, 2.7, 2.8 y 2.9 (menores a US$200,000). Cada proceso tiene dos no objeciones del BID, una a los términos de referencia y la lista corta y otra al informe de evaluación y al contrato negociado, y dura unos 127 dl (lista corta internacional) o 102 dl (lista corta nacional), por juicio de expertos a partir de los 50 dl del 3CV y los 5 días por revisión del BID del anexo 7.1 del ROP. Las evaluaciones de medio término y final (3.4.4-31 a 3.4.4-44) siguen la misma revisión ex ante, con las duraciones calibradas al plazo del PEP, y las auditorías ya tenían sus no objeciones.
- **S-III.6.** El técnico de apoyo administrativo (proceso P00014, "Asistente Administrativo" en el Plan de Adquisiciones 2026-2) se contrata por 3CV en 50 dl desde el inicio de proceso del Plan de Adquisiciones 2026-2 (14 de julio de 2026), por lo que firma hacia septiembre de 2026 y no el 15 de agosto que indica el plan.
- **S-III.7.** Hay cuatro contratos de auditoría (SBMC), uno por año: el del año k audita el ejercicio 2025 + k, y el cuarto audita el ejercicio 2029 junto con los estados financieros finales del cierre. El primero usa las fechas del Plan de Adquisiciones 2026-2; los otros tres firman en las fechas del PEP, con el inicio del proceso fijado para que no haya espera entre el proceso y la firma.
- **S-III.8.** Cada POA se empieza a elaborar el 1 de noviembre del año anterior, para tenerlo aprobado antes del 1 de enero. Hay un POA por año de 2027 a 2030.
- **S-III.9.** Los informes semestrales van del segundo semestre de 2026 al primero de 2029; el del segundo semestre de 2029 lo reemplaza el informe de terminación.
- **S-III.10.** La evaluación de medio término debe presentarse a más tardar 60 días después de que se haya desembolsado el 50% de los recursos o haya transcurrido el 50% del tiempo de ejecución planificado, lo que ocurra primero (contrato, cláusula 5.03(a)); el plazo no se mide sobre el plazo de desembolsos. Se toma como tiempo de ejecución planificado el del cronograma, del 2 de febrero de 2026 al 1 de abril de 2030: el 50% se cumple el 2 de marzo de 2028 y el informe vence el 1 de mayo de 2028 por tiempo (si cambia el fin del programa, hay que recalcularlo). Con el 50% desembolsado según los requisitos de financiamiento (con anticipo y con reserva de gestión, la misma serie del documento de la curva S), el 50% llega el 31 de enero de 2028 y el límite es el 31 de marzo de 2028. La contratación de la evaluación (3.4.4-31 a 3.4.4-35 y las no objeciones 3.4.4-41 y 3.4.4-42) empieza con la proyección del hito (3.5.3-01), que se enlaza a los contratos de obra y de supervisión del SSEI (tercer contrato de obra; con el estacionamiento y la terminal suman 88% del monto de las obras) y no a una fecha fija. Con esa lógica el informe (fin de 3.5.3-03) queda el 13 de marzo de 2028, 35 dl antes del límite por tiempo (1 de mayo) y 14 dl antes del límite por desembolso (31 de marzo), que es el primero. El margen de 14 dl queda por debajo de los 15 dl que se buscaban; no se movió el cronograma y se declara como un margen pequeño. La evaluación final vence 90 días después del fin del plazo original de desembolsos o del 95% desembolsado, lo que ocurra primero; como la línea base no llega al 95% del préstamo, el plazo original de desembolsos (cinco años, cláusula 2.04) termina en enero de 2031, y la evaluación se contrata unos tres meses antes del fin de la terminal, de modo que su informe queda en noviembre de 2029. El adelanto del desembolso por anticipos de fondos es un riesgo (S-III.19) y la vigencia que se usa se declara en S-III.20.
- **S-III.11.** La AAC aprueba el protocolo de seguridad operacional en unos 20 dl (3.3.2-04), sin plazo legal conocido.
- **S-III.12.** El mecanismo de quejas y los informes socioambientales terminan con las obras. La obligación de informar se extiende dos años después del último desembolso (contrato, cláusula 5.01), fuera del horizonte del cronograma.
- **S-III.13.** El último desembolso incluye el pago de la evaluación final, y los estados financieros finales se auditan en unos 40 dl después de ese desembolso, dentro de los 120 días del contrato.
- **S-III.14.** La UEP de la EDT son los siete puestos clave (P00004 a P00010) y el técnico de apoyo administrativo (P00014). La plantilla ampliada del Plan de Adquisiciones 2026-2 sí se incluye en la línea base: 21 procesos activos de consultores individuales 3CV, todos con revisión ex ante (P00011 a P00041, sin P00014, que ya estaba, ni P00019, cancelado), por unos US$1,920,425 con firmas estimadas de septiembre de 2026 a septiembre de 2027. Se agrupan en seis lotes por fecha de inicio de proceso, cada uno con cinco actividades (términos de referencia, no objeción del BID, selección, no objeción del BID a la selección y firma; 3.4.4-45 a 3.4.4-74), y las fechas de inicio del plan son restricciones de no comenzar antes. Con los 50 dl del ROP, las firmas resultan después de las fechas estimadas del plan. Lotes: 1, diez puestos (P00011, P00013, P00015, P00016, P00017, P00018 y P00029 a P00032; US$980,525); 2, P00040 (US$65,000); 3, P00033 (US$46,800); 4, P00012, P00020 y P00039 (US$199,550); 5, P00034 a P00038 (US$514,800); 6, P00041 (US$113,750). El trabajo de estos consultores y el de los siete puestos clave se recoge en la actividad de nivel de esfuerzo 3.1.1-06, que va de la incorporación del personal clave (16 de abril de 2026) a 3.5.4-04. El PEP de noviembre de 2025 preveía 19 plazas.
- **S-III.15.** El convenio de transferencia y la cuenta especial se tramitan en paralelo con el ROP. Así las condiciones previas al primer desembolso se cumplen el 10 de julio de 2026, antes del límite de 180 días desde la vigencia del contrato que fija el artículo 4.02 de las Normas Generales: 28 de julio de 2026 si la vigencia corre desde la ratificación del 29 de enero de 2026 (S-III.20), o 12 de julio de 2026 si corriera desde la firma del 13 de enero de 2026.
- **S-III.16.** Las actividades anteriores a la fecha de corte (31 de octubre de 2026) se presentan como plan. El avance real se registra en el cronograma, no en este listado.
- **S-III.17.** La solicitud de expresiones de interés de la supervisión de la terminal cerró el 6 de octubre de 2026 (EOI-T), pero no se conoce su fecha de publicación: se supone el 22 de septiembre de 2026, con el mismo plazo de 10 dl que la del estacionamiento. La evaluación se calibró para mantener la firma del 19 de mayo de 2027 del Plan de Adquisiciones 2026-2.
- **S-III.18.** El Aviso General de Adquisiciones se publicó el 5 de mayo de 2026 (SPN-E y SPN-T, numeral 1) y precede a todo aviso específico y a toda solicitud de expresiones de interés (3.2.3-06).
- **S-III.19.** Un desembolso acelerado por anticipos de fondos (hasta seis meses de gastos elegibles, Normas Generales, artículo 4.07) podría llevar el 50% desembolsado antes del 2 de marzo de 2028 y adelantar el plazo de la evaluación de medio término, que se cuenta desde lo que ocurra primero. Es un riesgo para la matriz de riesgos: la UEP debe vigilar el desembolso acumulado frente a la línea base y, si se acerca al 50% antes de esa fecha, adelantar la contratación de la evaluación (3.4.4-31).
- **S-III.20.** El contrato de préstamo adquirió plena validez jurídica, y por tanto entró en vigencia (cláusula 6.01), el 29 de enero de 2026, con la ratificación legislativa (D.L. 505) y su publicación, y no el 13 de enero de 2026, fecha de la firma. Es un supuesto: no se contó con el decreto publicado. De ahí parten el tiempo de ejecución del cronograma (inicio el 2 de febrero de 2026), el plazo original de desembolsos de cinco años y los 180 días de las condiciones previas.
- **S-III.21.** La auditoría del ejercicio 2026 conserva las fechas del Plan de Adquisiciones 2026-2 (P00003, firma el 5 de mayo de 2027), que es el plan oficial de CEPA. Los estados financieros auditados vencen 120 días después del cierre del ejercicio, el 30 de abril de 2027 (contrato, cláusula 5.02), y con esa firma la auditoría termina el 16 de junio de 2027 y se presenta el 23 de junio de 2027 (3.5.2-02 y 3.5.2-03): el incumplimiento del plazo es previsto. Es un riesgo para la matriz de riesgos: la UEP debe adelantar el proceso de la auditoría (3.4.4-11 a 3.4.4-15) o pedir al BID que acepte los estados financieros del ejercicio 2026 después del plazo. Está marcado en la fila 20 de la matriz de adquisiciones.

### Componente II. Fortalecimiento institucional

- **S-II.1.** Cada consultoría empieza con la firma de su contrato (3.4.3).
- **S-II.2.** Los estudios 2.1, 2.2.1, 2.3.1, 2.4, 2.5, 2.7 y 2.8 siguen seis pasos: plan de trabajo e informe inicial, diagnóstico, propuesta y borrador, revisión de CEPA, informe final y aprobación. La duración de cada paso es juicio de expertos, contrastado con el plazo del contrato en el PEP (TDR-ANA).
- **S-II.3.** CEPA, por medio de la UEP, aprueba los productos; el especialista responsable del paquete en la EDT revisa los borradores.
- **S-II.4.** Los productos 2.1 y 2.2.1 se remiten al BID para conocimiento, sin una no objeción con plazo propio; se reportan como anexo del informe semestral (MEL).
- **S-II.5.** La AAC revisa el borrador del Plan Maestro dentro de la actividad de revisión (2.2.1-04).
- **S-II.6.** Las duraciones de los cursos de 2.2.2 (21 funcionarios, 8 a 10 módulos), 2.3.2 (100 a 120 horas) y 2.6.2 (2 a 3 semanas) son estimaciones, con formación en horario parcial.
- **S-II.7.** El programa de igualdad e inclusión (2.9) forma una cohorte de 100 funcionarios por año durante tres años, como fija la tabla de metas del MEL; cada cohorte dura unas 7 semanas.
- **S-II.8.** El certificado preliminar EDGE vence 36 meses después de emitido o 12 meses después de terminada la obra, lo que ocurra primero (EDGE-P). Con el plazo de obra estimado no vence antes de la auditoría en sitio, pero si la terminal se atrasa haría falta una excepción del certificador.
- **S-II.9.** El acompañamiento EDGE durante la obra (2.6.1) es por hitos, no de presencia continua, y termina con la última de las dos obras certificadas.
- **S-II.10.** Una sola firma certifica la terminal y el estacionamiento en una sola auditoría en sitio.

## 10. Inconsistencias entre las fuentes

- **Plazos de obra.** Terminal: "18" sin unidad en el aviso de licitación (se interpreta en meses), 24 meses en el sondeo de mercado y 1,080 días calendario (35.5 meses) en el PEP. Estacionamiento: "15" sin unidad en el aviso y 750 días calendario (24.6 meses) en el PEP.
- **Fechas del PEP.** El PEP de noviembre de 2025 preveía publicar la terminal en abril de 2026 y firmar los contratos del Componente II entre junio de 2026 y enero de 2027. Los avisos reales son de septiembre y octubre de 2026, y el Plan de Adquisiciones 2026-2 no incluye el Componente II.
- **Plan de Adquisiciones 2026-2.** Sus fechas de inicio de proceso no coinciden con los avisos publicados (estacionamiento: 1 de noviembre frente al 4 de septiembre de 2026; terminal: 23 de noviembre frente al 8 de octubre). La firma estimada de la terminal, 24 de abril de 2027, cae en sábado; se modela el viernes 23. La supervisión del estacionamiento figura con inicio el 1 de noviembre de 2026 y estado "en curso", pero CEPA publicó su solicitud de expresiones de interés el 6 de mayo de 2026; la de la terminal figura con inicio el 13 de octubre de 2026, una semana después de que cerraran sus expresiones de interés (6 de octubre). La auditoría del ejercicio 2026 se firma el 5 de mayo de 2027, después del plazo contractual de 120 días (30 de abril de 2027): el plan oficial de CEPA no cumple la cláusula 5.02 y el cronograma lo conserva como incumplimiento previsto (S-III.21).
- **Supervisión.** El PEP la agrupa en un contrato para terminal y estacionamiento; el Plan de Adquisiciones 2026-2 la separa en procesos por obra. La supervisión de la terminal se firma 25 días después del contrato de obra.
- **Revisión de las consultorías.** La tabla 10 del ROP prevé revisión ex post para firmas consultoras por menos de US$200,000, pero el Anexo III.i (2.5) dice que todos los procesos serán objeto de supervisión ex ante y el Plan de Adquisiciones 2026-2 marca todos los suyos ex ante, incluso P00003 (US$40,000). Se usa ex ante en todos los procesos.
- **Componente II en el PEP.** Plazos de 730 días calendario para los estudios 2.4 y 2.5 frente a 200 y 180 para 2.7 y 2.8; un contrato de 120 días para 2.9 frente a las metas de tres años del MEL; el Plan Maestro figura como obra en una hoja y como consultoría en otra.
- **Descripción de las obras.** El EEO#3 dimensiona un estacionamiento de 700 plazas extrapolado a 2,000 y la licitación es de 2,050; el PGAS describe la calle Foxtrot en asfalto y el EEO#3 la agrupa con los pavimentos de concreto; el EEO#3 habla de 4 posiciones de contacto y el sondeo de mercado y el PGAS de 6; el PGAS ubica el sistema solar en otro edificio de estacionamiento.
- **Anexo III.i.** Preveía precalificar a los oferentes de las cuatro licitaciones y publicarlas entre marzo y agosto de 2026; los avisos publicados no tienen precalificación y salieron en septiembre y octubre de 2026.
- **ROP.** El encabezado de todas sus páginas corresponde al programa ES-L1157, una plantilla de otro préstamo.
- **EDT.** El paquete 1.1.1 pide coordinar la revisión de diseños de la terminal con la metodología BIM, pero la estrategia BIM (2.3.1) se contrata después; no se enlazaron.

## 11. Fuentes

Los identificadores son los que usa la columna "Fuente" del listado. Los documentos del programa están publicados en la página del préstamo ES-L1173 del BID (https://www.iadb.org/es/proyecto/ES-L1173).

### Documentos del programa

- **Contrato.** Contrato de préstamo 6073/OC-ES entre la República de El Salvador y el BID: cláusulas 2.04 (plazo de desembolsos), 3.01 (condiciones previas al primer desembolso), 4.04 a 4.08 (Plan de Adquisiciones, ROP, gestión ambiental y social con el mecanismo de quejas y el Plan de Gestión del Riesgo de Desastres y Cambio Climático final previo al inicio de las obras, protocolo de seguridad operacional), 5.01 (POA, PEP e informes semestrales a 30 días del semestre), 5.02 (estados financieros auditados a 120 días del cierre del ejercicio) y 5.03 (evaluaciones); Normas Generales, artículos 4.02 (180 días para las condiciones previas), 4.03(a) (última solicitud de desembolso), 4.06, 4.07, 4.14 (periodo de cierre), 6.01(c) (conservación de registros) y 7.03.
- **PP.** Propuesta de Préstamo ES-L1173, párrafo 4.6: protocolo de seguridad operacional aprobado por la AAC antes de las obras del lado aire, y SSEI reubicado y funcionando antes de la plataforma remota.
- **ROP.** Reglamento Operativo del Programa (EEO#1): anexo 7.1 (licitación pública internacional en 125 días hábiles: documentos 45, no objeción 5, ofertas 42, evaluación 15, no objeción 5, adjudicación y contrato 10; selección de consultores individuales 3CV en 50 días hábiles), tabla 10 (métodos por monto) y revisión ex ante de firmas consultoras.
- **PEP** (también PEP-C2). Plan de Ejecución, POA y Plan de Adquisiciones del programa (EER#3, noviembre de 2025): fechas de proceso y plazos de contrato en días calendario. https://www.iadb.org/es/viewer/EZIDB0003440-654689410-14
- **PA** (PA 2026-2; P00001 a P00041 son los números de proceso). Plan de Adquisiciones 2026-2 del programa (cobertura del 14 de julio de 2026 al 14 de marzo de 2027): métodos, inicio de proceso y firma estimada de cada contratación. https://www.iadb.org/es/viewer/EZIDB0003440-1039777545-69
- **SPN-E** (SPN IDB-6073OCES-P00001-SPN). Aviso específico de adquisiciones de la obra del estacionamiento, 4 de septiembre de 2026: Solicitud de Ofertas por licitación pública internacional, plazo de construcción "15" sin unidad, ofertas el 16 de octubre de 2026; cita el Aviso General de Adquisiciones del 5 de mayo de 2026. https://www.iadb.org/es/viewer/EZIDB0003440-1039777545-93
- **SPN-T** (SPN IDB-6073OCES-P00023-SPN). Aviso específico de adquisiciones de la obra de la terminal, 8 de octubre de 2026: Solicitud de Ofertas por licitación pública internacional, plazo de construcción "18" sin unidad, documentos hasta el 19 de noviembre y ofertas el 20 de noviembre de 2026.
- **EOI-E** (IDB-6073OCES-P00002-EOI). Solicitud de expresiones de interés para la supervisión del edificio de estacionamiento con su sistema solar: cierre el 20 de mayo de 2026, lista corta de 5 a 8 firmas.
- **EOI-T** (IDB-6073OCES-P00024-EOI). Solicitud de expresiones de interés para la supervisión del diseño y la construcción de la terminal: método SBCC (GN-2350-15), cierre el 6 de octubre de 2026, lista corta de 5 a 8 firmas; la supervisión incluye el diseño de la fachada sur (3 salas y puentes de abordaje), la validación del diseño de la fachada norte, BIM y EDGE Advanced.
- **RFI-T.** Solicitud de información 6073/OC-SDI-01/2026 de la terminal (julio de 2026): 18,555 m² en tres niveles, seis puentes de abordaje, BIM, EDGE Advanced, obra con el aeropuerto en operación, plazo estimado de 24 meses.
- **EEO3.** Análisis de costos del programa (EEO#3, julio de 2025): descripción técnica, superficies y cantidades de cada obra.
- **PGAS** (también EAS-PGAS). Evaluación ambiental y social y Plan de Gestión Ambiental y Social, versión 2 (1 de septiembre de 2025): descripción de las obras, temporada de lluvias e informes de seguimiento.
- **MEL** y **ToC.** Plan de monitoreo, evaluación y aprendizaje (EER#2) y teoría del cambio (EER#1). P2.1 a P2.9 son los productos del Componente II; R2.1 y T2 son indicadores de la matriz de resultados.
- **CEPA-EOI.** CEPA, "Expresión de interés pública internacional para la supervisión de la construcción del edificio de estacionamiento en el Aeropuerto Internacional de El Salvador", publicada el 6 de mayo de 2026. https://www.cepa.gob.sv/expresion-de-interes-publica-internacional-para-la-supervision-de-la-construccion-del-edificio-de-estacionamiento-en-el-aeropuerto-internacional-de-el-salvador/
- **Anexo III** (también Anexo III.i). Justificación de la separación de las licitaciones de infraestructura aeroportuaria (septiembre de 2025): cuatro licitaciones separadas, precalificación prevista, revisión ex ante de todos los procesos, contratos FIDIC amarillo, estado de los diseños de cada obra y medidas contra el trabajo forzoso en los paneles solares (GN-3062-1).
- **EDT.** Diccionario de la EDT de este proyecto (sección 5).
- **Matriz.** Matriz de adquisiciones de este proyecto.

### Políticas y guías

- **GN-2349-15** y **GN-2350-15.** Políticas del BID para la adquisición de obras y bienes y para la selección y contratación de consultores. https://www.iadb.org/es/como-trabajar-juntos/adquisiciones/adquisiciones-para-proyectos/marco-de-adquisiciones
- **FAA AC 150/5370-2G.** Operational Safety on Airports During Construction (2017): plan de seguridad y fases de obra con el aeropuerto en operación. https://www.faa.gov/documentLibrary/media/Advisory_Circular/150-5370-2G.pdf
- **FAA-AC.** FAA AC 150/5070-6B, Airport Master Plans: elementos de un plan maestro (inventario, pronósticos, requerimientos, alternativas, plan de desarrollo e implementación).
- **EDGE-P.** IFC, EDGE Certification Protocol, versión 5.0 (2022): autoevaluación y registro, auditoría de diseño y certificado preliminar, auditoría en sitio y certificado final. https://edgebuildings.com/wp-content/uploads/2022/10/EDGE-Certification-Protocol-5.0.pdf
- **GBCSA.** Green Building Council South Africa, proceso de certificación EDGE con rondas de revisión de 4 y 3 semanas. https://www.gbcsa.org.za/edge/
- **ICAO-LB.** Landrum & Brown, "Plan Maestro como un documento vivo, SJO y UIO", OACI, taller ADPLAN 2018. https://www.icao.int/sites/default/files/sp-files/SAM/Documents/2018-ADPLAN/3.4%20Plan%20Maestro%20como%20un%20documento%20vivo%20SJO%20y%20UIO%20%28BFernandez%29.pdf
- **TDR-ANA.** Estructura habitual de los términos de referencia de estudios financiados por el BID (plan de trabajo, diagnóstico, propuesta, borrador, informe final); se usa para la secuencia de pasos, no para las duraciones.

### Proyectos análogos

- **A-TERM.** Plazos de ampliaciones de terminales: Dubái T2 (25 meses), https://www.meed.com/arabtec-wins-contract-to-expand-terminal-2-at-dubai-international-airport ; Gdańsk T2 (18 meses), https://www.ndi.pl/en/signed-a-contract-for-the-extension-of-the-new-passenger-terminal-t2-of-gdansk-airport ; Gran Canaria (36 meses), https://www.fcc.es/en/w/fcc-ampliara-el-aeropuerto-de-gran-canaria-por-124-6-millones-de-euros ; Eindhoven (unos 32 meses con el aeropuerto en operación), https://www.eindhovenairport.nl/en/news-and-media/start-of-project-expansion-of-eindhoven-airport-terminal
- **A-EST.** Estacionamientos aeroportuarios de varios niveles: Jacksonville, 2,000 plazas en unos 19 meses, https://jaxdailyrecord.com/news/2025/apr/15/third-jacksonville-international-airport-parking-garage-taking-off ; Charleston, 2,400 plazas en unos 18 meses, https://www.live5news.com/2019/03/21/new-charleston-airport-parking-garage-will-add-more-than-spaces
- **A-GRR.** Gerald R. Ford International: reconstrucción de unos 128,000 m² de plataforma de concreto en 7 fases durante 2 años (unos 5,300 m² por mes). https://airportimprovement.com/article/gerald-r-ford-international-airport-completes-30-million-apron-reconstruction-project/
- **A-BRU.** Bruselas: renovación de casi 200,000 m² de plataformas de concreto entre 2018 y 2021 con operación diaria. https://airportintelligence.com/en/they-trusted-us/success-stories/apron-renovation-bru
- **A-PBB.** Adelte, Santiago de Compostela: 4 puentes de abordaje contratados en noviembre de 1998 e instalados en junio de 1999. https://www.adelte.com/project/santiago-de-compostela-international-airport/
- **A-TED.** Aviso de licitación 088305-2021 de Shannon: un puente de abordaje, diseño, fabricación, ensayo y montaje en 9 meses. https://ted.europa.eu/en/notice/088305-2021/pdf
- **A-PVM.** pv magazine, 17 de agosto de 2026: nuevo marco regulatorio de autoconsumo solar en El Salvador. https://www.pv-magazine.com/2026/08/17/el-salvador-launches-regulatory-framework-for-solar-self-consumption/

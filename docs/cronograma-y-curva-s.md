# Cronograma, ruta crítica y curva S

Cronograma del programa ES-L1173 construido a partir del listado de actividades (`docs/listado-actividades.md`): 449 actividades con estimación PERT, agrupadas en los 54 paquetes de trabajo de la EDT, y 10 hitos. Los paquetes son filas resumen que empiezan con su primera actividad y terminan con la última. El cálculo está en `planificacion/build_planificacion.py`; el Gantt exportado de Open Planner Studio está en `planificacion/cronograma_ES-L1173_gantt.pdf`, la tabla completa con duraciones, fechas, predecesoras y holguras en `planificacion/cronograma_ES-L1173_anexo_tabla.pdf` y el archivo para Open Planner o MS Project en `planificacion/cronograma_ES-L1173.xml`.

## Supuestos del cronograma

- Calendario de lunes a viernes, 8 horas por día, sin feriados. Inicio el 2 de febrero de 2026, días después de la ratificación del préstamo (29 de enero de 2026).
- La duración de cada actividad es su duración estimada PERT, De = (O + 4M + P) / 6, redondeada al día laborable entero. Las precedencias son las de la tabla de dependencias del listado (fin a inicio, inicio a inicio y fin a fin, con desfase).
- 43 actividades tienen una restricción "no comenzar antes de" con una fecha documentada. Con ellas el cronograma reproduce las fechas reales de 2026: incorporación de la UEP (abril y mayo), Aviso General de Adquisiciones (5 de mayo), avisos de licitación del estacionamiento (4 de septiembre) y de la terminal (8 de octubre), y las firmas que estima el Plan de Adquisiciones 2026-2 para las obras (27 de enero, 24 de abril, 27 de mayo y 22 de julio de 2027) y las supervisiones (3 de febrero, 19 de mayo, 10 de junio y 28 de julio de 2027). El 24 de abril de 2027 es sábado y el calendario del modelo es de lunes a viernes, así que la firma de la terminal cae el viernes 23 de abril de 2027.
- 13 actividades de seguimiento son de nivel de esfuerzo (supervisión, PGAS, mecanismo de quejas, informes socioambientales y desembolsos): duran lo que el trabajo que acompañan y no fijan el fin del programa.
- Condiciones del contrato de préstamo reflejadas como dependencias: el Plan de Gestión del Riesgo de Desastres y Cambio Climático final antes de cualquier obra, el protocolo de seguridad operacional aprobado por la AAC antes de las obras del lado aire y el SSEI funcionando antes de la plataforma remota.
- Los supuestos de cada actividad, las inconsistencias entre fuentes y las fuentes están en las secciones 9 a 11 del listado de actividades.

## Hitos

| Hito | Fecha |
|---|---|
| H01 Unidad Ejecutora conformada | 15-may-2026 |
| H02 Condiciones previas al primer desembolso cumplidas (ROP, convenio, cuenta) | 10-jul-2026 |
| H04 Protocolo de seguridad operacional aprobado por la AAC | 11-mar-2027 |
| H03 Contratos de obra y de supervisión firmados | 28-jul-2027 |
| H05 SSEI reubicado y en funcionamiento | 24-feb-2028 |
| H08 Estacionamiento con sistema solar concluido | 31-may-2028 |
| H06 Plataforma de posiciones remotas concluida | 31-ago-2028 |
| H07 Terminal ampliada concluida y equipada | 16-mar-2029 |
| H09 Obras recibidas (planos de obra ejecutada y actas aprobados) | 5-jul-2029 |
| H10 Cierre administrativo del programa | 1-abr-2030 |

## Ruta crítica

Duración total: 1,086 días laborables, del 2 de febrero de 2026 al 1 de abril de 2030.

La ruta crítica tiene 26 actividades: 3.4.1-21 (publicar el aviso específico de adquisiciones de las plataformas y la calle Foxtrot y recibir ofertas hasta la apertura), 3.4.1-22 (evaluar las ofertas de las plataformas y la calle Foxtrot y elaborar el informe de evaluación), 3.4.1-23 (obtener la no objeción del BID a la evaluación y a la recomendación de adjudicación de las plataformas y la calle Foxtrot), 3.4.1-24 (adjudicar y firmar el contrato de obra de las plataformas y la calle Foxtrot), 1.7.3-04 (revisar y aprobar el PGAS de construcción del contratista de plataformas y Foxtrot), 1.3.1-01 (movilizar al contratista de plataformas y Foxtrot e instalar el cerramiento y los accesos del lado aire), 1.3.1-02 (construir la terracería, el drenaje y la base de la fase 1 de la plataforma de contacto), 1.3.1-03 (colar el pavimento de concreto de la fase 1 de la plataforma de contacto y sellar las juntas), 1.3.1-04 (construir la terracería, el drenaje y la base de la fase 2 de la plataforma de contacto), 1.3.1-05 (colar el pavimento de concreto de la fase 2 de la plataforma de contacto y sellar las juntas), 1.2.4-03 (instalar y conectar los seis puentes de abordaje a la terminal y a la plataforma), 3.4.4-36 (preparar los términos de referencia y la solicitud de expresiones de interés de la evaluación final), 1.2.4-05 (probar los equipos, capacitar al personal de CEPA y entregar los manuales), 3.4.4-37 (publicar la solicitud de expresiones de interés y conformar la lista corta nacional de la evaluación final), 3.4.4-43 (obtener la no objeción del BID a los términos de referencia y a la lista corta de la evaluación final), 3.4.4-38 (invitar a las firmas de la lista corta y recibir las propuestas de la evaluación final), 1.2.4-06 (realizar las pruebas integradas de operación de la terminal con las aerolíneas y las autoridades), 3.4.4-39 (evaluar las propuestas y negociar el contrato de la evaluación final), 3.4.4-44 (obtener la no objeción del BID al informe de evaluación y al contrato negociado de la evaluación final), 3.4.4-40 (adjudicar y firmar el contrato de la evaluación final), 3.5.3-04 (ejecutar la evaluación final de efectividad sin atribución empírica), 3.5.3-05 (revisar el informe de evaluación final y presentarlo al BID), 3.5.4-02 (justificar los anticipos pendientes y tramitar el último desembolso), 3.5.4-03 (auditar y presentar al BID los estados financieros finales del programa), 3.5.4-04 (preparar y entregar al BID los insumos de la UEP para el informe de terminación del programa, con las lecciones aprendidas), 3.5.4-06 (cerrar el expediente administrativo del programa y archivar los documentos).

Empieza con la licitación de las plataformas y la calle Foxtrot, la última de las cuatro licitaciones de obra, sigue con la construcción de la plataforma de contacto en dos fases y pasa a la terminal, porque los puentes de abordaje se conectan a esa plataforma. Después vienen las pruebas integradas de la terminal, la evaluación final, el último desembolso, los estados financieros finales auditados, el informe de terminación y el cierre administrativo. La evaluación final está en la ruta porque se contrata con el fin de la terminal y el cierre la espera.

Actividades casi críticas (holgura de 10 días laborables o menos):

| Actividad | Holgura (dl) |
|---|---:|
| 1.7.2-01 Movilizar a la firma de supervisión de plataformas y calle Foxtrot | 4 |
| 3.4.2-19 Preparar los términos de referencia, la solicitud de expresiones de interés y la lista corta de la supervisión de las plataformas y la calle Foxtrot | 4 |
| 3.4.2-20 Obtener la no objeción del BID a los términos de referencia y a la lista corta de la supervisión de las plataformas y la calle Foxtrot | 4 |
| 3.4.2-21 Invitar a las firmas de la lista corta y recibir las propuestas de la supervisión de las plataformas y la calle Foxtrot | 4 |
| 3.4.2-22 Evaluar las propuestas técnicas y económicas y negociar el contrato de la supervisión de las plataformas y la calle Foxtrot | 4 |
| 3.4.2-23 Obtener la no objeción del BID al informe de evaluación combinado y al contrato negociado de la supervisión de las plataformas y la calle Foxtrot | 4 |
| 3.4.2-24 Firmar el contrato de supervisión de las plataformas y la calle Foxtrot | 4 |
| 3.1.1-01 Incorporar al Coordinador del Programa, al Coordinador general de obra y al Especialista de planificación y monitoreo | 10 |
| 3.1.1-06 Administrar el programa desde la Unidad Ejecutora | 10 |
| 3.4.4-01 Preparar los términos de referencia y la convocatoria de los siete consultores clave de la UEP | 10 |
| 3.4.4-02 Obtener la no objeción del BID a los términos de referencia de los siete consultores clave | 10 |
| 3.4.4-03 Recibir los currículos, evaluar y seleccionar a los siete consultores clave | 10 |
| 3.4.4-04 Obtener la no objeción del BID a la selección de los siete consultores clave | 10 |
| 3.4.4-05 Firmar los contratos de los siete consultores clave de la UEP | 10 |
| 3.5.4-05 Devolver los saldos no justificados al BID y cerrar la cuenta especial | 10 |

## Reserva de contingencia del cronograma

La clase 5 pide una reserva de tiempo explícita. Con la estimación de tres valores, la desviación de cada actividad es σ = (P − O) / 6, y la de la ruta crítica es la raíz de la suma de los cuadrados de sus actividades: σ = 19.6 días laborables. Para cumplir el fin con 80% de probabilidad se agregan 17 días laborables (0.84 σ), es decir hasta el 24 de abril de 2030; con 90% de probabilidad, 26 días laborables (1.28 σ), hasta el 7 de mayo de 2030. La reserva no se reparte entre las actividades: la administra el coordinador del programa y se consume solo si se materializan los atrasos. Es una aproximación: supone actividades independientes y no considera que una ruta casi crítica pueda volverse crítica.

## Curva S

La curva muestra el valor planificado acumulado, no desembolsos ni pagos. Su total es la línea base de costos (BAC) de US$160.3 millones: la estimación propia de los paquetes de trabajo (US$148.2 millones, valor esperado PERT) más la reserva de contingencia (US$12.1 millones, percentil 80). Con la reserva de gestión (US$8.0 millones, fuera de la línea base) el presupuesto del proyecto suma US$168.3 millones, US$26.7 millones por debajo del préstamo de US$195 millones. La composición de la estimación y sus fuentes están en `docs/estimacion-costos.md` y la curva en `planificacion/curva_s_ES-L1173.pdf`.

Como pide la clase 6, la curva suma mes a mes el costo de las actividades. El costo de cada paquete se asigna a las actividades de quien cobra el contrato (contratista, firma de supervisión, firma consultora o auditor) con pesos por elemento de costo y por actividad según el recurso: movilización y pruebas 2% (3% en las pruebas de 1.2.4-05 del mobiliario y de los sistemas de la terminal), informe final de la supervisión 4%, puentes de abordaje 85% a su fabricación y 11% a su instalación, sistemas de la terminal a su instalación, y el resto de cada elemento entre sus actividades de construcción en proporción a su duración (el listado no da cantidades de obra comparables entre actividades distintas). La supervisión se reparte antes entre sus cuatro contratos según el costo de la obra que supervisa, e incluye el seguimiento del PGAS y el apoyo a las recepciones. Las actividades de la UEP, CEPA, el BID y la AAC no tienen costo propio, salvo el costo indirecto de la UEP (US$3.9 millones con su contingencia), que lleva la actividad de nivel de esfuerzo 3.1.1-06. El diseño final de la fachada sur de la terminal tampoco tiene costo propio: 1.1.1-06 (del contratista) está dentro del precio del contrato de obra, que es de diseño y construcción (T1), y 1.1.1-07 (de la supervisión) dentro del contrato de supervisión (V1); que lo diseñe el contratista es una inferencia (S-I.8). Tienen costo 125 actividades; su costo y los elementos que lo forman están en `planificacion/cronograma_actividades.csv`.

| Año | Gasto del año (US$ M) | Acumulado (US$ M) | Avance |
|---|---:|---:|---:|
| 2026 | 0.4 | 0.4 | 0.3% |
| 2027 | 63.7 | 64.2 | 40.0% |
| 2028 | 93.3 | 157.4 | 98.2% |
| 2029 | 2.6 | 160.0 | 99.8% |
| 2030 | 0.3 | 160.3 | 100.0% |

Interpretación:

- Hasta la firma del primer contrato de obra (estacionamiento, 27 de enero de 2027) el valor planificado acumulado es de US$0.5 millones (0.3% del total) y es solo de la UEP: la revisión de diseños y la contratación no tienen costo propio. Los cuatro contratos de obra y de supervisión están firmados en H03 (28 de julio de 2027).
- Aceleración (febrero de 2027 a marzo de 2028): las obras se encadenan por contrato, con inicio de obra en estacionamiento (16-feb-2027), terminal (27-may-2027), SSEI (18-jun-2027) y plataformas (11-ago-2027). El valor mensual sube de US$0.3 millones a US$13.4 millones, el máximo de todo el programa, en marzo de 2028, con aportes de la terminal (US$8.8 millones), el estacionamiento y el sistema solar (US$3.0 millones), las plataformas y la calle Foxtrot (US$1.2 millones) y la supervisión de las obras (US$0.3 millones). En este tramo se alcanza el 25% en octubre de 2027 y el 50% en febrero de 2028.
- Desaceleración (abril de 2028 a abril de 2030): el valor mensual baja desde el pico y se alcanza el 75% en junio de 2028 y el 90% en septiembre de 2028. Al cierre de septiembre de 2028 ya concluyeron SSEI reubicado y en funcionamiento (H05, febrero de 2028), estacionamiento con sistema solar concluido (H08, mayo de 2028) y plataforma de posiciones remotas concluida (H06, agosto de 2028); quedan por ejecutar la terminal (US$9.7 millones), las plataformas y la calle Foxtrot (US$1.5 millones) y la supervisión de las obras (US$1.2 millones). Después del fin de la terminal (H07, 16 de marzo de 2029) quedan US$1.5 millones (0.9% de la línea base): US$0.2 millones de la supervisión y la recepción de las obras y US$1.2 millones de la UEP, las auditorías y las evaluaciones.

Distribución de cada actividad en el tiempo:

| Tipo de actividad | Distribución | Fundamento |
|---|---|---|
| Todas las actividades con costo, salvo 3.1.1-06 | Lineal en su duración (días laborables) | Es valor planificado: la forma de S sale de la secuencia del cronograma (pocas actividades al inicio, muchas en paralelo en 2027 y 2028, pocas al cierre), no de una función impuesta. Los pagos contra entrega y los anticipos no están en la curva. |
| Costo indirecto de la UEP (3.1.1-06) | Mensual por puesto desde su contratación | Es un flujo mensual por plaza: siete consultores clave desde abril y mayo de 2026, el técnico de apoyo y la plantilla ampliada del Plan de Adquisiciones desde sus firmas en el cronograma. |

Sensibilidad de la forma: con la curva DHSS del Reino Unido para contratos grandes (Hudson, 1978; C = 0.063, K = 3.344) aplicada a cada contrato de obra en todo su plazo, la curva acumulada cambia como máximo US$6.4 millones y el 25%, 50%, 75% y 90% se alcanzan en octubre de 2027, febrero de 2028, junio de 2028 y octubre de 2028.

Costo real a la fecha de corte (31 de octubre de 2026): US$0.24 millones estimados, que son los honorarios mensuales de los siete contratos de la UEP en ejecución (Plan de Adquisiciones 2026-2) por los meses transcurridos desde su inicio. Es un costo incurrido estimado, no un desembolso del BID, que no registra desembolsos publicados. El valor planificado a esa fecha es de US$0.30 millones.

## Requisitos de financiamiento frente a los desembolsos del préstamo

El Plan de Ejecución del Programa (PEP, noviembre de 2025) reparte los US$195 millones del préstamo en ocho semestres desde enero de 2026 (hoja Payments Flow). En la hoja Payments, cada contrato recibe un pago en el semestre de su firma, y el porcentaje no es uniforme (obra y supervisión: terminal 30% y 30%, estacionamiento 30% y 30%, plataformas y Foxtrot 45% y 35% y SSEI 15% y 35%). Que ese pago sea un anticipo es una inferencia: los avisos de adquisiciones no lo mencionan. La tabla compara los desembolsos del PEP con los requisitos de financiamiento, que son la línea base más la reserva de gestión (clase 6) en proporción al valor planificado de cada semestre, y con los mismos requisitos más ese anticipo, que se paga en el semestre de la firma de cada contrato y se amortiza descontando el mismo porcentaje de cada avance, sobre la base sin contingencia (millones de US$; detalle en `planificacion/requisitos_financiamiento.csv`).

| Semestre | Desembolso PEP | Acumulado PEP | Requisito | Acumulado | Requisito con anticipo | Acumulado | Diferencia acumulada con anticipo (PEP menos requisito) |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2026-S1 | 0.61 | 0.61 | 0.11 | 0.11 | 0.11 | 0.11 | 0.50 |
| 2026-S2 | 58.37 | 58.97 | 0.36 | 0.46 | 0.36 | 0.46 | 58.51 |
| 2027-S1 | 29.45 | 88.42 | 10.73 | 11.19 | 44.95 | 45.41 | 43.01 |
| 2027-S2 | 29.15 | 117.57 | 56.19 | 67.38 | 50.12 | 95.53 | 22.05 |
| 2028-S1 | 29.41 | 146.98 | 66.40 | 133.79 | 47.81 | 143.33 | 3.65 |
| 2028-S2 | 22.58 | 169.56 | 31.53 | 165.32 | 22.34 | 165.67 | 3.89 |
| 2029-S1 | 12.63 | 182.18 | 1.87 | 167.19 | 1.56 | 167.23 | 14.95 |
| 2029-S2 | 12.82 | 195.00 | 0.82 | 168.02 | 0.79 | 168.02 | 26.98 |
| 2030-S1 | 0.00 | 195.00 | 0.29 | 168.31 | 0.29 | 168.31 | 26.69 |

- El monto alcanza: el programa necesita US$160.3 millones de línea base (US$168.3 millones con la reserva de gestión) frente a US$195 millones. La diferencia con el PEP es de calendario, no de monto.
- El PEP preveía desembolsar US$59.0 millones hasta diciembre de 2026, con licitaciones y firmas en 2026. Como el primer contrato de obra se firma el 27 de enero de 2027, en 2026 el programa solo necesita US$0.5 millones: los US$29.7 millones que la reforma a la Ley de Presupuesto 2026 asignó al estacionamiento no se ejecutarán ese año y deben pasar al presupuesto de 2027.
- Es una reprogramación del PEP, no una falta de fondos: el PEP acumulado va por delante del requisito con anticipo en todos los semestres, entre US$0.5 y US$58.5 millones. El PEP llega al 25% en 2026-S2, al 50% en 2027-S2 y al 75% en 2028-S1 del préstamo, y el requisito con anticipo al 25% en 2027-S2, al 50% en 2028-S1 y al 75% en 2028-S2: un desfase de 1 a 2 semestres. Por año, el PEP prevé US$58.6 millones en 2027 y US$52.0 millones en 2028, frente a los US$95.1 y US$70.1 millones que requiere el programa; en 2026 y 2029 ocurre lo contrario. Hay que reprogramar el PEP y los POA 2027 y 2028 y las asignaciones de las leyes de presupuesto de 2027 y 2028, y dimensionar los anticipos de fondos que la UEP pide al BID.
- El último desembolso se tramita el 13 de diciembre de 2029 (3.5.4-02), dentro del plazo original de desembolsos, que vence el 29 de enero de 2031: cinco años desde la vigencia, que se supone el 29 de enero de 2026 (ratificación D.L. 505; falta la fecha de publicación, cláusula 6.01).
- El requisito de US$0.29 millones en 2030-S1 cae después del último desembolso (13 de diciembre de 2029): se cubre con el último anticipo de fondos o con el saldo de la cuenta especial.

## Evaluaciones

La cláusula 5.03(a) del contrato exige presentar la evaluación de medio término a más tardar 60 días después de que se haya desembolsado el 50% de los recursos o haya transcurrido el 50% del tiempo de ejecución planificado, lo que ocurra primero. El plazo no se mide sobre el plazo de desembolsos. El tiempo de ejecución planificado es el del cronograma, del 2 de febrero de 2026 al 1 de abril de 2030: el 50% se cumple el 2 de marzo de 2028 y el límite es el 1 de mayo de 2028. Con los requisitos de financiamiento de la tabla (con anticipo y con reserva de gestión), el 50% del préstamo se desembolsa en enero de 2028 y el límite es el 31 de marzo de 2028. El informe está programado para el 13 de marzo de 2028 (contrato de la evaluación firmado el 1 de noviembre de 2027): 35 días laborables antes del límite por tiempo y 14 antes del límite por desembolso, que es el primero, y cumple.

Riesgo: un desembolso no es un gasto. Las Normas Generales (art. 4.07) permiten anticipos de fondos para la liquidez de hasta 6 meses, así que el 50% desembolsado podría llegar antes que el 50% gastado. Si los desembolsos siguieran el PEP, el 50% llegaría el 31 de diciembre de 2027 y el plazo vencería el 29 de febrero de 2028, antes del informe programado. Con un anticipo de 6 meses, el 50% se desembolsaría en julio de 2027 y el plazo vencería el 29 de septiembre de 2027, antes de la firma del contrato de la evaluación. La actividad 3.5.3-01 proyecta el hito con los contratos firmados y la UEP debe pactar con el BID el monto de los anticipos o adelantar la contratación de la evaluación.

La evaluación final vence hasta 90 días después de terminar el plazo original de desembolsos o de desembolsar el 95% del préstamo, lo que ocurra primero. La línea base no llega al 95% del préstamo, así que vence 90 días después del fin del plazo de desembolsos (29 de enero de 2031), es decir el 29 de abril de 2031; su informe está programado para el 15 de noviembre de 2029. El plazo de desembolsos de cinco años (cláusula 2.04) cuenta desde la vigencia del contrato (cláusula 6.01), que se supone el 29 de enero de 2026.

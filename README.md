# proyecto-api-aeropuerto

Tarea de aplicación de Administración de Proyectos Informáticos (Escuela de Ingeniería de Sistemas Informáticos, Universidad de El Salvador): planificar la implementación de un proyecto con herramientas de gestión y procesos del PMBOK. El proyecto base es el Programa de Modernización del Aeropuerto Internacional de El Salvador (ES-L1173, BID).

## Entregables

- Acta de constitución del proyecto (propósito, objetivos, alcance, interesados, restricciones, supuestos y responsable).
- Los 7 entregables, cada uno vinculado a procesos del PMBOK y coherentes entre sí: EDT con diccionario, cronograma con ruta crítica, curva S, matriz de adquisiciones, matriz de riesgos, plan de comunicaciones y MAR (RACI).
- Documento final impreso (portada, índice, introducción, objetivos, desarrollo, conclusiones, recomendaciones, glosario, referencias y anexos) y la planificación en la herramienta elegida.

## Contenido del repositorio

- `indicaciones.md`: enunciado de la tarea.
- `docs/ingest/`: documentos fuente del estudio de factibilidad en Markdown.
- `docs/documento-final/`: secciones del documento final que no son entregables (introducción, objetivos, descripción del proyecto, conclusiones, recomendaciones, glosario, referencias y anexos).
- `scripts/build_documento.py`: arma el documento final en Word y PDF sobre la plantilla `docs/Proyecto API Base.docx` a partir de los `.md` de `docs/`, genera los anexos C y D, y deja todo en `entrega/` junto con los demás anexos y el cronograma en XML. Las correcciones se hacen en los `.md` y se vuelve a ejecutar `python -B scripts/build_documento.py` (requiere Word y Edge en Windows).
- `entrega/`: el documento final (`.docx` y `.pdf`), los anexos A a F en PDF y el cronograma para MS Project y Open Planner Studio.

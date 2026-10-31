#!/usr/bin/env python3
"""Genera la matriz de adquisiciones del programa (CSV y PDF A4 horizontal).

Base: Anexo III de la Propuesta de Préstamo (sección V, adquisiciones clave), la EDT (docs/edt.md) y el cronograma
(cronograma_paquetes.csv). Campos según la consigna (bien/servicio, justificación, modalidad, responsable, fecha requerida)
y los campos mínimos de la clase 7. Escribe matriz_adquisiciones.csv y matriz_adquisiciones_ES-L1173.pdf. Requiere PyMuPDF.
"""
from __future__ import annotations
import csv
import io
import json
from datetime import date
from html import escape
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
MESES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
pk = {r['code']: r for r in csv.DictReader((HERE / 'cronograma_paquetes.csv').open(encoding='utf-8-sig'))}
RES = json.loads((HERE / 'resumen.json').read_text(encoding='utf-8'))
EV = RES['evaluaciones']  # medio término y final, programadas desde el paquete 3.5.3


def m(d: str | date) -> str:
    d = date.fromisoformat(d) if isinstance(d, str) else d
    return f'{MESES[d.month - 1]}-{d.year}'


def ML(d: str) -> str:
    d = date.fromisoformat(d)
    return f"{['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'][d.month - 1]} de {d.year}"


def start(c): return pk[c]['start']
def finish(*cs): return max(pk[c]['finish'] for c in cs)


ADQ, OBRA, TEC, PLAN, SOC, COORD = ('Especialista de adquisiciones', 'Coordinador general de obra', 'Especialista técnico',
                                    'Especialista de planificación y monitoreo', 'Especialista socioambiental', 'Coordinador del Programa')

# (grupo, EDT, producto MR, adquisición, tipo, cantidad, justificación, modalidad, monto US$, inicio, firma, entrega,
#  inicio estimado en el Anexo III, responsable del proceso, área requirente, ruta crítica)
OBRAS = ('1.2.1', '1.2.2', '1.2.3', '1.2.4', '1.2.5'), ('1.3.1', '1.3.2', '1.3.3', '1.4.1', '1.4.2'), ('1.5.1', '1.5.2', '1.5.3'), ('1.6.1', '1.6.2')
c341 = (m(start('3.4.1')), m(finish('3.4.1')))
c342 = (m(start('3.4.2')), m(finish('3.4.2')))
c343 = (m(start('3.4.3')), m(finish('3.4.3')))
ROWS = [
    ('Obras', '1.2.1 a 1.2.5', 'P1.1.1', 'Ampliación de la terminal de pasajeros (fase 2), con accesibilidad universal y movilidad del cuidado', 'Obra', '1 contrato',
     'Elevar el espacio por pasajero en hora pico de 1.89 a 2.24 m² con seis salas de espera y posiciones de contacto. Por su magnitud se licita con precalificación de empresas.',
     'LPI', 78_992_537, *c341, m(finish(*OBRAS[0])), 'sep-2026', ADQ, OBRA, True),
    ('Obras', '1.3.1 a 1.4.2', 'P1.1.2, P1.1.3', 'Plataformas de posiciones de contacto y remotas, y calle de rodaje Foxtrot', 'Obra', '1 contrato',
     'Dar servicio a las nuevas posiciones de contacto, reponer las posiciones remotas y reducir el tiempo de rodaje en 28%. Las obras del lado aire requieren el protocolo aprobado por la AAC.',
     'LPI', 23_206_513, *c341, m(finish(*OBRAS[1])), 'ago-2026', ADQ, OBRA, True),
    ('Obras', '1.5.1 a 1.5.3', 'P1.2.1', 'Edificio de estacionamiento con accesibilidad universal y sistema de generación solar', 'Obra', '1 contrato',
     'Mantener la ocupación del estacionamiento en 75% con la demanda de 2031 y generar energía solar para el aeropuerto.',
     'LPI', 64_202_613, *c341, m(finish(*OBRAS[2])), 'dic-2026', ADQ, OBRA, True),
    ('Obras', '1.6.1, 1.6.2', 'P1.3.1', 'Edificio del Servicio de Salvamento y Extinción de Incendios (SSEI)', 'Obra', '1 contrato',
     'El SSEI debe estar reubicado y en operación antes de iniciar la plataforma de posiciones remotas (condición especial de ejecución).',
     'SBCC', 9_473_574, *c341, m(finish(*OBRAS[3])), 'ene-2027', ADQ, OBRA, True),
    ('Servicios de consultoría y auditoría (firmas)', '1.7.1 a 1.7.4', 'P1.4.1 a P1.4.3', 'Supervisión técnica, ambiental y social de las obras', 'Consultoría', '1 contrato',
     'Control independiente de calidad, estimaciones, PGAS y recepción. Un solo contrato cubre las cuatro obras.',
     'SBCC', 8_793_763, *c342, m(finish('1.7.1', '1.7.2', '1.7.3', '1.7.4')), 'sep-2026', ADQ, OBRA, False),
    ('Servicios de consultoría y auditoría (firmas)', '2.1', 'P2.1', 'Plan Estratégico para el Desarrollo del Sistema Aeronáutico', 'Consultoría', '1 contrato',
     'Orientar el desarrollo del sistema aeronáutico nacional (objetivo específico 2: capacidad institucional de CEPA).',
     'SBCC', 800_000, *c343, m(finish('2.1')), 'jun-2026', ADQ, PLAN, False),
    ('Servicios de consultoría y auditoría (firmas)', '2.2.1, 2.2.2', 'P2.2', 'Actualización del Plan Maestro Aeroportuario y capacitación de funcionarios', 'Consultoría', '1 contrato',
     'Actualizar el Plan Maestro con la demanda vigente y capacitar a 21 funcionarios en planificación, gestión y operación.',
     'SBCC', 3_000_000, *c343, m(finish('2.2.2')), 'jun-2026', ADQ, PLAN, False),
    ('Servicios de consultoría y auditoría (firmas)', '2.3.1 a 2.6.2', 'P2.3, P2.6', 'Estrategia y capacitación BIM, y auditoría y capacitación para la certificación EDGE', 'Consultoría', '1 contrato',
     'Adoptar BIM en CEPA y certificar EDGE las nuevas edificaciones. Se agrupan en un contrato por ser servicios técnicos afines.',
     'SCC', 275_000, *c343, m(finish('2.3.2', '2.6.1', '2.6.2')), 'jun-2026', ADQ, TEC, False),
    ('Servicios de consultoría y auditoría (firmas)', '2.4', 'P2.4', 'Estudio de conectividad terrestre del aeropuerto con enfoque de sostenibilidad e inclusión', 'Consultoría', '1 contrato',
     'Mejorar el acceso terrestre desde San Salvador y los destinos turísticos.',
     'SBCC', 350_000, *c343, m(finish('2.4')), 'ene-2027', ADQ, PLAN, False),
    ('Servicios de consultoría y auditoría (firmas)', '2.5', 'P2.5', 'Estudio de mercado para la diversificación de orígenes y destinos internacionales', 'Consultoría', '1 contrato',
     'Priorizar mercados y destinos que aumenten la conectividad aérea del país.',
     'SBCC', 350_000, *c343, m(finish('2.5')), 'ene-2027', ADQ, PLAN, False),
    ('Servicios de consultoría y auditoría (firmas)', '2.7', 'P2.7', 'Estudio de obras para separar los flujos de llegadas y salidas en la terminal antigua', 'Consultoría', '1 contrato',
     'Identificar y priorizar las intervenciones de la terminal existente.',
     'SCC', 100_000, *c343, m(finish('2.7')), 'mar-2027', ADQ, TEC, False),
    ('Servicios de consultoría y auditoría (firmas)', '2.8', 'P2.8', 'Estudio de movilidad del entorno del aeropuerto, con énfasis en el estacionamiento', 'Consultoría', '1 contrato',
     'Resolver los flujos vehiculares hacia el nuevo estacionamiento y las zonas de dejar y recoger pasajeros.',
     'SCC', 100_000, *c343, m(finish('2.8')), 'dic-2026', ADQ, TEC, False),
    ('Servicios de consultoría y auditoría (firmas)', '2.9', 'P2.9', 'Programa de capacitación en igualdad de oportunidades e inclusión de personas con discapacidad', 'Consultoría', '1 contrato',
     'Capacitar a 300 funcionarios de CEPA.',
     'SCC', 25_000, *c343, m(finish('2.9')), 'nov-2026', ADQ, SOC, False),
    ('Servicios de consultoría y auditoría (firmas)', '3.5.3', 'P3.2.1, P3.2.2', 'Evaluaciones de medio término y de cierre', 'Consultoría', '2 contratos',
     'Medir el avance y los resultados a mitad de la ejecución y al cierre, según el plan de monitoreo y evaluación (MEL).',
     'SCC', 300_000, *(' / '.join(m(e[k]) for e in EV) for k in ('inicio_proceso', 'firma', 'informe')), 'nov-2027 / may-2029', ADQ, PLAN, False),
    ('Servicios de consultoría y auditoría (firmas)', '3.5.2', '', 'Auditoría externa de los estados financieros del programa', 'Servicio de auditoría', '1 contrato plurianual',
     'Estados financieros auditados anuales y finales, exigidos por el BID y realizados por una firma aceptable para el Banco.',
     'SBMC', 350_000, 'dic-2026', 'mar-2027', m(finish('3.5.4')), 'no figura', ADQ, 'Especialista financiero', False),
    ('Consultores individuales', '3.1.1', 'P3.3.1 a P3.3.7', 'Personal clave de la Unidad Ejecutora del Programa', 'Consultoría individual', '7 consultores',
     'Condición previa al primer desembolso: coordinador, coordinador general de obra y especialistas de adquisiciones, finanzas, planificación, técnico y socioambiental, con dedicación exclusiva.',
     '3CV', 4_071_000, m(start('3.1.1')), m(finish('3.1.1')), f"{m(RES['fin'])} (todo el programa)", 'feb-2026', 'CEPA (organismo ejecutor)', COORD, True),
]
TOTAL = sum(r[8] for r in ROWS)
OTROS = 195_000_000 - TOTAL
assert TOTAL == 194_390_000 and OTROS == 610_000, (TOTAL, OTROS)

FIELDS = ['grupo', 'edt', 'producto_mr', 'adquisicion', 'tipo', 'cantidad', 'justificacion', 'modalidad', 'monto_usd', 'inicio_proceso',
          'firma_contrato', 'entrega_requerida', 'inicio_anexo_iii', 'responsable', 'area_requirente', 'ruta_critica']
with (HERE / 'matriz_adquisiciones.csv').open('w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(FIELDS)
    for r in ROWS:
        w.writerow([*r[:15], 'Sí' if r[15] else 'No'])

# ---------------- PDF ----------------
RED, BLUE, PURPLE, INK, MUTED, GRID = '#dc2626', '#2563eb', '#7c3aed', '#1f2430', '#5b6270', '#e3e6ea'
CSS = f'''
body {{ font-family: sans-serif; font-size: 6.9pt; color: {INK}; }}
h1 {{ font-size: 13pt; margin: 0 0 3pt 0; }}
h2 {{ font-size: 9.5pt; margin: 7pt 0 3pt 0; color: {INK}; }}
p {{ margin: 0 0 3pt 0; font-size: 7.6pt; }}
p.nota {{ font-size: 7pt; color: {MUTED}; }}
ul {{ margin: 0 0 0 12pt; padding: 0; }}
li {{ margin: 0 0 2.5pt 0; font-size: 7.6pt; }}
table {{ border-collapse: collapse; width: 100%; }}
th {{ background-color: #f1f3f6; color: #444a57; text-align: left; padding: 3pt 2pt; font-size: 6.8pt; border-bottom: 1pt solid #9ca3af; vertical-align: bottom; }}
td {{ padding: 2.5pt 2.5pt; border-bottom: 0.4pt solid {GRID}; vertical-align: top; }}
td.n {{ text-align: right; white-space: nowrap; }}
td.k {{ font-weight: bold; color: {BLUE}; }}
td.d {{ white-space: nowrap; }}
td.ref {{ color: {MUTED}; font-size: 6.4pt; }}
tr.c td.k, td.s {{ color: {RED}; font-weight: bold; }}
tr.g td {{ background-color: #f3effd; color: {PURPLE}; font-weight: bold; font-size: 7.2pt; }}
tr.t td {{ font-weight: bold; border-top: 1pt solid #9ca3af; }}
tr.o td {{ color: {MUTED}; }}
table.id td {{ border-bottom: 0; padding: 0.8pt 8pt 0.8pt 0; font-size: 7.6pt; }}
table.gl td {{ font-size: 7.4pt; padding: 2pt 4pt; }}
'''
HEAD = ('<tr><th style="width:3%">N.º</th><th style="width:6%">EDT</th><th style="width:16.5%">Bien, servicio u obra</th><th style="width:7%">Tipo y cantidad</th>'
        '<th style="width:21%">Justificación</th><th style="width:5%">Modalidad</th><th style="width:7.5%">Monto (US$)</th>'
        '<th style="width:7.5%">Inicio del proceso</th><th style="width:6%">Firma del contrato</th><th style="width:6.5%">Entrega requerida</th>'
        '<th style="width:11%">Responsable / área requirente</th><th style="width:3%">Crítica</th></tr>')

def wide(cls: str, text: str, amount: int) -> str:
    return (f'<tr class="{cls}"><td></td><td></td><td>{escape(text)}</td><td></td><td></td><td></td><td class="n">{amount:,.0f}</td>'
            + '<td></td>' * 5 + '</tr>')


body, group, n = [], None, 0
for r in ROWS:
    if r[0] != group:
        group = r[0]
        sub = sum(x[8] for x in ROWS if x[0] == group)
        body.append(wide('g', group, sub))
    n += 1
    (_, edt, mr, adq, tipo, cant, just, mod, monto, ini, firma, ent, anexo, resp, req, crit) = r
    anexo_txt = '' if anexo == ini else f'<br><span style="color:{MUTED};font-size:6.2pt">Anexo III: {anexo}</span>'
    body.append(f'<tr class="{"c" if crit else ""}"><td>{n}</td><td class="k">{edt}</td>'
                f'<td>{escape(adq)}<br><span style="color:{MUTED};font-size:6.2pt">{("Producto " + mr) if mr else "Requisito fiduciario"}</span></td>'
                f'<td>{escape(tipo)}<br>{escape(cant)}</td><td>{escape(just)}</td><td><b>{mod}</b></td><td class="n">{monto:,.0f}</td>'
                f'<td>{ini.replace(" / ", "<br>")}{anexo_txt}</td><td>{firma.replace(" / ", "<br>")}</td><td>{ent.replace(" / ", "<br>")}</td>'
                f'<td>{escape(resp)}<br><span style="color:{MUTED}">{escape(req)}</span></td><td class="{"s" if crit else ""}">{"Sí" if crit else "No"}</td></tr>')
body.append(wide('t', 'Total de la matriz', TOTAL))
body.append(wide('o', 'Gastos no derivados de adquisiciones y operación de la UEP (paquetes 3.3.2, 3.3.3, 3.3.4 y 3.5.4)', OTROS))
body.append(wide('t', 'Presupuesto del programa', 195_000_000))

ID = ('<table class="id"><tr><td><b>Proyecto</b></td><td>Programa de Modernización del Aeropuerto Internacional de El Salvador (ES-L1173)</td>'
      '<td><b>Organismo ejecutor</b></td><td>CEPA, mediante la UEP</td></tr>'
      '<tr><td><b>Fuente de financiamiento</b></td><td>Préstamo del BID (100% de cada adquisición)</td>'
      '<td><b>Políticas aplicables</b></td><td>GN-2349-15 (obras y bienes) y GN-2350-15 (consultores)</td></tr></table>')
P1 = f'''<h1>Matriz de adquisiciones del programa ES-L1173</h1>{ID}
<table>{HEAD}{"".join(body)}</table>'''

P2 = f'''<h2>Criterios de la matriz</h2>
<ul>
<li><b>Base.</b> Las 16 adquisiciones salen de las adquisiciones clave del Anexo III de la Propuesta de Préstamo (montos y modalidades), más la auditoría externa, que el Anexo III exige como requisito fiduciario. Cada una se vincula con los paquetes de trabajo de la EDT que abastece.</li>
<li><b>Fechas.</b> El inicio del proceso y la firma del contrato son las fechas de los paquetes de contratación del cronograma: 3.1.1 (UEP), 3.4.1 (obras), 3.4.2 (supervisión) y 3.4.3 (Componente II). La entrega requerida es la fecha en que termina el paquete que usa el contrato. Las evaluaciones se entregan cuando lo pide el plan de monitoreo y evaluación (medio término al 50% del tiempo de ejecución; final 90 días después de ejecutado el 95% de los recursos, aproximado con el valor planificado), y su firma e inicio se programan hacia atrás. La auditoría firma a tiempo para el primer ejercicio con desembolsos y entrega los estados financieros auditados finales en el cierre (3.5.4).</li>
<li><b>Diferencias con el Anexo III.</b> El cronograma inicia los procesos después de la no objeción del Plan de Adquisiciones (3.2.3, {ML(finish("3.2.3"))}), y las licitaciones de obra después de aprobar los diseños (1.1.1 a 1.1.4, {ML(finish("1.1.1", "1.1.2", "1.1.3", "1.1.4"))}) y de que el reglamento operativo esté vigente (3.1.2). Por eso algunos inicios difieren de los estimados del Anexo III, que se indican debajo de cada fecha. Los cuatro contratos de obra se firman en {ML(finish("3.4.1"))} (hito H03).</li>
<li><b>Adquisiciones críticas.</b> La contratación de la UEP (3.1.1) y la de las obras (3.4.1) están en la ruta crítica: un atraso en cualquiera de ellas mueve el fin del programa. El contrato de supervisión debe estar firmado antes de iniciar las obras; tiene {pk["3.4.2"]["float"]} días laborables de holgura.</li>
<li><b>Consolidación.</b> Las plataformas y la calle Foxtrot van en un solo contrato, la supervisión de las cuatro obras en otro, y BIM con EDGE en un tercero, como agrupa el Anexo III.</li>
<li><b>Responsables.</b> El especialista de adquisiciones conduce los procesos (paquetes 3.2.3 y 3.4 de la EDT). El área requirente prepara los términos de referencia o especificaciones y administra el contrato. La UEP la selecciona CEPA, porque el especialista aún no existe.</li>
<li><b>Gastos sin proceso de adquisición.</b> Los US$610,000 restantes del presupuesto corresponden a paquetes que ejecuta la UEP. Incluyen US$200,000 de gastos recurrentes y de mantenimiento que, según el Anexo III, siguen los procedimientos administrativos de CEPA definidos en el ROP.</li>
</ul>
<h2>Modalidades</h2>
<table class="gl">
<tr><th style="width:8%">Sigla</th><th style="width:28%">Modalidad</th><th style="width:64%">Uso en este programa</th></tr>
<tr><td><b>LPI</b></td><td>Licitación pública internacional</td><td>Obras de gran envergadura. Convocatoria internacional con los documentos estándar del BID y precalificación de empresas por capacidad y recursos (Anexo III).</td></tr>
<tr><td><b>SBCC</b></td><td>Selección basada en la calidad y el costo</td><td>Consultorías complejas (supervisión, plan estratégico, Plan Maestro, estudios de conectividad y de mercado). Se evalúan la propuesta técnica y el precio. El Anexo III registra también esta modalidad para el SSEI.</td></tr>
<tr><td><b>SCC</b></td><td>Selección basada en las calificaciones de los consultores</td><td>Consultorías pequeñas: BIM y EDGE, separación de flujos, movilidad, capacitación en inclusión y evaluaciones. Se elige la firma mejor calificada y se negocia su propuesta (GN-2350-15, párr. 3.8).</td></tr>
<tr><td><b>SBMC</b></td><td>Selección basada en el menor costo</td><td>Auditoría externa. La política de consultores admite para auditores la SBCC o el menor costo, por ser servicios con normas profesionales bien definidas (GN-2350-15, párr. 3.21).</td></tr>
<tr><td><b>3CV</b></td><td>Comparación de calificaciones de al menos tres candidatos</td><td>Consultores individuales de la UEP (GN-2350-15, sección V).</td></tr>
</table>
<p class="nota" style="margin-top:6pt">Fuentes: Propuesta de Préstamo ES-L1173, Anexo III (secciones II, III y V); EDT del programa; cronograma del programa; Políticas para la Selección y Contratación de Consultores financiados por el BID (GN-2350-15).</p>'''

mediabox = fitz.paper_rect('a4-l')
where = mediabox + (30, 28, -30, -34)


def html_doc(inner: str) -> str:
    return f'<html><head><style>{CSS}</style></head><body>{inner}</body></html>'


def fits(inner: str) -> bool:
    more, _ = fitz.Story(html=html_doc(inner)).place(where)
    return not more


# Una Story por página (como el anexo del cronograma): si la tabla se parte dentro de una misma Story, PyMuPDF deja fondos fantasma.
P1_HEAD = P1[:P1.index('<table>' + HEAD)]
pages, i = [], 0
while i < len(body):
    top = P1_HEAD if not pages else ''
    k = len(body) - i
    while k > 1 and not fits(f'{top}<table>{HEAD}{"".join(body[i:i + k])}</table>'):
        k -= 1
    pages.append(f'{top}<table>{HEAD}{"".join(body[i:i + k])}</table>')
    i += k
if fits(pages[-1] + P2):
    pages[-1] += P2
else:
    pages.append(P2)

buf = io.BytesIO()
writer = fitz.DocumentWriter(buf)
for inner in pages:
    story = fitz.Story(html=html_doc(inner))
    dev = writer.begin_page(mediabox)
    story.place(where)
    story.draw(dev)
    writer.end_page()
writer.close()
doc = fitz.open('pdf', buf.getvalue())
for k, page in enumerate(doc, start=1):
    page.insert_text((mediabox.width - 90, mediabox.height - 18), f'Página {k} de {len(doc)}', fontsize=7, color=(0.4, 0.42, 0.45))
    page.insert_text((30, mediabox.height - 18), 'ES-L1173 | Matriz de adquisiciones', fontsize=7, color=(0.4, 0.42, 0.45))
out = HERE / 'matriz_adquisiciones_ES-L1173.pdf'
pages = len(doc)
doc.save(str(out), garbage=3, deflate=True)
print(f'{out.name}: {pages} páginas, {len(ROWS)} adquisiciones, total US${TOTAL:,.0f} + otros US${OTROS:,.0f}')
for r in ROWS:
    print(r[1], '|', r[7], '|', r[9], '|', r[10], '|', r[11], '|', r[12])

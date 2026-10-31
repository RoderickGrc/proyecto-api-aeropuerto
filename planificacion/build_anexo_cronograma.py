#!/usr/bin/env python3
"""Genera el anexo del cronograma (tabla de actividades, duraciones, fechas, predecesoras, holgura y ruta critica) en PDF A4 horizontal.

Lee los archivos que produce build_planificacion.py (cronograma_paquetes.csv, hitos.csv y cronograma_ES-L1173.xml) y escribe
cronograma_ES-L1173_anexo_tabla.pdf en esta carpeta. Requiere PyMuPDF (fitz).
"""
from __future__ import annotations
import csv
import io
import json
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta
from html import escape
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
NS = {'m': 'http://schemas.microsoft.com/project'}

pk = {r['code']: r for r in csv.DictReader((HERE / 'cronograma_paquetes.csv').open(encoding='utf-8-sig'))}
hitos = list(csv.DictReader((HERE / 'hitos.csv').open(encoding='utf-8-sig')))
tasks = ET.parse(HERE / 'cronograma_ES-L1173.xml').getroot().find('m:Tasks', NS).findall('m:Task', NS)
summaries = {t.findtext('m:WBS', namespaces=NS): (t.findtext('m:Name', namespaces=NS), t.findtext('m:Start', namespaces=NS)[:10], t.findtext('m:Finish', namespaces=NS)[:10])
             for t in tasks if t.findtext('m:Summary', namespaces=NS) == '1' and t.findtext('m:WBS', namespaces=NS) not in (None, 'H')}


def d(s: str) -> date:
    return datetime.strptime(s, '%Y-%m-%d').date()


def fmt(s: str) -> str:
    return d(s).strftime('%d-%m-%Y')


def workdays(a: date, b: date) -> int:
    return sum(1 for i in range((b - a).days + 1) if (a + timedelta(days=i)).weekday() < 5)


def preds(deps: str) -> str:
    out = []
    for part in filter(None, deps.split(',')):
        code, _, rel = part.partition(':')
        out.append(f'{code} CC{rel[2:]}d' if rel.startswith('SS') and '+' in rel else (f'{code} CC' if rel.startswith('SS') else code))
    return ', '.join(out) or '-'


def key(code: str):
    return [int(p) for p in code.split('.')]


codes = sorted(set(pk) | set(summaries), key=lambda c: (key(c), 0 if c in summaries else 1))
rows = []
for c in codes:
    if c in summaries:
        name, s, f = summaries[c]
        level = c.count('.')
        rows.append(f'<tr class="g{min(level, 1)}"><td class="k">{c}</td><td>{escape(name)}</td><td class="n">{workdays(d(s), d(f))}</td>'
                    f'<td>{fmt(s)}</td><td>{fmt(f)}</td><td></td><td></td><td></td></tr>')
    else:
        r = pk[c]
        crit = r['critical'] == 'si'
        rows.append(f'<tr class="{"c" if crit else "p"}"><td class="k">{c}</td><td>{escape(r["name"])}</td><td class="n">{r["dur"]}</td>'
                    f'<td>{fmt(r["start"])}</td><td>{fmt(r["finish"])}</td><td>{preds(r["deps"])}</td>'
                    f'<td class="n{"" if crit else " h"}">{int(float(r["float"]))}</td><td class="n s">{"Sí" if crit else ""}</td></tr>')

hrows = []
for h in hitos:
    hrows.append(f'<tr class="m"><td class="k">{h["id"]}</td><td>{escape(h["name"])}</td><td>{fmt(h["date"])}</td><td>{h["preds"].replace(",", ", ")}</td></tr>')

crit_n = sum(1 for r in pk.values() if r['critical'] == 'si')
RES = json.loads((HERE / 'resumen.json').read_text(encoding='utf-8'))
LOE_TXT = '1.7.1 a 1.7.3, 3.2.2, 3.3.3, 3.3.4, 3.4.4 y 3.5.1 a 3.5.3'
# Paleta tomada del Gantt exportado de Open Planner Studio: ruta critica, normal, resumen e hito, holgura.
RED, BLUE, PURPLE, MINT = '#dc2626', '#2563eb', '#7c3aed', '#b7e3d8'
CSS = f'''
body {{ font-family: sans-serif; font-size: 7.6pt; color: #1f2430; }}
h1 {{ font-size: 13pt; margin: 0 0 2pt 0; color: #1f2430; }}
h2 {{ font-size: 10pt; margin: 8pt 0 3pt 0; color: #1f2430; }}
p {{ margin: 0 0 3pt 0; }}
p.nota {{ font-size: 7pt; color: #5b6270; }}
table {{ border-collapse: collapse; width: 100%; }}
th {{ background-color: #f1f3f6; color: #444a57; text-align: left; padding: 3pt 3pt; font-size: 7.4pt; border-bottom: 1pt solid #9ca3af; }}
td {{ padding: 2pt 3pt; border-bottom: 0.4pt solid #e3e6ea; vertical-align: top; }}
td.n {{ text-align: right; }}
td.k {{ font-weight: bold; }}
tr.p td.k {{ color: {BLUE}; }}
tr.c td {{ background-color: #fdeaea; }}
tr.c td.k, tr.c td.s {{ color: {RED}; font-weight: bold; }}
tr.g0 td, tr.g1 td {{ background-color: #f3effd; color: {PURPLE}; font-weight: bold; }}
tr.m td.k {{ color: {PURPLE}; }}
td.h {{ background-color: #e4f4ef; }}
td.sw {{ width: 9pt; border-bottom: 0; padding: 0; }}
td.lg {{ border-bottom: 0; padding: 0 10pt 0 3pt; font-size: 7pt; color: #5b6270; }}
'''
LEGEND = (f'<table style="width:60%"><tr>'
          f'<td class="sw" style="background-color:{RED}">&nbsp;</td><td class="lg">Ruta crítica</td>'
          f'<td class="sw" style="background-color:{BLUE}">&nbsp;</td><td class="lg">Paquete de trabajo</td>'
          f'<td class="sw" style="background-color:{PURPLE}">&nbsp;</td><td class="lg">Grupo de la EDT e hito</td>'
          f'<td class="sw" style="background-color:{MINT}">&nbsp;</td><td class="lg">Holgura</td></tr></table>')
HEAD = '<tr><th style="width:5%">EDT</th><th style="width:36%">Actividad (paquete de trabajo)</th><th style="width:6%">Dur. (dl)</th><th style="width:9%">Inicio</th><th style="width:9%">Fin</th><th style="width:21%">Predecesoras</th><th style="width:7%">Holgura (dl)</th><th style="width:7%">Crítica</th></tr>'
INTRO = f'''<h1>Anexo. Cronograma del programa ES-L1173: actividades, duraciones, predecesoras y ruta crítica</h1>
<p>Inicio: {fmt(RES["inicio"])}. Fin: {fmt(RES["fin"])}. Duración total: {RES["dias_laborables"]:,} días laborables (dl), con calendario de lunes a viernes, jornada de 8 horas y sin feriados.</p>
<p class="nota"><b>Notas.</b> Predecesoras: salvo indicación, la relación es fin a comienzo (FC): la actividad inicia cuando termina su predecesora. CC indica comienzo a comienzo con un desfase en dl; por ejemplo, 1.2.1 CC+150d significa que la actividad inicia 150 dl después del inicio de 1.2.1. Holgura: dl que una actividad puede retrasarse sin modificar la fecha de fin del programa (holgura total). Ruta crítica: actividades con holgura cero ({crit_n} paquetes de trabajo). Los paquetes de seguimiento ({LOE_TXT}) duran lo mismo que las actividades que acompañan: la supervisión, el PGAS, el mecanismo de quejas y los informes socioambientales terminan con las obras; los planes operativos, desembolsos y auditorías anuales, con la recepción; las evaluaciones, con el informe final; y 3.4.4, con la firma del contrato de la evaluación final. 1.7.2 y 1.7.3 tienen holgura cero porque acompañan a la cadena crítica del lado aire hasta la señalización de plataformas (1.3.3).</p>
{LEGEND}
<h2>Hitos</h2>
<table><tr><th style="width:6%">Hito</th><th style="width:56%">Descripción</th><th style="width:12%">Fecha</th><th style="width:26%">Se alcanza al terminar</th></tr>{''.join(hrows)}</table>
<h2>Actividades</h2>'''

mediabox = fitz.paper_rect('a4-l')
where = mediabox + (30, 28, -30, -34)


def page_html(first: bool, chunk: list[str]) -> str:
    return f'<html><head><style>{CSS}</style></head><body>{INTRO if first else ""}<table>{HEAD}{"".join(chunk)}</table></body></html>'


def fits(html: str) -> bool:
    more, _ = fitz.Story(html=html).place(where)
    return not more


pages_html, i = [], 0
while i < len(rows):
    first = not pages_html
    n = len(rows) - i
    while n > 1 and not fits(page_html(first, rows[i:i + n])):
        n -= 1
    pages_html.append(page_html(first, rows[i:i + n]))
    i += n

buf = io.BytesIO()
writer = fitz.DocumentWriter(buf)
for html in pages_html:
    story = fitz.Story(html=html)
    dev = writer.begin_page(mediabox)
    story.place(where)
    story.draw(dev)
    writer.end_page()
writer.close()

out = HERE / 'cronograma_ES-L1173_anexo_tabla.pdf'
doc = fitz.open('pdf', buf.getvalue())
for k, page in enumerate(doc, start=1):
    page.insert_text((mediabox.width - 90, mediabox.height - 18), f'Página {k} de {len(doc)}', fontsize=7, color=(0.4, 0.42, 0.45))
    page.insert_text((30, mediabox.height - 18), 'ES-L1173 | Cronograma del programa', fontsize=7, color=(0.4, 0.42, 0.45))
n_pages = len(doc)
doc.save(str(out))
doc.close()
print(f'{out.name}: {n_pages} páginas, {len(pk)} paquetes, {len(summaries)} grupos, {len(hitos)} hitos, {crit_n} críticos')

#!/usr/bin/env python3
"""Genera el anexo del cronograma (tabla jerarquica de actividades, duraciones, fechas, predecesoras, holgura y ruta critica) en PDF A4 horizontal.

Lee los archivos que produce build_planificacion.py (cronograma_actividades.csv, cronograma_paquetes.csv, hitos.csv y cronograma_ES-L1173.xml) y escribe
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
acts = {r['code']: r for r in csv.DictReader((HERE / 'cronograma_actividades.csv').open(encoding='utf-8-sig'))}
hitos = list(csv.DictReader((HERE / 'hitos.csv').open(encoding='utf-8-sig')))
tasks = ET.parse(HERE / 'cronograma_ES-L1173.xml').getroot().find('m:Tasks', NS).findall('m:Task', NS)
# Grupos de la EDT (resumen que no son paquetes), en el orden jerarquico del XML.
summaries = {t.findtext('m:WBS', namespaces=NS): (t.findtext('m:Name', namespaces=NS), t.findtext('m:Start', namespaces=NS)[:10], t.findtext('m:Finish', namespaces=NS)[:10])
             for t in tasks if t.findtext('m:Summary', namespaces=NS) == '1' and (t.findtext('m:WBS', namespaces=NS) or '')[:1].isdigit()
             and t.findtext('m:WBS', namespaces=NS) not in pk}
order = [t.findtext('m:WBS', namespaces=NS) for t in tasks]


def d(s: str) -> date:
    return datetime.strptime(s, '%Y-%m-%d').date()


def fmt(s: str) -> str:
    return d(s).strftime('%d-%m-%Y')


def workdays(a: date, b: date) -> int:
    return sum(1 for i in range((b - a).days + 1) if (a + timedelta(days=i)).weekday() < 5)


def preds(deps: str) -> str:
    """Predecesoras: 'pred' (FI sin desfase) o 'pred TIPO+desfase' (por ejemplo 1.2.1-02 II+40)."""
    out = []
    for part in filter(None, deps.split(',')):
        code, _, rel = part.partition(':')
        if rel in ('', 'FI', 'FI+0'):
            out.append(code)
        else:
            out.append(f'{code} {rel.replace("+0", "") if rel.endswith("+0") else rel}')
    return ', '.join(out) or '-'


def hol(v: str) -> str:
    return str(int(float(v))) if v not in ('', None) else ''


rows = []
for c in order:
    if c in summaries:
        name, s, f = summaries[c]
        rows.append(f'<tr class="g{min(c.count("."), 1)}"><td class="k">{c}</td><td>{escape(name)}</td><td class="n">{workdays(d(s), d(f))}</td>'
                    f'<td>{fmt(s)}</td><td>{fmt(f)}</td><td></td><td></td><td></td></tr>')
    elif c in pk:
        r = pk[c]
        crit = r['critical'] == 'si'
        rows.append(f'<tr class="{"pc" if crit else "pk"}"><td class="k">{c}</td><td>{escape(r["name"])}</td><td class="n">{r["dur"]}</td>'
                    f'<td>{fmt(r["start"])}</td><td>{fmt(r["finish"])}</td><td>{preds(r["deps"])}</td>'
                    f'<td class="n{"" if crit else " h"}">{hol(r["float"])}</td><td class="n s">{"Sí" if crit else ""}</td></tr>')
    elif c in acts:
        r = acts[c]
        crit = r['critical'] == 'si'
        rows.append(f'<tr class="{"c" if crit else "a"}"><td class="k">{c}</td><td>{escape(r["name"])}</td><td class="n">{r["dur"]}</td>'
                    f'<td>{fmt(r["start"])}</td><td>{fmt(r["finish"])}</td><td>{preds(r["deps"])}</td>'
                    f'<td class="n{"" if crit else " h"}">{hol(r["float"])}</td><td class="n s">{"Sí" if crit else ""}</td></tr>')
rows.append('<tr class="g0"><td class="k"></td><td>Hitos del programa</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>')
for h in hitos:
    rows.append(f'<tr class="m"><td class="k">{h["id"]}</td><td>{escape(h["name"])}</td><td class="n">0</td><td>{fmt(h["date"])}</td><td>{fmt(h["date"])}</td>'
                f'<td>{preds(h["preds"])}</td><td></td><td></td></tr>')

crit_n = sum(1 for r in acts.values() if r['critical'] == 'si')
crit_pk = sum(1 for r in pk.values() if r['critical'] == 'si')
RES = json.loads((HERE / 'resumen.json').read_text(encoding='utf-8'))
# Paleta tomada del Gantt exportado de Open Planner Studio: ruta critica, normal, resumen e hito, holgura.
RED, BLUE, PURPLE, MINT = '#dc2626', '#2563eb', '#7c3aed', '#b7e3d8'
CSS = f'''
body {{ font-family: sans-serif; font-size: 7.6pt; color: #1f2430; }}
h1 {{ font-size: 13pt; margin: 0 0 2pt 0; color: #1f2430; }}
h2 {{ font-size: 10pt; margin: 8pt 0 3pt 0; color: #1f2430; }}
p {{ margin: 0 0 3pt 0; }}
p.nota {{ font-size: 7pt; color: #5b6270; }}
table {{ border-collapse: collapse; width: 100%; table-layout: fixed; }}
th {{ background-color: #f1f3f6; color: #444a57; text-align: left; padding: 3pt 3pt; font-size: 7.4pt; border-bottom: 1pt solid #9ca3af; }}
td {{ padding: 2pt 3pt; border-bottom: 0.4pt solid #e3e6ea; vertical-align: top; }}
td.n {{ text-align: right; }}
td.k {{ font-weight: bold; }}
tr.a td.k {{ font-weight: normal; }}
tr.pk td {{ background-color: #eef3fd; font-weight: bold; }}
tr.pk td.k {{ color: {BLUE}; }}
tr.pc td {{ background-color: #fdeaea; font-weight: bold; }}
tr.pc td.k {{ color: {RED}; }}
tr.c td {{ background-color: #fdeaea; }}
tr.c td.k, tr.c td.s, tr.pc td.s {{ color: {RED}; font-weight: bold; }}
tr.g0 td, tr.g1 td {{ background-color: #f3effd; color: {PURPLE}; font-weight: bold; }}
tr.m td.k {{ color: {PURPLE}; }}
tr.m td {{ background-color: #f8f6fe; }}
td.h {{ background-color: #e4f4ef; }}
td.sw {{ width: 9pt; border-bottom: 0; padding: 0; }}
td.lg {{ border-bottom: 0; padding: 0 10pt 0 3pt; font-size: 7pt; color: #5b6270; }}
'''
LEGEND = (f'<table style="width:75%"><tr>'
          f'<td class="sw" style="background-color:{RED}">&nbsp;</td><td class="lg">Ruta crítica</td>'
          f'<td class="sw" style="background-color:{BLUE}">&nbsp;</td><td class="lg">Paquete de trabajo (resumen)</td>'
          f'<td class="sw" style="background-color:{PURPLE}">&nbsp;</td><td class="lg">Grupo de la EDT e hito</td>'
          f'<td class="sw" style="background-color:{MINT}">&nbsp;</td><td class="lg">Holgura</td></tr></table>')
HEAD = '<tr><th style="width:7%">EDT</th><th style="width:41%">Actividad (paquete de trabajo)</th><th style="width:5%">Dur. (dl)</th><th style="width:8%">Inicio</th><th style="width:8%">Fin</th><th style="width:19%">Predecesoras</th><th style="width:6%">Holg. (dl)</th><th style="width:6%">Crítica</th></tr>'
INTRO = f'''<h1>Anexo. Cronograma del programa ES-L1173: actividades, duraciones, predecesoras y ruta crítica</h1>
<p>Inicio: {fmt(RES["inicio"])}. Fin: {fmt(RES["fin"])}. Duración total: {RES["dias_laborables"]:,} días laborables (dl), con calendario de lunes a viernes, jornada de 8 horas y sin feriados. El programa tiene {len(acts)} actividades en {len(pk)} paquetes de trabajo y {len(hitos)} hitos; {crit_n} actividades son críticas (en {crit_pk} paquetes).</p>
<p class="nota"><b>Notas.</b> La tabla sigue la EDT: grupos en morado, cada paquete de trabajo como fila resumen en negrita y, debajo, sus actividades; los hitos van al final. Predecesoras: salvo indicación, la relación es fin a inicio (FI) sin desfase. Los otros tipos se escriben después del código: II es inicio a inicio, FF es fin a fin e IF es inicio a fin; el desfase va en dl, por ejemplo 1.2.1-02 II+40 significa que la actividad inicia 40 dl después del inicio de 1.2.1-02. Holgura: dl que una actividad puede retrasarse sin modificar la fecha de fin del programa (holgura total). Ruta crítica: actividades con holgura cero, resaltadas en rojo.</p>
{LEGEND}
<h2>Actividades</h2>'''

mediabox = fitz.paper_rect('a4-l')
where = mediabox + (30, 28, -30, -34)


WIDTHS = [round(750 * w / 100, 1) for w in (7, 41, 5, 8, 8, 19, 6, 6)]


def sized(row: str) -> str:
    parts = row.split('<td')
    return parts[0] + ''.join(f'<td style="width:{WIDTHS[k]}pt"' + x for k, x in enumerate(parts[1:]))


def page_html(first: bool, chunk: list[str]) -> str:
    return f'<html><head><style>{CSS}</style></head><body>{INTRO if first else ""}<table style="width:750pt">{HEAD}{"".join(sized(r) for r in chunk)}</table></body></html>'


def fits(html: str) -> bool:
    more, filled = fitz.Story(html=html).place(where)
    return not more and filled[3] <= where.y1 + 0.01


pages_html, i = [], 0
while i < len(rows):
    first = not pages_html
    n = min(len(rows) - i, 60)
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
print(f'{out.name}: {n_pages} páginas, {len(acts)} actividades, {len(pk)} paquetes, {len(summaries)} grupos, {len(hitos)} hitos, {crit_n} críticos')

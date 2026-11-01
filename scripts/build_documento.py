"""Genera el documento final y los anexos a partir de los .md de docs/.

Uso:  python -B scripts/build_documento.py [--sin-word]

Toma la portada, el índice, los estilos y el pie de página de "docs/Proyecto API Base.docx"
y agrega el contenido de los .md en el orden de PARTES. Las correcciones se hacen en los .md
y se vuelve a ejecutar este script. Salida en entrega/:

- el documento final en Word y en PDF;
- los anexos en PDF: los que ya genera planificacion/ se copian, y el listado de actividades
  y la estimación de costos se arman aquí con el mismo formato;
- el cronograma en XML de MS Project (la planificación en herramienta).

Requiere python-docx, Pillow y matplotlib. Microsoft Word actualiza el índice y exporta a PDF
(sin Word, --sin-word deja solo el .docx con el índice sin actualizar). Microsoft Edge convierte
los SVG a PNG. Los bloques mermaid se dibujan aquí: el árbol de la EDT con Pillow y la matriz
poder e interés con matplotlib, porque mermaid no deja legibles en una página los árboles anchos.
"""
from __future__ import annotations

import copy
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True

import docx  # noqa: E402
from docx.enum.section import WD_ORIENT, WD_SECTION  # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402
from docx.enum.style import WD_STYLE_TYPE  # noqa: E402
from docx.oxml import OxmlElement  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.shared import Cm, Pt, Twips  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / 'docs'
DF = DOCS / 'documento-final'
PLAN = REPO / 'planificacion'
BASE = DOCS / 'Proyecto API Base.docx'
OUT = REPO / 'entrega'
NOMBRE = 'ES-L1173 Documento final'

EDGE = Path(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
FUENTE = 'Times New Roman'
ARIAL = r'C:\Windows\Fonts\arial.ttf'
ARIAL_B = r'C:\Windows\Fonts\arialbd.ttf'

# ---------------------------------------------------------------- estructura del documento
# h1/h2: título en el documento (los del índice de la plantilla). md: archivo o lista de archivos.
# secciones: solo esas secciones "##" del .md (y sin su introducción si intro=False).
ADQ_COLUMNAS = ['N.º', 'EDT', 'Actividades del cronograma', 'Bien, servicio u obra', 'Justificación', 'Modalidad',
                'Monto (US$)', 'Firma del contrato', 'Entrega requerida', 'Responsable']
PARTES = [
    dict(h1='Introducción', md=DF / 'introduccion.md'),
    dict(h1='Objetivos', md=DF / 'objetivos.md'),
    dict(h1='Acta de constitución del proyecto', md=DOCS / 'acta-constitucion.md', quitar_numeros=True),
    dict(h1='Desarrollo del proyecto', subpartes=[
        dict(h2='Descripción del proyecto seleccionado', md=DF / 'descripcion-proyecto.md'),
        dict(h2='Estructura organizativa del proyecto', md=DOCS / 'estructura-organizacional.md'),
        dict(h2='Creación de la EDT (Estructura de Desglose del Trabajo)', md=DOCS / 'edt.md',
             leyendas=['EDT del programa: objetivo, componentes y productos',
                       'EDT del Componente I. Obras y adecuaciones',
                       'EDT del Componente II. Fortalecimiento institucional',
                       'EDT de Administración, evaluación y auditorías']),
        dict(h2='Elaboración del cronograma del proyecto', md=DOCS / 'cronograma-y-curva-s.md',
             secciones=['Supuestos del cronograma', 'Hitos', 'Ruta crítica', 'Reserva de contingencia del cronograma',
                        'Evaluaciones']),
        dict(h2='Desarrollo de la curva de uso de recursos (Curva S)', md=DOCS / 'cronograma-y-curva-s.md', intro=False,
             secciones=['Curva S', 'Requisitos de financiamiento frente a los desembolsos del préstamo'],
             # el gráfico de la página 1 del Anexo E, recortado sin su encabezado ni su pie
             figura=('Curva S', (PLAN / 'curva_s_ES-L1173.pdf', 0, (45, 138, 765, 530)),
                     'Curva S del programa: valor planificado acumulado y mensual, requisitos de financiamiento, '
                     'desembolsos previstos en el PEP e hitos H03, H05, H07 y H09')),
        dict(h2='Preparación de la matriz de adquisiciones', md=DOCS / 'matriz-adquisiciones.md',
             columnas={0: ADQ_COLUMNAS},
             nota={0: 'La tabla muestra las columnas que pide la consigna y las actividades del cronograma de cada contrato. '
                      'La matriz completa, con todas sus columnas, está en el Anexo F.'}),
        dict(h2='Elaboración de la matriz de riesgos', md=DOCS / 'matriz-riesgos.md'),
        dict(h2='Información de los interesados y matriz de comunicaciones', md=DOCS / 'matriz-comunicaciones.md'),
        dict(h2='Creación de la matriz de asignación de responsabilidades (MAR)', md=DOCS / 'matriz-raci.md'),
        dict(h2='Relación de cada entregable con los procesos del PMBOK', md=DOCS / 'relacion-entregables-pmbok.md'),
    ]),
    dict(h1='Conclusiones', md=DF / 'conclusiones.md'),
    dict(h1='Recomendaciones', md=DF / 'recomendaciones.md'),
    dict(h1='Glosario', md=DF / 'glosario.md'),
    dict(h1='Referencias bibliográficas', md=DF / 'referencias.md', referencias=True),
    dict(h1='Anexos', md=DF / 'anexos.md'),
]
ANEXOS_COPIADOS = [
    ('A', 'Diagrama de Gantt', PLAN / 'cronograma_ES-L1173_gantt.pdf'),
    ('B', 'Tabla del cronograma', PLAN / 'cronograma_ES-L1173_anexo_tabla.pdf'),
    ('E', 'Curva S', PLAN / 'curva_s_ES-L1173.pdf'),
    ('F', 'Matriz de adquisiciones', PLAN / 'matriz_adquisiciones_ES-L1173.pdf'),
]
ANEXOS_GENERADOS = [
    ('C', 'Listado de actividades', DOCS / 'listado-actividades.md', 'Listado de actividades del cronograma', True),
    ('D', 'Estimación de costos', DOCS / 'estimacion-costos.md', 'Estimación de costos', False),
]
XML_CRONOGRAMA = (PLAN / 'cronograma_ES-L1173.xml', 'Cronograma ES-L1173 (MS Project XML).xml')

# Lo que no puede aparecer en un entregable: rutas, archivos de trabajo y rayas largas.
PROHIBIDO = re.compile(r'\.md\b|\.py\b|\.csv\b|\.json\b|(?<![\w./-])(docs|planificacion|scripts)/|\u2014|\bassert\b|\bTODO\b')

# ---------------------------------------------------------------- markdown


def parse_md(text):
    """Bloques: ('h', nivel, texto), ('p', texto), ('ul'|'ol', [items]), ('table', cab, alin, filas),
    ('code', lenguaje, texto), ('img', alt, ruta)."""
    lines = text.splitlines()
    out, i = [], 0
    while i < len(lines):
        s = lines[i].rstrip()
        if not s.strip() or s.strip().startswith('<!--'):
            i += 1
            continue
        if s.startswith('```'):
            lang, buf = s[3:].strip(), []
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                buf.append(lines[i])
                i += 1
            out.append(('code', lang, '\n'.join(buf)))
            i += 1
            continue
        m = re.match(r'(#{1,6})\s+(.*)', s)
        if m:
            out.append(('h', len(m.group(1)), m.group(2).strip()))
            i += 1
            continue
        m = re.match(r'!\[([^\]]*)\]\(([^)]+)\)\s*$', s)
        if m:
            out.append(('img', m.group(1), m.group(2)))
            i += 1
            continue
        if s.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
                i += 1
            alin = ['right' if c.endswith(':') and not c.startswith(':') else 'center' if c.startswith(':') and c.endswith(':') else 'left'
                    for c in rows[1]]
            out.append(('table', rows[0], alin, rows[2:]))
            continue
        if re.match(r'[-*]\s+', s) or re.match(r'\d+\.\s+', s):
            kind = 'ol' if re.match(r'\d+\.\s+', s) else 'ul'
            items = []
            while i < len(lines) and (re.match(r'[-*]\s+', lines[i]) if kind == 'ul' else re.match(r'\d+\.\s+', lines[i])):
                items.append(re.sub(r'^([-*]|\d+\.)\s+', '', lines[i].rstrip()))
                i += 1
            out.append((kind, items))
            continue
        buf = [s.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r'(#|\||```|!\[|[-*]\s|\d+\.\s)', lines[i]):
            buf.append(lines[i].strip())
            i += 1
        out.append(('p', ' '.join(buf)))
    return out


def seleccionar(blocks, secciones, intro=True):
    """Introducción del .md (antes del primer ##) y las secciones ## pedidas, en el orden del .md."""
    out, dentro = [], intro
    for b in blocks:
        if b[0] == 'h' and b[1] == 1:
            continue
        if b[0] == 'h' and b[1] == 2:
            dentro = b[2] in secciones
        if dentro:
            out.append(b)
    return out


INLINE = re.compile(r'(\*\*.+?\*\*|\*[^*\s][^*]*?\*|`[^`]+`|\[[^\]]+\]\([^)]+\))')


def runs(par, text, bold=False, italic=False):
    for tok in INLINE.split(text):
        if not tok:
            continue
        if tok.startswith('**') and tok.endswith('**'):
            runs(par, tok[2:-2], True, italic)
        elif tok.startswith('`'):
            r = par.add_run(tok[1:-1])
            r.bold, r.italic = bold or None, italic or None
        elif tok.startswith('[') and '](' in tok:
            runs(par, tok[1:tok.index('](')], bold, italic)
        elif tok.startswith('*') and tok.endswith('*') and len(tok) > 2:
            runs(par, tok[1:-1], bold, True)
        else:
            r = par.add_run(tok)
            if bold:
                r.bold = True
            if italic:
                r.italic = True


def texto_plano(text):
    return re.sub(r'\*\*|\*|`', '', re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text))

# ---------------------------------------------------------------- figuras


def _fuente(size, bold=False):
    from PIL import ImageFont
    return ImageFont.truetype(ARIAL_B if bold else ARIAL, size)


def _envolver(draw, text, font, ancho):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if draw.textlength(t, font=font) <= ancho or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


PALETA = {'1': ('#1565C0', '#EAF3FC'), '2': ('#2E7D32', '#EBF6EC'), '3': ('#AD5A00', '#FFF3E5')}


def dibujar_arbol(code, destino):
    """Árbol de un bloque mermaid "graph": raíz arriba y descendientes como lista sangrada.
    Si la raíz tiene tres hijos o menos, cada hijo es una columna."""
    from PIL import Image, ImageDraw
    labels, hijos, padres = {}, {}, set()
    for line in code.splitlines():
        for nid, lab in re.findall(r'(\w+)\["([^"]+)"\]', line):
            labels.setdefault(nid, lab)
        if '-->' in line:
            a, b = line.split('-->', 1)
            a, b = re.match(r'\s*(\w+)', a).group(1), re.match(r'\s*(\w+)', b).group(1)
            hijos.setdefault(a, []).append(b)
            padres.add(b)
    raiz = next(n for n in labels if n not in padres and n in hijos)
    dpi = 300
    px = lambda pt: int(pt * dpi / 72)  # noqa: E731
    W = int(15.5 / 2.54 * dpi)
    f_raiz, f_n1, f_n2 = _fuente(px(10), True), _fuente(px(9), True), _fuente(px(8.5))
    pad, gap, ind = px(5), px(4), px(16)

    def color(nid):
        m = re.match(r'(\d)', labels[nid])
        return PALETA.get(m.group(1) if m else '', ('#173B63', '#E8EEF5'))

    def medir(nid, ancho, font):
        d = ImageDraw.Draw(Image.new('RGB', (10, 10)))
        lines = _envolver(d, labels[nid], font, ancho - 2 * pad)
        alto = len(lines) * int(font.size * 1.25) + 2 * pad
        return lines, alto

    ops = []  # operaciones de dibujo diferidas: (tipo, args)

    def caja(nid, x0, x1, y, font, fondo, borde, tinta):
        lines, alto = medir(nid, x1 - x0, font)
        ops.append(('box', (x0, y, x1, y + alto), fondo, borde))
        for k, ln in enumerate(lines):
            ops.append(('text', (x0 + pad, y + pad + k * int(font.size * 1.25)), ln, font, tinta))
        return y + alto

    def lista(nids, x0, x1, y, nivel):
        """Dibuja los nodos sangrados bajo un conector vertical en x0 + ind/2. Devuelve la y final."""
        xc = x0 + ind // 2
        y_ini, y_ult = y, y
        for nid in nids:
            fuerte, claro = color(nid)
            y += gap
            font = f_n1 if nivel == 1 else f_n2
            fondo, borde, tinta = (claro, fuerte, fuerte) if nivel == 1 else ('#FFFFFF', '#9AA9B8', '#1F2A36')
            y_fin = caja(nid, x0 + ind, x1, y, font, fondo, borde, tinta)
            ymid = y + (medir(nid, x1 - x0 - ind, font)[1]) // 2
            ops.append(('line', (xc, ymid, x0 + ind, ymid)))
            y_ult = ymid
            y = y_fin
            if hijos.get(nid):
                y = lista(hijos[nid], x0 + ind, x1, y, nivel + 1)
        ops.append(('line', (xc, y_ini, xc, y_ult)))
        return y

    fuerte, claro = color(raiz)
    y = caja(raiz, 0, W, 0, f_raiz, fuerte, fuerte, '#FFFFFF')
    cols = hijos[raiz]
    if len(cols) <= 3:
        y_bar = y + px(6)
        ops.append(('line', (W // 2, y, W // 2, y_bar)))
        cw = (W - (len(cols) - 1) * px(6)) // len(cols)
        xs = [k * (cw + px(6)) for k in range(len(cols))]
        ops.append(('line', (xs[0] + cw // 2, y_bar, xs[-1] + cw // 2, y_bar)))
        y_max = 0
        for x0, nid in zip(xs, cols):
            ops.append(('line', (x0 + cw // 2, y_bar, x0 + cw // 2, y_bar + px(6))))
            fu, cl = color(nid)
            yc = caja(nid, x0, x0 + cw, y_bar + px(6), f_n1, fu, fu, '#FFFFFF')
            if hijos.get(nid):
                yc = lista(hijos[nid], x0, x0 + cw, yc, 2)
            y_max = max(y_max, yc)
        H = y_max + px(2)
    else:
        H = lista(cols, 0, W, y, 1) + px(2)
    img = Image.new('RGB', (W + 4, H + 4), 'white')
    d = ImageDraw.Draw(img)
    lw = max(2, px(0.8))
    for op in ops:
        if op[0] == 'line':
            d.line(op[1], fill='#7890A8', width=lw)
    for op in ops:
        if op[0] == 'box':
            d.rounded_rectangle(op[1], radius=px(3), fill=op[2], outline=op[3], width=lw)
        elif op[0] == 'text':
            d.text(op[1], op[2], font=op[3], fill=op[4])
    img.save(destino, dpi=(dpi, dpi))
    return destino


def dibujar_cuadrante(code, destino):
    """Bloque mermaid "quadrantChart" con matplotlib. El título va como leyenda de la figura."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    q, pts, ejes = {}, [], {}
    for line in code.splitlines():
        s = line.strip()
        m = re.match(r'quadrant-(\d)\s+(.*)', s)
        if m:
            q[int(m.group(1))] = m.group(2)
        m = re.match(r'([xy])-axis\s+(.*?)\s*-->\s*(.*)', s)
        if m:
            ejes[m.group(1)] = (m.group(2), m.group(3))
        m = re.match(r'(.+?):\s*\[([\d.]+),\s*([\d.]+)\]', s)
        if m:
            pts.append((m.group(1).strip(), float(m.group(2)), float(m.group(3))))
    plt.rcParams['font.family'] = 'Times New Roman'
    fig, ax = plt.subplots(figsize=(15.5 / 2.54, 11.5 / 2.54), dpi=300)
    fondos = {1: '#E3ECF7', 2: '#F2F2F2', 3: '#FAFAFA', 4: '#EEF5EA'}
    for k, (x0, y0) in {1: (.5, .5), 2: (0, .5), 3: (0, 0), 4: (.5, 0)}.items():
        ax.add_patch(plt.Rectangle((x0, y0), .5, .5, color=fondos[k], zorder=0))
        arriba = y0 > 0
        ax.text(x0 + .25, y0 + (.48 if arriba else .02), q.get(k, ''), ha='center', va='top' if arriba else 'bottom',
                fontsize=9, color='#555555', fontweight='bold')
    ax.axhline(.5, color='#999999', lw=.8)
    ax.axvline(.5, color='#999999', lw=.8)
    puestos = []
    for nombre, x, y in sorted(pts, key=lambda p: -p[2]):
        ancho, alto = .011 * len(nombre) + .02, .035
        ly = y
        while any(abs(ly - py) < alto and not (x + ancho < px_ or px_ + pw < x) for px_, py, pw in puestos):
            ly -= .01
        puestos.append((x, ly, ancho))
        ax.plot(x, y, 'o', color='#1F4E79', ms=4, zorder=3)
        if abs(ly - y) > .004:
            ax.plot([x, x + .012], [y, ly], color='#888888', lw=.5)
        ax.text(x + .015, ly, nombre, va='center', fontsize=8)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([.01, .99])
    ax.set_yticks([.01, .99])
    ax.set_xticklabels(ejes.get('x', ('', '')), fontsize=9)
    ax.set_yticklabels(ejes.get('y', ('', '')), fontsize=9, rotation=90)
    for lab, ha in zip(ax.get_xticklabels(), ('left', 'right')):
        lab.set_ha(ha)
    for lab, va in zip(ax.get_yticklabels(), ('bottom', 'top')):
        lab.set_va(va)
    ax.tick_params(length=0)
    for sp in ax.spines.values():
        sp.set_color('#999999')
    fig.tight_layout()
    fig.savefig(destino, dpi=300)
    plt.close(fig)
    return destino


def recorte_pdf(pdf, pagina, rect, destino, dpi=250):
    """Región (x0, y0, x1, y1 en puntos) de una página de PDF como PNG."""
    import fitz
    with fitz.open(str(pdf)) as d:
        d[pagina].get_pixmap(dpi=dpi, clip=fitz.Rect(*rect)).save(str(destino))
    return destino


def svg_a_png(svg, destino):
    head = svg.read_text(encoding='utf-8', errors='replace')[:600]
    w = int(float(re.search(r'width="([\d.]+)"', head).group(1)))
    h = int(float(re.search(r'height="([\d.]+)"', head).group(1)))
    with tempfile.TemporaryDirectory() as perfil:
        subprocess.run([str(EDGE), '--headless=new', '--disable-gpu', '--no-first-run', f'--user-data-dir={perfil}',
                        f'--window-size={w},{h}', f'--screenshot={destino}', svg.resolve().as_uri()],
                       check=True, capture_output=True, timeout=120)
    return destino

# ---------------------------------------------------------------- estilos y numeración


def _rfonts(rpr, font=FUENTE):
    for e in rpr.findall(qn('w:rFonts')):
        rpr.remove(e)
    rf = OxmlElement('w:rFonts')
    for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
        rf.set(qn(a), font)
    rpr.insert(0, rf)


def _estilo(doc, nombre, base='Normal', tipo=WD_STYLE_TYPE.PARAGRAPH):
    try:
        return doc.styles[nombre]
    except KeyError:
        st = doc.styles.add_style(nombre, tipo)
        st.base_style = doc.styles[base]
        return st


def _fmt(st, size=None, bold=None, italic=None, color_auto=True, font=FUENTE):
    rpr = st.element.get_or_add_rPr()
    _rfonts(rpr, font)
    if color_auto:
        for e in rpr.findall(qn('w:color')):
            rpr.remove(e)
        c = OxmlElement('w:color')
        c.set(qn('w:val'), 'auto')
        rpr.append(c)
    if size:
        st.font.size = Pt(size)
    if bold is not None:
        st.font.bold = bold
    if italic is not None:
        st.font.italic = italic


def _numbering(doc):
    numbering = doc.part.numbering_part.element
    absn = [int(a.get(qn('w:abstractNumId'))) for a in numbering.findall(qn('w:abstractNum'))]
    nums = [int(n.get(qn('w:numId'))) for n in numbering.findall(qn('w:num'))]
    return numbering, max(absn, default=0) + 1, max(nums, default=0) + 1


def _abstract(numbering, aid, niveles):
    """niveles: lista de (fmt, texto, sangría izquierda, colgante, estilo o None, fuente del símbolo)."""
    a = OxmlElement('w:abstractNum')
    a.set(qn('w:abstractNumId'), str(aid))
    mlt = OxmlElement('w:multiLevelType')
    mlt.set(qn('w:val'), 'multilevel')
    a.append(mlt)
    for i, (fmt, txt, left, hang, pstyle, sym) in enumerate(niveles):
        lvl = OxmlElement('w:lvl')
        lvl.set(qn('w:ilvl'), str(i))
        for tag, val in (('w:start', '1'), ('w:numFmt', fmt)):
            e = OxmlElement(tag)
            e.set(qn('w:val'), val)
            lvl.append(e)
        if pstyle:
            e = OxmlElement('w:pStyle')
            e.set(qn('w:val'), pstyle)
            lvl.append(e)
        if pstyle:
            e = OxmlElement('w:suff')
            e.set(qn('w:val'), 'space')
            lvl.append(e)
        e = OxmlElement('w:lvlText')
        e.set(qn('w:val'), txt)
        lvl.append(e)
        e = OxmlElement('w:lvlJc')
        e.set(qn('w:val'), 'left')
        lvl.append(e)
        ppr = OxmlElement('w:pPr')
        ind = OxmlElement('w:ind')
        ind.set(qn('w:left'), str(left))
        ind.set(qn('w:hanging'), str(hang))
        ppr.append(ind)
        lvl.append(ppr)
        rpr = OxmlElement('w:rPr')
        _rfonts(rpr, sym or FUENTE)
        lvl.append(rpr)
        a.append(lvl)
    ultimos = numbering.findall(qn('w:abstractNum'))
    if ultimos:
        ultimos[-1].addnext(a)
    else:
        numbering.insert(0, a)


def _num(numbering, nid, aid, reiniciar=False):
    n = OxmlElement('w:num')
    n.set(qn('w:numId'), str(nid))
    e = OxmlElement('w:abstractNumId')
    e.set(qn('w:val'), str(aid))
    n.append(e)
    if reiniciar:
        o = OxmlElement('w:lvlOverride')
        o.set(qn('w:ilvl'), '0')
        s = OxmlElement('w:startOverride')
        s.set(qn('w:val'), '1')
        o.append(s)
        n.append(o)
    numbering.append(n)


def _numpr(ppr, numid, ilvl=0):
    for e in ppr.findall(qn('w:numPr')):
        ppr.remove(e)
    np_ = OxmlElement('w:numPr')
    il = OxmlElement('w:ilvl')
    il.set(qn('w:val'), str(ilvl))
    ni = OxmlElement('w:numId')
    ni.set(qn('w:val'), str(numid))
    np_.append(il)
    np_.append(ni)
    ppr.insert(0, np_)


class Escritor:
    def __init__(self, doc, numerar_titulos):
        self.doc = doc
        self.figura = 0
        self.horizontal = False
        self.fijo_horizontal = False
        self.referencias = False
        st = doc.styles
        for nombre, size, bold, italic in (('Heading 1', 18, False, False), ('Heading 2', 16, False, False),
                                           ('Heading 3', 13, True, False), ('Heading 4', 12, True, False),
                                           ('Heading 5', 12, True, True)):
            s = st[nombre]
            _fmt(s, size, bold, italic)
            s.paragraph_format.space_before = Pt(18 if nombre == 'Heading 1' else 12)
            s.paragraph_format.space_after = Pt(8 if nombre in ('Heading 1', 'Heading 2') else 4)
            s.paragraph_format.keep_with_next = True
        st['Heading 1'].paragraph_format.page_break_before = True
        cuerpo = _estilo(doc, 'Cuerpo')
        _fmt(cuerpo, 12)
        pf = cuerpo.paragraph_format
        pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        pf.space_before, pf.space_after, pf.line_spacing = Pt(0), Pt(6), 1.15
        _fmt(_estilo(doc, 'Lista cuerpo', 'Cuerpo'), 12)
        _estilo(doc, 'Lista cuerpo', 'Cuerpo').paragraph_format.space_after = Pt(3)
        for nombre, size in (('Tabla texto', 9), ('Tabla texto 8', 8)):
            t = _estilo(doc, nombre)
            _fmt(t, size)
            t.paragraph_format.space_before, t.paragraph_format.space_after = Pt(1), Pt(1)
            t.paragraph_format.line_spacing = 1.0
            t.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        ley = _estilo(doc, 'Leyenda de figura')
        _fmt(ley, 10, italic=True)
        ley.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        ley.paragraph_format.space_after = Pt(10)
        fig = _estilo(doc, 'Figura')
        fig.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fig.paragraph_format.keep_with_next = True
        fig.paragraph_format.space_before, fig.paragraph_format.space_after = Pt(6), Pt(4)
        for nombre, size, left in (('toc 1', 12, 0), ('toc 2', 12, 0.4), ('toc 3', 11, 0.8)):
            t = _estilo(doc, nombre)
            _fmt(t, size)
            t.paragraph_format.left_indent = Cm(left)
            t.paragraph_format.space_after = Pt(2)
        self.ids_titulo = {st[f'Heading {i}'].style_id for i in range(1, 6)}
        ref = _estilo(doc, 'Referencia', 'Cuerpo')
        ref.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        ref.paragraph_format.left_indent, ref.paragraph_format.first_line_indent = Cm(1.27), Cm(-1.27)
        numbering, aid, nid = _numbering(doc)
        self.numbering = numbering
        _abstract(numbering, aid, [('bullet', '\u2022', 720, 360, None, None)])
        _abstract(numbering, aid + 1, [('decimal', '%1.', 720, 360, None, None)])
        self.aid_vineta, self.aid_decimal = aid, aid + 1
        _num(numbering, nid, aid)
        self.num_vineta = nid
        self.next_num = nid + 1
        if numerar_titulos:
            h1, h2 = st['Heading 1'].style_id, st['Heading 2'].style_id
            _abstract(numbering, aid + 2, [('decimal', '%1.', 0, 0, h1, None), ('decimal', '%1.%2.', 0, 0, h2, None)])
            _num(numbering, self.next_num, aid + 2)
            _numpr(st['Heading 1'].element.get_or_add_pPr(), self.next_num, 0)
            _numpr(st['Heading 2'].element.get_or_add_pPr(), self.next_num, 1)
            self.next_num += 1
            try:  # el título del índice hereda de Heading 1: sin número
                _numpr(st['TOC Heading'].element.get_or_add_pPr(), 0, 0)
            except KeyError:
                pass

    # -- secciones
    def ancho_cm(self):
        s = self.doc.sections[-1]
        return (s.page_width - s.left_margin - s.right_margin) / 360000

    def orientar(self, horizontal, arrastrar=False):
        """Nueva sección con la orientación pedida. Con arrastrar, el título que precede a la tabla o figura
        (y el párrafo entre ambos) pasa a la nueva sección, para que no quede solo al pie de la página anterior."""
        if horizontal == self.horizontal or self.fijo_horizontal:
            return
        body = self.doc.element.body
        movidos = []
        if arrastrar:
            cola = [e for e in body if e.tag != qn('w:sectPr')][-4:]

            def es_titulo(e):
                estilo = e.find(qn('w:pPr') + '/' + qn('w:pStyle'))
                return e.tag == qn('w:p') and estilo is not None and estilo.get(qn('w:val')) in self.ids_titulo
            for k in range(len(cola) - 1, -1, -1):
                if es_titulo(cola[k]):
                    while k > 0 and es_titulo(cola[k - 1]):  # títulos seguidos viajan juntos
                        k -= 1
                    movidos = cola[k:]
                    break
            if any(e.tag != qn('w:p') or e.find('.//' + qn('w:sectPr')) is not None for e in movidos):
                movidos = []
            for e in movidos:
                body.remove(e)
        resto = [e for e in body if e.tag != qn('w:sectPr')]
        corte = resto[-1].find(qn('w:pPr') + '/' + qn('w:sectPr')) if resto and resto[-1].tag == qn('w:p') else None
        if corte is not None and self._orientacion_de(corte) == horizontal:
            # la sección actual quedó vacía: se deshace el corte anterior en vez de dejar una página en blanco
            for ref in corte.findall(qn('w:headerReference')) + corte.findall(qn('w:footerReference')):
                body.sectPr.insert(0, ref)
            body.remove(resto[-1])
            self._aplicar(self.doc.sections[-1], horizontal)
            for e in movidos:
                body.sectPr.addprevious(e)
            return
        sec = self.doc.add_section(WD_SECTION.NEW_PAGE)
        self._aplicar(sec, horizontal)
        for e in movidos:
            body.sectPr.addprevious(e)

    @staticmethod
    def _orientacion_de(sectpr):
        pgsz = sectpr.find(qn('w:pgSz'))
        return pgsz is not None and pgsz.get(qn('w:orient')) == 'landscape'

    def _aplicar(self, sec, horizontal):
        w, h = Twips(12240), Twips(15840)
        if horizontal:
            sec.orientation, sec.page_width, sec.page_height = WD_ORIENT.LANDSCAPE, h, w
            sec.left_margin = sec.right_margin = Twips(1417)
            sec.top_margin = sec.bottom_margin = Twips(1417)
        else:
            sec.orientation, sec.page_width, sec.page_height = WD_ORIENT.PORTRAIT, w, h
            sec.left_margin = sec.right_margin = Twips(1701)
            sec.top_margin = sec.bottom_margin = Twips(1417)
        self.horizontal = horizontal

    # -- bloques
    def titulo(self, nivel, texto, salto=False, sin_numero=False):
        p = self.doc.add_paragraph(style=f'Heading {min(nivel, 5)}')
        runs(p, texto)
        if salto:
            p.paragraph_format.page_break_before = True
        if sin_numero:
            _numpr(p._p.get_or_add_pPr(), 0, 0)
        return p

    def parrafo(self, texto, estilo='Cuerpo'):
        p = self.doc.add_paragraph(style=estilo)
        runs(p, texto)
        return p

    def lista(self, items, ordenada):
        if self.referencias and not ordenada:
            for it in items:
                self.parrafo(it, 'Referencia')
            return
        if ordenada:
            _num(self.numbering, self.next_num, self.aid_decimal, reiniciar=True)
            numid = self.next_num
            self.next_num += 1
        else:
            numid = self.num_vineta
        for it in items:
            p = self.doc.add_paragraph(style='Lista cuerpo')
            _numpr(p._p.get_or_add_pPr(), numid, 0)
            if 'http' in it:  # justificar una URL larga abre espacios enormes en la línea anterior
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            runs(p, it)

    def imagen(self, ruta, leyenda, horizontal=False, max_alto_cm=None):
        from PIL import Image
        if horizontal:
            self.orientar(True, arrastrar=True)
        with Image.open(ruta) as im:
            w, h = im.size
        ancho = self.ancho_cm()
        alto_disp = max_alto_cm or (14.0 if self.horizontal else 20.5)
        ancho_img = min(ancho, alto_disp * w / h)
        p = self.doc.add_paragraph(style='Figura')
        p.add_run().add_picture(str(ruta), width=Cm(ancho_img))
        if leyenda:
            self.figura += 1
            self.parrafo(f'Figura {self.figura}. {leyenda}', 'Leyenda de figura')
        if horizontal:
            self.orientar(False)

    def tabla(self, cab, alin, filas, columnas=None, nota=None):
        if columnas:
            idx = [cab.index(c) for c in columnas]
            cab, alin = [cab[i] for i in idx], [alin[i] for i in idx]
            filas = [[f[i] if i < len(f) else '' for i in idx] for f in filas]
        n = len(cab)
        filas = [f + [''] * (n - len(f)) for f in filas]
        natural, minimo, media = [], [], []
        for j in range(n):
            cuerpo = [len(texto_plano(f[j])) for f in filas] or [0]
            palabras = [len(w) for c in [cab[j]] + [f[j] for f in filas] for w in texto_plano(c).split()] or [1]
            minimo.append(min(max(palabras), 16) + 3)  # la palabra más larga y los márgenes de la celda
            natural.append(max(minimo[-1], min(max(cuerpo), 42) + 2))
            media.append(sum(cuerpo) / len(cuerpo))
        req = sum(natural)
        horizontal = self.horizontal or (req * 0.17 > 15.6 and n >= 5)
        self.orientar(horizontal, arrastrar=True)
        ancho = self.ancho_cm()
        estilo = 'Tabla texto'
        if req * 0.17 > ancho * 1.6:
            estilo = 'Tabla texto 8'
        chars = ancho / (0.17 if estilo == 'Tabla texto' else 0.15)
        if sum(natural) <= chars:
            pesos = natural
        else:
            resto = max(chars - sum(minimo), 0)
            extra = [max(media[j] - minimo[j], 0) ** 0.8 for j in range(n)]
            se = sum(extra) or 1
            pesos = [minimo[j] + resto * extra[j] / se for j in range(n)]
        total = sum(pesos)
        tw = int(ancho * 567)
        anchos = [int(tw * p / total) for p in pesos]
        if nota:
            self.parrafo(nota)
        t = self.doc.add_table(rows=1 + len(filas), cols=n)
        t.autofit = False
        tbl = t._tbl
        tblpr = tbl.tblPr
        for tag, attrs in (('w:tblW', {'w:w': str(sum(anchos)), 'w:type': 'dxa'}), ('w:tblLayout', {'w:type': 'fixed'})):
            for e in tblpr.findall(qn(tag)):
                tblpr.remove(e)
            e = OxmlElement(tag)
            for k, v in attrs.items():
                e.set(qn(k), v)
            tblpr.append(e)
        bordes = OxmlElement('w:tblBorders')
        for lado in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
            e = OxmlElement(f'w:{lado}')
            e.set(qn('w:val'), 'single')
            e.set(qn('w:sz'), '4')
            e.set(qn('w:color'), '808080')
            bordes.append(e)
        tblpr.append(bordes)
        mar = OxmlElement('w:tblCellMar')
        for lado, v in (('left', 60), ('right', 60)):
            e = OxmlElement(f'w:{lado}')
            e.set(qn('w:w'), str(v))
            e.set(qn('w:type'), 'dxa')
            mar.append(e)
        tblpr.append(mar)
        for j, gc in enumerate(tbl.tblGrid.findall(qn('w:gridCol'))):
            gc.set(qn('w:w'), str(anchos[j]))
        for i, fila in enumerate([cab] + filas):
            row = t.rows[i]
            if i == 0:
                trpr = row._tr.get_or_add_trPr()
                e = OxmlElement('w:tblHeader')
                trpr.append(e)
            for j, cell in enumerate(row.cells):
                cell.width = Twips(anchos[j])
                p = cell.paragraphs[0]
                p.style = self.doc.styles[estilo]
                if alin[j] == 'right' and i > 0:
                    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                elif alin[j] == 'center':
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                runs(p, fila[j], bold=(i == 0))
                if i == 0:
                    tcpr = cell._tc.get_or_add_tcPr()
                    shd = OxmlElement('w:shd')
                    shd.set(qn('w:val'), 'clear')
                    shd.set(qn('w:color'), 'auto')
                    shd.set(qn('w:fill'), 'BFBFBF')
                    tcpr.append(shd)
        sep = self.doc.add_paragraph(style='Cuerpo')
        sep.paragraph_format.space_after = Pt(4)
        sep.paragraph_format.line_spacing = 0.8
        if horizontal and not self.fijo_horizontal:
            self.pendiente_vertical = True
        return t

    def bloques(self, blocks, base, quitar_numeros=False, leyendas=None, figura=None, columnas=None, nota=None, origen=None):
        """base: nivel del documento que corresponde a '##' del .md."""
        leyendas = list(leyendas or [])
        ntabla, cuenta_h = 0, None
        self.pendiente_vertical = False
        for k, b in enumerate(blocks):
            if self.pendiente_vertical and b[0] != 'table':
                self.orientar(False)
                self.pendiente_vertical = False
            if b[0] == 'h':
                nivel = base + b[1] - 2
                texto = re.sub(r'^\d+(\.\d+)*\.?\s+', '', b[2]) if quitar_numeros and b[1] == 2 else b[2]
                self.titulo(nivel, texto)
                cuenta_h = b[2]
            elif b[0] == 'p':
                self.parrafo(b[1])
                if figura and cuenta_h == figura[0]:
                    if isinstance(figura[1], tuple):
                        self.imagen(recorte_pdf(*figura[1], TMP / 'recorte.png'), figura[2], horizontal=True,
                                    max_alto_cm=9.8)
                    else:
                        self.imagen(figura[1], figura[2])
                    figura = None
            elif b[0] in ('ul', 'ol'):
                self.lista(b[1], b[0] == 'ol')
            elif b[0] == 'table':
                self.tabla(b[1], b[2], b[3], (columnas or {}).get(ntabla), (nota or {}).get(ntabla))
                ntabla += 1
            elif b[0] == 'code' and b[1] == 'mermaid':
                ley = leyendas.pop(0) if leyendas else None
                destino = TMP / f'mermaid_{len(list(TMP.iterdir()))}.png'
                if b[2].lstrip().startswith('quadrantChart'):
                    m = re.search(r'title\s+(.*)', b[2])
                    self.imagen(dibujar_cuadrante(b[2], destino), ley or (m.group(1).strip() if m else None))
                else:
                    self.imagen(dibujar_arbol(b[2], destino), ley)
            elif b[0] == 'img':
                ruta = (origen.parent / b[2]).resolve()
                if ruta.suffix.lower() == '.svg':
                    ruta = svg_a_png(ruta, TMP / (ruta.stem + '.png'))
                from PIL import Image
                with Image.open(ruta) as im:
                    ancho = im.size[0] / im.size[1] > 1.3
                self.imagen(ruta, b[1], horizontal=ancho)
        if self.pendiente_vertical:
            self.orientar(False)
            self.pendiente_vertical = False


def limpiar_cuerpo(doc, desde_toc):
    """Quita el contenido de la plantilla. Con desde_toc conserva portada e índice."""
    body = doc.element.body
    hijos = list(body)
    corte = 0
    if desde_toc:
        corte = next(i for i, e in enumerate(hijos)
                     if e.tag == qn('w:sdt') and any('TOC' in t.text for t in e.iter(qn('w:instrText')) if t.text)) + 1
    for e in hijos[corte:]:
        if e.tag != qn('w:sectPr'):
            body.remove(e)


def documento_final(destino):
    doc = docx.Document(str(BASE))
    limpiar_cuerpo(doc, desde_toc=True)
    for t in doc.element.body.iter(qn('w:instrText')):  # índice con títulos de nivel 1 y 2
        if t.text and 'TOC' in t.text:
            t.text = t.text.replace('"1-3"', '"1-2"')
    esc = Escritor(doc, numerar_titulos=True)
    for parte in PARTES:
        esc.titulo(1, parte['h1'])
        esc.referencias = parte.get('referencias', False)
        if 'md' in parte:
            blocks = [b for b in parse_md(parte['md'].read_text(encoding='utf-8')) if not (b[0] == 'h' and b[1] == 1)]
            esc.bloques(blocks, 2, quitar_numeros=parte.get('quitar_numeros', False), origen=parte['md'])
        for k, sp in enumerate(parte.get('subpartes', [])):
            esc.titulo(2, sp['h2'], salto=k > 0)
            mds = sp['md'] if isinstance(sp['md'], list) else [sp['md']]
            for md in mds:
                blocks = parse_md(md.read_text(encoding='utf-8'))
                if len(mds) > 1:
                    base = 4
                    for b in blocks:
                        if b[0] == 'h' and b[1] == 1:
                            esc.titulo(3, b[2])
                    blocks = [b for b in blocks if not (b[0] == 'h' and b[1] == 1)]
                else:
                    base = 3
                    blocks = [b for b in blocks if not (b[0] == 'h' and b[1] == 1)]
                if 'secciones' in sp:
                    blocks = seleccionar(blocks, sp['secciones'], sp.get('intro', True))
                esc.bloques(blocks, base, leyendas=sp.get('leyendas'), figura=sp.get('figura'),
                            columnas=sp.get('columnas'), nota=sp.get('nota'), origen=md)
    doc.save(str(destino))


def documento_anexo(letra, titulo, md, destino, horizontal):
    doc = docx.Document(str(BASE))
    limpiar_cuerpo(doc, desde_toc=False)
    esc = Escritor(doc, numerar_titulos=False)
    esc._aplicar(doc.sections[-1], horizontal)
    esc.fijo_horizontal = horizontal
    p = esc.titulo(1, f'Anexo {letra}. {titulo}')
    p.paragraph_format.page_break_before = False
    esc.parrafo('Programa de Modernización del Aeropuerto Internacional de El Salvador (ES-L1173)')
    blocks = [b for b in parse_md(md.read_text(encoding='utf-8')) if not (b[0] == 'h' and b[1] == 1)]
    esc.bloques(blocks, 2, origen=md)
    doc.save(str(destino))

# ---------------------------------------------------------------- Word


PS_WORD = r'''
param([string]$entrada, [string]$pdf, [string]$guardar)
$ErrorActionPreference = 'Stop'
$w = New-Object -ComObject Word.Application
$w.Visible = $false
$w.DisplayAlerts = 0
try {
  $d = $w.Documents.Open($entrada, $false, $false)
  $d.Repaginate()
  foreach ($t in $d.TablesOfContents) { $t.Update() }
  $d.Repaginate()
  foreach ($t in $d.TablesOfContents) { $t.UpdatePageNumbers() }
  if ($guardar -eq '1') { $d.Save() }
  $d.ExportAsFixedFormat($pdf, 17, $false, 0, 0, 1, 1, 0, $true, $true, 1)
  $d.Close(0)
} finally { $w.Quit() }
'''


def word(entrada, pdf, guardar):
    ps = TMP / 'word.ps1'
    ps.write_text(PS_WORD, encoding='utf-8-sig')
    subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', str(ps), '-entrada', str(entrada),
                    '-pdf', str(pdf), '-guardar', '1' if guardar else '0'], check=True, timeout=900)


def revisar_pdf(pdf):
    import fitz
    malos = []
    with fitz.open(str(pdf)) as d:
        for i, page in enumerate(d):
            for m in PROHIBIDO.finditer(page.get_text()):
                malos.append(f'{pdf.name}, página {i + 1}: {m.group(0)!r}')
    return malos


def main():
    global TMP
    sin_word = '--sin-word' in sys.argv
    OUT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        TMP = Path(tmp)
        final = OUT / f'{NOMBRE}.docx'
        documento_final(final)
        print('docx:', final.relative_to(REPO))
        pdfs = []
        if not sin_word:
            word(final, OUT / f'{NOMBRE}.pdf', guardar=True)
            pdfs.append(OUT / f'{NOMBRE}.pdf')
            for letra, nombre, md, titulo, horizontal in ANEXOS_GENERADOS:
                tmp_docx = TMP / f'anexo_{letra}.docx'
                documento_anexo(letra, titulo, md, tmp_docx, horizontal)
                destino = OUT / f'Anexo {letra} - {nombre}.pdf'
                word(tmp_docx, destino, guardar=False)
                pdfs.append(destino)
        for letra, nombre, origen in ANEXOS_COPIADOS:
            destino = OUT / f'Anexo {letra} - {nombre}.pdf'
            shutil.copyfile(origen, destino)
            pdfs.append(destino)
        shutil.copyfile(XML_CRONOGRAMA[0], OUT / XML_CRONOGRAMA[1])
        malos = [m for p in pdfs for m in revisar_pdf(p)]
        for p in sorted(pdfs):
            print('pdf:', p.relative_to(REPO))
        if malos:
            print('REVISAR, texto que no debe estar en un entregable:')
            for m in malos:
                print('  ', m)
            sys.exit(1)


TMP = Path(tempfile.gettempdir())

if __name__ == '__main__':
    main()

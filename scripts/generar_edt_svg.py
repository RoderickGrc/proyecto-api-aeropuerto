from html import escape
from pathlib import Path


OUTPUT = Path(__file__).with_name("edt-jerarquico.svg")

OBJECTIVE = "Objetivo: Mejorar la conectividad aérea del AIES para el desarrollo turístico"

COMPONENTS = [
    (
        "1. Obras y adecuaciones",
        "#1565C0",
        "#EAF3FC",
        [
            ("1.1 Diseños de las obras aprobados", [
                "1.1.1 Diseños de la terminal revisados y aprobados",
                "1.1.2 Diseños de plataformas y calle Foxtrot revisados y aprobados",
                "1.1.3 Diseños del estacionamiento y del sistema solar revisados y aprobados",
                "1.1.4 Diseños del SSEI revisados y aprobados",
            ]),
            ("1.2 Terminal de pasajeros ampliada", [
                "1.2.1 Estructura y envolvente de la terminal construidas",
                "1.2.2 Salas de espera, circulación y áreas de apoyo terminadas",
                "1.2.3 Instalaciones eléctricas, hidráulicas, climatización y contra incendio recibidas",
                "1.2.4 Puentes de abordaje, mobiliario y equipos instalados",
                "1.2.5 Accesibilidad universal, movilidad del cuidado y criterios de sostenibilidad incorporados",
            ]),
            ("1.3 Plataformas de contacto y remotas", [
                "1.3.1 Plataforma de posiciones de contacto construida",
                "1.3.2 Plataforma de posiciones remotas construida",
                "1.3.3 Señalización, luces y torres de iluminación de plataforma instaladas",
            ]),
            ("1.4 Calle de rodaje Foxtrot", [
                "1.4.1 Pavimento y hombros de la calle Foxtrot construidos",
                "1.4.2 Señalización y balizamiento de la calle Foxtrot instalados",
            ]),
            ("1.5 Estacionamiento y energía solar", [
                "1.5.1 Edificio de estacionamiento construido",
                "1.5.2 Sistemas de acceso, tráfico y áreas de alquiler instalados",
                "1.5.3 Sistema de generación solar instalado",
            ]),
            ("1.6 SSEI reubicado y en operación", [
                "1.6.1 Edificio del SSEI y vías de acceso construidos",
                "1.6.2 SSEI en funcionamiento en la nueva ubicación",
            ]),
            ("1.7 Supervisión, PGAS de obra y recepción", [
                "1.7.1 Supervisión de la terminal y del estacionamiento ejecutada",
                "1.7.2 Supervisión de plataformas, calle Foxtrot y SSEI ejecutada",
                "1.7.3 PGAS de construcción implementado",
                "1.7.4 Planos de obra ejecutada y actas de recepción aprobados",
            ]),
        ],
    ),
    (
        "2. Fortalecimiento institucional",
        "#2E7D32",
        "#EBF6EC",
        [
            ("2.1 Plan estratégico del sistema aeronáutico aprobado", []),
            ("2.2 Plan Maestro actualizado y funcionarios capacitados", [
                "2.2.1 Plan Maestro Aeroportuario actualizado y aprobado",
                "2.2.2 Funcionarios capacitados en planificación, gestión y operación",
            ]),
            ("2.3 Estrategia y capacitación BIM", [
                "2.3.1 Estrategia BIM aprobada",
                "2.3.2 Personal de ingeniería capacitado en BIM",
            ]),
            ("2.4 Estudio de conectividad terrestre entregado", []),
            ("2.5 Estudio de diversificación de destinos entregado", []),
            ("2.6 Auditoría y capacitación EDGE", [
                "2.6.1 Auditoría para la certificación EDGE realizada",
                "2.6.2 Personal capacitado en certificación EDGE",
            ]),
            ("2.7 Estudio de separación de flujos entregado", []),
            ("2.8 Estudio de movilidad interna entregado", []),
            ("2.9 Programa de igualdad e inclusión ejecutado", []),
        ],
    ),
    (
        "3. Administración, evaluación y auditorías",
        "#AD5A00",
        "#FFF3E5",
        [
            ("3.1 Condiciones de arranque cumplidas", [
                "3.1.1 Unidad ejecutora conformada y en funciones",
                "3.1.2 Reglamento operativo vigente",
                "3.1.3 Convenio de transferencia de recursos vigente",
                "3.1.4 Cuenta especial aperturada",
            ]),
            ("3.2 Planes de ejecución aprobados", [
                "3.2.1 Plan de ejecución plurianual aprobado",
                "3.2.2 Planes operativos anuales aprobados",
                "3.2.3 Plan de adquisiciones aprobado",
            ]),
            ("3.3 Condiciones socioambientales y de seguridad operacional", [
                "3.3.1 Sistema de gestión ambiental y social y plan de acción vigentes",
                "3.3.2 Protocolo de seguridad operacional aprobado por la AAC",
                "3.3.3 Mecanismo de quejas y reclamos en operación",
                "3.3.4 Informes de cumplimiento socioambiental presentados",
            ]),
            ("3.4 Contratos del programa firmados", [
                "3.4.1 Contratos de obras del Componente I firmados",
                "3.4.2 Contrato de supervisión firmado",
                "3.4.3 Contratos de consultorías del Componente II firmados",
                "3.4.4 Contratos de la unidad ejecutora, evaluación y auditoría firmados",
            ]),
            ("3.5 Control financiero, evaluación y cierre", [
                "3.5.1 Desembolsos justificados e informes financieros presentados",
                "3.5.2 Auditorías externas emitidas",
                "3.5.3 Evaluaciones de medio término y de cierre realizadas",
                "3.5.4 Informe de terminación y cierre administrativo del programa",
            ]),
        ],
    ),
]

WIDTH = 3600
MARGIN = 80
GAP = 50
COLUMN_WIDTH = (WIDTH - 2 * MARGIN - 2 * GAP) // 3
ROOT_Y = 55
ROOT_H = 105
COMPONENT_Y = 250
COMPONENT_H = 95
GROUP_START_Y = 420
GROUP_GAP = 24
GROUP_PAD = 22
OUTCOME_X_PAD = 38
OUTCOME_W_PAD = 76
LEAF_INDENT = 72
LEAF_RIGHT_PAD = 34
BOX_GAP = 13


def wrap(text, width):
    return [text]


def text_height(text, chars, line_height=25, padding=25):
    return len(wrap(text, chars)) * line_height + padding


def svg_text(lines, x, y, width, line_height, size, color, weight="400", anchor="start"):
    if anchor == "middle":
        tx = x + width / 2
    else:
        tx = x
    tspans = []
    for index, line in enumerate(lines):
        dy = 0 if index == 0 else line_height
        tspans.append(
            f'<tspan x="{tx:.1f}" dy="{dy}">{escape(line)}</tspan>'
        )
    return (
        f'<text x="{tx:.1f}" y="{y:.1f}" text-anchor="{anchor}" '
        f'font-family="Arial, Helvetica, sans-serif" font-size="{size}" '
        f'font-weight="{weight}" fill="{color}">{"".join(tspans)}</text>'
    )


def build():
    columns = []
    max_bottom = 0

    for component_index, (component, color, tint, outcomes) in enumerate(COMPONENTS):
        x = MARGIN + component_index * (COLUMN_WIDTH + GAP)
        y = GROUP_START_Y
        groups = []
        for outcome, leaves in outcomes:
            outcome_h = text_height(outcome, 48, 27, 31)
            leaf_specs = []
            leaf_y = y + GROUP_PAD + outcome_h + 18
            for leaf in leaves:
                leaf_h = text_height(leaf, 49, 24, 29)
                leaf_specs.append((leaf, leaf_y, leaf_h))
                leaf_y += leaf_h + BOX_GAP

            if leaves:
                group_h = leaf_y - y - BOX_GAP + GROUP_PAD
            else:
                group_h = GROUP_PAD + outcome_h + GROUP_PAD

            groups.append((outcome, y, group_h, outcome_h, leaf_specs))
            y += group_h + GROUP_GAP

        bottom = y - GROUP_GAP
        max_bottom = max(max_bottom, bottom)
        columns.append((x, component, color, tint, groups, bottom))

    height = max_bottom + 90
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" '
        f'viewBox="0 0 {WIDTH} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Estructura jerárquica de la EDT del proyecto de aeropuerto</title>',
        '<desc id="desc">Objetivo general, tres componentes, resultados y productos de la estructura de desglose del trabajo.</desc>',
        '<rect width="100%" height="100%" fill="#F7F9FC"/>',
        '<defs><filter id="shadow" x="-10%" y="-10%" width="120%" height="130%">'
        '<feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#17324D" flood-opacity=".12"/>'
        '</filter></defs>',
    ]

    root_x = 780
    root_w = 2040
    parts.append(
        f'<rect x="{root_x}" y="{ROOT_Y}" width="{root_w}" height="{ROOT_H}" rx="22" '
        'fill="#173B63" filter="url(#shadow)"/>'
    )
    root_lines = wrap(OBJECTIVE, 76)
    root_text_y = ROOT_Y + (ROOT_H - (len(root_lines) - 1) * 34) / 2 + 10
    parts.append(svg_text(root_lines, root_x, root_text_y, root_w, 34, 30, "#FFFFFF", "500", "middle"))

    root_center_x = root_x + root_w / 2
    junction_y = 205
    parts.append(
        f'<path d="M {root_center_x} {ROOT_Y + ROOT_H} V {junction_y}" '
        'stroke="#7890A8" stroke-width="5" fill="none"/>'
    )
    first_center = columns[0][0] + COLUMN_WIDTH / 2
    last_center = columns[-1][0] + COLUMN_WIDTH / 2
    parts.append(
        f'<path d="M {first_center} {junction_y} H {last_center}" '
        'stroke="#7890A8" stroke-width="5" fill="none"/>'
    )

    for x, component, color, tint, groups, bottom in columns:
        center_x = x + COLUMN_WIDTH / 2
        parts.append(
            f'<path d="M {center_x} {junction_y} V {COMPONENT_Y}" '
            'stroke="#7890A8" stroke-width="5" fill="none"/>'
        )
        parts.append(
            f'<rect x="{x}" y="{COMPONENT_Y}" width="{COLUMN_WIDTH}" height="{COMPONENT_H}" '
            f'rx="18" fill="{color}" filter="url(#shadow)"/>'
        )
        component_lines = wrap(component, 40)
        component_text_y = COMPONENT_Y + (COMPONENT_H - (len(component_lines) - 1) * 29) / 2 + 9
        parts.append(svg_text(component_lines, x, component_text_y, COLUMN_WIDTH, 29, 26, "#FFFFFF", "500", "middle"))

        trunk_x = x + 26
        parts.append(
            f'<path d="M {center_x} {COMPONENT_Y + COMPONENT_H} V {GROUP_START_Y - 18} '
            f'H {trunk_x} V {bottom - 30}" stroke="{color}" stroke-width="4" fill="none" opacity=".72"/>'
        )

        for outcome, group_y, group_h, outcome_h, leaves in groups:
            outcome_x = x + OUTCOME_X_PAD
            outcome_w = COLUMN_WIDTH - OUTCOME_W_PAD
            outcome_y = group_y + GROUP_PAD
            parts.append(
                f'<path d="M {trunk_x} {outcome_y + outcome_h / 2} H {outcome_x}" '
                f'stroke="{color}" stroke-width="4" fill="none" opacity=".72"/>'
            )
            parts.append(
                f'<rect x="{x + 14}" y="{group_y}" width="{COLUMN_WIDTH - 28}" height="{group_h}" '
                f'rx="18" fill="#FFFFFF" stroke="{color}" stroke-width="2" opacity=".98"/>'
            )
            parts.append(
                f'<rect x="{outcome_x}" y="{outcome_y}" width="{outcome_w}" height="{outcome_h}" '
                f'rx="13" fill="{tint}" stroke="{color}" stroke-width="2.5"/>'
            )
            outcome_lines = wrap(outcome, 48)
            outcome_text_y = outcome_y + (outcome_h - (len(outcome_lines) - 1) * 27) / 2 + 8
            parts.append(svg_text(outcome_lines, outcome_x + 22, outcome_text_y, outcome_w - 44, 27, 23, color, "500"))

            if leaves:
                leaf_x = x + LEAF_INDENT
                leaf_w = COLUMN_WIDTH - LEAF_INDENT - LEAF_RIGHT_PAD
                leaf_trunk_x = x + 54
                first_leaf_mid = leaves[0][1] + leaves[0][2] / 2
                last_leaf_mid = leaves[-1][1] + leaves[-1][2] / 2
                parts.append(
                    f'<path d="M {leaf_trunk_x} {outcome_y + outcome_h} V {last_leaf_mid}" '
                    f'stroke="{color}" stroke-width="3" fill="none" opacity=".52"/>'
                )
                for leaf, leaf_y, leaf_h in leaves:
                    leaf_mid = leaf_y + leaf_h / 2
                    parts.append(
                        f'<path d="M {leaf_trunk_x} {leaf_mid} H {leaf_x}" '
                        f'stroke="{color}" stroke-width="3" fill="none" opacity=".52"/>'
                    )
                    parts.append(
                        f'<rect x="{leaf_x}" y="{leaf_y}" width="{leaf_w}" height="{leaf_h}" '
                        'rx="11" fill="#FFFFFF" stroke="#CBD6E2" stroke-width="2"/>'
                    )
                    leaf_lines = wrap(leaf, 49)
                    leaf_text_y = leaf_y + (leaf_h - (len(leaf_lines) - 1) * 24) / 2 + 7
                    parts.append(svg_text(leaf_lines, leaf_x + 19, leaf_text_y, leaf_w - 38, 24, 20, "#263746"))

    parts.append("</svg>")
    return "\n".join(parts)


OUTPUT.write_text(build(), encoding="utf-8")
print(OUTPUT)

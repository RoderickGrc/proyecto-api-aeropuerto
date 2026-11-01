#!/usr/bin/env python3
"""Genera la matriz de adquisiciones del programa (CSV, PDF A4 horizontal y tabla de docs/matriz-adquisiciones.md).

Base: Anexo III y Anexo III.i de la Propuesta de Préstamo, los avisos de 2026, el Plan de Adquisiciones 2026-2,
la EDT (docs/edt.md) y el cronograma por actividades (cronograma_actividades.csv). Una fila por contrato (o por grupo de contratos homogéneo),
con los campos mínimos de la clase 7 (código EDT, paquete, bien/servicio/obra, cantidad, presupuesto, fuente y porcentaje, modalidad, fechas de
inicio, publicación, firma y término, fecha requerida de entrega, responsable y estado) y las actividades del cronograma de cada contrato
(proceso de compra y ejecución), para la trazabilidad entre adquisiciones y actividades planificadas. Escribe matriz_adquisiciones.csv,
matriz_adquisiciones_ES-L1173.pdf y la tabla entre las marcas <!-- matriz:inicio --> y <!-- matriz:fin --> del documento. Requiere PyMuPDF.
"""
from __future__ import annotations
import csv
import io
import json
import math
from datetime import date, timedelta
from html import escape
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
DOC = HERE.parent / 'docs' / 'matriz-adquisiciones.md'
MESES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
RES = json.loads((HERE / 'resumen.json').read_text(encoding='utf-8'))
EST = json.loads((HERE / 'estimacion_costos.json').read_text(encoding='utf-8'))
ELEM = {r['id']: float(r['E_usd']) for r in csv.DictReader((HERE / 'estimacion_costos.csv').open(encoding='utf-8-sig'))}
ACT = {}
for _r in csv.DictReader((HERE / 'cronograma_actividades.csv').open(encoding='utf-8-sig')):
    _r['float'] = int(_r['float'] or 0)
    _r['crit'] = bool(_r['critical'].strip())
    _r['base'] = float(_r['base'])  # US$ M sin contingencia: es el valor esperado PERT de la estimación
    ACT[_r['code']] = _r
FIN = RES['fin']  # fin del programa
PAQ = {r['code']: r['name'] for r in csv.DictReader((HERE / 'cronograma_paquetes.csv').open(encoding='utf-8-sig'))}
ORDEN = {c: i for i, c in enumerate(ACT)}  # orden del cronograma, para los rangos de actividades


def D(code: str, k: str) -> date:
    return date.fromisoformat(ACT[code][k])


def add_bd(d: date, n: int) -> date:
    """Suma n días laborables (lunes a viernes, sin feriados)."""
    while n > 0:
        d += timedelta(days=1)
        if d.weekday() < 5:
            n -= 1
    return d


def bd_between(a: date, b: date) -> int:
    """Días laborables (lunes a viernes) de a a b: positivo si b es posterior a a, negativo si es anterior."""
    if b < a:
        return -bd_between(b, a)
    return sum(1 for i in range(1, (b - a).days + 1) if (a + timedelta(days=i)).weekday() < 5)


MARGEN_MIN = 15  # días laborables: por debajo se marca el margen contractual aunque la holgura del CPM sea grande


def dm(d: date | str | None) -> str:
    """Fecha corta: 04-sep-2026."""
    if d is None:
        return 'n/d'
    d = date.fromisoformat(d) if isinstance(d, str) else d
    return f'{d.day:02d}-{MESES[d.month - 1]}-{d.year}'


def ML(d: str | date) -> str:
    d = date.fromisoformat(d) if isinstance(d, str) else d
    return f"{['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'][d.month - 1]} de {d.year}"


def seq(prefix: str, a: int, b: int) -> list[str]:
    return [f'{prefix}-{i:02d}' for i in range(a, b + 1)]


def pk(*packages: str) -> list[str]:
    return [c for c, r in ACT.items() if r['package'] in packages]


def rangos(codes) -> str:
    """Códigos compactos en el orden del cronograma: corridas de dos o más actividades consecutivas como 'a a b'."""
    cs = sorted(set(codes), key=ORDEN.__getitem__)
    out, i = [], 0
    while i < len(cs):
        j = i
        while j + 1 < len(cs) and ORDEN[cs[j + 1]] == ORDEN[cs[j]] + 1:
            j += 1
        out.append(cs[i] if i == j else f'{cs[i]} a {cs[j]}')
        i = j + 1
    return '; '.join(out)


def usd(codes: list[str]) -> float:
    return sum(ACT[c]['base'] for c in codes) * 1e6


ADQ, OBRA, TEC, PLAN, SOC, COORD, FIN_ESP = ('Especialista de adquisiciones', 'Coordinador general de obra', 'Especialista en ingeniería aeroportuaria',
                                              'Especialista de planificación y monitoreo', 'Especialista socioambiental',
                                              'Coordinador del Programa', 'Especialista financiero')
BID, CEPA_F = 'BID 6073/OC-ES (100%)', 'CEPA, fondos propios (100%; 0% BID)'
G_OBRA, G_SUP, G_C2 = 'Obras', 'Supervisión de las obras', 'Componente II: consultorías de fortalecimiento institucional'
G_EVA, G_UEP, G_CEPA = 'Evaluaciones y auditoría externa', 'Unidad Ejecutora del Programa (UEP)', 'Diseños financiados por CEPA, fuera del préstamo'


def contrato(grupo, edt, mr, pa, adq, tipo, cant, just, fuente, mod, rev, tcont, monto, proc, pub, sign, ex, term, anexo, resp, req, estado,
             pkgs=(), corto='', n=1, plazo=None):
    """Fila de la matriz. proc: actividades del proceso de compra; pub y sign: actividades de publicación y de firma;
    ex: actividades de ejecución del contrato; term: las que fijan el término (la que termina última, con su holgura);
    pkgs: paquetes de la EDT; corto: nombre breve del entregable cuando hay más de dos paquetes; n: contratos que agrupa la fila;
    plazo: fecha contractual de entrega, si existe; la entrega requerida es el mínimo entre la fecha más tardía del CPM y ese plazo."""
    last = max(term, key=lambda c: (ACT[c]['finish'], -ACT[c]['float'])) if term else None
    termino = D(last, 'finish') if last else date.fromisoformat(FIN)
    holg_term = ACT[last]['float'] if last else 0
    allc = proc + ex
    cpm = add_bd(termino, holg_term)
    entrega = min(cpm, plazo) if plazo else cpm
    margen = bd_between(termino, plazo) if plazo else None  # margen contractual: del término planificado al plazo del contrato
    return dict(grupo=grupo, edt=edt, mr=mr, pa=pa, adq=adq, tipo=tipo, cant=cant, just=just, fuente=fuente, mod=mod, rev=rev, tcont=tcont,
                monto=monto, inicio=min(D(c, 'start') for c in proc) if proc else None, pub=D(pub, 'start') if pub else None,
                firma=D(sign, 'finish') if sign else None, termino=termino, entrega=entrega, cpm=cpm, plazo=plazo,
                margen=margen, anexo=anexo, resp=resp, req=req, crit=any(ACT[c]['crit'] for c in allc), holg=min(ACT[c]['float'] for c in allc) if allc else None,
                estado=estado, pkgs=list(pkgs), corto=corto, n=n, proc=list(proc), ex=list(ex))


ROWS: list[dict] = []
CORTE = date(2026, 10, 31)
SSEI_CONT = sum(float(ACT[c]['budget']) for c in pk('1.6.1', '1.6.2'))  # US$ M, línea base con contingencia
assert SSEI_CONT >= 5.0, SSEI_CONT
# ---------------- Obras (LPI, FIDIC amarillo, ex ante) ----------------
OBRAS = [
    ('1.2.1 a 1.2.5', 'P1.1.1', 'P00023', 'Ampliación de la terminal de pasajeros (fase 2), con accesibilidad universal y movilidad del cuidado', '1 contrato (18,555 m², 3 niveles, 6 puentes de abordaje)',
     'Elevar el espacio por pasajero en hora pico de 1.89 a 2.24 m² con seis salas de espera y seis posiciones de contacto. Inferencia del cronograma: el contratista diseña la fachada sur (actividades 1.1.1-06 a 1.1.1-08) y la supervisión la revisa. La fuente directa es que el contrato es FIDIC amarillo (diseño y construcción, Anexo III.i, 2.4) y que la expresión de interés P00024 pide "supervisión del diseño de la fachada sur"; el aviso P00023 no menciona diseño. El Anexo III.i (2.1 y 2.4) preveía precalificar, pero el aviso P00023 del 8-oct-2026 es una Solicitud de Ofertas con los requisitos de calificación en la Sección II.A del documento de licitación.',
     ('1.2.1', '1.2.2', '1.2.3', '1.2.4', '1.2.5'), seq('3.4.1', 7, 12), seq('1.1.1', 6, 8), '3.4.1-09', '3.4.1-12', 'sep-2026', 'En licitación: ofertas el 20-nov-2026 (aviso P00023 del 8-oct-2026)', 'Terminal ampliada y equipada'),
    ('1.3.1 a 1.4.2', 'P1.1.2, P1.1.3', 'P00027', 'Plataformas de posiciones de contacto y remotas, y calle de rodaje Foxtrot', '1 contrato (un solo proceso)',
     'Dar servicio a las nuevas posiciones de contacto, reponer las posiciones remotas y reducir el tiempo de rodaje en 28%. Lado aire: requiere el protocolo de seguridad operacional aprobado por la AAC (Anexo III.i, 3.2) y el SSEI reubicado antes de la plataforma remota. Sin aviso publicado al 31-oct-2026, y sin precalificación como las demás licitaciones.',
     ('1.3.1', '1.3.2', '1.3.3', '1.4.1', '1.4.2'), seq('3.4.1', 19, 24), [], '3.4.1-21', '3.4.1-24', 'ago-2026', 'Previsto (PA 2026-2: firma 22-jul-2027)', 'Plataformas y calle Foxtrot con su señalización'),
    ('1.5.1 a 1.5.3', 'P1.2.1', 'P00001', 'Edificio de estacionamiento con accesibilidad universal y sistema de generación solar', '1 contrato (2,050 plazas, 1,920 kWp)',
     'Mantener la ocupación del estacionamiento en 75% con la demanda de 2031 y generar energía solar para el aeropuerto. Aplica las medidas del Grupo BID contra el trabajo forzoso en la cadena de suministro de paneles de silicio (GN-3062-1). Aviso P00001 del 4-sep-2026: Solicitud de Ofertas sin precalificación.',
     ('1.5.1', '1.5.2', '1.5.3'), seq('3.4.1', 1, 6), [], '3.4.1-03', '3.4.1-06', 'dic-2026', 'En licitación: fecha límite de ofertas el 16-oct-2026 (aviso P00001); sin dato del resultado de la evaluación', 'Estacionamiento con accesos y sistema solar'),
    ('1.6.1, 1.6.2', 'P1.3.1', 'P00025', 'Edificio del Servicio de Salvamento y Extinción de Incendios (SSEI)', '1 contrato',
     'El SSEI debe estar reubicado y en operación antes de iniciar la plataforma de posiciones remotas (condición especial de ejecución). El Anexo III registra SBCC, que es un método de consultoría; el Plan de Adquisiciones 2026-2 la corrige a LPI. Con nuestra estimación (valor esperado menor a US$5 M) podría ir por LPN, pero se mantiene LPI porque su línea base con contingencia (US$' + f'{SSEI_CONT:.2f}' + ' M) supera US$5 M. Sin aviso publicado.',
     ('1.6.1', '1.6.2'), seq('3.4.1', 13, 18), [], '3.4.1-15', '3.4.1-18', 'ene-2027', 'Previsto (PA 2026-2: firma 27-may-2027)', 'SSEI construido y en funcionamiento'),
]
for edt, mr, pa, adq, cant, just, packs, proc, extra, pub, sign, anexo, estado, corto in OBRAS:
    ex = pk(*packs)
    term = [c for c in ex if ACT[c]['owner'] == 'Contratista de obra']  # fin de la última actividad del contratista
    ROWS.append(contrato(G_OBRA, edt, mr, pa, adq, 'Obra', cant, just, BID, 'LPI sin precalificación (Solicitud de Ofertas)', 'Internacional, ex ante',
                         'FIDIC amarillo (Anexo III.i, 2.4)', usd(ex), proc, pub, sign, extra + ex, term, anexo, ADQ, OBRA, estado, pkgs=packs, corto=corto))
# ---------------- Supervisiones (SBCC, ex ante, lista corta de 5 a 8 firmas) ----------------
SUPS = [
    ('1.7.1', 'P00024', 'Supervisión del diseño y la construcción de la terminal de pasajeros', 'Revisa el diseño de la fachada sur del contratista (inferencia, ver la fila 1) y valida el de la fachada norte, y supervisa BIM y EDGE Advanced. Solicitud de expresiones de interés P00024 con cierre el 6-oct-2026 (publicación supuesta el 22-sep-2026, S-III.17). Lista corta de 5 a 8 firmas con experiencia en terminales de más de 10,000 m².',
     seq('1.7.1', 1, 2) + ['1.7.1-05'], ['1.1.1-07'], seq('3.4.2', 7, 12), '3.4.2-07', '3.4.2-12', 'Expresiones de interés cerradas el 6-oct-2026 (PA 2026-2: previsto, firma 19-may-2027)'),
    ('1.7.1', 'P00002', 'Supervisión de la construcción del estacionamiento y del sistema solar', 'Control independiente de calidad, estimaciones y recepción del estacionamiento. Expresiones de interés del 6 al 20-may-2026, lista corta de 5 a 8 firmas. El PA 2026-2 la marca en curso; la firma sigue el contrato de obra.',
     seq('1.7.1', 3, 4) + ['1.7.1-06'], [], seq('3.4.2', 1, 6), '3.4.2-01', '3.4.2-06', 'En curso (PA 2026-2): expresiones de interés cerradas el 20-may-2026; firma prevista 3-feb-2027'),
    ('1.7.2', 'P00026', 'Supervisión de la construcción del edificio del SSEI', 'Control independiente de calidad, estimaciones y recepción del SSEI. Lista corta de 5 a 8 firmas.',
     seq('1.7.2', 3, 4) + ['1.7.2-06'], [], seq('3.4.2', 13, 18), '3.4.2-13', '3.4.2-18', 'Previsto (PA 2026-2: firma 10-jun-2027)'),
    ('1.7.2', 'P00028', 'Supervisión de la construcción de las plataformas y de la calle Foxtrot', 'Control independiente de calidad, estimaciones y recepción de las obras del lado aire, con el aeropuerto en operación. Lista corta de 5 a 8 firmas. Holgura de 4 dl: la firma debe seguir al contrato de obra, que es crítico.',
     seq('1.7.2', 1, 2) + ['1.7.2-05'], [], seq('3.4.2', 19, 24), '3.4.2-19', '3.4.2-24', 'Previsto (PA 2026-2: firma 28-jul-2027)'),
]
for edt, pa, adq, just, ex, extra, proc, pub, sign, estado in SUPS:
    # el monto es el de las actividades de supervisión (V1 y V2, que incluye el seguimiento del PGAS); extra: actividades sin costo que la supervisión también ejecuta
    ROWS.append(contrato(G_SUP, edt, 'P1.4.1 a P1.4.3', pa, adq, 'Consultoría', '1 contrato', just, BID,
                         'SBCC', 'Lista corta de 5 a 8 firmas, ex ante', 'Servicios de consultoría (firma)', usd(ex), proc, pub, sign, extra + ex, ex, 'sep-2026',
                         ADQ, OBRA, estado, pkgs=(edt,)))
# ---------------- Componente II: nueve contratos, uno por producto, todos con revisión ex ante ----------------
NOOBJ = {'2.3.1, 2.3.2': ('3.4.3-51', '3.4.3-52'), '2.5': ('3.4.3-53', '3.4.3-54'), '2.6.1, 2.6.2': ('3.4.3-55', '3.4.3-56'),
         '2.7': ('3.4.3-57', '3.4.3-58'), '2.8': ('3.4.3-59', '3.4.3-60'), '2.9': ('3.4.3-61', '3.4.3-62')}  # no objeciones del BID agregadas (S-III.5)
C2 = [  # edt, producto MR, adquisición, justificación, paquetes, proceso, publicación, firma, método, revisión, anexo, área
    ('2.1', 'P2.1', 'Plan Estratégico para el Desarrollo del Sistema Aeronáutico', 'Orientar el desarrollo del sistema aeronáutico nacional (objetivo específico 2: capacidad institucional de CEPA).',
     ('2.1',), seq('3.4.3', 3, 8), '3.4.3-03', '3.4.3-08', 'SBCC', 'Lista corta internacional, ex ante', 'jun-2026', PLAN),
    ('2.2.1, 2.2.2', 'P2.2', 'Actualización del Plan Maestro Aeroportuario y capacitación de 21 funcionarios', 'Actualizar el Plan Maestro con la demanda vigente y capacitar a 21 funcionarios en planificación, gestión y operación. Usa como insumo el Plan Estratégico.',
     ('2.2.1', '2.2.2'), seq('3.4.3', 9, 14), '3.4.3-09', '3.4.3-14', 'SBCC', 'Lista corta internacional, ex ante', 'jun-2026', PLAN),
    ('2.3.1, 2.3.2', 'P2.3', 'Estrategia y capacitación BIM', 'Adoptar BIM en CEPA. Se contrata aparte de EDGE (el Anexo III las registraba juntas). SBCC con lista corta internacional y revisión ex ante: su monto (unos US$259,000) supera el umbral de US$200,000 de la tabla 10 del ROP (S-III.5).',
     ('2.3.1', '2.3.2'), seq('3.4.3', 15, 19), '3.4.3-16', '3.4.3-19', 'SBCC', 'Lista corta internacional, ex ante', 'jun-2026', TEC),
    ('2.4', 'P2.4', 'Estudio de conectividad terrestre del aeropuerto con enfoque de sostenibilidad e inclusión', 'Mejorar el acceso terrestre desde San Salvador y los destinos turísticos.',
     ('2.4',), seq('3.4.3', 20, 25), '3.4.3-20', '3.4.3-25', 'SBCC', 'Lista corta internacional, ex ante', 'ene-2027', PLAN),
    ('2.5', 'P2.5', 'Estudio de mercado para la diversificación de orígenes y destinos internacionales', 'Priorizar mercados y destinos que aumenten la conectividad aérea del país. SBCC con lista corta nacional (menos de US$200,000) y revisión ex ante, como todos los procesos del Anexo III.i (2.5).',
     ('2.5',), seq('3.4.3', 26, 30), '3.4.3-27', '3.4.3-30', 'SBCC', 'Lista corta nacional, ex ante', 'ene-2027', PLAN),
    ('2.6.1, 2.6.2', 'P2.6', 'Auditoría y capacitación para la certificación EDGE', 'Certificar EDGE la terminal y el estacionamiento en una sola auditoría en sitio; el acompañamiento llega hasta el certificado final de la terminal.',
     ('2.6.1', '2.6.2'), seq('3.4.3', 31, 35), '3.4.3-32', '3.4.3-35', 'SCC', 'Lista corta nacional, ex ante', 'jun-2026', TEC),
    ('2.7', 'P2.7', 'Estudio de obras para separar los flujos de llegadas y salidas en la terminal antigua', 'Identificar y priorizar las intervenciones de la terminal existente.',
     ('2.7',), seq('3.4.3', 36, 40), '3.4.3-37', '3.4.3-40', 'SCC', 'Lista corta nacional, ex ante', 'mar-2027', TEC),
    ('2.8', 'P2.8', 'Estudio de movilidad del entorno del aeropuerto, con énfasis en el estacionamiento', 'Resolver los flujos vehiculares hacia el nuevo estacionamiento y las zonas de dejar y recoger pasajeros.',
     ('2.8',), seq('3.4.3', 41, 45), '3.4.3-42', '3.4.3-45', 'SCC', 'Lista corta nacional, ex ante', 'dic-2026', TEC),
    ('2.9', 'P2.9', 'Programa de capacitación en igualdad de oportunidades e inclusión de personas con discapacidad', 'Capacitar a 300 funcionarios de CEPA en tres cohortes de 100.',
     ('2.9',), seq('3.4.3', 46, 50), '3.4.3-47', '3.4.3-50', 'SCC', 'Lista corta nacional, ex ante', 'nov-2026', SOC),
]
for edt, mr, adq, just, packs, proc, pub, sign, mod, rev, anexo, req in C2:
    ex = pk(*packs)
    extra = list(NOOBJ.get(edt, ()))
    for c in extra:  # cada no objeción agregada debe tener la holgura del contrato al que se asigna
        assert ACT[c]['float'] == ACT[sign]['float'], (edt, c)
    ROWS.append(contrato(G_C2, edt, mr, '', adq, 'Consultoría', '1 contrato', just, BID, mod, rev, 'Servicios de consultoría (firma)', usd(ex),
                         ['3.4.3-01', '3.4.3-02'] + proc + extra, pub, sign, ex, ex, anexo, ADQ, req, 'Atrasado (no figura en el PA 2026)', pkgs=packs))
# ---------------- Evaluaciones (SCC) y auditoría externa (SBMC), con su plazo contractual ----------------
EV = {e['tipo']: e for e in RES['evaluaciones']}
EM, EF = EV['Medio término'], EV['Final']
ROWS.append(contrato(G_EVA, '3.5.3', 'P3.2.1', '', 'Evaluación de medio término', 'Consultoría', '1 contrato',
                     f'Medir el avance y los resultados a mitad de la ejecución, según el plan de monitoreo y evaluación (MEL). Plazo contractual (cláusula 5.03): el informe vence 60 días después del primero entre el 50% del tiempo de ejecución planificado ({dm(EM["hito_50_tiempo"])}) y el 50% desembolsado; con el cronograma, el límite es el {dm(EM["limite"])}. Un desembolso acelerado por anticipos de fondos podría adelantarlo (S-III.19). El proceso empieza al proyectar el hito con los contratos de obra firmados (3.5.3-01).',
                     BID, 'SCC', 'Lista corta nacional, ex ante', 'Servicios de consultoría (firma)', usd(['3.5.3-02']),
                     ['3.5.3-01'] + seq('3.4.4', 31, 35) + ['3.4.4-41', '3.4.4-42'], '3.4.4-32', '3.4.4-35',
                     ['3.5.3-02', '3.5.3-03'], ['3.5.3-02', '3.5.3-03'], 'nov-2027', ADQ, PLAN, 'Programado (aún sin proceso en el PA 2026-2)',
                     pkgs=('3.5.3',), plazo=date.fromisoformat(EM['limite'])))
ROWS.append(contrato(G_EVA, '3.5.3', 'P3.2.2', '', 'Evaluación final', 'Consultoría', '1 contrato',
                     f'Medir los resultados al cierre: vence 90 días después del 95% desembolsado o del fin del plazo de desembolsos (S-III.10), el {dm(EF["limite"])} con el cronograma. Su informe precede al último desembolso y a los estados financieros finales: está en la ruta crítica, así que su fecha requerida la fija el CPM y no el plazo contractual.',
                     BID, 'SCC', 'Lista corta nacional, ex ante', 'Servicios de consultoría (firma)', usd(['3.5.3-04']),
                     seq('3.4.4', 36, 40) + ['3.4.4-43', '3.4.4-44'], '3.4.4-37', '3.4.4-40',
                     ['3.5.3-04', '3.5.3-05'], ['3.5.3-04', '3.5.3-05'], 'may-2029', ADQ, PLAN, 'Programado (aún sin proceso en el PA 2026-2)',
                     pkgs=('3.5.3',), plazo=date.fromisoformat(EF['limite'])))
ULT_DESEMB = D('3.5.4-02', 'finish')  # último desembolso: los estados financieros finales vencen 120 días después (cláusula 5.02)
AUD = [  # año, proceso, firma, dictamen, ejecución, ejercicio, estado
    (1, seq('3.4.4', 11, 15), '3.4.4-13', '3.4.4-15', ['3.5.2-02'], 'ejercicio 2026', 'Previsto (PA 2026-2, P00003: firma 5-may-2027)'),
    (2, seq('3.4.4', 16, 20), '3.4.4-18', '3.4.4-20', ['3.5.2-05'], 'ejercicio 2027', 'Programado (fuera del horizonte del PA 2026-2)'),
    (3, seq('3.4.4', 21, 25), '3.4.4-23', '3.4.4-25', ['3.5.2-08'], 'ejercicio 2028', 'Programado (fuera del horizonte del PA 2026-2)'),
    (4, seq('3.4.4', 26, 30), '3.4.4-28', '3.4.4-30', ['3.5.4-03'], 'ejercicio 2029 y estados financieros finales del programa', 'Programado (fuera del horizonte del PA 2026-2)'),
]
for yr, proc, pub, sign, ex, que, estado in AUD:
    plazo = date(2025 + yr, 12, 31) + timedelta(days=120)  # cláusula 5.02: 120 días después del cierre del ejercicio
    if yr == 4:
        plazo = min(plazo, ULT_DESEMB + timedelta(days=120))  # y 120 días después del último desembolso
    ROWS.append(contrato(G_EVA, '3.5.2' if yr < 4 else '3.5.4', '', 'P00003' if yr == 1 else '', f'Auditoría externa, año {yr}: {que}', 'Servicio de auditoría', '1 contrato',
                         f'Estados financieros auditados exigidos por el BID, a cargo de una firma aceptable para el Banco. Plazo contractual (cláusula 5.02): a más tardar el {dm(plazo)}, '
                         + ('120 días después del cierre del ejercicio.' if yr < 4 else '120 días después del último desembolso (3.5.4-02), que es anterior al cierre del ejercicio 2029 más 120 días.')
                         + (' Primer contrato: conserva las fechas del PA 2026-2, el plan oficial de CEPA (proceso P00003, firma el 5-may-2027); el dictamen queda planificado el 16-jun-2027, después de ese plazo. El incumplimiento está previsto y es un riesgo del programa: se gestiona con el BID o se adelanta el proceso.' if yr == 1 else '')
                         + (' Su dictamen es parte de la ruta crítica del cierre.' if yr == 4 else ''),
                         BID, 'SBMC', 'Lista corta nacional, ex ante', 'Servicio de auditoría anual', usd(ex), proc, pub, sign, ex, ex, 'no figura', ADQ, FIN_ESP, estado,
                         pkgs=('3.5.2',) if yr < 4 else ('3.5.4',), plazo=plazo))
# ---------------- UEP: 3CV, contratos del préstamo (elementos U1 y U3 de la estimación) ----------------
# Cada puesto pesa por su honorario mensual PERT y los meses que trabaja. U1 (puestos clave y técnico) y U3 (plantilla ampliada) los lleva 3.1.1-06.
UW = [(v['O'] + 4 * v['M'] + v['P']) / 6 * v['meses'] for v in EST['uep']]
U1, U3 = ELEM['U1'], ELEM['U3']
PL = EST['plantilla']
W3 = {n: sum(x['mensual'] * x['meses'] for x in PL if x['lote'] == n) for n in sorted({x['lote'] for x in PL})}
UEP_EX = ['3.1.1-06']  # nivel de esfuerzo "Administrar el programa": ejecución de los contratos de la UEP hasta el cierre
ROWS.append(contrato(G_UEP, '3.1.1', 'P3.3.1 a P3.3.7', 'P00004 a P00010', 'Personal clave de la UEP: coordinador del programa, coordinador general de obra y especialistas de adquisiciones, financiero, de planificación y monitoreo, técnico y socioambiental',
                     'Consultoría individual', '7 contratos',
                     'Condición previa al primer desembolso, con dedicación exclusiva. Contratos anuales (PA 2026-2: 12 meses desde abril o mayo de 2026) que se renuevan hasta el cierre; el término es el fin de la administración del programa (3.1.1-06).',
                     BID, '3CV', 'Consultores estratégicos, ex ante', 'Consultor individual (contrato anual)', U1 * sum(UW[:7]) / sum(UW), seq('3.4.4', 1, 5), '3.4.4-01', '3.4.4-05', UEP_EX, UEP_EX,
                     'feb-2026', ADQ, COORD, 'Contratados (abr-may 2026); PA 2026-2: contrato en ejecución', pkgs=('3.1.1',), n=7))
ROWS.append(contrato(G_UEP, '3.1.1', 'Requisito del ROP, sección 3.1.2', 'P00014', 'Técnico de apoyo administrativo, llamado "Asistente Administrativo" en el PA',
                     'Consultoría individual', '1 contrato',
                     'Apoyo administrativo de la UEP que agrega el ROP a los siete puestos clave. Contrato anual renovable hasta el cierre.',
                     BID, '3CV', 'Consultores estratégicos, ex ante', 'Consultor individual (contrato anual)', U1 * UW[7] / sum(UW), seq('3.4.4', 6, 10), '3.4.4-06', '3.4.4-10', UEP_EX, UEP_EX,
                     'no figura', ADQ, COORD,
                     'Sin confirmar: el PA 2026-2 lo marca Previsto con firma el 15-ago-2026 y el cronograma la fija el 15-sep-2026, ambas fechas vencidas al corte; no hay dato de contratación',
                     pkgs=('3.1.1',)))
# Plantilla ampliada: una fila por lote (seis). Cada lote tiene sus propias fechas y actividades (3.4.4-45 a 3.4.4-74); una sola fila de 21 contratos
# mezclaría firmas de septiembre de 2026 a octubre de 2027, y 21 filas repetirían las mismas cinco actividades. Cada lote lista sus procesos P000xx.
# Por qué U3 es menor que el monto del PA (se calcula con los datos): el monto del PA cubre 56 meses desde abril de 2026 (hasta PA_FIN) y el programa
# termina antes (UEP_FIN); el atraso de la firma respecto del PA pesa poco.
_pa_tot = sum(x['monto_pa'] for x in PL)
_hz, _fin = date.fromisoformat(EST['supuestos']['horizonte_pa']), date.fromisoformat(EST['uep_periodo']['fin'])
_u3 = sum(x['mensual'] * x['meses'] for x in PL)
_sin_atraso = sum(x['mensual'] * (_fin - date.fromisoformat(str(x['firma_pa']))).days / 30.4375 for x in PL)
MESES_FIN = (_hz - _fin).days / 30.4375
ATRASO = sum(x['monto_pa'] * (date.fromisoformat(str(x['firma_modelo'])) - date.fromisoformat(str(x['firma_pa']))).days for x in PL) / _pa_tot / 30.4375
DIF_PA = (f'sobre todo porque el programa termina el {dm(_fin)}, unos {MESES_FIN:.0f} meses antes del horizonte de 56 meses que suponen los montos del PA '
          f'({dm(_hz)}), y el atraso de la firma, de {ATRASO:.1f} meses en promedio, pesa poco. De los US${(_pa_tot - _u3) / 1e3:,.0f} mil de diferencia en la plantilla completa, '
          f'US${(_pa_tot - _sin_atraso) / 1e3:,.0f} mil son por el horizonte y US${(_sin_atraso - _u3) / 1e3:,.0f} mil por el atraso.')
LOTES = {1: 'diez puestos de agosto de 2026', 2: 'pavimentos aeroportuarios', 3: 'analista social', 4: 'tres puestos de enero de 2027', 5: 'cinco puestos de marzo de 2027', 6: 'Administrador 4 de Proyectos'}
for n in sorted(W3):
    xs = [x for x in PL if x['lote'] == n]
    first = 45 + 5 * (n - 1)  # cinco actividades por lote, de 3.4.4-45 a 3.4.4-74
    proc = seq('3.4.4', first, first + 4)
    ids = [x['proceso'] for x in xs]
    pa_f = sorted({str(x['firma_pa']) for x in xs})
    pa_txt = dm(pa_f[0]) if len(pa_f) == 1 else f'{dm(pa_f[0])} a {dm(pa_f[-1])}'
    vencida = D(proc[-1], 'finish') <= CORTE
    ROWS.append(contrato(G_UEP, '3.1.1', 'Requisito del PEP: plantilla ampliada de 19 plazas', ', '.join(ids), f'Plantilla ampliada de la UEP, lote {n}: {LOTES[n]}',
                         'Consultoría individual', f'{len(xs)} contrato' + ('s' if len(xs) > 1 else ''),
                         f'{"Proceso" if len(ids) == 1 else "Procesos"} {", ".join(ids)}: {"; ".join(x["puesto"] for x in xs)}. Monto del PA 2026-2: US${sum(x["monto_pa"] for x in xs):,.0f}. La matriz usa el valor esperado de la estimación (elemento U3), menor que ese monto sobre todo porque el programa termina unos {MESES_FIN:.0f} meses antes del horizonte de 56 meses del PA (criterio Montos).',
                         BID, '3CV', 'Consultores estratégicos, ex ante', 'Consultor individual (contrato anual)', U3 * W3[n] / sum(W3.values()), proc, proc[0], proc[-1], UEP_EX, UEP_EX,
                         'no figura', ADQ, COORD,
                         f'Previsto en el PA 2026-2 (firma {pa_txt}); el cronograma la fija el {dm(D(proc[-1], "finish"))}' + ('; fecha vencida al corte, sin dato de contratación' if vencida else ''),
                         pkgs=('3.1.1',), n=len(xs)))
# ---------------- Diseños de CEPA, fuera del préstamo (Anexo III.i, sección 3) ----------------


def cepa(edt, adq, just, ajuste, estado):
    r = contrato(G_CEPA, edt, 'Diseño previo a la licitación', '', adq, 'Consultoría de diseño', '1 contrato', just, CEPA_F, 'Contratación de CEPA (fuera de las políticas del BID)',
                 'No aplica (fuera del préstamo)', 'Servicios de consultoría (firma)', None, [], None, None, [ajuste], [ajuste], 'no figura', 'CEPA', TEC, estado, pkgs=(edt,))
    r['crit'] = False
    r['holg'] = ACT[ajuste]['float']
    return r


ROWS.append(cepa('1.1.1', 'Actualización del diseño final de la terminal de pasajeros',
                 'Insumo del paquete 1.1.1: la UEP revisa el expediente desde el 18-may-2026 y lo ajusta con esta firma (1.1.1-02). No tiene monto en el programa.', '1.1.1-02',
                 'En contratación según el Anexo III.i (sep-2025); sin dato posterior. El cronograma supone el expediente entregado antes del 18-may-2026'))
ROWS.append(cepa('1.1.3', 'Diseño final del edificio de estacionamiento con sistema solar',
                 'Insumo del paquete 1.1.3: la UEP revisa el expediente desde el 18-may-2026 y lo ajusta con esta firma (1.1.3-03). No tiene monto en el programa.', '1.1.3-03',
                 'Contratada según el Anexo III.i (sep-2025); la firma ya diseñaba el edificio'))
ROWS.append(cepa('1.1.4', 'Actualización del diseño final del SSEI',
                 'Insumo del paquete 1.1.4: la UEP revisa el diseño desde el 1-jul-2026 y lo ajusta con esta firma (1.1.4-03). No tiene monto en el programa.', '1.1.4-03',
                 'En contratación según el Anexo III.i (sep-2025); sin dato posterior. El cronograma supone el diseño entregado antes del 1-jul-2026'))

# ---------------- Montos: redondeo a miles con resto mayor, para que el total cuadre con la estimación ----------------
# Trazabilidad del costo: toda actividad con costo (salvo 3.1.1-06, que lleva los elementos U1, U2 y U3) está en la ejecución de exactamente un contrato.
CON_COSTO = {c for c, r in ACT.items() if r['base'] > 0}
VECES = {c: sum(c in r['ex'] for r in ROWS if r['monto'] is not None and r['grupo'] != G_UEP) for c in CON_COSTO}
assert all(v == 1 for c, v in VECES.items() if c != '3.1.1-06'), {c: v for c, v in VECES.items() if v != 1 and c != '3.1.1-06'}
assert abs(ACT['3.1.1-06']['base'] * 1e6 - (ELEM['U1'] + ELEM['U2'] + ELEM['U3'])) < 5  # 3.1.1-06 es la única actividad de la UEP con costo
OTROS = [('Gastos operativos de la UEP (ROP 5.4, elemento U2)', ELEM['U2'])]  # lo único que no se contrata como un contrato propio
raw = [r['monto'] for r in ROWS if r['monto'] is not None] + [v for _, v in OTROS]
assert abs(sum(raw) - EST['total_E']) < 5, (sum(raw), EST['total_E'])  # las filas y los gastos operativos son toda la estimación (total_E)
tgt = round(sum(raw) / 1000)
fl = [math.floor(x / 1000) for x in raw]
for i in sorted(range(len(raw)), key=lambda i: raw[i] / 1000 - fl[i], reverse=True)[:tgt - sum(fl)]:
    fl[i] += 1
rounded = [v * 1000 for v in fl]
it = iter(rounded)
for r in ROWS:
    if r['monto'] is not None:
        r['monto'] = next(it)
OTROS = [(n, next(it)) for n, _ in OTROS]
TOTAL = sum(r['monto'] or 0 for r in ROWS)
SIN_CONTRATO = sum(v for _, v in OTROS)
EST_TOTAL = TOTAL + SIN_CONTRATO
# Cada total se redondea a miles por sí mismo y las reservas son la diferencia, para que la tabla cuadre sin saltos de un millar.
BAC = int(round(EST['linea_base'], -3))
CONT = BAC - EST_TOTAL
PRES = int(round(EST['presupuesto'], -3))
GEST = PRES - BAC
assert EST_TOTAL == int(round(EST['total_E'], -3)) and abs(CONT - EST['contingencia']) <= 1000 and abs(GEST - EST['reserva_gestion']) <= 1000
def marca(r: dict) -> str:
    """Marca del margen contractual: la holgura del CPM no basta cuando el contrato fija un plazo más cercano."""
    m = r['margen']
    if m is None or m >= MARGEN_MIN:
        return ''
    if m < 0:
        return f'incumple el plazo contractual del {dm(r["plazo"])} en {-m} dl'
    return f'margen contractual de {m} dl hasta el {dm(r["plazo"])}'


for r in ROWS:
    if r['margen'] is not None and r['margen'] < 0:
        r['estado'] = f'Incumplimiento previsto del plazo contractual ({dm(r["plazo"])}): {r["estado"]}'
RUTA = [r for r in ROWS if r['crit']]
PRESTAMO = [r for r in ROWS if r['monto'] is not None]
N_CONT = sum(r['n'] for r in PRESTAMO)  # contratos reales del préstamo (una fila agrupa varios)
N_CEPA = len(ROWS) - len(PRESTAMO)
for k, r in enumerate(ROWS, start=1):
    r['num'] = k
    r['paq'] = '; '.join(f'{c} {PAQ[c]}' for c in r['pkgs'])
    r['paq_pdf'] = r['paq'] if len(r['pkgs']) <= 2 else r['corto']
    r['acts'] = '; '.join(x for x in (rangos(r['proc']), rangos(r['ex'])) if x)

# ---------------- CSV ----------------
FIELDS = ['n', 'grupo', 'edt', 'paquete_entregable', 'actividades_cronograma', 'contratos', 'producto_mr', 'proceso_pa', 'adquisicion', 'tipo', 'cantidad',
          'justificacion', 'fuente_financiamiento', 'modalidad', 'alcance_revision', 'tipo_contrato', 'monto_usd', 'inicio_proceso', 'publicacion',
          'firma_contrato', 'termino_contrato', 'entrega_cpm', 'plazo_contractual', 'entrega_requerida', 'inicio_anexo_iii', 'responsable', 'area_requirente',
          'ruta_critica', 'holgura_dl', 'margen_contractual_dl', 'estado_2026_10_31']


def iso(d): return d.isoformat() if d else 'n/d'


with (HERE / 'matriz_adquisiciones.csv').open('w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(FIELDS)
    for r in ROWS:
        w.writerow([r['num'], r['grupo'], r['edt'], r['paq'], r['acts'], 0 if r['monto'] is None else r['n'], r['mr'], r['pa'], r['adq'], r['tipo'], r['cant'],
                    r['just'], r['fuente'], r['mod'], r['rev'], r['tcont'], '' if r['monto'] is None else r['monto'], iso(r['inicio']), iso(r['pub']),
                    iso(r['firma']), iso(r['termino']), iso(r['cpm']), r['plazo'].isoformat() if r['plazo'] else '', iso(r['entrega']),
                    r['anexo'], r['resp'], r['req'], 'Sí' if r['crit'] else 'No', r['holg'], '' if r['margen'] is None else r['margen'], r['estado']])

# ---------------- Tablas del documento ----------------
FOOT = [('Total de la matriz (contratos del préstamo)', TOTAL, True)] + [(n, v, False) for n, v in OTROS] + [
    ('Estimación de costos del programa (PERT)', EST_TOTAL, True), ('Reserva de contingencia (percentil 80), incluida en la línea base', CONT, False),
    ('Línea base de costos (BAC)', BAC, True), ('Reserva de gestión (5%), fuera de la línea base', GEST, False), ('Presupuesto del proyecto', PRES, True)]


def ref_txt(r: dict) -> str:
    """Producto de la matriz de resultados (o referencia) y número de proceso del Plan de Adquisiciones."""
    plural = ',' in r['pa'] or ' a ' in r['pa']
    parts = [f'Producto {r["mr"]}' if r['mr'].startswith('P') else r['mr'], f'{"procesos" if plural else "proceso"} {r["pa"]}' if r['pa'] else '']
    return ', '.join(x for x in parts if x)


def entrega_txt(r: dict) -> str:
    """Entrega requerida con su origen cuando la fija un plazo contractual."""
    return dm(r['entrega']) + (' (plazo contractual)' if r['plazo'] and r['plazo'] < r['cpm'] else '')


def md_table() -> str:
    h = ['N.º', 'EDT', 'Paquete de trabajo o entregable', 'Actividades del cronograma', 'Bien, servicio u obra', 'Tipo y cantidad', 'Justificación',
         'Fuente de financiamiento', 'Modalidad', 'Alcance y revisión', 'Tipo de contrato', 'Monto (US$)', 'Inicio del proceso', 'Publicación', 'Firma del contrato',
         'Término del contrato', 'Entrega requerida', 'Inicio según el Anexo III', 'Responsable', 'Área requirente', 'Crítica (holgura mínima)', 'Estado al 31-oct-2026']
    out = ['| ' + ' | '.join(h) + ' |', '|---:|---|---|---|---|---|---|---|---|---|---|---:|' + '---|' * 10]
    grp = None
    for r in ROWS:
        if r['grupo'] != grp:
            grp = r['grupo']
            sub = sum(x['monto'] or 0 for x in ROWS if x['grupo'] == grp)
            out.append('| | | | | **' + grp + '** | | | | | | | **' + (f'{sub:,.0f}' if sub else 'sin monto en el programa') + '** |' + ' |' * 10)
        sub_ref = ref_txt(r)
        name = r['adq'] + (f' ({sub_ref})' if sub_ref else '')
        out.append('| ' + ' | '.join([str(r['num']), r['edt'], r['paq'], r['acts'], name, f'{r["tipo"]}, {r["cant"]}', r['just'], r['fuente'], r['mod'], r['rev'], r['tcont'],
                                      '' if r['monto'] is None else f'{r["monto"]:,.0f}', dm(r['inicio']), dm(r['pub']), dm(r['firma']), dm(r['termino']), entrega_txt(r),
                                      r['anexo'], r['resp'], r['req'], f'{"Sí" if r["crit"] else "No"} ({r["holg"]} dl)' + (f'; **{marca(r)}**' if marca(r) else ''), r['estado']]) + ' |')
    for name, v, bold in FOOT:
        out.append('| | | | | ' + (f'**{name}**' if bold else name) + ' | | | | | | | ' + (f'**{v:,.0f}**' if bold else f'{v:,.0f}') + ' |' + ' |' * 10)
    return '\n'.join(out)


def crit_table() -> str:
    out = ['| N.º | Contrato | Actividades sin holgura | Firma | Término |', '|---:|---|---|---|---|']
    for r in RUTA:
        cr = [c for c in r['proc'] + r['ex'] if ACT[c]['crit']]
        out.append(f'| {r["num"]} | {r["adq"]} ({r["edt"]}) | {rangos(cr)} | {dm(r["firma"])} | {dm(r["termino"])} |')
    return '\n'.join(out)


def put(text: str, tag: str, body: str) -> str:
    a, b = f'<!-- {tag}:inicio -->', f'<!-- {tag}:fin -->'
    assert a in text and b in text, tag
    return text[:text.index(a) + len(a)] + '\n\n' + body + '\n\n' + text[text.index(b):]


text = DOC.read_text(encoding='utf-8')
text = put(put(text, 'matriz', md_table()), 'criticos', crit_table())
DOC.write_text(text, encoding='utf-8')

# ---------------- PDF ----------------
RED, BLUE, PURPLE, INK, MUTED, GRID = '#dc2626', '#2563eb', '#7c3aed', '#1f2430', '#5b6270', '#e3e6ea'
CSS = f'''
body {{ font-family: sans-serif; font-size: 6.2pt; color: {INK}; }}
h1 {{ font-size: 13pt; margin: 0 0 3pt 0; }}
h2 {{ font-size: 9.5pt; margin: 7pt 0 3pt 0; color: {INK}; }}
p {{ margin: 0 0 3pt 0; font-size: 7.6pt; }}
p.nota {{ font-size: 7pt; color: {MUTED}; }}
ul {{ margin: 0 0 0 12pt; padding: 0; }}
li {{ margin: 0 0 2.5pt 0; font-size: 7.4pt; }}
table {{ border-collapse: collapse; width: 100%; }}
th {{ background-color: #f1f3f6; color: #444a57; text-align: left; padding: 3pt 2pt; font-size: 6pt; border-bottom: 1pt solid #9ca3af; vertical-align: bottom; }}
td {{ padding: 2.2pt 2pt; border-bottom: 0.4pt solid {GRID}; vertical-align: top; }}
td.n {{ text-align: right; white-space: nowrap; }}
td.k {{ font-weight: bold; color: {BLUE}; }}
td.d {{ white-space: nowrap; }}
tr.c td.k, td.s {{ color: {RED}; font-weight: bold; }}
tr.g td {{ background-color: #f3effd; color: {PURPLE}; font-weight: bold; font-size: 7pt; }}
tr.t td {{ font-weight: bold; border-top: 1pt solid #9ca3af; }}
tr.o td {{ color: {MUTED}; }}
table.id td {{ border-bottom: 0; padding: 0.8pt 8pt 0.8pt 0; font-size: 7.4pt; }}
table.gl td {{ font-size: 7.2pt; padding: 2pt 4pt; }}
'''
W = [2.2, 4.0, 13.2, 10.0, 11.4, 3.6, 7.4, 4.8, 5.4, 6.1, 5.9, 6.6, 7.0, 3.4, 8.8]
HEAD = ('<tr>' + ''.join(f'<th style="width:{w}%">{t}</th>' for w, t in zip(W, [
    'N.º', 'EDT', 'Bien, servicio u obra', 'Actividades del cronograma', 'Justificación', 'Fuente', 'Modalidad y revisión', 'Tipo de contrato', 'Monto (US$)',
    'Inicio del proceso / publicación', 'Firma del contrato', 'Término / entrega requerida', 'Responsable / área requirente', 'Crítica', 'Estado'])) + '</tr>')


def wide(cls: str, text: str, amount: str) -> str:
    return f'<tr class="{cls}"><td></td><td></td><td>{escape(text)}</td>' + '<td></td>' * 5 + f'<td class="n">{amount}</td>' + '<td></td>' * 6 + '</tr>'


def two(a: str, b: str, b_note: str = '') -> str:
    return f'{a}<br><span style="color:{MUTED}">{b}</span>{b_note}'


body, group = [], None
for r in ROWS:
    if r['grupo'] != group:
        group = r['grupo']
        sub = sum(x['monto'] or 0 for x in ROWS if x['grupo'] == group)
        body.append(wide('g', group, f'{sub:,.0f}' if sub else 'sin monto'))
    ref = ref_txt(r)
    anexo = '' if r['anexo'] == 'no figura' else f'<br><span style="color:{MUTED};font-size:5.8pt">Anexo III: {r["anexo"]}</span>'
    ini = two(dm(r['inicio']), dm(r['pub'])) + anexo
    alerta = f'<br><span style="color:{RED};font-weight:bold;font-size:5.6pt">{escape(marca(r))}</span>' if marca(r) else ''
    crit = (f'<td class="s">Sí<br><span style="color:{MUTED};font-weight:normal">{r["holg"]} dl</span>{alerta}</td>' if r['crit']
            else f'<td>No<br><span style="color:{MUTED}">{r["holg"]} dl</span>{alerta}</td>')
    por_plazo = f'<br><span style="color:{RED};font-size:5.6pt">plazo<br>contractual</span>' if r['plazo'] and r['plazo'] < r['cpm'] else ''
    body.append(f'<tr class="{"c" if r["crit"] else ""}"><td>{r["num"]}</td><td class="k">{escape(r["edt"])}</td>'
                f'<td>{escape(r["adq"])}<br><span style="color:{MUTED};font-size:5.9pt">{escape(r["tipo"])}, {escape(r["cant"])}{'. ' + escape(ref[0].upper() + ref[1:]) if ref else ''}. '
                f'Paquete: {escape(r["paq_pdf"])}</span></td>'
                f'<td style="font-size:5.9pt">{"<br>".join(escape(x).replace(" a ", "&nbsp;a&nbsp;") for x in r["acts"].split("; "))}</td>'
                f'<td>{escape(r["just"])}</td><td>{"BID<br>100%" if r["fuente"].startswith("BID") else "CEPA<br>100%"}</td>'
                f'<td><b>{escape(r["mod"])}</b><br><span style="color:{MUTED};font-size:5.9pt">{escape(r["rev"])}</span></td><td>{escape(r["tcont"])}</td>'
                f'<td class="n">{"sin monto" if r["monto"] is None else format(r["monto"], ",.0f")}</td><td class="d">{ini}</td><td class="d">{dm(r["firma"])}</td>'
                f'<td class="d">{two(dm(r["termino"]), dm(r["entrega"]), por_plazo)}</td><td>{escape(r["resp"])}<br><span style="color:{MUTED}">{escape(r["req"])}</span></td>'
                f'{crit}<td>{escape(r["estado"])}</td></tr>')
CUADRE = ('<h2>Cuadre con la estimación de costos</h2><table class="gl" style="width:55%">'
          + ''.join(f'<tr><td{" style=\"font-weight:bold\"" if bold else ""}>{escape(name)}</td><td class="n"{" style=\"font-weight:bold\"" if bold else ""}>US$ {v:,.0f}</td></tr>'
                    for name, v, bold in FOOT) + '</table>')

ID = ('<table class="id"><tr><td><b>Proyecto</b></td><td>Programa de Modernización del Aeropuerto Internacional de El Salvador (ES-L1173)</td>'
      '<td><b>Organismo ejecutor</b></td><td>CEPA, mediante la UEP</td></tr>'
      '<tr><td><b>Fuente de financiamiento</b></td><td>Préstamo del BID 6073/OC-ES (100% de cada contrato del programa); los tres diseños de CEPA, fondos propios</td>'
      '<td><b>Políticas aplicables</b></td><td>GN-2349-15 (obras y bienes) y GN-2350-15 (consultores)</td></tr></table>')
P1 = f'<h1>Matriz de adquisiciones del programa ES-L1173</h1>{ID}<table>{HEAD}{"".join(body)}</table>'

NCRIT = ', '.join(f'{r["num"]} ({r["edt"]})' for r in RUTA)
AJUSTADAS = [r for r in ROWS if r['plazo'] and r['plazo'] < r['cpm']]
NMARG = '; '.join(f'fila {r["num"]}, {marca(r)}' for r in ROWS if marca(r)) or 'ninguno'
NAJ = ', '.join(f'{r["num"]} ({dm(r["entrega"])})' for r in AJUSTADAS)
P2 = CUADRE + f'''<h2>Criterios de la matriz</h2>
<ul>
<li><b>Filas.</b> Una por contrato, o por grupo de contratos homogéneo (los siete consultores clave y cada lote de la plantilla ampliada de la UEP): {len(ROWS)} filas, que suman {N_CONT} contratos del préstamo ({len(PRESTAMO)} filas) y {N_CEPA} diseños que CEPA financia fuera de él.</li>
<li><b>Base.</b> Anexo III y Anexo III.i de la Propuesta de Préstamo, avisos de 2026 (P00001, P00002, P00023 y P00024), Plan de Adquisiciones 2026-2 y cronograma por actividades. El diseño de las plataformas lo hace la Gerencia de Ingeniería de CEPA, sin adquisición.</li>
<li><b>Trazabilidad.</b> La columna Actividades del cronograma lista las actividades de cada contrato: primero las del proceso de compra y después las de su ejecución, con rangos en el orden del cronograma (por ejemplo, 1.2.1-01 a 1.2.5-06). Las columnas EDT y Paquete indican los paquetes de trabajo que entrega.</li>
<li><b>Montos.</b> Valor esperado PERT de la estimación del programa (sin reserva de contingencia): la suma del costo de las actividades de cada contrato, redondeada a miles con el resto mayor para que el total cuadre. Las supervisiones incluyen el seguimiento del PGAS y las recepciones. Los contratos de la UEP reparten los elementos U1 y U3 de la estimación en proporción a su honorario mensual y sus meses. Los US${SIN_CONTRATO:,.0f} de gastos operativos de la UEP no son un contrato. El monto del PA 2026-2 de la plantilla ampliada (US${_pa_tot:,.0f}) es mayor que su valor esperado (U3, US${_u3:,.0f} sin escalamiento) {DIF_PA} Las filas suman US${TOTAL:,.0f} y, con esos gastos, la estimación del programa (US${EST_TOTAL:,.0f}).</li>
<li><b>Fechas.</b> Inicio del proceso: primera actividad de compra. Publicación: inicio de la actividad de publicación del aviso o de la solicitud de expresiones de interés (en 3CV y auditoría, de la convocatoria o la invitación a la lista corta). Firma: fin de la actividad de firma. Término: fin de la última actividad del contratista (obras), el informe final (supervisión), la aprobación del producto (consultorías), el dictamen (auditoría) o el fin de la administración del programa (UEP).</li>
<li><b>Entrega requerida.</b> Es el mínimo entre la fecha más tardía del CPM (el término más la holgura de esa actividad, en días laborables) y el plazo contractual cuando existe: el informe de medio término, 60 días después del primero entre el 50% del tiempo de ejecución planificado y el 50% desembolsado (cláusula 5.03), y los estados financieros auditados, 120 días después del cierre de cada ejercicio y del último desembolso (cláusula 5.02). Filas ajustadas por plazo contractual: {NAJ}.</li>
<li><b>Ruta crítica.</b> Una fila es crítica si alguna actividad de su proceso de compra o de su ejecución lo es: {NCRIT}. Las filas se agrupan por tipo de contrato, que se lee mejor que una lista ordenada por holgura; las críticas se marcan en rojo y la columna Crítica indica la holgura mínima en días laborables. Cuando un contrato tiene plazo contractual, esa columna agrega en rojo el margen contractual si es menor de {MARGEN_MIN} dl (el término planificado frente al plazo): {NMARG}.</li>
<li><b>Revisión.</b> Todos los procesos son de revisión ex ante (Anexo III.i, 2.5, y Plan de Adquisiciones 2026-2). Obras: contratos FIDIC amarillo (2.4), publicados como Solicitud de Ofertas sin precalificación.</li>
<li><b>Responsables.</b> El especialista de adquisiciones conduce los procesos; el área requirente prepara los términos de referencia o las especificaciones y administra el contrato. Los consultores de la UEP los selecciona CEPA.</li>
</ul>
<h2>Modalidades</h2>
<table class="gl">
<tr><th style="width:8%">Sigla</th><th style="width:28%">Modalidad</th><th style="width:64%">Uso en este programa</th></tr>
<tr><td><b>LPI</b></td><td>Licitación pública internacional</td><td>Las cuatro obras, con revisión ex ante y contrato FIDIC amarillo. Se publican como Solicitud de Ofertas, sin precalificación.</td></tr>
<tr><td><b>SBCC</b></td><td>Selección basada en la calidad y el costo</td><td>Las cuatro supervisiones (lista corta de 5 a 8 firmas) y los productos 2.1, 2.2, 2.3 (BIM), 2.4 y 2.5. Se evalúan la propuesta técnica y el precio.</td></tr>
<tr><td><b>SCC</b></td><td>Selección basada en las calificaciones de los consultores</td><td>Productos 2.6, 2.7, 2.8 y 2.9 y las dos evaluaciones. Se elige la firma mejor calificada y se negocia su propuesta (GN-2350-15, párr. 3.8).</td></tr>
<tr><td><b>SBMC</b></td><td>Selección basada en el menor costo</td><td>Los cuatro contratos anuales de auditoría externa (GN-2350-15, párr. 3.21).</td></tr>
<tr><td><b>3CV</b></td><td>Comparación de calificaciones de al menos tres candidatos</td><td>Consultores individuales de la UEP: los puestos clave, el técnico de apoyo y la plantilla ampliada (GN-2350-15, sección V).</td></tr>
</table>
<p class="nota" style="margin-top:6pt">Fuentes: Propuesta de Préstamo ES-L1173, Anexos III y III.i; avisos P00001, P00002, P00023 y P00024; Plan de Adquisiciones 2026-2; EDT; cronograma por actividades; estimación de costos del programa; contrato de préstamo, cláusulas 5.02 y 5.03; GN-2350-15.</p>'''

mediabox = fitz.paper_rect('a4-l')
where = mediabox + (24, 26, -24, -32)


def html_doc(inner: str) -> str:
    return f'<html><head><style>{CSS}</style></head><body>{inner}</body></html>'


def fits(inner: str) -> bool:
    more, _ = fitz.Story(html=html_doc(inner)).place(where)
    return not more


def more_ok(inner: str) -> bool:
    """Cabe con holgura (el pie de página no debe tocar el texto)."""
    return not fitz.Story(html=html_doc(inner)).place(where + (0, 0, 0, -26))[0]


# Una Story por página (como el anexo del cronograma): si la tabla se parte dentro de una misma Story, PyMuPDF deja fondos fantasma.
P1_HEAD = P1[:P1.index('<table>' + HEAD)]
pages, i = [], 0
while i < len(body):
    top = P1_HEAD if not pages else ''
    k = len(body) - i
    while k > 1 and not fits(f'{top}<table>{HEAD}{"".join(body[i:i + k])}</table>'):
        k -= 1
    while k > 1 and body[i + k - 1].startswith('<tr class="g"'):  # no dejar el encabezado de un grupo solo al final de la página
        k -= 1
    pages.append(f'{top}<table>{HEAD}{"".join(body[i:i + k])}</table>')
    i += k
if more_ok(pages[-1] + P2):
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
    page.insert_text((24, mediabox.height - 18), 'ES-L1173 | Matriz de adquisiciones', fontsize=7, color=(0.4, 0.42, 0.45))
out = HERE / 'matriz_adquisiciones_ES-L1173.pdf'
pages = len(doc)
doc.save(str(out), garbage=3, deflate=True)
print(f'{out.name}: {pages} páginas, {len(ROWS)} filas, {N_CONT} contratos del préstamo + {N_CEPA} diseños de CEPA, total US${TOTAL:,.0f} + sin contrato US${SIN_CONTRATO:,.0f} = US${EST_TOTAL:,.0f} (total_E {EST["total_E"]:,.0f})')
for r in ROWS:
    print(r['num'], r['edt'], '|', r['mod'], '|', r['monto'], '|', r['inicio'], r['pub'], r['firma'], r['termino'], 'cpm', r['cpm'], 'plazo', r['plazo'], 'ent', r['entrega'], '|', r['crit'], r['holg'], '|', r['acts'])

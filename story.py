"""Sección de inicio con panel fijo: el texto avanza a la izquierda y la escena de la derecha cambia.

Las cifras y estados de las escenas son un ejemplo ilustrativo (se rotulan así en la página).
"""

STEPS = [
    ("Diagnóstico", "Vea dónde está su operación frente a la norma",
     "Revisamos procesos, registros y documentos, y le entregamos las brechas frente a la norma que necesita cumplir, con prioridades claras: qué ya cumple, qué está en curso y qué necesita atención.",
     "Solicitar diagnóstico", "contacto.html"),
    ("Plan de trabajo", "Un avance que puede seguir etapa por etapa",
     "Cada etapa termina con un entregable verificable: levantamiento, diagnóstico, documentación, capacitación y auditoría. Usted sabe en todo momento qué está listo y qué sigue.",
     "Conozca el método", "como-trabajamos.html"),
    ("Un solo sistema", "Documente una vez y úselo en varias normas",
     "Las normas ISO de sistemas de gestión comparten una estructura común. La política, la gestión de riesgos, la auditoría interna y la revisión por la dirección se construyen una vez y sirven para ISO 9001, ISO 14001, ISO/IEC 27001 e ISO/IEC 42001.",
     "Ver los servicios", "servicios.html"),
]

# (x, y, icono, etiqueta, estado) sobre un escenario de 520 x 460 px
NODES = [
    (260, 52, "med", "FEUM 7.0", "ok"),
    (96, 134, "q", "ISO 9001", "ok"),
    (424, 134, "leaf", "ISO 14001", "warn"),
    (96, 326, "ai", "ISO/IEC 42001", "bad"),
    (424, 326, "lock", "ISO/IEC 27001", "warn"),
    (260, 408, "shield", "Regulatorio", "bad"),
]
STATUS = {"ok": "Cumple", "warn": "En curso", "bad": "Requiere atención"}

STAGES = [("Levantamiento", "done", "Listo"), ("Diagnóstico", "done", "Listo"),
          ("Documentación", "doing", "En curso"), ("Capacitación", "todo", "Pendiente"),
          ("Auditoría y mejora", "todo", "Pendiente")]

MATRIX_ROWS = ["Política y objetivos", "Riesgos y oportunidades", "Auditoría interna", "Revisión por la dirección", "Acciones correctivas"]
MATRIX_COLS = ["9001", "14001", "27001", "42001"]


def scene_hub(icon):
    lines, nodes, chips = [], [], []
    for i, (x, y, ic, label, st) in enumerate(NODES):
        lines.append(f'<line x1="260" y1="230" x2="{x}" y2="{y}"/>')
        nodes.append(f'<div class="hub-node pop" style="left:{x - 46}px;top:{y - 46}px;--i:{i + 1}"><span class="hn-ico">{icon[ic]}</span><small>{label}</small></div>')
        cx, cy = 260 + (x - 260) * 0.56, 230 + (y - 230) * 0.56
        chips.append(f'<span class="chip-st {st} pop" style="left:{cx:.0f}px;top:{cy:.0f}px;--i:{i + 4}"><i></i>{STATUS[st]}</span>')
    return (f'<div class="scene s0 on" data-i="0"><div class="stage">'
            f'<svg class="hub-lines" viewBox="0 0 520 460" aria-hidden="true">{"".join(lines)}</svg>'
            f'<div class="hub-core pop" style="--i:0"><b>Su sistema<br>de gestión</b></div>{"".join(nodes)}{"".join(chips)}'
            f'</div></div>')


def scene_dash():
    rows = "".join(
        f'<li class="st {k} pop" style="--i:{i + 2}"><i></i><span>{n}</span><em>{t}</em></li>'
        for i, (n, k, t) in enumerate(STAGES))
    return ('<div class="scene s1" data-i="1"><div class="stage"><div class="dash">'
            '<div class="dash-top pop" style="--i:0"><div><small>Plan de trabajo</small><b>60<span>%</span></b><small>de las etapas completadas</small></div>'
            '<div class="ring" style="--w:60"><svg viewBox="0 0 44 44"><circle cx="22" cy="22" r="18"/><circle class="arc" cx="22" cy="22" r="18"/></svg></div></div>'
            '<div class="fill-bar pop" style="--i:1;--w:60%"><i></i></div>'
            f'<ul class="stages">{rows}</ul></div></div></div>')


def scene_matrix(check):
    head = '<span></span>' + "".join(f'<b>{c}</b>' for c in MATRIX_COLS)
    rows = []
    n = 0
    for r in MATRIX_ROWS:
        cells = []
        for _ in MATRIX_COLS:
            cells.append(f'<i class="ck pop" style="--i:{n + 1}">{check}</i>')
            n += 1
        rows.append(f'<div class="mx-row"><span>{r}</span>{"".join(cells)}</div>')
    return ('<div class="scene s2" data-i="2"><div class="stage"><div class="matrix">'
            f'<div class="mx-head pop" style="--i:0">{head}</div>{"".join(rows)}'
            '<p class="mx-foot pop" style="--i:22">Se documenta una vez y se usa en todas las normas</p></div></div></div>')


def _compose(steps, scenes):
    copies = "".join(
        f'<div class="step-copy{" on" if i == 0 else ""}" data-scene="{i}"><span class="eyebrow">{e}</span>'
        f'<h2 class="title">{h}</h2><p class="lead">{p}</p><a class="tlink" href="{href}">{label} →</a></div>'
        for i, (e, h, p, label, href) in enumerate(steps))
    dots = "".join(f'<i class="{"on" if i == 0 else ""}"></i>' for i in range(len(steps)))
    return (f'<section class="story" id="story"><div class="container"><div class="story-grid"><div class="story-steps">{copies}</div>'
            f'<div class="story-panel" data-scroll data-scroll-sticky data-scroll-target="#story"><span class="ex">Ejemplo ilustrativo</span>'
            f'{scenes}<div class="sdots">{dots}</div></div></div></div></section>')


def story_section(icon, check):
    return _compose(STEPS, scene_hub(icon) + scene_dash() + scene_matrix(check))


# ---------------- versión para páginas de servicio ----------------
CHECK_PATTERN = ["ok", "ok", "warn", "warn", "bad", "bad"]


def scene_checklist(items):
    rows = "".join(
        f'<li class="cl {CHECK_PATTERN[i % len(CHECK_PATTERN)]} pop" style="--i:{i + 1}"><i></i><span>{t}</span><em>{STATUS[CHECK_PATTERN[i % len(CHECK_PATTERN)]]}</em></li>'
        for i, t in enumerate(items))
    return ('<div class="scene s0 on" data-i="0"><div class="stage"><div class="checklist">'
            f'<div class="cl-top pop" style="--i:0"><small>Avance por componente</small><b>{len(items)} componentes</b></div>'
            f'<ul>{rows}</ul></div></div></div>')


def scene_matrix_hl(check, hl):
    """Tabla de normas con la columna de la norma de la página resaltada."""
    html = scene_matrix(check)
    parts = html.split('<i class="ck pop"')
    out = [parts[0]]
    for n, part in enumerate(parts[1:]):
        out.append(('<i class="ck pop hl"' if n % len(MATRIX_COLS) == hl else '<i class="ck pop"') + part)
    html = "".join(out)
    heads = html.split("<b>")
    return heads[0] + "".join(('<b class="hl">' if i == hl else "<b>") + h for i, h in enumerate(heads[1:]))


def service_story(x, hl, icon, check):
    tag = x["tag"]
    steps = [
        ("Qué se trabaja", f"Cada componente de {tag}, con su avance visible",
         "Dividimos el sistema en los componentes que pide la norma y los avanzamos uno a uno, para que sepa qué ya está, qué está en curso y qué necesita atención.",
         "Solicitar diagnóstico", "contacto.html"),
        ("Plan de trabajo", "Un entregable verificable en cada etapa",
         "Levantamiento, diagnóstico, documentación, capacitación y auditoría. Al cierre de cada etapa recibe un entregable que puede revisar con su equipo.",
         "Conozca el método", "como-trabajamos.html"),
        ("Un solo sistema", f"{tag} se integra con las demás normas",
         f"Como las normas ISO de sistemas de gestión comparten una estructura común, lo que construye para {tag} se reutiliza si más adelante suma otra: política, riesgos, auditoría interna y revisión por la dirección.",
         "Ver todos los servicios", "servicios.html"),
    ]
    scenes = scene_checklist(x["incluye"][:6]) + scene_dash() + scene_matrix_hl(check, hl)
    return _compose(steps, scenes)

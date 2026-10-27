"""Secciones con panel fijo: el texto avanza a la izquierda y la escena de la derecha cambia.

Cada escena lleva su propia etiqueta. Las que muestran estados o cifras de ejemplo se rotulan
"Ejemplo ilustrativo"; las que se basan en hechos citan su fuente o su tema.
"""

ILUS = "Ejemplo ilustrativo"
STATUS = {"ok": "Cumple", "warn": "En curso", "bad": "Requiere atención"}

# ---------------- inicio ----------------
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

# (x, y, icono, etiqueta, texto del chip, clase del chip) sobre un escenario de 520 x 460 px
HOME_NODES = [
    (260, 52, "med", "FEUM 7.0", STATUS["ok"], "ok"),
    (96, 134, "q", "ISO 9001", STATUS["ok"], "ok"),
    (424, 134, "leaf", "ISO 14001", STATUS["warn"], "warn"),
    (96, 326, "ai", "ISO/IEC 42001", STATUS["bad"], "bad"),
    (424, 326, "lock", "ISO/IEC 27001", STATUS["warn"], "warn"),
    (260, 408, "shield", "Regulatorio", STATUS["bad"], "bad"),
]

AUTH_NODES = [
    (260, 52, "shield", "COFEPRIS", "México", "info"),
    (96, 134, "shield", "INVIMA", "Colombia", "info"),
    (424, 134, "shield", "Salud Panamá", "Panamá", "info"),
    (96, 326, "shield", "ANVISA", "Brasil", "info"),
    (424, 326, "shield", "FDA", "Estados Unidos", "info"),
    (260, 408, "search", "Auditorías", "Previas a la inspección", "info"),
]

STAGES = [("Levantamiento", "done", "Listo"), ("Diagnóstico", "done", "Listo"),
          ("Documentación", "doing", "En curso"), ("Capacitación", "todo", "Pendiente"),
          ("Auditoría y mejora", "todo", "Pendiente")]

MATRIX_ROWS = ["Política y objetivos", "Riesgos y oportunidades", "Auditoría interna", "Revisión por la dirección", "Acciones correctivas"]
MATRIX_COLS = ["9001", "14001", "27001", "42001"]
CHECK_PATTERN = ["ok", "ok", "warn", "warn", "bad", "bad"]


def _ex(label):
    return f'<span class="ex">{label}</span>'


def scene_hub(icon, nodes=None, core="Su sistema<br>de gestión", label=ILUS):
    nodes = nodes or HOME_NODES
    lines, boxes, chips = [], [], []
    for i, (x, y, ic, name, chip, cls) in enumerate(nodes):
        lines.append(f'<line x1="260" y1="230" x2="{x}" y2="{y}"/>')
        boxes.append(f'<div class="hub-node pop" style="left:{x - 46}px;top:{y - 46}px;--i:{i + 1}"><span class="hn-ico">{icon[ic]}</span><small>{name}</small></div>')
        cx, cy = 260 + (x - 260) * 0.56, 230 + (y - 230) * 0.56
        chips.append(f'<span class="chip-st {cls} pop" style="left:{cx:.0f}px;top:{cy:.0f}px;--i:{i + 4}"><i></i>{chip}</span>')
    return (f'<div class="scene s0 on" data-i="0">{_ex(label)}<div class="stage">'
            f'<svg class="hub-lines" viewBox="0 0 520 460" aria-hidden="true">{"".join(lines)}</svg>'
            f'<div class="hub-core pop" style="--i:0"><b>{core}</b></div>{"".join(boxes)}{"".join(chips)}'
            f'</div></div>')


def scene_dash(label=ILUS):
    rows = "".join(
        f'<li class="st {k} pop" style="--i:{i + 2}"><i></i><span>{n}</span><em>{t}</em></li>'
        for i, (n, k, t) in enumerate(STAGES))
    return (f'<div class="scene s1" data-i="1">{_ex(label)}<div class="stage"><div class="dash">'
            '<div class="dash-top pop" style="--i:0"><div><small>Plan de trabajo</small><b>60<span>%</span></b><small>de las etapas completadas</small></div>'
            '<div class="ring" style="--w:60"><svg viewBox="0 0 44 44"><circle cx="22" cy="22" r="18"/><circle class="arc" cx="22" cy="22" r="18"/></svg></div></div>'
            '<div class="fill-bar pop" style="--i:1;--w:60%"><i></i></div>'
            f'<ul class="stages">{rows}</ul></div></div></div>')


def scene_matrix(check, label=ILUS, hl=None):
    head = '<span></span>' + "".join(f'<b class="{"hl" if j == hl else ""}">{c}</b>' for j, c in enumerate(MATRIX_COLS))
    rows, n = [], 0
    for r in MATRIX_ROWS:
        cells = []
        for j, _ in enumerate(MATRIX_COLS):
            cells.append(f'<i class="ck pop{" hl" if j == hl else ""}" style="--i:{n + 1}">{check}</i>')
            n += 1
        rows.append(f'<div class="mx-row"><span>{r}</span>{"".join(cells)}</div>')
    return (f'<div class="scene s2" data-i="2">{_ex(label)}<div class="stage"><div class="matrix">'
            f'<div class="mx-head pop" style="--i:0">{head}</div>{"".join(rows)}'
            '<p class="mx-foot pop" style="--i:22">Se documenta una vez y se usa en todas las normas</p></div></div></div>')


def scene_list(items, title="Avance por componente", count=None, label=ILUS, compact=False, first=False, idx=0, foot=None):
    """items: lista de (texto, clase, insignia). Clase: ok, warn, bad o info."""
    rows = "".join(
        f'<li class="cl {cls} pop" style="--i:{i + 1}"><i></i><span>{t}</span><em>{badge}</em></li>'
        for i, (t, cls, badge) in enumerate(items))
    right = f'<b>{count}</b>' if count else ""
    foot_html = f'<p class="cl-foot pop" style="--i:{len(items) + 1}">{foot}</p>' if foot else ""
    return (f'<div class="scene s{idx}{" on" if first else ""}" data-i="{idx}">{_ex(label)}<div class="stage"><div class="checklist{" compact" if compact else ""}">'
            f'<div class="cl-top pop" style="--i:0"><small>{title}</small>{right}</div><ul>{rows}</ul>{foot_html}</div></div></div>')


def scene_flow(title, nodes, label, idx=2):
    """Cadena vertical: nodes = lista de (nombre, descripción)."""
    rows = "".join(
        f'<li class="fl pop" style="--i:{i + 1}"><span class="fl-n">{i + 1}</span><div><b>{n}</b><small>{d}</small></div></li>'
        for i, (n, d) in enumerate(nodes))
    return (f'<div class="scene s{idx}" data-i="{idx}">{_ex(label)}<div class="stage"><div class="flow">'
            f'<div class="cl-top pop" style="--i:0"><small>{title}</small></div><ol>{rows}</ol></div></div></div>')


def _compose(steps, scenes):
    copies = "".join(
        f'<div class="step-copy{" on" if i == 0 else ""}" data-scene="{i}"><span class="eyebrow">{e}</span>'
        f'<h2 class="title">{h}</h2><p class="lead">{p}</p><a class="tlink" href="{href}">{label} →</a></div>'
        for i, (e, h, p, label, href) in enumerate(steps))
    dots = "".join(f'<i class="{"on" if i == 0 else ""}"></i>' for i in range(len(steps)))
    return (f'<section class="story" id="story"><div class="container"><div class="story-grid"><div class="story-steps">{copies}</div>'
            f'<div class="story-panel" data-scroll data-scroll-sticky data-scroll-target="#story">'
            f'{scenes}<div class="sdots">{dots}</div></div></div></div></section>')


def story_section(icon, check):
    return _compose(STEPS, scene_hub(icon) + scene_dash() + scene_matrix(check))


# ---------------- páginas de servicio ----------------
def _components(x, idx=0):
    items = [(t, CHECK_PATTERN[i % len(CHECK_PATTERN)], STATUS[CHECK_PATTERN[i % len(CHECK_PATTERN)]]) for i, t in enumerate(x["incluye"][:6])]
    return scene_list(items, "Avance por componente", f"{len(items)} componentes", ILUS, first=True, idx=idx)


def _step1(tag, kind="la norma"):
    return ("Qué se trabaja", f"Cada componente de {tag}, con su avance visible",
            f"Dividimos el servicio en los componentes que {kind} y los avanzamos uno a uno, para que sepa qué ya está, qué está en curso y qué necesita atención.",
            "Solicitar diagnóstico", "contacto.html")


STEP2 = ("Plan de trabajo", "Un entregable verificable en cada etapa",
         "Levantamiento, diagnóstico, documentación, capacitación y auditoría. Al cierre de cada etapa recibe un entregable que puede revisar con su equipo.",
         "Conozca el método", "como-trabajamos.html")

FEUM_CHAPTERS = [
    "I. Boticas, droguerías y farmacias", "II. Almacenes de depósito y distribución", "III. Procedimientos normalizados de operación",
    "IV. Control de existencias", "V. Manejo y almacenamiento", "VI. Receta médica",
    "VII. Medicamentos estupefacientes y psicotrópicos", "VIII. Control de antimicrobianos", "XIII. Gestión de residuos",
]

BPAD_CHAIN = [("Proveedor", "Evaluado y con contrato de servicio"), ("Recepción", "Producto y documentos verificados"),
              ("Almacén", "Temperatura y humedad registradas, con termohigrómetros calibrados"),
              ("Transporte", "Procedimiento y control durante el traslado"), ("Cliente", "Entrega con trazabilidad y evidencia para auditorías")]

VAL_CHAIN = [("Requerimientos del usuario (URS)", "Qué debe hacer el sistema"), ("Evaluación de riesgos", "Qué puede afectar la calidad y los datos"),
             ("Calificación de instalación (IQ)", "Instalado como se especificó"), ("Calificación de operación (OQ)", "Funciona según lo previsto"),
             ("Calificación de desempeño (PQ)", "Funciona de forma consistente en el uso real"), ("Informe y trazabilidad", "Cada requisito ligado a su prueba y su evidencia")]


def service_story(x, hl, icon, check):
    """hl: índice de la columna ISO a resaltar; None para los servicios del grupo farmacéutico."""
    tag, slug = x["tag"], x["slug"]
    if hl is not None:
        steps = [_step1(tag, "pide la norma"), STEP2,
                 ("Un solo sistema", f"{tag} se integra con las demás normas",
                  f"Como las normas ISO de sistemas de gestión comparten una estructura común, lo que construye para {tag} se reutiliza si más adelante suma otra: política, riesgos, auditoría interna y revisión por la dirección.",
                  "Ver todos los servicios", "servicios.html")]
        scenes = _components(x) + scene_dash() + scene_matrix(check, ILUS, hl)
        return _compose(steps, scenes)

    if slug == "bpad":
        third = ("Cadena completa", "Controles y registros desde el proveedor hasta el cliente",
                 "Documentamos y operamos los controles de cada punto de la cadena: evaluación de proveedores, recepción, almacenamiento con temperatura y humedad, calibración de termohigrómetros y transporte, para que pueda demostrarlo en una auditoría.",
                 "Ver cumplimiento regulatorio", "servicios/cumplimiento-regulatorio.html")
        scene3 = scene_flow("Cadena de almacenamiento y distribución", BPAD_CHAIN, "Puntos de control")
    elif slug == "farmacopea-feum":
        third = ("Edición 7.0", "Sepa qué capítulos cambiaron y cómo le afectan",
                 "La edición 7.0 reorganiza y actualiza capítulos de la sexta edición, desde los requisitos de operación de farmacias y almacenes hasta el control de antimicrobianos y la gestión de residuos. El diagnóstico identifica cuáles le corresponden.",
                 "Solicitar diagnóstico", "contacto.html")
        scene3 = scene_list([(c, "info", "Modificado") for c in FEUM_CHAPTERS], "Capítulos modificados en la 7.0", None,
                            "Fuente: FEUM, Suplemento 7.0", compact=True, idx=2,
                            foot="Cambios respecto a la sexta edición del Suplemento")
    elif slug == "cumplimiento-regulatorio":
        third = ("Un sistema, varias autoridades", "Un sistema de calidad que responde a cada autoridad",
                 "Montamos el sistema de gestión de calidad, los procedimientos y los registros que esperan COFEPRIS, INVIMA, el Ministerio de Salud de Panamá, ANVISA y la FDA, y lo comprobamos con auditorías internas antes de la inspección.",
                 "Ver validación de software", "servicios/validacion-software.html")
        scene3 = scene_hub(icon, AUTH_NODES, "Su sistema<br>de calidad", "Autoridades con las que trabajamos").replace('class="scene s0 on" data-i="0"', 'class="scene s2" data-i="2"')
    else:  # validacion-software
        third = ("Etapas de la validación", "De los requerimientos al informe, con trazabilidad",
                 "Definimos qué debe hacer el sistema, evaluamos sus riesgos y lo calificamos en instalación, operación y desempeño. Cada requisito queda ligado a una prueba y a su evidencia.",
                 "Ver cumplimiento regulatorio", "servicios/cumplimiento-regulatorio.html")
        scene3 = scene_flow("Validación de un sistema computarizado", VAL_CHAIN, "Etapas habituales (GAMP 5)")

    steps = [_step1(tag, "pide el servicio"), STEP2, third]
    return _compose(steps, _components(x) + scene_dash() + scene3)

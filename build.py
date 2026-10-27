"""Genera las páginas estáticas de AC Soluciones. Uso: py build.py"""
import json
import os
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "dist"  # salida publicable; Vercel sirve esta carpeta
sys.path.insert(0, str(ROOT))
LOCO = "https://cdn.jsdelivr.net/npm/locomotive-scroll@4.1.3/dist/locomotive-scroll.min"


def finish(html):
    """En Vercel no se sube assets/vendor: Locomotive se carga desde CDN."""
    if os.environ.get("VERCEL"):
        html = re.sub(r"(?:\.\./)?assets/vendor/locomotive-scroll\.min", LOCO, html)
    return html


shutil.rmtree(OUT, ignore_errors=True)
shutil.copytree(ROOT / "assets", OUT / "assets")
from services_content import SVC  # noqa: E402
from blog_content import ARTICLES, CATS  # noqa: E402

SITE = "https://acsgi.com.mx"
TODAY = "2026-10-27"
SLUGS = [s["slug"] for s in SVC]
PAGES = [("index.html", "Inicio"), ("servicios.html", "Servicios"),
         ("como-trabajamos.html", "Cómo trabajamos"), ("blog.html", "Blog"), ("nosotros.html", "Nosotros")]
PHONES = ["+52 55 3245 3954", "+52 55 3007 7521", "+52 55 7379 7376", "+57 300 760 2388"]

ICON = {
 "q": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="9"/></svg>',
 "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 019.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.9-5.4 5-6"/></svg>',
 "box": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 8l-9-5-9 5v8l9 5 9-5z"/><path d="M3 8l9 5 9-5M12 13v8"/></svg>',
 "cap": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10L12 5 2 10l10 5z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/></svg>',
 "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>',
 "ai": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="5" width="14" height="14" rx="3"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/><path d="M9 14l1.5-4 1.5 4M9.6 13h2.8M15 10v4"/></svg>',
 "lock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 018 0v3"/></svg>',
 "db": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3.1 19.5 19.5 0 01-6-6A19.8 19.8 0 012.1 4.2 2 2 0 014.1 2h3a2 2 0 012 1.7c.1 1 .4 1.9.7 2.8a2 2 0 01-.5 2.1L8.1 9.9a16 16 0 006 6l1.3-1.3a2 2 0 012.1-.4c.9.3 1.8.6 2.8.7a2 2 0 011.7 2z"/></svg>',
}

SERVICES = [
 ("q", "ISO 9001", "Gestión de la calidad", "Implementación de todos los numerales de la norma: contexto, liderazgo, riesgos, procesos, indicadores, auditoría interna y revisión por la dirección.", ["Diagnóstico", "Documentación", "Acompañamiento a certificación"]),
 ("leaf", "ISO 14001", "Gestión ambiental", "Identificación de aspectos e impactos ambientales, requisitos legales aplicables, objetivos ambientales y control operacional de residuos y emisiones.", ["Matriz de aspectos", "Cumplimiento legal", "Integración con ISO 9001"]),
 ("box", "BPAD", "Buenas Prácticas de Almacenamiento y Distribución", "Cumplimiento de la NOM-059-SSA1-2015 en lo aplicable: procedimientos de transporte, control de temperatura y humedad, calibración de termohigrómetros, contratos de servicio y evaluación de proveedores.", ["Procedimientos", "Auditorías de clientes", "Cadena seca"]),
 ("cap", "Formación", "Capacitación", "Cursos de interpretación de normas, formación de auditores internos, BPD, BPAD, seguridad de la información, uso responsable de la IA y capacitación en los procedimientos de su empresa, presenciales o en línea.", ["Constancias DC-3", "Grupos a la medida"]),
 ("search", "Consultoría", "Asesoría y consultoría", "Diagnósticos de brechas, auditorías internas y de segunda parte, evaluaciones de riesgos de ciberseguridad y de IA, preparación para auditorías de clientes y de la autoridad, y atención de hallazgos.", ["Auditorías", "Planes de acción", "Seguimiento"]),
 ("ai", "ISO/IEC 42001", "Inteligencia artificial", "Sistema de gestión para el uso responsable de la inteligencia artificial: inventario de usos de IA, evaluación de riesgos e impactos, controles, supervisión humana y políticas para el personal.", ["Política de IA", "Evaluación de impacto", "Controles"]),
 ("lock", "ISO/IEC 27001", "Ciberseguridad", "Sistema de gestión de seguridad de la información: análisis de riesgos, declaración de aplicabilidad, controles de acceso, respaldo, continuidad y respuesta a incidentes.", ["Análisis de riesgos", "Controles", "Auditoría interna"]),
 ("db", "ISO/IEC 38505 · 27701", "Gobernanza de datos", "Políticas y roles para la calidad, integridad, privacidad y uso de los datos de la empresa, incluida la integridad de registros en entornos regulados.", ["Políticas", "Responsables de datos", "Privacidad"]),
]
STEPS = [
 ("Levantamiento", "Entrevistas con los encargados de cada proceso, en sitio o por videollamada."),
 ("Diagnóstico", "Brechas frente a la norma y plan de trabajo con fechas."),
 ("Documentación", "Procedimientos, formatos e indicadores hechos con su personal."),
 ("Capacitación", "Cada procedimiento se enseña a quien lo aplica, con constancia."),
 ("Auditoría y mejora", "Auditoría interna, revisión por la dirección y, si lo decide, certificación."),
]
VALUES = [
 ("Integridad", "Decimos lo que encontramos, aunque no sea lo que se espera escuchar."),
 ("Rigor técnico", "Cada recomendación se sustenta en la norma y en evidencia."),
 ("Mejora continua", "Aplicamos en nuestro trabajo lo que enseñamos a nuestros clientes."),
 ("Cercanía", "Trabajamos junto a su personal, no solo con la dirección."),
 ("Confidencialidad", "La información y los datos de cada cliente se resguardan con estricta reserva."),
]


def _logo_svg():
    import math
    def arc(a0, a1, color, r=38):
        p = lambda a: (50 + r * math.cos(math.radians(a)), 50 - r * math.sin(math.radians(a)))
        (x0, y0), (x1, y1) = p(a0), p(a1)
        large = 1 if abs(a1 - a0) > 180 else 0
        sweep = 1 if a1 < a0 else 0  # sentido horario en pantalla
        return f'<path d="M{x0:.2f} {y0:.2f}A{r} {r} 0 {large} {sweep} {x1:.2f} {y1:.2f}" fill="none" stroke="{color}" stroke-width="7.5"/>'
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
            + arc(196, 96, "#d89b2b") + arc(82, -8, "#1e2d55") + arc(-142, -38, "#1a7f6b")
            + '<text x="50" y="50" text-anchor="middle" dominant-baseline="central" font-family="Sora,Inter,Arial,sans-serif" font-weight="800" font-size="30" letter-spacing="-1.5" fill="#1e2d55">AC</text></svg>')


LOGO = _logo_svg()
(OUT / "assets" / "logo.svg").write_text(LOGO, encoding="utf-8")


ORG = {"@context": "https://schema.org", "@type": "ProfessionalService", "name": "AC Soluciones", "alternateName": "AC Soluciones Sistemas de Gestión Integral",
       "url": SITE + "/", "logo": SITE + "/assets/logo.svg", "telephone": PHONES, "email": "contacto@acsgi.com.mx",
       "description": "Diseñamos, implementamos y auditamos sistemas de calidad, ambiente, buenas prácticas, ciberseguridad e inteligencia artificial.",
       "areaServed": ["México", "Latinoamérica"],
       "knowsAbout": ["ISO 9001", "ISO 14001", "ISO/IEC 27001", "ISO/IEC 42001", "NOM-059-SSA1-2015", "ISO/IEC 27701", "ISO/IEC 38505"]}


def head(title, desc, path=None, schema=None, og="website", css=""):
    seo = ""
    if path is not None:
        url = f"{SITE}/{path}"
        seo = (f'<link rel="canonical" href="{url}"><meta property="og:type" content="{og}"><meta property="og:locale" content="es_MX">'
               f'<meta property="og:site_name" content="AC Soluciones"><meta property="og:title" content="{title}">'
               f'<meta property="og:description" content="{desc}"><meta property="og:url" content="{url}">'
               '<meta name="twitter:card" content="summary"><meta name="theme-color" content="#0a1628">')
    for sc in (schema or []):
        seo += '<script type="application/ld+json">' + json.dumps(sc, ensure_ascii=False, separators=(",", ":")) + "</script>"
    return f'''<!doctype html>
<html lang="es"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">{seo}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Sora:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/vendor/locomotive-scroll.min.css"><link rel="stylesheet" href="assets/styles.css">{css}
</head><body>
<div id="veil"><div class="ring"></div></div><div id="progress"></div>'''


def navbar(active):
    links = "".join(f'<li><a class="link{" active" if h == active else ""}" href="{h}">{n}</a></li>' for h, n in PAGES)
    return f'''<header class="nav"><div class="container">
<a class="logo" href="index.html"><span class="logo-mark"><img src="assets/logo.svg" alt="AC"></span><span>AC Soluciones<small>Sistemas de gestión integral</small></span></a>
<nav><ul>{links}<li><a class="btn btn-primary" href="contacto.html">Solicitar diagnóstico <span class="arr">→</span></a></li></ul></nav>
<button class="burger" aria-label="Menú"><span></span><span></span><span></span></button></div></header>
<div data-scroll-container>'''


def cta():
    return '''<section style="padding-top:0"><div class="container"><div class="cta-strip reveal zoom">
<div><h3>¿No sabe por dónde empezar?</h3><p>Agende un diagnóstico inicial. Revisamos su operación y le entregamos las brechas frente a la norma que necesita cumplir.</p></div>
<a class="btn btn-dark" href="contacto.html">Solicitar diagnóstico <span class="arr">→</span></a></div></div></section>'''


def footer():
    nav = "".join(f'<a href="{h}">{n}</a>' for h, n in PAGES)
    ph = "".join(f'<a href="tel:{p.replace(" ", "")}">{p}</a>' for p in PHONES)
    svc_links = "".join(f'<a href="servicios/{x["slug"]}.html">{x["tag"] if x["slug"] in ("iso-9001", "iso-14001", "iso-27001", "iso-42001", "bpad") else x["name"]}</a>' for x in SVC)
    return f'''<footer><div class="container"><div class="foot">
<div><a class="logo" href="index.html"><span class="logo-mark"><img src="assets/logo.svg" alt="AC"></span><span>AC Soluciones</span></a>
<p style="margin-top:18px;max-width:300px">Sistemas de gestión que funcionan en la operación, no solo en el papel.</p></div>
<div><h5>Sitio</h5>{nav}<a href="contacto.html">Contacto</a></div>
<div><h5>Servicios</h5>{svc_links}</div>
<div><h5>Contacto</h5>{ph}<a href="mailto:contacto@acsgi.com.mx">contacto@acsgi.com.mx</a></div>
</div><div class="foot-bottom"><span>AC Soluciones · Sistemas de Gestión Integral · Atención en México y Latinoamérica</span><span>Mejora continua en cada proceso.</span></div></div></footer></div>
<a class="wa" href="https://wa.me/525532453954" aria-label="WhatsApp"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 00-8.6 15L2 22l5.1-1.3A10 10 0 1012 2zm5.2 13.9c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7a11.3 11.3 0 01-4.6-4c-.4-.5-1.2-1.6-1.2-3s.8-2 1-2.3c.3-.3.6-.3.8-.3h.5c.2 0 .4 0 .6.5l.8 1.9c.1.2.1.4 0 .5l-.4.6-.3.4c-.1.2-.3.3-.1.6a7 7 0 002.1 2.6c.8.7 1.5.9 1.7 1 .3.1.4.1.6-.1l.8-1c.2-.3.4-.2.6-.1l1.8.9c.3.1.5.2.5.3.1.2.1.8-.1 1.5z"/></svg></a>
<script src="assets/vendor/locomotive-scroll.min.js"></script><script src="assets/main.js"></script></body></html>'''


def card(i, s, delay=True):
    ic, tag, title, text, deliv = s
    d = f" d{(i % 3) + 1}" if delay else ""
    chips = "".join(f"<em>{x}</em>" for x in deliv)
    return (f'<article class="card reveal{d}"><div class="ico">{ICON[ic]}</div><span class="tag">{tag}</span><h3>{title}</h3><p>{text}</p>'
            f'<div class="deliv">{chips}</div><a class="more" href="servicios/{SLUGS[i]}.html">Ver detalle <span>→</span></a></article>')


def steps():
    items = "".join(f'<div class="step reveal d{i+1}"><div class="num">{i+1}</div><div><h4>{t}</h4><p>{p}</p></div></div>' for i, (t, p) in enumerate(STEPS))
    return f'<div class="steps"><div class="fill"></div>{items}</div>'


def page_hero(eyebrow, h1, p):
    return f'''<section class="page-hero"><canvas data-net></canvas><div class="container">
<span class="eyebrow">{eyebrow}</span><h1 data-split data-scroll data-scroll-speed="2">{h1}</h1><p class="reveal in">{p}</p></div></section>'''


# ---------------- index ----------------
cycle = '''<div data-scroll data-scroll-speed="-2"><div class="cycle reveal zoom"><svg viewBox="0 0 400 400">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#14b8a6"/><stop offset="1" stop-color="#6366f1"/></linearGradient></defs>
<g class="ring-b"><circle cx="200" cy="200" r="185" fill="none" stroke="rgba(255,255,255,.12)" stroke-dasharray="3 12" stroke-width="2"/></g>
<g class="ring-a"><circle cx="200" cy="200" r="140" fill="none" stroke="url(#g)" stroke-width="6" stroke-dasharray="190 60" stroke-linecap="round"/>
<circle cx="200" cy="60" r="9" fill="#22d3ee"/><circle cx="340" cy="200" r="9" fill="#14b8a6"/><circle cx="200" cy="340" r="9" fill="#a3e635"/><circle cx="60" cy="200" r="9" fill="#6366f1"/></g>
<circle cx="200" cy="200" r="92" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.15)"/></svg>
<div class="cycle-center"><div><b>Mejora<br>continua</b><span>PHVA</span></div></div>
<span class="cyc-label p">Planear</span><span class="cyc-label h">Hacer</span><span class="cyc-label v">Verificar</span><span class="cyc-label a">Actuar</span></div></div>'''

norms = ["ISO 9001", "ISO 14001", "BPAD", "ISO/IEC 27001", "ISO/IEC 42001", "NOM-059-SSA1-2015", "ISO/IEC 27701", "ISO/IEC 38505"]
mq = "".join(f"<span>{n}</span>" for n in norms) * 2

index = head("AC Soluciones · Sistemas de Gestión Integral", "Diseñamos, implementamos y auditamos sistemas de calidad, ambiente, buenas prácticas, ciberseguridad e inteligencia artificial.", "", [ORG]) + navbar("index.html") + f'''
<section class="hero"><canvas data-net></canvas><div class="container"><div>
<div class="chips" data-scroll data-scroll-speed="1"><span class="chip">ISO 9001</span><span class="chip">ISO 14001</span><span class="chip">BPAD</span><span class="chip">ISO/IEC 27001</span><span class="chip">ISO/IEC 42001</span></div>
<h1 data-split>Sistemas de gestión que funcionan en la <span class="grad-text">operación,</span> no solo en el papel.</h1>
<p class="sub reveal in d3">Diseñamos, implementamos y auditamos sistemas de calidad, ambiente, buenas prácticas, ciberseguridad e inteligencia artificial, para empresas que necesitan cumplir la normativa, proteger su información y crecer con orden.</p>
<div class="cta reveal in d4"><a class="btn btn-primary" href="contacto.html">Solicitar diagnóstico <span class="arr">→</span></a><a class="btn btn-ghost" href="servicios.html">Ver servicios</a></div>
</div>{cycle}</div></section>
<div class="marquee"><div class="marquee-track">{mq}</div></div>
<section class="stats"><div class="container"><div class="stat-grid">
<div class="stat reveal d1"><b data-count="16" data-pre="+">0</b><span>años de experiencia</span></div>
<div class="stat reveal d2"><b data-count="8">0</b><span>líneas de servicio</span></div>
<div class="stat reveal d3"><b data-count="5">0</b><span>etapas con entregable</span></div>
<div class="stat reveal d4"><b data-count="1" data-suf=" día">0</b><span>hábil de respuesta</span></div></div></div></section>
<section><div class="container"><div class="band reveal zoom"><div class="big" data-scroll data-scroll-speed="2">+16<small>años de experiencia</small></div>
<div><h3>Personal calificado que conoce su operación desde dentro</h3><p>Especialistas en sistemas de gestión, auditoría y capacitación que han acompañado a empresas de industrias reguladas en cada etapa, del diagnóstico a la mejora continua.</p></div></div></div></section>
<section style="padding-top:20px"><div class="ghost" data-scroll data-scroll-speed="-4" aria-hidden="true">ISO</div><div class="container"><span class="eyebrow reveal">Servicios</span>
<h2 class="title reveal d1">Un solo equipo para calidad, ambiente, buenas prácticas y tecnología</h2>
<p class="lead reveal d2">Integramos las normas en un sistema que su personal entiende y usa todos los días, con o sin certificación.</p>
<div class="grid-3">{"".join(card(i, s) for i, s in enumerate(SERVICES[:6]))}</div>
<div style="text-align:center;margin-top:50px" class="reveal"><a class="btn btn-dark" href="servicios.html">Ver los 8 servicios <span class="arr">→</span></a></div></div></section>
<section style="background:#fff;overflow:hidden"><div class="ghost r" data-scroll data-scroll-speed="3" aria-hidden="true">PHVA</div><div class="container"><span class="eyebrow reveal">Cómo trabajamos</span>
<h2 class="title reveal d1">Cinco etapas, un entregable verificable en cada una</h2>{steps()}</div></section>
{cta()}''' + footer()

# ---------------- servicios ----------------
servicios = head("Servicios de sistemas de gestión ISO | AC Soluciones", "ISO 9001, ISO 14001, BPAD, ISO/IEC 27001, ISO/IEC 42001, capacitación, consultoría y gobernanza de datos.", "servicios.html") + navbar("servicios.html") + \
    page_hero("Servicios", "Un solo equipo para calidad, ambiente, buenas prácticas y tecnología", "Integramos las normas en un sistema que su personal entiende y usa todos los días, con o sin certificación.") + \
    f'<section><div class="container"><div class="grid-3" style="margin-top:0">{"".join(card(i, s) for i, s in enumerate(SERVICES))}</div></div></section>' + cta() + footer()

# ---------------- como trabajamos ----------------
como = head("Cómo trabajamos · AC Soluciones", "Cinco etapas con un entregable verificable en cada una: levantamiento, diagnóstico, documentación, capacitación y auditoría.", "como-trabajamos.html") + navbar("como-trabajamos.html") + \
    page_hero("Cómo trabajamos", "Cinco etapas, un entregable verificable en cada una", "De la entrevista inicial a la auditoría interna, cada paso deja evidencia concreta que su equipo puede usar.") + \
    f'<section><div class="container">{steps()}</div></section>' + cta() + footer()

# ---------------- nosotros ----------------
vals = "".join(f'<div class="value reveal d{i+1}"><h4>{t}</h4><p>{p}</p></div>' for i, (t, p) in enumerate(VALUES))
nosotros = head("Nosotros · AC Soluciones", "Misión, visión y valores de AC Soluciones, consultoría en sistemas de gestión para México y Latinoamérica.", "nosotros.html") + navbar("nosotros.html") + \
    page_hero("Nosotros", "Mejora continua en cada proceso", "Aplicamos en nuestro trabajo lo que enseñamos a nuestros clientes.") + f'''
<section><div class="container"><div class="mv">
<div class="card reveal left"><span class="tag">Misión</span><h3>Sistemas prácticos y medibles</h3><p>Ayudar a las empresas a implementar sistemas de gestión prácticos y medibles, que ordenen su operación, cumplan la normativa aplicable, protejan su información, usen la tecnología de forma responsable y generen mejora continua, con un acompañamiento cercano y técnicamente riguroso.</p></div>
<div class="card reveal right"><span class="tag">Visión</span><h3>La consultoría de confianza</h3><p>Ser la consultoría de confianza en México y Latinoamérica para las empresas que buscan cumplir con calidad, cuidado ambiental, buenas prácticas, ciberseguridad y uso responsable de la inteligencia artificial, reconocida por sistemas que su personal usa todos los días.</p></div></div>
<span class="eyebrow reveal" style="margin-top:80px">Valores</span><h2 class="title reveal d1">Lo que nos guía</h2><div class="values">{vals}</div></div></section>''' + cta() + footer()

# ---------------- contacto ----------------
opts = "".join(f"<option>{s[1]} · {s[2]}</option>" for s in SERVICES)
ph = "".join(f'<a class="phone reveal d{i+1}" href="tel:{p.replace(" ", "")}">{ICON["phone"]}<span>{p}<small>{"Colombia" if p.startswith("+57") else "México"}</small></span></a>' for i, p in enumerate(PHONES))
contacto = head("Contacto · AC Soluciones", "Agende su diagnóstico inicial. Respondemos en un día hábil. Atención en México y Latinoamérica.", "contacto.html") + navbar("contacto.html") + \
    page_hero("Contacto", "Agende su <span class='grad-text'>diagnóstico inicial</span>", "Cuéntenos qué norma necesita cumplir y le respondemos en un día hábil. Atendemos empresas en México y Latinoamérica, en sitio o en línea.") + f'''
<section><div class="container contact-wrap"><div><span class="eyebrow reveal">Hablemos</span><h2 class="title reveal d1" style="font-size:2.2rem">Llámenos o escríbanos</h2>
<div class="phones">{ph}</div><div class="mailbox reveal">✉ contacto@acsgi.com.mx</div></div>
<form class="f reveal right" id="contactForm">
<div class="row2"><div class="field"><input name="nombre" placeholder=" " required><label>Nombre</label></div><div class="field"><input name="empresa" placeholder=" " required><label>Empresa</label></div></div>
<div class="field"><input type="email" name="correo" placeholder=" " required><label>Correo</label></div>
<div class="field"><select name="servicio">{opts}</select><label>Servicio de interés</label></div>
<div class="field"><textarea name="mensaje" placeholder=" " required></textarea><label>Mensaje</label></div>
<button class="btn btn-primary" type="submit">Enviar solicitud <span class="arr">→</span></button><div class="f-status"></div></form></div></section>''' + footer()

# ---------------- páginas de servicio ----------------
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5 9-10"/></svg>'


def esc(t):
    return t.replace("&", "&amp;").replace('"', "&quot;")


def service_page(x):
    by = {y["slug"]: y for y in SVC}
    url = f'{SITE}/servicios/{x["slug"]}.html'
    label = x["tag"] + " · " + x["name"]
    schema = [
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Servicios", "item": SITE + "/servicios.html"},
            {"@type": "ListItem", "position": 3, "name": label, "item": url}]},
        {"@context": "https://schema.org", "@type": "Service", "name": x["h1"], "serviceType": label, "description": x["desc"], "url": url,
         "provider": {"@type": "ProfessionalService", "name": "AC Soluciones", "url": SITE + "/"}, "areaServed": ["México", "Latinoamérica"]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in x["faqs"]]},
    ]
    hero = f'''<section class="page-hero"><canvas data-net></canvas><div class="container">
<nav class="crumbs" aria-label="Ruta"><a href="index.html">Inicio</a><span>/</span><a href="servicios.html">Servicios</a><span>/</span><span aria-current="page">{x["tag"]}</span></nav>
<span class="eyebrow">{label}</span><h1 data-split data-scroll data-scroll-speed="2">{x["h1"]}</h1><p class="reveal in">{x["intro"]}</p>
<div class="reveal in d3" style="display:flex;gap:16px;margin-top:34px;flex-wrap:wrap"><a class="btn btn-primary" href="contacto.html">Solicitar diagnóstico <span class="arr">→</span></a><a class="btn btn-ghost" href="servicios.html">Ver todos los servicios</a></div></div></section>'''
    que = "".join(f"<p>{t}</p>" for t in x["que_es"])
    para = "".join(f"<li>{CHECK}<span>{t}</span></li>" for t in x["para"])
    inc = "".join(f'<li class="reveal d{(i % 3) + 1}">{CHECK}<span>{t}</span></li>' for i, t in enumerate(x["incluye"]))
    faq = "".join(f'<details class="faq reveal"><summary>{q}</summary><div class="ans"><p>{a}</p></div></details>' for q, a in x["faqs"])
    rel = "".join(f'<a class="rel reveal d{i+1}" href="servicios/{y}.html"><span class="ico">{ICON[by[y]["icon"]]}</span><span class="tag">{by[y]["tag"]}</span><b>{by[y]["name"]}</b><span class="go">Ver servicio →</span></a>' for i, y in enumerate(x["related"]))
    body = f'''
<section><div class="container two"><div><span class="eyebrow reveal">Qué es</span><h2 class="title reveal d1">¿Qué es {x["tag"]} y por qué importa?</h2><div class="prose reveal d2">{que}</div></div>
<aside class="card reveal right"><span class="tag">¿Para quién es?</span><ul class="checks">{para}</ul></aside></div></section>
<section style="background:#fff"><div class="container"><span class="eyebrow reveal">Qué incluye</span><h2 class="title reveal d1">Lo que incluye el servicio de {x["name"].lower() if x["slug"] != "bpad" else "BPAD"}</h2>
<ul class="checks grid2">{inc}</ul></div></section>
<section><div class="container"><span class="eyebrow reveal">Cómo trabajamos</span><h2 class="title reveal d1">Cinco etapas, un entregable verificable en cada una</h2>{steps()}
<p class="lead reveal" style="margin-top:34px">Con o sin certificación: usted decide hasta dónde llevar el sistema. <a class="tlink" href="como-trabajamos.html">Conozca el método completo</a>.</p></div></section>
<section style="background:#fff"><div class="container narrow"><span class="eyebrow reveal">Preguntas frecuentes</span><h2 class="title reveal d1">Preguntas frecuentes sobre {x["tag"]}</h2><div class="faqs">{faq}</div></div></section>
<section><div class="container"><span class="eyebrow reveal">Servicios relacionados</span><h2 class="title reveal d1">También le puede interesar</h2><div class="grid-3 rels">{rel}</div></div></section>'''
    html = head(x["title"], esc(x["desc"]), f'servicios/{x["slug"]}.html', schema) + navbar("servicios.html") + hero + body + cta() + footer()
    # estas páginas viven en /servicios/: las rutas hacia la raíz llevan "../"
    return re.sub(r'(href|src)="(?!https?:|tel:|mailto:|#|\.\./|servicios/)', r'\1="../', html).replace('href="servicios/', 'href="../servicios/')


(OUT / "servicios").mkdir(parents=True, exist_ok=True)
for x in SVC:
    (OUT / "servicios" / f'{x["slug"]}.html').write_text(finish(service_page(x)), encoding="utf-8")

# ---------------- blog ----------------
BLOG_CSS = '<link rel="stylesheet" href="assets/blog.css">'
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def fecha(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} de {MESES[int(m) - 1]} de {y}"


def slugify(t):
    t = t.lower()
    for a, b in zip("áéíóúüñ", "aeiouun"):
        t = t.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def minutos(a):
    words = len(" ".join([a["lead"]] + [b if isinstance(b, str) else " ".join(b) for _, b in a["body"]]).split())
    return max(1, round(words / 200))


def up(html):
    """Páginas dentro de una subcarpeta: las rutas internas suben un nivel."""
    return re.sub(r'(href|src)="(?!https?:|tel:|mailto:|#|\.\./)', r'\1="../', html)


def post_card(a, i):
    return (f'<article class="card post reveal d{(i % 3) + 1}" data-cat="{a["cat"]}"><span class="tag">{a["cat"]}</span>'
            f'<h3>{a["h1"]}</h3><p>{a["desc"]}</p><div class="meta"><span>{fecha(a["date"])}</span><span>{minutos(a)} min de lectura</span></div>'
            f'<a class="more" href="blog/{a["slug"]}.html">Leer artículo <span>→</span></a></article>')


def blog_index():
    chips = '<button class="fchip on" data-filter="all">Todos</button>' + "".join(f'<button class="fchip" data-filter="{c}">{c}</button>' for c in CATS)
    cards = "".join(post_card(a, i) for i, a in enumerate(ARTICLES))
    schema = [{"@context": "https://schema.org", "@type": "Blog", "name": "Blog de AC Soluciones", "url": SITE + "/blog.html",
               "publisher": {"@type": "ProfessionalService", "name": "AC Soluciones", "url": SITE + "/"},
               "blogPost": [{"@type": "BlogPosting", "headline": a["h1"], "url": f'{SITE}/blog/{a["slug"]}.html', "datePublished": a["date"]} for a in ARTICLES]}]
    script = """<script>
document.querySelectorAll('.fchip').forEach(function(b){b.addEventListener('click',function(){
  document.querySelectorAll('.fchip').forEach(function(x){x.classList.toggle('on',x===b)});
  var f=b.dataset.filter;
  document.querySelectorAll('.post').forEach(function(c){c.classList.toggle('off',f!=='all'&&c.dataset.cat!==f)});
});});
</script>"""
    return (head("Blog de sistemas de gestión | AC Soluciones", "Guías prácticas sobre ISO 9001, ISO 14001, BPAD, seguridad de la información, inteligencia artificial y auditorías, escritas por el equipo de AC Soluciones.",
                 "blog.html", schema, css=BLOG_CSS) + navbar("blog.html")
            + page_hero("Blog", "Guías prácticas para que sus normas funcionen en la operación", "Respondemos las preguntas que más se hacen las empresas al implementar, auditar y mantener sus sistemas de gestión.")
            + f'<section><div class="container"><div class="fbar reveal">{chips}</div><div class="grid-3 posts" style="margin-top:34px">{cards}</div></div></section>'
            + cta() + footer().replace("</body>", script + "</body>"))


def blog_post(a):
    by = {s["slug"]: s for s in SVC}
    svc = by[a["service"]]
    url = f'{SITE}/blog/{a["slug"]}.html'
    h2s = [t for k, t in a["body"] if k == "h2"]
    toc = "".join(f'<li><a href="#{slugify(t)}">{t}</a></li>' for t in h2s)
    out = []
    for k, v in a["body"]:
        if k == "h2":
            out.append(f'<h2 id="{slugify(v)}">{v}</h2>')
        elif k == "p":
            out.append(f"<p>{v}</p>")
        elif k == "ul":
            out.append("<ul>" + "".join(f"<li>{i}</li>" for i in v) + "</ul>")
        elif k == "ol":
            out.append("<ol>" + "".join(f"<li>{i}</li>" for i in v) + "</ol>")
        elif k == "note":
            out.append(f'<aside class="note">{v}</aside>')
    others = [b for b in ARTICLES if b["slug"] != a["slug"]][:2]
    more = "".join(f'<a class="rel reveal d{i+1}" href="blog/{b["slug"]}.html"><span class="tag">{b["cat"]}</span><b>{b["h1"]}</b><span class="go">Leer artículo →</span></a>' for i, b in enumerate(others))
    schema = [
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog.html"},
            {"@type": "ListItem", "position": 3, "name": a["h1"], "item": url}]},
        {"@context": "https://schema.org", "@type": "BlogPosting", "headline": a["h1"], "description": a["desc"], "inLanguage": "es",
         "datePublished": a["date"], "dateModified": a["date"], "mainEntityOfPage": url,
         "author": {"@type": "Organization", "name": "AC Soluciones", "url": SITE + "/"},
         "publisher": {"@type": "Organization", "name": "AC Soluciones", "url": SITE + "/", "logo": {"@type": "ImageObject", "url": SITE + "/assets/logo.svg"}}},
    ]
    hero = f'''<section class="page-hero"><canvas data-net></canvas><div class="container">
<nav class="crumbs" aria-label="Ruta"><a href="index.html">Inicio</a><span>/</span><a href="blog.html">Blog</a><span>/</span><span aria-current="page">{a["cat"]}</span></nav>
<span class="eyebrow">{a["cat"]}</span><h1 data-split data-scroll data-scroll-speed="2">{a["h1"]}</h1>
<div class="pmeta reveal in"><span>Equipo AC Soluciones</span><span>{fecha(a["date"])}</span><span>{minutos(a)} min de lectura</span></div></div></section>'''
    body = f'''<section><div class="container post-wrap"><article class="post-body">
<p class="lead-p reveal in">{a["lead"]}</p>
<nav class="toc reveal" aria-label="En este artículo"><b>En este artículo</b><ol>{toc}</ol></nav>
<div class="prose2">{"".join(out)}</div>
<div class="postcta reveal zoom"><div><span class="tag">{svc["tag"]} · {svc["name"]}</span><h3>¿Necesita apoyo con este tema?</h3><p>Revisamos su operación y le entregamos las brechas y un plan de trabajo con fechas.</p></div>
<div class="pc-btns"><a class="btn btn-primary" href="contacto.html">Solicitar diagnóstico <span class="arr">→</span></a><a class="btn btn-ghost" href="servicios/{svc["slug"]}.html">Ver el servicio</a></div></div>
</article></div></section>
<section style="background:#fff"><div class="container"><span class="eyebrow reveal">Seguir leyendo</span><h2 class="title reveal d1">Más artículos</h2><div class="grid-3 rels">{more}</div></div></section>'''
    html = head(a["title"], esc(a["desc"]), f'blog/{a["slug"]}.html', schema, og="article", css=BLOG_CSS) + navbar("blog.html") + hero + body + cta() + footer()
    return up(html)


(OUT / "blog").mkdir(parents=True, exist_ok=True)
for a in ARTICLES:
    (OUT / "blog" / f'{a["slug"]}.html').write_text(finish(blog_post(a)), encoding="utf-8")
(OUT / "blog.html").write_text(finish(blog_index()), encoding="utf-8")

# ---------------- sitemap y robots ----------------
urls = [("", "1.0"), ("servicios.html", "0.9")] + [(f"servicios/{x['slug']}.html", "0.8") for x in SVC] + [
    ("blog.html", "0.7")] + [(f"blog/{a['slug']}.html", "0.6") for a in ARTICLES] + [
    ("como-trabajamos.html", "0.6"), ("nosotros.html", "0.6"), ("contacto.html", "0.7")]
sm = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
      + "".join(f"<url><loc>{SITE}/{u}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>\n" for u, pr in urls) + "</urlset>\n")
(OUT / "sitemap.xml").write_text(sm, encoding="utf-8")
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")

for name, html in {"index.html": index, "servicios.html": servicios, "como-trabajamos.html": como,
                   "nosotros.html": nosotros, "contacto.html": contacto}.items():
    (OUT / name).write_text(finish(html), encoding="utf-8")
print("ok")



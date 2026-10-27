(() => {
  // ====== CONFIG: cambie este correo por el real de AC Soluciones ======
  const CONTACT_EMAIL = 'contacto@acsgi.com.mx';
  // Opcional: endpoint de Formspree/Web3Forms para envío directo sin abrir el cliente de correo.
  const FORM_ENDPOINT = '';

  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];

  // loader
  const hideVeil = () => $('#veil')?.classList.add('hide');
  window.addEventListener('load', () => setTimeout(hideVeil, 350));
  setTimeout(hideVeil, 1500);

  // Locomotive Scroll: scroll suave con inercia + parallax (data-scroll-speed)
  const bar = $('#progress'), nav = $('header.nav');
  const reduce = false; // sitio de marca: animaciones siempre activas
  let loco = null;
  const paint = y => {
    const h = document.documentElement, max = (loco ? loco.scroll.instance.limit.y : h.scrollHeight - h.clientHeight) || 1;
    bar.style.width = Math.min(y / max * 100, 100) + '%';
    nav.classList.toggle('scrolled', y > 40);
  };
  if (window.LocomotiveScroll && !reduce) {
    loco = new LocomotiveScroll({
      el: $('[data-scroll-container]'), smooth: true, lerp: 0.08, multiplier: 1,
      smartphone: { smooth: false }, tablet: { smooth: false }
    });
    loco.on('scroll', a => paint(a.scroll.y));
    const refresh = () => loco.update();
    addEventListener('load', () => { refresh(); setTimeout(refresh, 600); setTimeout(refresh, 1800); });
    document.fonts?.ready.then(refresh);
    new ResizeObserver(refresh).observe($('[data-scroll-container]'));
    // enlaces ancla / "volver arriba" con scroll suave
    $$('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
      const t = $(a.getAttribute('href')); if (t) { e.preventDefault(); loco.scrollTo(t, { offset: -80 }); }
    }));
  } else {
    addEventListener('scroll', () => paint(document.documentElement.scrollTop), { passive: true });
  }
  paint(0);
  // llegar a una sección por ancla desde otra página (p. ej. servicios.html#industria-farmaceutica)
  if (location.hash.length > 1) {
    const go = () => { const t = $(location.hash); if (t) (loco ? loco.scrollTo(t, { offset: -80, duration: 900 }) : t.scrollIntoView({ behavior: 'smooth' })); };
    addEventListener('load', () => setTimeout(go, 900));
  }

  // mobile menu
  $('.burger')?.addEventListener('click', () => $('nav ul').classList.toggle('open'));

  // transición de página: cortina de 5 paneles con nombre de la sección
  const names = { 'index.html': 'Inicio', 'servicios.html': 'Servicios', 'como-trabajamos.html': 'Cómo trabajamos', 'nosotros.html': 'Nosotros', 'contacto.html': 'Contacto', 'blog.html': 'Blog',
    'iso-9001.html': 'ISO 9001', 'iso-14001.html': 'ISO 14001', 'bpad.html': 'BPAD', 'farmacopea-feum.html': 'FEUM 7.0', 'cumplimiento-regulatorio.html': 'Cumplimiento', 'validacion-software.html': 'Validación de software', 'capacitacion.html': 'Capacitación', 'consultoria.html': 'Consultoría',
    'iso-42001.html': 'ISO/IEC 42001', 'iso-27001.html': 'ISO/IEC 27001', 'gobernanza-datos.html': 'Gobernanza de datos' };
  const out = document.createElement('div'); out.className = 'page-out';
  out.innerHTML = '<div class="panels">' + '<i></i>'.repeat(5) + '</div><div class="pname"><span></span></div>';
  document.body.append(out);
  $$('a[href]').forEach(a => {
    const u = a.getAttribute('href');
    if (!u || u.startsWith('#') || u.startsWith('http') || u.startsWith('tel') || u.startsWith('mailto')) return;
    a.addEventListener('click', e => {
      e.preventDefault(); loco?.stop();
      $('.pname span', out).textContent = names[u.split('/').pop()] || (u.indexOf('blog/') > -1 ? 'Blog' : '');
      out.classList.add('go');
      setTimeout(() => location.href = u, 900);
    });
  });
  addEventListener('pageshow', e => { if (e.persisted) { out.classList.remove('go'); loco?.start(); } });

  // split hero title into animated words
  $$('[data-split]').forEach(el => {
    const nodes = [...el.childNodes]; el.textContent = ''; let i = 0;
    nodes.forEach(n => {
      const wrap = n.nodeType === 3 ? null : n;
      const text = n.textContent;
      const target = wrap ? (wrap.textContent = '', wrap) : el;
      text.split(/\s+/).filter(Boolean).forEach(w => {
        const s = document.createElement('span'); s.className = 'word';
        s.innerHTML = `<i style="animation-delay:${0.45 + i++ * 0.08}s">${w}&nbsp;</i>`;
        target.append(s);
      });
      if (wrap) el.append(wrap);
    });
  });

  // reveal on scroll
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return;
    e.target.classList.add('in'); io.unobserve(e.target);
  }), { threshold: .15 });
  $$('.reveal,.steps').forEach(el => io.observe(el));

  // counters
  const cio = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return;
    const el = e.target, end = +el.dataset.count, pre = el.dataset.pre || '', suf = el.dataset.suf || '';
    const t0 = performance.now(), dur = 1800;
    const tick = t => {
      const p = Math.min((t - t0) / dur, 1), v = Math.round(end * (1 - Math.pow(1 - p, 4)));
      el.textContent = pre + v + suf; if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick); cio.unobserve(el);
  }), { threshold: .6 });
  $$('[data-count]').forEach(el => cio.observe(el));

  // 3D tilt + spotlight on cards
  if (matchMedia('(hover:hover)').matches) {
    $$('.card').forEach(c => {
      c.addEventListener('mousemove', e => {
        const r = c.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
        c.style.setProperty('--mx', x + 'px'); c.style.setProperty('--my', y + 'px');
        c.style.transform = `perspective(900px) rotateX(${(y / r.height - .5) * -7}deg) rotateY(${(x / r.width - .5) * 7}deg) translateY(-6px)`;
      });
      c.addEventListener('mouseleave', () => c.style.transform = '');
    });
  }

  // particle network canvas
  $$('canvas[data-net]').forEach(cv => {
    const ctx = cv.getContext('2d'); let w, h, pts = [], mouse = { x: -999, y: -999 };
    const size = () => {
      w = cv.width = cv.offsetWidth; h = cv.height = cv.offsetHeight;
      pts = Array.from({ length: Math.min(90, w / 14) }, () => ({ x: Math.random() * w, y: Math.random() * h, vx: (Math.random() - .5) * .45, vy: (Math.random() - .5) * .45 }));
    };
    size(); addEventListener('resize', size);
    cv.parentElement.addEventListener('mousemove', e => { const r = cv.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top; });
    (function loop() {
      ctx.clearRect(0, 0, w, h);
      pts.forEach((p, i) => {
        p.x += p.vx; p.y += p.vy;
        if (p.x < 0 || p.x > w) p.vx *= -1; if (p.y < 0 || p.y > h) p.vy *= -1;
        const dm = Math.hypot(p.x - mouse.x, p.y - mouse.y);
        if (dm < 140) { p.x += (p.x - mouse.x) * .012; p.y += (p.y - mouse.y) * .012; }
        ctx.beginPath(); ctx.arc(p.x, p.y, 1.8, 0, 7); ctx.fillStyle = 'rgba(34,211,238,.8)'; ctx.fill();
        for (let j = i + 1; j < pts.length; j++) {
          const q = pts[j], d = Math.hypot(p.x - q.x, p.y - q.y);
          if (d < 125) { ctx.strokeStyle = `rgba(20,184,166,${(1 - d / 125) * .35})`; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(q.x, q.y); ctx.stroke(); }
        }
      });
      requestAnimationFrame(loop);
    })();
  });

  // contact form -> correo
  const form = $('#contactForm');
  if (form) form.addEventListener('submit', async e => {
    e.preventDefault();
    const d = Object.fromEntries(new FormData(form)), st = $('.f-status', form);
    const body = `Nombre: ${d.nombre}\nEmpresa: ${d.empresa}\nCorreo: ${d.correo}\nServicio de interés: ${d.servicio}\n\n${d.mensaje}`;
    if (FORM_ENDPOINT) {
      try {
        const r = await fetch(FORM_ENDPOINT, { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(d) });
        if (!r.ok) throw 0;
        st.className = 'f-status ok'; st.textContent = '¡Gracias! Le responderemos en un día hábil.'; form.reset(); return;
      } catch { st.className = 'f-status err'; st.textContent = 'No se pudo enviar. Abriremos su correo como alternativa.'; }
    }
    location.href = `mailto:${CONTACT_EMAIL}?subject=${encodeURIComponent('Solicitud de diagnóstico - ' + d.servicio)}&body=${encodeURIComponent(body)}`;
    st.className = 'f-status ok'; st.textContent = 'Abriendo su aplicación de correo para enviar la solicitud…';
  });
})();

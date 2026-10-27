# Sitio web de AC Soluciones

Sitio estático generado con Python. Vercel lo construye y publica solo cada vez que se guarda un cambio en la rama `main`.

## Dónde está cada cosa

| Quiero cambiar… | Archivo |
|---|---|
| Textos de las páginas de servicio (qué es, qué incluye, preguntas frecuentes) | `services_content.py` |
| Agregar o editar artículos del blog | `blog_content.py` |
| Teléfonos, correo, menú, textos de inicio, nosotros y contacto | `build.py` |
| Colores y animaciones | `assets/styles.css`, `assets/blog.css`, `assets/main.js` |
| Plan de temas del blog | `BLOG_PLAN.md` |

## Cómo publicar un cambio
1. Edite el archivo en GitHub (botón del lápiz) y guarde con "Commit changes".
2. Vercel tarda cerca de un minuto en publicar. No hay que hacer nada más.

## Ver el sitio en su computadora
```bash
py build.py
py -m http.server 8099 --directory dist
```
Abra http://localhost:8099

## Pendientes antes del lanzamiento
- Cambiar `contacto@acsgi.com.mx` por el correo real (en `build.py` y `assets/main.js`).
- Revisión técnica de los textos de servicios y blog.
- Conectar el dominio propio en Vercel (Settings → Domains).

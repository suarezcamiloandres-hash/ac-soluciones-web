"""Artículos del blog. Cada entrada genera blog/<slug>.html y aparece en blog.html.

Bloques del cuerpo: ("h2", texto) · ("p", texto) · ("ul", [items]) · ("ol", [items]) · ("note", texto)
"""

CATS = ["Calidad", "Inteligencia artificial", "Auditoría"]

ARTICLES = [
 dict(
  slug="como-implementar-iso-9001",
  cat="Calidad", date="2026-10-27", service="iso-9001",
  title="Cómo implementar ISO 9001 paso a paso | AC Soluciones",
  h1="Cómo implementar ISO 9001 paso a paso",
  desc="Guía práctica para implementar ISO 9001: qué pide cada numeral, qué pasos seguir y qué errores evitar para que el sistema se use en la operación.",
  lead="Implementar ISO 9001 no consiste en escribir manuales. Consiste en que los procesos de la empresa se ejecuten de forma consistente y en poder demostrarlo. Esta guía resume qué pide la norma y en qué orden conviene avanzar.",
  body=[
   ("h2", "Qué es ISO 9001"),
   ("p", "ISO 9001 es la norma internacional de sistemas de gestión de la calidad. Su versión vigente es ISO 9001:2015. Define requisitos para que una organización planifique, controle y mejore sus procesos, y cumpla de forma consistente con lo que esperan sus clientes y la normativa que le aplica."),
   ("p", "Es una norma de requisitos, no una receta: dice qué debe lograr el sistema, no cómo debe ser cada procedimiento. Por eso dos empresas pueden cumplirla con sistemas muy distintos."),
   ("h2", "Lo que pide la norma, numeral por numeral"),
   ("p", "Los requisitos auditables están en los numerales 4 al 10. En resumen:"),
   ("ul", [
     "4. Contexto de la organización: entender qué factores internos y externos le afectan, quiénes son las partes interesadas y cuál es el alcance del sistema.",
     "5. Liderazgo: la dirección se compromete, define la política de calidad y asigna roles y responsabilidades.",
     "6. Planificación: riesgos y oportunidades, y objetivos de calidad medibles.",
     "7. Apoyo: recursos, competencia del personal, comunicación e información documentada.",
     "8. Operación: planificación y control de la producción o del servicio, control de proveedores externos y liberación de productos.",
     "9. Evaluación del desempeño: seguimiento y medición, satisfacción del cliente, auditoría interna y revisión por la dirección.",
     "10. Mejora: tratamiento de las no conformidades, acciones correctivas y mejora continua."]),
   ("h2", "Los pasos para implementarla"),
   ("ol", [
     "Diagnóstico de brechas: comparar cómo opera hoy la empresa con lo que pide la norma. De ahí sale un plan de trabajo con fechas.",
     "Alcance, contexto y política: definir qué procesos y sitios cubre el sistema y qué se compromete la dirección a lograr.",
     "Mapa de procesos e indicadores: identificar los procesos clave, sus responsables y cómo se va a medir si funcionan.",
     "Riesgos y oportunidades: anticipar qué puede salir mal en cada proceso y qué controles hacen falta.",
     "Documentación: procedimientos, instructivos y formatos hechos con las personas que los usan. Solo lo necesario, no más.",
     "Capacitación: cada procedimiento se enseña a quien lo aplica.",
     "Operar y registrar: el sistema debe funcionar un tiempo suficiente para generar registros reales.",
     "Auditoría interna y revisión por la dirección: verificar que el sistema funciona y decidir qué mejorar.",
     "Certificación, si se decide: la realiza un organismo de certificación independiente."]),
   ("h2", "Errores que dejan el sistema solo en papel"),
   ("ul", [
     "Copiar un manual de otra empresa en lugar de describir cómo trabaja la propia.",
     "Documentar de más: procedimientos que nadie consulta y que se vuelven obsoletos.",
     "Dejar el sistema en manos de una sola persona, sin involucrar a los responsables de cada proceso.",
     "No medir: sin indicadores no hay forma de saber si algo mejora.",
     "Tratar la auditoría interna como un trámite y no como una revisión honesta."]),
   ("h2", "¿Hay que certificarse?"),
   ("p", "No es obligatorio. Se puede implementar el sistema para ordenar la operación y decidir después si se certifica, por ejemplo cuando un cliente lo exija. Lo importante es que la implementación sea real: un certificado sobre un sistema que nadie usa no aporta valor."),
  ]),

 dict(
  slug="reglas-uso-inteligencia-artificial-empresa",
  cat="Inteligencia artificial", date="2026-10-27", service="iso-42001",
  title="Reglas para usar IA en la empresa (ISO/IEC 42001) | AC Soluciones",
  h1="Reglas para usar inteligencia artificial en la empresa",
  desc="Cómo ordenar el uso de IA en su empresa: inventario, riesgos, datos permitidos y supervisión humana, con la estructura de ISO/IEC 42001.",
  lead="En muchas empresas el personal ya usa herramientas de inteligencia artificial, con o sin permiso. La pregunta ya no es si se usa, sino con qué reglas. Esta guía propone una forma ordenada de empezar.",
  body=[
   ("h2", "El problema: uso sin reglas"),
   ("p", "Cuando cada persona decide por su cuenta qué herramienta usar y qué información ingresar, aparecen riesgos que la dirección no ve: información confidencial en servicios de terceros, respuestas incorrectas que se toman como ciertas, o decisiones que se delegan sin revisión."),
   ("p", "Los riesgos más comunes son estos:"),
   ("ul", [
     "Confidencialidad: datos de clientes, contratos o información financiera ingresados en una herramienta sin acuerdos de protección.",
     "Exactitud: las herramientas generativas pueden producir respuestas que suenan correctas y no lo son.",
     "Sesgos y trato injusto cuando la IA apoya decisiones sobre personas.",
     "Derechos de autor y propiedad intelectual sobre lo que se genera y lo que se ingresa.",
     "Requisitos de clientes o de la normativa sobre cómo se tratan los datos."]),
   ("h2", "Qué es ISO/IEC 42001"),
   ("p", "ISO/IEC 42001 es la primera norma internacional de sistemas de gestión para la inteligencia artificial, publicada en 2023. Tiene la misma lógica que otras normas ISO de gestión: política, roles, evaluación de riesgos, controles, auditoría y mejora continua. Aplica a quienes desarrollan IA, a quienes la proveen y también a quienes la usan."),
   ("h2", "Seis pasos para empezar"),
   ("ol", [
     "Inventario de usos: registrar qué herramientas de IA se usan, en qué áreas, para qué y con qué datos.",
     "Clasificar por riesgo: no es lo mismo redactar un borrador interno que apoyar una decisión sobre una persona o tratar datos personales.",
     "Definir qué datos se pueden y no se pueden ingresar en cada herramienta.",
     "Establecer supervisión humana: quién revisa los resultados y qué decisiones nunca se delegan por completo.",
     "Publicar una política de IA y capacitar al personal en reglas concretas.",
     "Revisar periódicamente: las herramientas y los riesgos cambian rápido."]),
   ("h2", "Ejemplos de reglas concretas"),
   ("p", "A modo de ejemplo, no como regla universal; cada empresa debe definir las suyas según sus riesgos:"),
   ("ul", [
     "Se puede usar IA para redactar borradores a partir de información pública o no sensible.",
     "No se ingresan datos personales de clientes o empleados en herramientas que no cuenten con un acuerdo que proteja esa información.",
     "Todo texto o análisis generado que llegue a un cliente lo revisa una persona responsable antes de enviarlo.",
     "Las decisiones que afecten a personas no se toman únicamente con el resultado de una herramienta."]),
   ("note", "Estas reglas funcionan mejor cuando se construyen con quienes ya usan las herramientas. Una prohibición total suele empujar el uso a la sombra."),
   ("h2", "Relación con la seguridad de la información"),
   ("p", "El uso de IA toca directamente la protección de la información. Si su empresa ya opera un sistema ISO/IEC 27001, muchas piezas ya existen: clasificación de la información, control de proveedores y gestión de incidentes. La gestión de IA se apoya en ellas y añade lo propio, como la evaluación de impactos y la supervisión humana."),
  ]),

 dict(
  slug="como-atender-hallazgos-de-auditoria",
  cat="Auditoría", date="2026-10-27", service="consultoria",
  title="Cómo atender un hallazgo de auditoría | AC Soluciones",
  h1="Cómo atender un hallazgo de auditoría: causa raíz y acción correctiva",
  desc="Qué es un hallazgo, la diferencia entre corrección y acción correctiva, y los pasos para cerrarlo con evidencia que el auditor acepte.",
  lead="Un hallazgo de auditoría no es una sanción: es información sobre dónde el sistema no funciona como debería. Atenderlo bien significa corregir el problema, entender por qué ocurrió y comprobar que no se repite.",
  body=[
   ("h2", "Qué es un hallazgo"),
   ("p", "Es un resultado de la auditoría que indica que algo no cumple un requisito, ya sea de una norma, de un cliente, de la regulación o de los propios procedimientos de la empresa. Según el esquema de auditoría se clasifican, por ejemplo, como no conformidades mayores o menores, observaciones u oportunidades de mejora."),
   ("h2", "Corrección y acción correctiva no son lo mismo"),
   ("ul", [
     "La corrección resuelve el problema puntual: por ejemplo, retirar un instrumento vencido o completar un registro faltante.",
     "La acción correctiva elimina la causa para que el problema no vuelva a ocurrir: por ejemplo, un control que avise antes del vencimiento."]),
   ("p", "Muchos planes de acción se quedan solo en la corrección y por eso los hallazgos reaparecen en la siguiente auditoría."),
   ("h2", "Los pasos para cerrarlo"),
   ("ol", [
     "Entender el hallazgo: leerlo completo, confirmar a qué requisito se refiere y qué evidencia observó el auditor.",
     "Corregir: contener el problema y resolver el caso concreto.",
     "Analizar la causa raíz: preguntar por qué ocurrió, varias veces, hasta llegar a algo que se pueda cambiar. Herramientas habituales son los cinco porqués y el diagrama de causa y efecto.",
     "Definir la acción correctiva: qué se va a cambiar, quién es el responsable y para qué fecha.",
     "Implementarla y conservar la evidencia: registros, capacitaciones, procedimientos actualizados.",
     "Verificar la eficacia: pasado un tiempo, comprobar que el problema no se repitió.",
     "Cerrar el hallazgo con la evidencia completa."]),
   ("h2", "Un ejemplo"),
   ("p", "Hallazgo: un termohigrómetro de una bodega tenía la calibración vencida. La corrección es calibrarlo o sustituirlo. Al preguntar por qué ocurrió, se descubre que nadie tenía la responsabilidad de vigilar las fechas. La acción correctiva es asignar un responsable y crear un programa de calibración con avisos previos al vencimiento. La verificación consiste en revisar, en la siguiente auditoría interna, que todos los instrumentos estén vigentes."),
   ("h2", "Errores frecuentes"),
   ("ul", [
     "Responder siempre con «capacitar al personal», sin comprobar que la falta de capacitación fue realmente la causa.",
     "Fijar plazos que no se pueden cumplir y quedar con acciones vencidas.",
     "No verificar la eficacia: se implementa la acción, pero nadie comprueba que funcionó.",
     "Cerrar sin evidencia: el auditor necesita ver registros, no solo una declaración."]),
   ("h2", "Qué debe tener un buen plan de acción"),
   ("ul", [
     "Descripción del hallazgo y requisito incumplido.",
     "Corrección realizada y evidencia.",
     "Causa raíz identificada.",
     "Acción correctiva, responsable y fecha.",
     "Criterio y fecha de verificación de la eficacia."]),
  ]),
]

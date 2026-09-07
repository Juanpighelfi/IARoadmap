# Sistema de actualización

El objetivo es mantener útil tu estudio sin perseguir cada lanzamiento. La selección semanal de papers, si ya la recibís, es una bandeja de candidatos: no una obligación de leerlos todos ni una tarea nueva que se active desde este repo.

## Cadencia personal

| Momento | Acción | Presupuesto orientativo |
| --- | --- | --- |
| Mientras estudiás un fundamento | Consultar el material elegido y sus erratas | Dentro del módulo |
| Cuando una novedad afecta tu proyecto | Leer la fuente primaria y probar una hipótesis | Reemplaza otra sesión, no se suma |
| Cada cuatro semanas | Revisar qué aprendiste, recursos que no funcionaron y horas reales | 20–30 min |
| Cada trimestre | Revisar enlaces, herramientas, compatibilidad y rutas | 1–2 h |

No hay publicación mensual ni paper semanal obligatorio. En matemáticas puede rendir más resolver un problema que leer un artículo nuevo.

## Seleccionar una novedad

Anotá problema que resuelve, evidencia disponible, costo de probarla y qué resultado justificaría adoptarla. Si es solo curiosidad, acotá una sesión. Un resultado negativo también se registra.

## Revisar recursos

La [guía de recursos](Guia%20de%20recursos.md) distingue contenido consultado, documentación dinámica y referencias históricas. Una respuesta HTTP 200 no demuestra vigencia ni calidad. Un bloqueo anti-bot tampoco demuestra que el enlace haya desaparecido.

Usá `python scripts/check_roadmap.py` para estructura y enlaces internos. Si hay acceso a internet, el modo `--external` permite revisar disponibilidad; contrastá manualmente redirects, errores y cambios de contenido. Revisá especificaciones de proveedores antes de usar código antiguo.

Registrá revisiones en [CHANGELOG](../CHANGELOG.md) con fecha y qué se comprobó. Los fundamentos envejecen a otra velocidad que APIs, modelos y precios. No descartar un recurso únicamente por el año.

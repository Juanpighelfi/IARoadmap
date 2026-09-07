# Diseño aprobado: ruta de IA aplicada y SaaS

El usuario autorizó modificar el repositorio para orientar su formación hacia desarrollo de software con IA, automatización para empresas y pymes, y un SaaS administrativo como proyecto conductor.

## Alcance

Conservar fundamentos de programación, datos y evaluación. Incorporar web, backend y permisos, integraciones y cobros, operación de un SaaS y análisis de procesos/pilotos. Reutilizar LLMs, contexto, workflows, análisis de errores y costos. Conservar la ruta anterior de robótica como opcional.

Planificar diez horas semanales de formación y práctica aplicada, con pausas y flexibilidad, sin duplicar tiempo dedicado al SaaS. Añadir primera sesión, ciclo de doce semanas y relación con el trabajo de productos 3D. No publicar horarios privados exactos ni información personal innecesaria.

## Arquitectura curricular

`curriculum.json` conserva la autoridad sobre IDs, horas y prerrequisitos. Los bloques de rutas y catálogo se regeneran con el script existente. Los nuevos módulos incluyen recurso seleccionado, diagnóstico, práctica, variantes, casos de aceptación y retención. No se cambian los scripts ni los laboratorios ejecutables existentes.

El proyecto describe un entorno administrativo con datos ficticios. El stack del SaaS aún no se revisó; no se presume tecnología ni se prescribe reescribir. Los ejercicios añadidos son consignas con criterios de aceptación, no laboratorios con autocorrección ya implementada. Funciones clínicas quedan fuera del ejercicio inicial.

## Verificación

Validar enlaces locales, Canvas, dependencias, estimaciones y bloques generados. Ejecutar las pruebas existentes de herramientas y laboratorios. Revisar Markdown con el linter del workflow cuando esté disponible. Publicar un único commit coherente sin forzar la rama ni sobrescribir cambios concurrentes.

# Mi ruta: desarrollo con IA, SaaS y automatización para pymes

Objetivo: entender, construir y mantener software que mejore procesos de empresas y pymes. La formación autodidacta es el eje de aprendizaje; la carrera aporta contexto y contenidos que se pueden acreditar con ejercicios. Se empieza por fundamentos, sin asumir dominio por haber generado código con IA.

## Proyecto conductor

[SaaS administrativo para profesionales](../03-Proyectos/SaaS%20administrativo%20con%20IA.md): recuperar comprensión del producto existente y completar un flujo pequeño, antes de ampliar funciones. El repositorio del SaaS y su tecnología todavía no se han revisado; esta ruta no prescribe migrarlo ni rehacerlo.

Python se usa para aprender programación y para los laboratorios existentes. En 01c se aprende el puente a JavaScript para la web; TypeScript se incorpora si el proyecto lo utiliza. Elegir un único backend después de inspeccionar el SaaS, sin cursar dos frameworks en paralelo.

## Cómo avanzar

1. Empezá por 00 y el diagnóstico de Python. Haber visto videos no acredita dominio, pero una prueba independiente sí permite evitar repeticiones.
2. Mantené un módulo principal. Aplicá revisión de código, pruebas y evaluación sobre su misma práctica.
3. Leé o mirá el recurso seleccionado, intentá un ejercicio, corregí y explicá lo esencial sin ayuda. Después resolvé una variante.
4. Guardá evidencia y el siguiente paso en `Mi-progreso/`. Una sesión aplicada al SaaS cuenta una sola vez dentro del presupuesto de estudio.
5. Si faltan fundamentos para tocar el producto, trabajá sobre una función aislada o una muestra sintética. Volvé al SaaS cuando puedas explicar el cambio.

## Etapas y entregas

| Etapa | Módulos | Resultado verificable |
| --- | --- | --- |
| Programar y comprender | 00, 01, 01b | Script pequeño, errores comprobados y diff explicado |
| Entender datos y necesidades | 02, 10, 12d | Datos sintéticos, permisos definidos y un proceso con métrica inicial |
| Construir un flujo web | 01c, 02b | Formulario, API y persistencia; dos cuentas aisladas |
| Integrar y operar | 08c, 11d | Evento repetido sin efecto duplicado, despliegue de prueba y recuperación |
| Aplicar IA con criterio | 06, 06b, 08, 10b, 11b | Baseline por reglas, alternativa con IA, evaluación y costo por tarea |
| Convertirlo en un servicio | 12b y aplicación de 12d | Demo documentada, propuesta de piloto, límites y mantenimiento |

El análisis inicial del proceso en 12d se retoma al final con resultados reales; no se registra como otro módulo completo. No hay que esperar al último módulo para mostrar un flujo administrativo a un profesional interesado, siempre que el entorno de prueba y su alcance estén claros.

## Tiempo y límites

Meta inicial: **10 horas semanales**, cinco bloques movibles de dos horas entre lunes y viernes. Probá dos semanas antes de ampliar; revisá estimaciones al mes. Consultá la [semana flexible](../03-Proyectos/Semana%20flexible.md) y el [plan de 12 semanas](../03-Proyectos/Plan%20de%2012%20semanas.md).

Los tres primeros meses son un ciclo de aprendizaje y validación, no una promesa de terminar todo el SaaS ni de obtener ingresos. El avance se decide por evidencia, no por calendario.

## Extensiones que se eligen por necesidad

- RAG (07): si el caso requiere responder sobre documentos, después de 06 y 10. No toda automatización necesita una base vectorial.
- MCP (08b): si hay necesidad concreta de interoperabilidad; no es un paso obligatorio para usar herramientas.
- Multimodalidad (09): si el proceso requiere imágenes o audio.
- Matemáticas y ML (03, 04): para predicción, clasificación tabular o decisiones que requieran entrenamiento. Conservá estadística práctica del 02 desde el inicio.
- Deep learning, fine-tuning e IA local: luego de acreditar sus prerrequisitos, si el problema lo justifica.
- [Robótica y visión](IA%20local%20y%20robotica%20opcional.md): ruta conservada, opcional.

## Secuencia y horas

<!-- ROUTE:personal:START -->
**Carga orientativa:** 290–494 horas.

Los prerrequisitos aparecen antes del módulo que los requiere.

- [00 - Orientacion y alfabetizacion en IA](../01-Niveles/00%20-%20Orientacion%20y%20alfabetizacion%20en%20IA.md) — 4–6 horas
- [01 - Computacion, Python, Git y entorno](../01-Niveles/01%20-%20Computacion%20Python%20Git%20y%20entorno.md) — 35–60 horas
- [01b - Ingenieria asistida por IA](../01-Niveles/01b%20-%20Ingenieria%20asistida%20por%20IA.md) — 6–10 horas
- [02 - Datos, SQL, visualizacion y estadistica practica](../01-Niveles/02%20-%20Datos%20SQL%20visualizacion%20y%20estadistica.md) — 25–40 horas
- [10 - Evaluacion, seguridad, privacidad y gobernanza](../01-Niveles/10%20-%20Evaluacion%20seguridad%20gobernanza.md) — 12–20 horas
- [12d - Procesos, pilotos y servicios para pymes](../01-Niveles/12d%20-%20Procesos%20y%20servicios%20para%20pymes.md) — 12–20 horas
- [01c - Web, HTTP y JavaScript](../01-Niveles/01c%20-%20Web%20HTTP%20y%20JavaScript.md) — 30–50 horas
- [02b - Backend, autenticación y aplicaciones SaaS](../01-Niveles/02b%20-%20Backend%20autenticacion%20y%20aplicaciones%20SaaS.md) — 35–60 horas
- [08c - Integraciones, webhooks y cobros confiables](../01-Niveles/08c%20-%20Integraciones%20y%20cobros%20confiables.md) — 20–35 horas
- [11d - Operación y mantenimiento de un SaaS](../01-Niveles/11d%20-%20Operacion%20de%20un%20SaaS.md) — 20–35 horas
- [06 - LLMs aplicados](../01-Niveles/06%20-%20LLMs%20aplicados.md) — 20–35 horas
- [06b - Context engineering](../01-Niveles/06b%20-%20Context%20engineering.md) — 15–25 horas
- [08 - Agentes, workflows y automatizacion segura](../01-Niveles/08%20-%20Agentes%20workflows%20automatizacion.md) — 25–45 horas
- [10b - Análisis de errores y evaluación desde trazas](../01-Niveles/10b%20-%20Error%20analysis%20y%20evals%20desde%20trazas.md) — 12–20 horas
- [11b - Inferencia, latencia y economia unitaria](../01-Niveles/11b%20-%20Inferencia%20costos%20y%20economia%20unitaria.md) — 15–25 horas
- [12b - Capa profesional](../01-Niveles/12b%20-%20Capa%20profesional.md) — 4–8 horas
<!-- ROUTE:personal:END -->

La secuencia y los rangos se generan desde [curriculum.json](../curriculum.json). Incluyen un ciclo acotado de práctica, no la producción completa del SaaS ni todos los recursos adicionales. Ampliar el proyecto, repetir ejercicios o cursar extensiones requiere recalcular.

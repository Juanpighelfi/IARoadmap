# Guía de recursos

Elegí un recurso principal por módulo. Las secciones “Qué estudiar” acotan capítulos o temas; las referencias adicionales son consulta o una explicación alternativa, no cursos que haya que terminar todos. Los tiempos estiman esa selección y su práctica.

## Selección para software y servicios: 7 de septiembre de 2026

Se consultaron las páginas oficiales siguientes al adaptar la ruta; no se ejecutaron sus ejemplos ni se verificó cada enlace interno. Seguí las secciones acotadas en cada módulo. La selección personal se vincula ahora al [código real del SaaS](../03-Proyectos/Estudiar%20con%20el%20SaaS%20real.md), sin asumir que las integraciones estén operativas.

| Módulo | Recurso principal | Uso acotado |
| --- | --- | --- |
| 01 | [Node.js: introducción](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs) | Entender el runtime; funciones y objetos con MDN |
| 01c | [React Learn](https://react.dev/learn) | Componentes, props, estado y eventos del panel existente |
| 01c | [MDN Learn](https://developer.mozilla.org/en-US/docs/Learn_web_development) | Formularios, JavaScript y peticiones |
| 02b | [Fastify](https://fastify.dev/docs/latest/Guides/Getting-Started/) y [Drizzle](https://orm.drizzle.team/docs/overview) | Leer una ruta y su consulta en el proyecto |
| 02b | [MDN servidor](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps) | Responsabilidades del backend |
| 02 y 02b | [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html) | SQL, relaciones y transacciones; adaptar al motor existente |
| 10 y 02b | [OWASP Top 10](https://owasp.org/www-project-top-ten/) | Relacionar acceso y riesgos con pruebas concretas |
| 08c | [Mercado Pago webhooks](https://www.mercadopago.com.ar/developers/es/docs/your-integrations/notifications/webhooks) | Contrastar eventos y firma con el código; verificar sandbox antes de ejecutar |
| 08c | [BullMQ workers](https://docs.bullmq.io/guide/workers) | Productor, consumidor y reintentos en la cola existente |
| 11d | [The Twelve-Factor App](https://12factor.net/) | Configuración, dependencias, procesos y registros |
| 12d | [GOV.UK: necesidades de usuarios](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) | Observar una tarea y separar necesidades de soluciones |

[TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) complementa 01 y 01c después de JavaScript: el producto usa TypeScript. [GitHub Get Started](https://docs.github.com/en/get-started) complementa Git en 01 y 01b.

La siguiente tabla reúne también ramas opcionales. Su presencia no las convierte en tareas de la ruta personal.

## Selección y acceso

| Área | Principal | Alternativa / consulta | Acceso y uso |
| --- | --- | --- | --- |
| Python | [CS50P](https://cs50.harvard.edu/python/) | [Python Tutorial](https://docs.python.org/3/tutorial/) para quien ya programa | Material OpenCourseWare; no requiere certificado |
| Datos | [Pandas, tutoriales iniciales](https://pandas.pydata.org/docs/getting_started/intro_tutorials/) | SQLite de la biblioteca estándar y las consignas del 02 | Documentación abierta; CPU |
| Matemáticas | [Mathematics for Machine Learning](https://mml-book.github.io/) | [3Blue1Brown, álgebra lineal](https://www.3blue1brown.com/topics/linear-algebra) para intuición | PDF disponible; resolver problemas, no solo videos |
| Búsqueda y decisiones | [Berkeley CS188, archivo 2025](https://inst.eecs.berkeley.edu/~cs188/archive/fa25/) | Laboratorios 03 y 05 del repo | Material de un semestre archivado; ignorar entregas y anuncios |
| ML | [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) | [Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) | Documentación dinámica; registrar versión instalada |
| DL | [Dive into Deep Learning](https://d2l.ai/) | [PyTorch Tutorials](https://docs.pytorch.org/tutorials/) | Libro abierto; empezar pequeño en CPU |
| Visión | [CS231n notes](https://cs231n.github.io/) | Proyecto de inspección y PyTorch | Conceptos y notas; APIs de ejemplos se verifican contra versión instalada |
| LLMs | [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/) | Documentación del runtime/proveedor usado | Lectura abierta; entrenamiento e inferencia pueden requerir cómputo |
| Contexto y agentes | [Context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) y [workflows](https://www.anthropic.com/engineering/building-effective-agents) | Implementación propia pequeña | Artículos de ingeniería; patrones como hipótesis, no recetas universales |
| RAG | [Qdrant documentation](https://qdrant.tech/documentation/) | Baseline lexical propia y sección de evaluación del 07 | Documentación abierta y opción local; no hace falta contratar cloud |
| Post-training | [TRL](https://huggingface.co/docs/trl/) | [PEFT](https://huggingface.co/docs/peft) | Documentación abierta; hacer presupuesto antes de entrenar |
| MCP | [Especificación y documentación](https://modelcontextprotocol.io/) | Misma herramienta como función local | Lectura abierta; guardar versión de protocolo/SDK |
| Análisis de errores | [Field Guide de Hamel Husain](https://hamel.dev/blog/posts/field-guide/) | Muestra propia y condiciones de salida del 10b | Artículo abierto; no requiere tráfico de terceros |
| Operación | [Made With ML](https://madewithml.com/) | Endpoint local y documentación del framework | Material abierto; adaptar servicios pagos de ejemplos si aparecen |
| Inferencia local | [llama.cpp](https://github.com/ggml-org/llama.cpp) para LLMs compatibles; PyTorch para el primer modelo visual | Comparar modelo menor antes de cambiar runtime | Software y pesos tienen licencias distintas; medir en el equipo disponible |
| Robótica | [Modern Robotics](https://modernrobotics.northwestern.edu/nu-gm-book-resource/) | [MIT Underactuated](https://underactuated.mit.edu/) y [LeRobot](https://huggingface.co/docs/lerobot/index) | Libro/recursos y docs; simulación antes de hardware |
| Investigación | [CS336](https://cs336.stanford.edu/) como referencia de profundidad | [How to Read a Paper](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) | Ver prerrequisitos; no cursar completo como introducción |

La mayoría está en inglés. Usá traducción para una primera lectura y conservá términos, ecuaciones y código originales; comprobá lo que afecte una decisión. [Recursos en español](Recursos%20en%20espanol.md) ofrece explicaciones complementarias.

## Registro de revisión: 6 de septiembre de 2026

Se consultaron las páginas principales seleccionadas, no se ejecutó todo el código de cursos externos ni se verificó cada enlace del inventario histórico. “Consultado” significa que la página y el material indicado estuvieron accesibles durante esta revisión, no que cada capítulo sea autosuficiente.

- El curso RAG de DeepLearning.AI no pudo verificarse desde la consulta; queda como referencia opcional. La extensión RAG usa Qdrant y la consigna propia.
- Papers with Code redirigía a [Hugging Face Papers](https://huggingface.co/papers/); se actualizó su rol como fuente de descubrimiento.
- [Hugging Face Robotics Course](https://huggingface.co/learn/robotics-course/en/unit0/1) sirve de complemento, pero la página aún mostraba unidades avanzadas pendientes; no se usa como único temario de robótica.
- La consulta a tutoriales de ROS 2 Jazzy encontró una protección anti-bot. Eso no demuestra que el sitio esté roto; comprobar acceso al elegir esa extensión. No bloquea el ejercicio de simulación del módulo 12c.
- Los precios, cuotas de GPU y licencias de modelos concretos no quedan validados por este listado. Revisarlos antes de una ejecución con gasto o distribución.

## Ficha para sustituir una fuente

Anotá URL, capítulo usado, fecha, motivo del cambio, idioma, prerequisitos, costo de acceso y entorno necesario. Probá un ejercicio del nuevo material antes de reemplazar toda la selección. Actualizá el enlace del módulo y este registro; mantené una sola fuente principal.

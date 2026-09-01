# Registro de cambios

Este vault trata un campo que se mueve rapido. Un roadmap sin fecha ni historial
envejece en silencio: sirve saber cuando se agrego cada cosa y cuando se reviso por
ultima vez.

Convencion: una entrada por revision, con fecha. Las revisiones trimestrales se anotan
aunque no cambien nada, porque "revisado y sigue vigente" tambien es informacion.

## 2026-09-01

### Agregado

#### Sistema de seguimiento

- `06-Bitacora/` con el metodo de registro semanal y una entrada de ejemplo.
- `00-MOC/Estado actual.md`: tablero unico de progreso, portfolio y revision
  trimestral, con consultas opcionales de Dataview.
- Plantillas de bitacora semanal, sesion de estudio y lectura de paper.
- `04-Recursos/Repaso espaciado.md` con un mazo base de unas 100 tarjetas.
- Campos `estado`, `inicio` y `fin` en el frontmatter de todos los niveles.

#### Niveles nuevos

- `01b - Ingenieria asistida por IA`: codigo agentico, revision de diffs, y cuando no
  delegar.
- `05b - Post-training aplicado`: SFT, LoRA/QLoRA, DPO, destilacion, y sobre todo
  cuando NO fine-tunear. Cierra el hueco que dejaba el portfolio, que pedia una pieza
  de PEFT sin nivel que la ensenara.
- `06b - Context engineering`: presupuesto de contexto, compactacion, memoria,
  sub-agentes, caching.
- `08b - MCP y protocolos de herramientas`: el estandar de integracion que faltaba en
  el nivel de agentes.
- `10b - Error analysis y evals desde trazas`: el bucle que va de datos reales a
  taxonomia de fallas a evals, complementando el bucle hacia adelante del nivel 10.
- `11b - Inferencia, costos y economia unitaria`: latencia p95, costo por tarea,
  routing, cuantizacion, servido propio.
- `12b - Capa profesional`: escribir sobre lo construido, presentar el portfolio, leer
  papers, entrevistas y clientes.

#### Recursos

- `04-Recursos/Regulacion y cumplimiento.md`: EU AI Act con fechas de aplicacion,
  regimenes de datos personales, dominios sensibles y propiedad intelectual.
- `04-Recursos/Sistema de actualizacion.md`: el reemplazo concreto del "no persigas el
  hype" del Anti-roadmap.
- `04-Recursos/Recursos en espanol.md`.
- Sumados a los niveles: Karpathy Zero to Hero, Chip Huyen, Anthropic sobre agentes y
  context engineering, Hamel Husain sobre evals, cursos de Hugging Face, Raschka,
  bbycroft, Kaggle competitions, Made With ML, vLLM, PEFT y TRL.

#### Ruta nueva

- `02-Rutas/Si estas construyendo un producto.md`, con el mapeo de que sale de cada
  nivel para un producto real y una seccion para dominios sensibles.

### Cambiado

- El capstone puede ser el producto que ya estas construyendo, y ahora exige costo por
  tarea, p95 y taxonomia de fallas.
- `Plan de 12 meses` incorpora los niveles nuevos, las practicas continuas y una
  revision trimestral.
- `Anti-roadmap` gana una tabla de que hacer en lugar de cada error.
- `Mapa de estudio`, `Indice del vault` y la nota de entrada reflejan la estructura
  nueva.

## 2026-06-08

- Primera version del vault: 13 niveles, 4 rutas, proyectos, recursos y plantillas.

## Proxima revision

Trimestral, junto con la revision de [[00-MOC/Estado actual]]. Que mirar:

- Enlaces rotos, dentro y fuera del vault.
- Fechas del EU AI Act en [[04-Recursos/Regulacion y cumplimiento]], que ya se
  movieron mas de una vez.
- Herramientas discontinuadas o reemplazadas en
  [[04-Recursos/Herramientas recomendadas]].
- Temas que dejaron de ser emergentes y ya son parte del temario base.

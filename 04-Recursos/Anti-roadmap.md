---
tags:
  - recursos
  - criterio
---

# Anti-roadmap

Que evitar:

- Aprender 20 frameworks antes de construir un proyecto.
- Empezar con fine-tuning sin tener evals ni datos de calidad.
- Usar agentes donde un workflow determinista bastaba.
- Medir prompts solo con impresion subjetiva.
- Ignorar costos, latencia, privacidad y logs.
- Pensar que RAG soluciona datos malos.
- Creer que saber usar ChatGPT equivale a saber IA.
- Saltar fundamentos si quieres trabajar en ML engineering o investigacion.
- Perseguir cada modelo nuevo sin aprender patrones estables.
- Estudiar y construir por separado, pagando dos veces por el mismo aprendizaje.
- Fine-tunear antes de agotar prompting, structured outputs y retrieval.
- Escribir evals desde la imaginacion en vez de desde trazas reales.
- Delegar codigo a un asistente y confundir que funcione con haberlo aprendido.
- Seguir un plan de 12 meses sin registrar las horas reales.

## Que hacer en su lugar

Cada linea de arriba tiene su reemplazo concreto en el vault:

| En vez de | Hace esto |
| --- | --- |
| Perseguir cada lanzamiento | [[Sistema de actualizacion]]: cadencia fija, pocas fuentes, una pregunta filtro |
| Estudiar y construir por separado | [[02-Rutas/Si estas construyendo un producto]] |
| Fine-tunear por reflejo | La seccion "cuando NO fine-tunear" de [[01-Niveles/05b - Post-training aplicado]] |
| Evals imaginados | [[01-Niveles/10b - Error analysis y evals desde trazas]] |
| Delegar sin entender | El criterio de salida de [[01-Niveles/01b - Ingenieria asistida por IA]] |
| Un plan sin medicion | [[00-MOC/Estado actual]] y [[06-Bitacora/Como usar la bitacora]] |

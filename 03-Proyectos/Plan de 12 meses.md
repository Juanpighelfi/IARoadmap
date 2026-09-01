---
tags:
  - proyectos
  - plan
  - 12-meses
---

# Plan de 12 meses

Pensado para 8 a 10 horas por semana.

## Antes de empezar

- Abri [[00-MOC/Estado actual]] y marca el nivel donde arrancas.
- Lee [[06-Bitacora/Como usar la bitacora]]. Una entrada por semana, sin excepciones.
- Elegi una ruta de `02-Rutas/`. Si ya tenes un producto en marcha, la ruta es
  [[02-Rutas/Si estas construyendo un producto]] y este plan se reordena bastante.

Una advertencia aritmetica: el plan supone 8-10 h semanales. Si tu promedio real de las
primeras 4 semanas es 5, no te exijas el plan de 12 meses: ajustalo a 20. Ese numero
sale de la bitacora, no de la intencion.

## Continuo, todos los meses

- Una entrada semanal de bitacora.
- 15-20 min, 3 veces por semana, de [[04-Recursos/Repaso espaciado]].
- Una pasada semanal por las fuentes de [[04-Recursos/Sistema de actualizacion]].
- Desde el mes 3, un texto publico por mes. Ver [[01-Niveles/12b - Capa profesional]].

## Mes 1

- Orientacion, Python, Git, entorno.
- [[01-Niveles/01b - Ingenieria asistida por IA]] en la segunda quincena.
- Proyecto: CLI de procesamiento de texto con tests.

## Mes 2

- Datos, SQL, Pandas, visualizacion.
- Proyecto: analisis de dataset y reporte.

## Mes 3

- Matematicas practica y ML clasico.
- Proyecto: modelo predictivo con baseline y metricas, comparado contra el leaderboard
  de una competencia de Kaggle ya cerrada.
- Primer texto publico.

## Mes 4

- Deep learning basico con PyTorch o fast.ai.
- Proyecto: clasificador de imagenes o texto con deploy simple.

## Mes 5

- LLM APIs, prompting, structured outputs.
- Context engineering: presupuesto de tokens y politica de memoria.
- Proyecto: asistente con JSON validado y evals.

## Mes 6

- Tool calling, workflows y MCP.
- Proyecto: app que llama herramientas internas con permisos, logs y un servidor MCP
  propio.

## Mes 7

- RAG y vector search.
- Proyecto: chatbot con docs propias, citas y no-answer.

## Mes 8

- RAG avanzado: hybrid search, reranking, evaluacion.
- Proyecto: suite de preguntas, eval automatica y dashboard.

## Mes 9

- Agentes y orquestacion.
- Error analysis: leer 100 trazas reales y armar la taxonomia de fallas.
- Proyecto: agente con trazas, limites y human-in-the-loop.

## Mes 10

- Seguridad, privacidad, gobernanza, cumplimiento y red teaming.
- Proyecto: informe de riesgos, clasificacion segun el EU AI Act, mitigaciones y
  ataques reproducibles.

## Mes 11

- LLMOps/MLOps, Docker, CI/CD, observabilidad.
- Inferencia y costos: costo por tarea, p95 y una palanca de optimizacion aplicada.
- Proyecto: deploy con metricas, rollback y eval gate.

## Mes 12

- Capstone segun ruta.
- Proyecto: producto IA completo con README, arquitectura, evals, demo y postmortem,
  mas el texto publico que lo explica.

## Que queda fuera de estos 12 meses

- [[01-Niveles/05b - Post-training aplicado]]: entra solo si tu caso lo pide, y despues
  de agotar prompting, structured outputs y RAG.
- [[01-Niveles/09 - Multimodalidad]]: se intercala en el mes que corresponda si tu
  producto procesa documentos, imagenes o audio; si no, se pospone.
- [[01-Niveles/12 - Profundizacion]]: es el ano siguiente.

Posponer con motivo escrito en [[00-MOC/Estado actual]] es parte del plan. Posponer sin
escribirlo es como se abandona un roadmap sin darse cuenta.

## Revision trimestral

Meses 3, 6, 9 y 12: abri las ultimas 12 entradas de bitacora y responde tres preguntas.
Horas reales por semana, ratio construir sobre leer, y que tema se repite en "que no
entendi". Ajusta el plan a esos numeros. La tabla esta en [[00-MOC/Estado actual]].

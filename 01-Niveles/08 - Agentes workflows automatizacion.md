---
tags:
  - nivel
  - agentes
  - workflows
  - automatizacion
duracion: 6-10 semanas
---

# 08 - Agentes, workflows y automatizacion segura

## Debes aprender

- Diferencia entre workflow determinista, agent loop y multi-agent system.
- Patrones: planner-executor, ReAct, router, evaluator-optimizer.
- Tool use: contratos, permisos, sandboxing, retries, timeouts, audit logs.
- Memoria: episodica, semantica, working memory, retrieval memory.
- Orquestacion: state machines, queues, human-in-the-loop.
- Seguridad: prompt injection, data exfiltration, herramientas destructivas, autorizaciones.
- Observabilidad: traces, spans, decisiones, inputs/outputs de herramientas.

## Practica

- Agente que investiga un tema, cita fuentes, genera reporte y registra cada paso.
- Workflow de documentos con OCR, extraccion estructurada, revision humana y export.
- Agente con herramientas limitadas y politica de permisos explicita.

## Criterio de salida

Puedes explicar cada accion del agente, reproducir sus trazas y limitar su dano cuando falla.

## Recursos

- ReAct paper: https://arxiv.org/abs/2210.03629
- LangGraph docs: https://langchain-ai.github.io/langgraph/
- CrewAI docs: https://docs.crewai.com/

## Siguiente

- [[09 - Multimodalidad]]
- [[10 - Evaluacion seguridad gobernanza]]

## Prácticas

- **Módulo 6: Agentes y Despliegue**
  - [Prácticas del Módulo 6](practicas/modulo_6/)

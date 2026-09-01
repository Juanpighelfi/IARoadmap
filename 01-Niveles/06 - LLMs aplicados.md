---
tags:
  - nivel
  - llm
  - prompting
  - tool-calling
duracion: 4-8 semanas
estado: pendiente
inicio:
fin:
---

# 06 - LLMs aplicados

## Debes aprender

- Tokens, contexto, temperatura, top-p, streaming, latencia, costos.
- Prompting: instrucciones, ejemplos, restricciones, formato, decomposition.
- Structured outputs: JSON schema, validacion, parsers, retries.
- Tool/function calling: contratos, permisos, idempotencia, errores.
- Memoria conversacional: que guardar, que no guardar, privacidad.
- Model selection: proveedor, modelo open source, costo, calidad, latencia, datos.
- Limitaciones: hallucinations, prompt injection, dependencia de contexto.

## Practica

- Asistente CLI que resume, extrae datos y responde con JSON validado.
- API de soporte que decide si responde, pide aclaracion o llama una herramienta.
- Suite de 30 casos de prueba para prompts y outputs.

## Criterio de salida

Puedes construir una app LLM pequena que no dependa de probar a ojo: tiene validacion, tests y fallbacks.

## Recursos

- Prompt Engineering Guide: <https://www.promptingguide.ai/>
- Hugging Face Course: <https://huggingface.co/course>
- DeepLearning.AI short courses: <https://www.deeplearning.ai/courses/>
- Hugging Face LLM Course: <https://huggingface.co/learn/llm-course>
- Chip Huyen, AI Engineering (el libro que mas se solapa con los niveles 06, 10 y 11):
  <https://huyenchip.com/books/>
- Visualizacion de un LLM ejecutandose paso a paso: <https://bbycroft.net/llm>

## Siguiente

- [[06b - Context engineering]]
- [[07 - RAG busqueda embeddings]]
- [[08 - Agentes workflows automatizacion]]
- [[10 - Evaluacion seguridad gobernanza]]

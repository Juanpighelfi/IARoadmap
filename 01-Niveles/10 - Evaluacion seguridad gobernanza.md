---
tags:
  - nivel
  - evals
  - seguridad
  - gobernanza
duracion: 4-8 semanas
estado: pendiente
inicio:
fin:
---

# 10 - Evaluacion, seguridad, privacidad y gobernanza

## Debes aprender

- Evals deterministas: schema, regex, exact match, unit tests, tool-call shape.
- Evals semanticas: rubricas, LLM-as-judge con cautela, pairwise comparison.
- Evals de RAG: retrieval, groundedness, citation faithfulness.
- Red teaming: prompt injection, jailbreaks, datos sensibles, herramientas peligrosas.
- Privacidad: PII, minimizacion, retention, logs, proveedores.
- Gobernanza: owners, risk register, aprobaciones, incident response.
- Fairness y sesgo: datasets, segmentos, monitoreo, impacto.
- Cumplimiento: clasificacion de riesgo del EU AI Act, obligaciones de transparencia,
  regimenes de datos personales y reglas extra en dominios sensibles. Ver
  [[04-Recursos/Regulacion y cumplimiento]].

## Practica

- Crear un eval harness con 50 a 100 casos reales o simulados.
- Red-team de tu app: 30 ataques y mitigaciones.
- Documento de riesgos: que puede salir mal, severidad, deteccion, mitigacion.
- Clasificar tu propia app segun el EU AI Act y listar que obligaciones te tocan.

## Criterio de salida

Ninguna app de IA pasa a produccion sin tests de regresion, trazas, limites de accion y plan de incidentes.

## Recursos

- NIST AI RMF: <https://airc.nist.gov/airmf-resources/>
- OWASP Top 10 for LLM Applications: <https://owasp.org/www-project-top-10-for-large-language-model-applications/>
- RAGAS: <https://docs.ragas.io/>
- Arize Phoenix: <https://phoenix.arize.com/>
- Hamel Husain, Your AI Product Needs Evals: <https://hamel.dev/blog/posts/evals/>
- Explorador del EU AI Act: <https://artificialintelligence-act.eu/>

## Siguiente

- [[10b - Error analysis y evals desde trazas]]
- [[11 - MLOps LLMOps despliegue]]
- [[04-Recursos/Regulacion y cumplimiento]]

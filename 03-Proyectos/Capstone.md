---
tags:
  - proyecto
  - capstone
---

# Capstone

## Si ya estas construyendo algo

El mejor capstone no es un proyecto nuevo: es lo que ya construis, llevado al estandar
de abajo. Ver [[02-Rutas/Si estas construyendo un producto]]. Un sistema con usuarios
reales tiene datos sucios, fallas raras y consecuencias, que es exactamente lo que un
proyecto de ejercicio no puede darte.

## Requisitos minimos

- Problema real y usuario definido.
- Datos o herramientas conectadas.
- Evals antes del deploy.
- Logs y trazas.
- Seguridad basica: permisos, secretos, PII y limites de accion.
- Costo por tarea y latencia p95 medidos, no estimados. Ver
  [[01-Niveles/11b - Inferencia costos y economia unitaria]].
- Taxonomia de fallas reales con frecuencias, si hubo usuarios. Ver
  [[01-Niveles/10b - Error analysis y evals desde trazas]].
- README con arquitectura, tradeoffs, setup y demo.
- Postmortem: que fallo, que se midio, que falta.
- Un texto publico que lo explique. Ver [[01-Niveles/12b - Capa profesional]].

## Ideas

- Asistente RAG para un dominio propio.
- Agente de investigacion con citas y trazas.
- Herramienta de extraccion de documentos con revision humana.
- API de prediccion con model registry, monitoring y rollback.
- Copiloto de workflow para una tarea laboral repetitiva.

## Entregables

- Repo publico o privado.
- Demo local o deploy.
- Dataset de evaluacion.
- Informe de riesgos.
- Capturas o video corto.

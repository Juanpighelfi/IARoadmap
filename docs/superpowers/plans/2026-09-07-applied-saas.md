# Applied SaaS Roadmap Implementation Plan

> **For agentic workers:** Execute inline using the approved design. Steps use checkbox syntax for tracking.

**Goal:** Reorientar el currículo personal a software con IA y servicios para pymes.

**Architecture:** Mantener la fuente curricular única y generar sus vistas. Integrar módulos nuevos con prácticas progresivas del mismo SaaS y preservar especializaciones opcionales.

**Tech Stack:** Markdown, JSON y herramientas Python existentes.

**Spec:** [Diseño aprobado](../specs/2026-09-07-applied-saas-design.md).

## Global Constraints

- Diez horas semanales propuestas, sin duplicar práctica del SaaS.
- No asumir el stack del producto ni acreditar progreso inexistente.
- Preservar módulos y laboratorios de especialización; no reescribir código ejecutable.
- Datos ficticios y alcance administrativo para la práctica inicial.

## Task 1: Currículo y proyectos

- [x] Inspeccionar rutas, manifiesto, scripts, tests, navegación y workflow.
- [x] Agregar 01c, 02b, 08c, 11d y 12d con práctica evaluable y recursos oficiales.
- [x] Actualizar ruta personal y conservar la ruta de robótica opcional.
- [x] Escribir proyecto SaaS, prácticas, primera sesión, semana flexible y ciclo de doce semanas.

## Task 2: Coherencia y publicación

- [x] Actualizar README, diagnóstico, índices, mapas, recursos y plantillas.
- [x] Regenerar catálogo y rutas con `python scripts/build_catalog.py`.
- [x] Ejecutar validación local y las 34 pruebas existentes; revisar cambios y corregir inconsistencias.
- [x] Preparar el conjunto de cambios para publicación vía GitHub.

La publicación y el resultado del workflow remoto quedan registrados en el pull request de esta adaptación.

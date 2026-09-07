# Personal Roadmap Implementation Plan

> For agentic workers: usar superpowers:subagent-driven-development para las unidades independientes; integrar y revisar antes de publicar.

**Goal:** Convertir el vault en un recorrido personal, verificable y flexible de IA con énfasis en sistemas locales y robótica.

**Architecture:** Markdown conserva el contenido; curriculum.json centraliza metadatos y rutas. Scripts de biblioteca estándar generan catálogo y validan estructura. Laboratorios autónomos ofrecen comprobación individual.

**Tech Stack:** Markdown, JSON, Python 3.11+, GitHub Actions y Obsidian Canvas.

**Spec:** ../specs/2026-09-06-personal-roadmap-design.md

## Global Constraints

- Conservar nombres existentes; ningún dato de progreso inventado.
- Sin dependencias obligatorias de GPU, API comercial o otros estudiantes.
- No modificar configuraciones personales de Obsidian.
- Revisión remota con avance no forzado de la rama.

## Tareas

- [x] Preparar snapshot aislado y verificar la revisión base.
- [x] Actualizar módulos, diagnóstico, rutas, tiempos, recursos, seguimiento y canvas; convertir navegación interna a Markdown.
- [x] Crear laboratorios con consignas, datos sintéticos identificados, pistas, corrección y pruebas de referencia.
- [x] Crear generador y validador con pruebas de dependencias cíclicas, enlaces rotos y rutas inválidas.
- [x] Ejecutar validación, laboratorios y lint; revisar el diff y corregir los hallazgos.
- [ ] Publicar el conjunto validado y verificar la revisión remota.

## Interfaces compartidas

curriculum.json: objeto con schema_version=1, modules (lista de {id, path, title, prerequisites: lista de IDs, hours: [mínimo,máximo], category}) y routes (objeto clave -> {title, path, modules: lista ordenada de IDs}). Las horas cubren un ciclo de práctica, incluyendo lectura, ejercicio, corrección y primer repaso; no certifican dominio permanente.

scripts/check_roadmap.py valida ese contrato, archivos, rutas y enlaces Markdown/Canvas. scripts/build_catalog.py genera 00-MOC/Catalogo de modulos.md y se comprueba con --check. 07-Laboratorios usa unittest, sin instalaciones obligatorias; resultados personales se escriben fuera de los archivos curriculares.

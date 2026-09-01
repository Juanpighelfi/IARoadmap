---
tags:
  - moc
  - estado
  - seguimiento
actualizado: 2026-09-01
---

# Estado actual

Tablero unico de progreso. Se actualiza a mano al abrir y al cerrar cada nivel, y una
vez por semana desde [[06-Bitacora/Como usar la bitacora]].

Estados posibles en el frontmatter de cada nivel: `pendiente`, `en curso`, `hecho`,
`omitido`. Omitir un nivel es una decision valida siempre que quede escrito el motivo.

## Resumen

- Nivel en curso:
- Ruta elegida: ver [[02-Rutas/Si ya eres developer]] u otra en `02-Rutas/`
- Horas por semana, promedio real de las ultimas 4:
- Proximo criterio de salida a cumplir:

## Niveles

| Nivel | Duracion | Estado | Inicio | Fin | Criterio de salida cumplido |
| --- | --- | --- | --- | --- | --- |
| [[01-Niveles/00 - Orientacion y alfabetizacion en IA\|00 Orientacion]] | 1-3 sem | pendiente | | | [ ] |
| [[01-Niveles/01 - Computacion Python Git y entorno\|01 Python, Git, entorno]] | 4-8 sem | pendiente | | | [ ] |
| [[01-Niveles/01b - Ingenieria asistida por IA\|01b Ingenieria asistida por IA]] | 2-4 sem | pendiente | | | [ ] |
| [[01-Niveles/02 - Datos SQL visualizacion y estadistica\|02 Datos y estadistica]] | 4-8 sem | pendiente | | | [ ] |
| [[01-Niveles/03 - Matematicas para ML\|03 Matematicas]] | 4-10 sem | pendiente | | | [ ] |
| [[01-Niveles/04 - Machine learning clasico\|04 ML clasico]] | 6-10 sem | pendiente | | | [ ] |
| [[01-Niveles/05 - Deep learning y PyTorch\|05 Deep learning]] | 8-14 sem | pendiente | | | [ ] |
| [[01-Niveles/05b - Post-training aplicado\|05b Post-training]] | 4-8 sem | pendiente | | | [ ] |
| [[01-Niveles/06 - LLMs aplicados\|06 LLMs aplicados]] | 4-8 sem | pendiente | | | [ ] |
| [[01-Niveles/06b - Context engineering\|06b Context engineering]] | 3-5 sem | pendiente | | | [ ] |
| [[01-Niveles/07 - RAG busqueda embeddings\|07 RAG y busqueda]] | 6-10 sem | pendiente | | | [ ] |
| [[01-Niveles/08 - Agentes workflows automatizacion\|08 Agentes y workflows]] | 6-10 sem | pendiente | | | [ ] |
| [[01-Niveles/08b - MCP y protocolos de herramientas\|08b MCP]] | 2-4 sem | pendiente | | | [ ] |
| [[01-Niveles/09 - Multimodalidad\|09 Multimodalidad]] | 4-10 sem | pendiente | | | [ ] |
| [[01-Niveles/10 - Evaluacion seguridad gobernanza\|10 Evals y gobernanza]] | 4-8 sem | pendiente | | | [ ] |
| [[01-Niveles/10b - Error analysis y evals desde trazas\|10b Error analysis]] | 3-5 sem | pendiente | | | [ ] |
| [[01-Niveles/11 - MLOps LLMOps despliegue\|11 MLOps y despliegue]] | 8-14 sem | pendiente | | | [ ] |
| [[01-Niveles/11b - Inferencia costos y economia unitaria\|11b Inferencia y costos]] | 3-6 sem | pendiente | | | [ ] |
| [[01-Niveles/12 - Profundizacion\|12 Profundizacion]] | abierta | pendiente | | | [ ] |
| [[01-Niveles/12b - Capa profesional\|12b Capa profesional]] | continua | pendiente | | | [ ] |

## Portfolio

Marca cada pieza cuando este publicada con README y demo, no cuando este "casi lista".
Ver [[03-Proyectos/Portfolio minimo]].

- [ ] App con LLM API
- [ ] Automatizacion util
- [ ] App con structured outputs y tool calling
- [ ] RAG con citas y evals
- [ ] Agente con trazas y permisos
- [ ] Deploy con CI/CD, monitoreo y costos
- [ ] Modelo clasico con pipeline reproducible
- [ ] Modelo deep learning con PyTorch
- [ ] Fine-tuning o PEFT
- [ ] [[03-Proyectos/Capstone|Capstone]]

## Revision trimestral

| Trimestre | Horas/sem reales | Ratio construir/leer | Hueco detectado | Ajuste al plan |
| --- | --- | --- | --- | --- |
| T1 | | | | |
| T2 | | | | |
| T3 | | | | |
| T4 | | | | |

## Version con Dataview

Si instalas el plugin comunitario Dataview, esta consulta arma la tabla de niveles sola
a partir del frontmatter y deja de haber dos lugares que actualizar:

```text
TABLE duracion AS "Duracion", estado AS "Estado", inicio AS "Inicio", fin AS "Fin"
FROM "01-Niveles"
SORT file.name ASC
```

Y esta resume las horas registradas en la bitacora:

```text
TABLE semana AS "Semana", nivel AS "Nivel", horas AS "Horas"
FROM "06-Bitacora"
WHERE horas
SORT semana DESC
LIMIT 12
```

Ambas consultas van dentro de un bloque de codigo con el lenguaje `dataview`. Sin el
plugin, la tabla de arriba se mantiene a mano y funciona igual en GitHub.

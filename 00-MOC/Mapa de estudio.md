# Mapa de estudio

La [ruta personal](../02-Rutas/Mi%20ruta%20personal.md) prioriza software con IA y procesos de pymes. El [catálogo](Catalogo%20de%20modulos.md) es la referencia exacta de prerrequisitos; el dibujo agrupa capacidades y no sustituye su secuencia.

```mermaid
flowchart TD
    F["Programación, Git y datos"] --> W["Web y backend"]
    F --> P["Procesos y evaluación"]
    W --> I["Integraciones y SaaS"]
    I --> O["Operación y recuperación"]
    F --> L["LLMs y contexto"]
    P --> A["Automatización evaluada"]
    L --> A
    A --> S["Piloto y servicio"]
    O --> S
```

## Elegir profundidad

| Objetivo | Recorrido |
| --- | --- |
| Construir software con IA y ofrecerlo a pymes | [Ruta personal](../02-Rutas/Mi%20ruta%20personal.md) |
| Incorporar LLMs a software cuya base ya comprendés | Ruta developer o producto |
| Entrenar modelos predictivos | Ruta ML, con datos y matemáticas |
| Consultar documentos propios | Extensión RAG, después de LLMs y evaluación |
| Retomar proyectos físicos | [IA local y robótica opcional](../02-Rutas/IA%20local%20y%20robotica%20opcional.md) |
| Reproducir investigación | Ruta investigación y una subárea elegida |

Mantené un módulo principal y una sola tarea aplicada en curso. Antes de agregar una extensión, anotá el problema que resuelve y su costo de tiempo. El [Canvas](Mapa%20visual.canvas) distingue ruta principal y módulos opcionales en Obsidian.

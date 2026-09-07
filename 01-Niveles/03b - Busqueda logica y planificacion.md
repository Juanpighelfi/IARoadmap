---
id: "03b"
tags: [nivel, fundamentos]
revisado: 2026-09-06
---

# 03b - Búsqueda, lógica y planificación

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://inst.eecs.berkeley.edu/~cs188/archive/fa25/>

Qué estudiar: Clases 2–5: búsqueda, A*, heurísticas y restricciones; clase 6 como introducción a búsqueda adversarial. Usar problemas y soluciones del archivo, no fechas de entrega.

### Diagnóstico breve

Representá una cuadrícula como estados y acciones. Explicá por qué una búsqueda en profundidad puede encontrar un camino más largo. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Resolvé el laboratorio 03: BFS y A* con obstáculos. Compará costo del camino y estados expandidos usando Manhattan y heurística cero.

Práctica ejecutable vinculada: [abrir laboratorio](../07-Laboratorios/03-busqueda-cuadricula/README.md). El [índice](../07-Laboratorios/README.md) reúne los demás. Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Bloqueá la meta y luego cambiá el objetivo. Sumá como ejercicio manual tres variables de color con restricciones de desigualdad y resolvé por backtracking.

### Cómo comprobar que aprendí

Camino válido y óptimo en el caso de costo unitario, ausencia de camino correctamente reportada; justificar admisibilidad y consistencia; formular variables, dominios y restricciones.

Comprobá que podés resolver el ejercicio, explicar el resultado y hacer una variante sin copiar. No hace falta puntuarte ni completar otra plantilla. Se mantienen los criterios técnicos anteriores: no inventar resultados ni usar datos de evaluación para ajustar la solución. Los tests solo comprueban los casos que cubren.

### Si no sale

Si A* pierde optimalidad, revisar costo acumulado frente a prioridad y condición de parada. Si cuesta modelar, dibujar cinco estados y sus sucesores.

### Retención

Cada tanto, retomá una variante sin mirar la solución. Si no sale, anotá ese punto como próximo ejercicio en [Mi seguimiento](../00-MOC/Estado%20actual.md), sin otra planilla ni fechas obligatorias. No hace falta reiniciar el módulo.

## Debes aprender

- Estados, acciones, metas y costos; BFS, Dijkstra y A*.
- Heurísticas admisibles y consistentes; límites de optimalidad.
- Lógica proposicional, reglas, variables, dominios y restricciones.
- Backtracking y comparación entre planificación explícita y decisión de un agente LLM.

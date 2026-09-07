---
id: "04b"
tags: [nivel, fundamentos]
revisado: 2026-09-06
---

# 04b - Incertidumbre, decisiones y aprendizaje por refuerzo

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://inst.eecs.berkeley.edu/~cs188/archive/fa25/>

Qué estudiar: Clases de MDPs y RL (8–11), redes bayesianas (13–16) y HMMs (18–19). Trabajar primero con estados discretos; deep RL queda para una extensión.

### Diagnóstico breve

Diferenciá incertidumbre del sensor, estado oculto y acción. Calculá una actualización de Bellman en un MDP de dos estados. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Resolvé el laboratorio 05 de value iteration. Compará la política óptima con una política fija; repetí con distinta recompensa y descuento. Construí a mano una red bayesiana de defecto y alerta de sensor.

Práctica ejecutable vinculada: [abrir laboratorio](../07-Laboratorios/05-value-iteration/README.md). El [índice](../07-Laboratorios/README.md) reúne los demás. Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Introducí una transición que falla con probabilidad conocida. Explicá cómo cambia la acción elegida; diseñá un experimento Q-learning con semillas y episodios de evaluación separados.

### Rúbrica de salida

Valores y acciones consistentes con Bellman; terminal sin recompensa futura espuria; interpretación de probabilidad condicional; comparación que no usa episodios de entrenamiento como evaluación.

Evaluá cuatro dimensiones: implementación correcta, comparación válida, explicación propia y transferencia a una variante. Cada una: 0 ausente/incorrecta, 1 con ayuda, 2 independiente. **Dominado:** al menos 7/8 y ninguna dimensión en 0; cualquier fuga de test o resultado inventado invalida la comparación. Los tests automáticos acreditan solo los casos que cubren.

### Si no sale

Si las recompensas se cuentan dos veces, escribir una trayectoria paso por paso. Antes de Q-learning resolver el MDP con dinámica conocida.

### Retención

A los 7 días repetí una variante breve sin mirar la solución. A los 30 días reconstruí el razonamiento central. Si no sale, registrá qué olvidaste y volvé al ejercicio correspondiente; no reinicies todo el módulo. Guardá evidencia y fechas en tu [seguimiento personal](../00-MOC/Estado%20actual.md).

## Debes aprender

- Probabilidad condicional, independencia y redes bayesianas.
- Estado oculto, HMM y filtrado como introducción a estimación.
- MDPs, retorno descontado, Bellman, value iteration y policy iteration.
- Q-learning, exploración y evaluación independiente de políticas; deep RL es una extensión.

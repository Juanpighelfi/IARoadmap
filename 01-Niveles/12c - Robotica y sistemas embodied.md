---
id: "12c"
tags: [nivel, especializacion]
revisado: 2026-09-06
---

# 12c - Robótica y sistemas embodied

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://modernrobotics.northwestern.edu/nu-gm-book-resource/>

Qué estudiar: Capítulos 2–4: configuración, transformaciones y cinemática; 11: control; 13: robots móviles. MIT Underactuated y LeRobot son extensiones según proyecto.

### Diagnóstico breve

Diferenciá percepción, estimación, planificación y control. Transformá un punto entre dos marcos 2D y explicá por qué un LLM no debe ser el lazo de control rápido. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Construí una simulación 2D de robot que va a una meta con obstáculos conocidos. Reutilizá A* como planificador y control proporcional limitado; logueá posición, error, acción y tiempo.

Los laboratorios numerados están en el [índice ejecutable](../07-Laboratorios/README.md). Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Agregá ruido de sensor y retardo de un paso. Compará desempeño y fallos con la referencia sin ruido. Solo luego explorar ROS 2 o imitación con datasets de LeRobot.

### Rúbrica de salida

Transformaciones y unidades comprobadas, control acotado, parada por timeout/estado inválido, éxito y fallos medidos en escenarios reservados; distinguir simulación de validación física.

Evaluá cuatro dimensiones: implementación correcta, comparación válida, explicación propia y transferencia a una variante. Cada una: 0 ausente/incorrecta, 1 con ayuda, 2 independiente. **Dominado:** al menos 7/8 y ninguna dimensión en 0; cualquier fuga de test o resultado inventado invalida la comparación. Los tests automáticos acreditan solo los casos que cubren.

### Si no sale

Si oscila, revisar signo, paso temporal y ganancia antes de usar RL. Si colisiona, revisar representación y margen geométrico antes del controlador.

### Retención

A los 7 días repetí una variante breve sin mirar la solución. A los 30 días reconstruí el razonamiento central. Si no sale, registrá qué olvidaste y volvé al ejercicio correspondiente; no reinicies todo el módulo. Guardá evidencia y fechas en tu [seguimiento personal](../00-MOC/Estado%20actual.md).

## Debes aprender

- Marcos de coordenadas, cinemática y estimación de estado.
- Percepción, planificación, control y límites de tiempo real.
- Simulación, ruido, retardo y transferencia a hardware.
- ROS 2, aprendizaje por imitación y modelos visión-lenguaje-acción como extensiones después de una baseline clásica.

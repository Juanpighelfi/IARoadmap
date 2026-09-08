---
id: "12c"
tags: [nivel, especializacion]
revisado: 2026-09-06
---

# 12c - Robótica y sistemas embodied

[Abrir la hoja de ejercicios 12c, lista para completar](../08-Ejercicios/12c.md). Resolvé ahí el diagnóstico, la práctica y las variantes. Si hay código o laboratorio, la hoja indica qué probar y dónde anotar el resultado.

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://modernrobotics.northwestern.edu/nu-gm-book-resource/>

Qué estudiar: Capítulos 2–4: configuración, transformaciones y cinemática; 11: control; 13: robots móviles. MIT Underactuated y LeRobot son extensiones según proyecto.

### Diagnóstico breve

Diferenciá percepción, estimación, planificación y control. Transformá un punto entre dos marcos 2D y explicá por qué un LLM no debe ser el lazo de control rápido. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Construí una simulación 2D de robot que va a una meta con obstáculos conocidos. Reutilizá A* como planificador y control proporcional limitado; logueá posición, error, acción y tiempo.

Los laboratorios numerados están en el [índice ejecutable](../07-Laboratorios/README.md). La hoja de este módulo reúne los espacios de respuesta; las referencias amplían el procedimiento.

### Práctica independiente

Agregá ruido de sensor y retardo de un paso. Compará desempeño y fallos con la referencia sin ruido. Solo luego explorar ROS 2 o imitación con datasets de LeRobot.

### Cómo comprobar que aprendí

Transformaciones y unidades comprobadas, control acotado, parada por timeout/estado inválido, éxito y fallos medidos en escenarios reservados; distinguir simulación de validación física.

Comprobá que podés resolver el ejercicio, explicar el resultado y hacer una variante sin copiar. No hace falta puntuarte ni completar otra plantilla. Se mantienen los criterios técnicos anteriores: no inventar resultados ni usar datos de evaluación para ajustar la solución. Los tests solo comprueban los casos que cubren.

### Si no sale

Si oscila, revisar signo, paso temporal y ganancia antes de usar RL. Si colisiona, revisar representación y margen geométrico antes del controlador.

### Retención

Cada tanto, retomá una variante sin mirar la solución. Si no sale, anotá ese punto como próximo ejercicio en [Mi seguimiento](../00-MOC/Estado%20actual.md), sin otra planilla ni fechas obligatorias. No hace falta reiniciar el módulo.

## Debes aprender

- Marcos de coordenadas, cinemática y estimación de estado.
- Percepción, planificación, control y límites de tiempo real.
- Simulación, ruido, retardo y transferencia a hardware.
- ROS 2, aprendizaje por imitación y modelos visión-lenguaje-acción como extensiones después de una baseline clásica.

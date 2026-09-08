---
id: "05"
tags: [nivel, fundamentos]
revisado: 2026-09-06
---

# 05 - Deep learning y PyTorch

[Abrir la hoja de ejercicios 05, lista para completar](../08-Ejercicios/05.md). Resolvé ahí el diagnóstico, la práctica y las variantes. Si hay código o laboratorio, la hoja indica qué probar y dónde anotar el resultado.

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://d2l.ai/>

Qué estudiar: Capítulos 2, 3, 5, 7 y secciones 11.1, 11.5–11.7: tensores, regresión, MLP, CNN y atención. Usar implementación PyTorch; no estudiar todas las arquitecturas.

### Diagnóstico breve

Escribí un training loop corto y señalá dónde van train/eval, zero_grad, backward y el optimizador. Explicá las dimensiones de un batch. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Entrená un MLP pequeño en un dataset incorporado y comprobá que puede sobreajustar 20 ejemplos. Después separá train/validación y guardá/cargá un checkpoint.

Los laboratorios numerados están en el [índice ejecutable](../07-Laboratorios/README.md). La hoja de este módulo reúne los espacios de respuesta; las referencias amplían el procedimiento.

### Práctica independiente

Desactivá regularización o cambiá el learning rate y predecí el efecto antes de correr. Compará varias semillas y explicá una curva que no aprende.

### Cómo comprobar que aprendí

Checkpoint reproduce predicciones dentro de tolerancia; separación de datos intacta; curvas registradas; diferencia entre error de datos, optimización y generalización explicada.

Comprobá que podés resolver el ejercicio, explicar el resultado y hacer una variante sin copiar. No hace falta puntuarte ni completar otra plantilla. Se mantienen los criterios técnicos anteriores: no inventar resultados ni usar datos de evaluación para ajustar la solución. Los tests solo comprueban los casos que cubren.

### Si no sale

Si no puede sobreajustar 20 casos, revisar etiquetas, shapes, gradientes y modo del modelo antes de aumentar la red.

### Retención

Cada tanto, retomá una variante sin mirar la solución. Si no sale, anotá ese punto como próximo ejercicio en [Mi seguimiento](../00-MOC/Estado%20actual.md), sin otra planilla ni fechas obligatorias. No hace falta reiniciar el módulo.

## Debes aprender

- Tensores, autograd, training loop, optimizadores, regularizacion.
- MLPs, CNNs, embeddings, secuencias y atencion.
- Transfer learning.
- PyTorch datasets, dataloaders, checkpoints y mixed precision.
- Debugging: underfitting, overfitting, exploding gradients, data bugs.
- GPU basics: memoria, batch size, throughput.

## Práctica adicional opcional

La práctica guiada y la variante de arriba constituyen el ciclo principal. Elegí una de estas extensiones solo si aporta; no se suman todas al rango de horas.

- Clasificador de imagenes con transfer learning.
- Modelo de texto pequeno con embeddings.
- Experimentos con tracking y reporte de resultados.

## Referencias adicionales

Consulta estas fuentes solo si el recurso principal no alcanza; no son una lista de cursos obligatorios.

- fast.ai Practical Deep Learning: <https://course.fast.ai/>
- PyTorch tutorials: <https://pytorch.org/tutorials/>
- Dive into Deep Learning: <https://d2l.ai/>
- Stanford CS231n notes: <https://cs231n.github.io/>
- Andrej Karpathy, Neural Networks Zero to Hero: <https://karpathy.ai/zero-to-hero.html>
- Sebastian Raschka, Build a Large Language Model (From Scratch):
  <https://github.com/rasbt/LLMs-from-scratch>

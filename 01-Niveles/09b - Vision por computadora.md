---
id: "09b"
tags: [nivel, especializacion]
revisado: 2026-09-06
---

# 09b - Visión por computadora

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://cs231n.github.io/>

Qué estudiar: Image classification, linear classifiers, optimization, convolutional networks y transfer learning. Detección y segmentación se introducen como tareas distintas con métricas propias.

### Diagnóstico breve

Explicá por qué dos fotos de la misma pieza en train y test inflan la evaluación y cuándo clasificación no localiza el defecto. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Seguí el proyecto de inspección visual: manifest por pieza, split por pieza y sesión, baseline de atributos simples y transfer learning. Empezar con una familia de pieza y un defecto visible.

Los laboratorios numerados están en el [índice ejecutable](../07-Laboratorios/README.md). Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Reservá una sesión con iluminación distinta. Compará resultados por material, fondo e iluminación; para localización anotá cajas o máscaras y elegí IoU/mAP según tarea.

### Cómo comprobar que aprendí

Evaluación en piezas no usadas al entrenar, errores por segmento, rechazo de imágenes fuera de alcance y comparación honesta con baseline; si faltan datos reales, acreditar solo el prototipo.

Comprobá que podés resolver el ejercicio, explicar el resultado y hacer una variante sin copiar. No hace falta puntuarte ni completar otra plantilla. Se mantienen los criterios técnicos anteriores: no inventar resultados ni usar datos de evaluación para ajustar la solución. Los tests solo comprueban los casos que cubren.

### Si no sale

Si aprende el fondo, cruzar fondo y clase en nuevas capturas. Si hay pocas piezas, informar incertidumbre y recolectar variedad antes de aumentar arquitectura.

### Retención

Cada tanto, retomá una variante sin mirar la solución. Si no sale, anotá ese punto como próximo ejercicio en [Mi seguimiento](../00-MOC/Estado%20actual.md), sin otra planilla ni fechas obligatorias. No hace falta reiniciar el módulo.

## Debes aprender

- Clasificación, detección y segmentación: distintas etiquetas y métricas.
- Transfer learning, augmentations y particiones por objeto/sesión.
- Iluminación, materiales, cambio de dominio y sesgos del fondo.
- Embeddings visuales, autoencoders y difusión como panorama de modelos generativos; profundizar solo si el proyecto lo necesita.

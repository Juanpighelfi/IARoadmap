---
id: "03"
tags: [nivel, fundamentos]
revisado: 2026-09-06
---

# 03 - Matematicas para ML

[Abrir la hoja de ejercicios 03, lista para completar](../08-Ejercicios/03.md). Resolvé ahí el diagnóstico, la práctica y las variantes. Si hay código o laboratorio, la hoja indica qué probar y dónde anotar el resultado.

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://mml-book.github.io/>

Qué estudiar: Capítulos 2 y 3: vectores y geometría; 5: derivadas; 6: probabilidad; 7: optimización; 9: regresión como aplicación. Descomposiciones del 4 después de proyecciones.

### Diagnóstico breve

Calculá a mano el gradiente de una pérdida cuadrática con dos observaciones, las dimensiones de Xw y una probabilidad condicional sencilla. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Resolvé el laboratorio 02 de gradientes. Derivá primero la fórmula, contrastala por diferencias finitas y explicá el efecto de cambiar la escala de x.

Práctica ejecutable vinculada: [abrir laboratorio](../07-Laboratorios/02-gradiente-lineal/README.md). El [índice](../07-Laboratorios/README.md) reúne los demás. La hoja de este módulo reúne los espacios de respuesta; las referencias amplían el procedimiento.

### Práctica independiente

Repetí con intercepto no nulo y entradas negativas. Mostrá una tasa de aprendizaje que reduzca la pérdida y una que no sea estable.

### Cómo comprobar que aprendí

Gradiente analítico y numérico concuerdan con tolerancia declarada; dimensiones correctas; Bayes aplicado con denominador; pérdida y métrica distinguidas.

Comprobá que podés resolver el ejercicio, explicar el resultado y hacer una variante sin copiar. No hace falta puntuarte ni completar otra plantilla. Se mantienen los criterios técnicos anteriores: no inventar resultados ni usar datos de evaluación para ajustar la solución. Los tests solo comprueban los casos que cubren.

### Si no sale

Si falla el gradiente, separar derivada escalar y regla de la cadena. Si falla probabilidad, dibujar una tabla de contingencia antes de usar notación.

### Retención

Cada tanto, retomá una variante sin mirar la solución. Si no sale, anotá ese punto como próximo ejercicio en [Mi seguimiento](../00-MOC/Estado%20actual.md), sin otra planilla ni fechas obligatorias. No hace falta reiniciar el módulo.

Conectá notación y derivaciones con decisiones. Para investigación, agregá las demostraciones y ejercicios que pida la subárea; la intuición por sí sola no acredita rigor.

## Debes aprender

- Algebra lineal: vectores, matrices, producto punto, norma, proyecciones, SVD/PCA intuitivo.
- Calculo: derivadas, gradientes, regla de la cadena, optimizacion.
- Probabilidad: distribuciones, esperanza, Bayes, incertidumbre.
- Estadistica: estimacion, generalizacion, varianza, tests, intervalos.
- Informacion: entropia, cross-entropy, KL divergence a nivel intuitivo.

## Práctica adicional opcional

La práctica guiada y la variante de arriba constituyen el ciclo principal. Elegí una de estas extensiones solo si aporta; no se suman todas al rango de horas.

- Implementar regresion lineal y logistica con NumPy.
- Visualizar descenso de gradiente.
- Explicar por que una metrica puede mejorar mientras el producto empeora.

## Referencias adicionales

Consulta estas fuentes solo si el recurso principal no alcanza; no son una lista de cursos obligatorios.

- 3Blue1Brown Linear Algebra: <https://www.3blue1brown.com/topics/linear-algebra>
- Mathematics for Machine Learning: <https://mml-book.github.io/>
- StatQuest: <https://www.youtube.com/user/joshstarmer>
- 3Blue1Brown, Essence of Calculus: <https://www.3blue1brown.com/topics/calculus>
- Andrej Karpathy, Neural Networks Zero to Hero (micrograd es la mejor puerta entre
  este nivel y el 05): <https://karpathy.ai/zero-to-hero.html>

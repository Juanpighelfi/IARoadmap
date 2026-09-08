---
id: "01"
tags: [nivel, fundamentos]
revisado: 2026-09-07
---

# 01 - Programación, Git y entorno

[Abrir la hoja de ejercicios 01, lista para completar](../08-Ejercicios/01.md). Resolvé ahí el diagnóstico, la práctica y las variantes. Si hay código o laboratorio, la hoja indica qué probar y dónde anotar el resultado.

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

## Camino principal: JavaScript, TypeScript y Node.js

Para estudiar el SaaS, este camino sustituye al de Python de abajo; no se cursan ambos completos en paralelo. El archivo conserva su nombre histórico para no romper enlaces. En ambos caminos comprobás lo mismo: resolver, explicar y adaptar el ejercicio del lenguaje elegido, sin puntajes.

Usá [MDN Learn](https://developer.mozilla.org/en-US/docs/Learn_web_development), sección JavaScript: variables, tipos, condicionales, bucles, funciones, objetos y arrays. Después [Node.js Learn](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs) para ejecutar scripts, módulos y asincronía; y [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) para parámetros, objetos, uniones y valores opcionales. Seleccioná lecturas para el ejercicio activo, no tres cursos completos.

El SaaS declara Node 22 o posterior y usa TypeScript con ESM. Conservá lockfiles y herramientas; no actualizar dependencias para estudiar. Los comandos Python del README de IARoadmap validan el material, no prueban el SaaS.

### Diagnóstico para el SaaS

Escribir una función que decida si un turno cabe en una franja, expresando los tiempos en minutos desde medianoche. En una franja 540–720, inicio 675 y duración 45 cabe; inicio 690 y duración 45 no. Explicar entrada, salida, límites y un dato inválido sin ayuda.

### Práctica guiada en TypeScript

1. Empezar en JavaScript con una función de cuatro parámetros: inicio y fin de franja, inicio del turno y duración.
2. Para este ejercicio, exigir enteros entre 0 y 1440, duración positiva y franja con inicio menor que fin; devolver `false` para una entrada inválida. No asumir que la función del producto usa ese mismo contrato.
3. Escribir casos antes de ejecutar: inicio exacto, fin exacto, desborde, duración cero y valor no numérico.
4. Agregar una lista de franjas y comprobar si alguna admite el turno.
5. Tipar parámetros y salida en TypeScript. Explicar por qué los datos externos siguen necesitando validación en ejecución.
6. Comparar con la función y los tests existentes en [Estudiar con el SaaS real](../03-Proyectos/Estudiar%20con%20el%20SaaS%20real.md). No reemplazar código del producto por la versión didáctica.

Después, leer una lista JSON ficticia desde un archivo y producir un resumen de turnos válidos e inválidos. Practicar Git con una rama y un diff de la copia de aprendizaje.

### Variante y cierre del camino TypeScript

Agregar modalidad presencial/virtual, archivo ausente y JSON malformado. Documentar qué error detiene el script. Conservar función, pruebas y comando con el código; explicar la solución y resolver una variante independiente. No hace falta una ficha de evaluación. Cada tanto, retomar una variante. Si algo falla, volver al concepto específico sin reiniciar toda la ruta.

Esta práctica es una consigna, no un laboratorio nuevo con autocorrección ya incluida. No requiere conectar PostgreSQL, Redis, WhatsApp ni un modelo.

## Camino Python: especializaciones y laboratorios existentes

Para ML, investigación o robótica, conservar el recorrido siguiente. Acreditar fundamentos en TypeScript no acredita manejo de Python: demostrar esa habilidad antes de cursar ejercicios que dependan de ella. Si se agrega este camino después, recalcular horas; no está incluido como segundo curso completo en el mismo rango.

**Recurso principal de este camino:** <https://cs50.harvard.edu/python/>

Qué estudiar: Funciones y variables, condicionales, bucles, excepciones, archivos y pruebas; OOP solo después de la CLI. Hacer ejercicios seleccionados, no completar dos cursos a la vez.

### Diagnóstico breve

En 30 minutos, escribí una función que lea filas válidas de un CSV, rechace datos inválidos y produzca un total. Corré una prueba y explicá un diff. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Resolvé el laboratorio 01 del índice de laboratorios: validación de datos sintéticos de piezas. Agregá una CLI que reciba la ruta del archivo y un README con el comando exacto.

Práctica ejecutable vinculada: [abrir laboratorio](../07-Laboratorios/01-python-csv/README.md). El [índice](../07-Laboratorios/README.md) reúne los demás. La hoja de este módulo reúne los espacios de respuesta; las referencias amplían el procedimiento.

### Práctica independiente

Procesá un archivo con columnas reordenadas, una fila vacía y un valor negativo. Elegí y documentá qué errores frenan todo y cuáles se reportan por fila.

### Cómo comprobar que aprendí

Pruebas del laboratorio aprobadas; ejecución desde una carpeta nueva; errores explicados sin ocultarlos; implementación esencial reproducida sin asistente.

Comprobá que podés resolver el ejercicio, explicar el resultado y hacer una variante sin copiar. No hace falta puntuarte ni completar otra plantilla. Se mantienen los criterios técnicos anteriores: no inventar resultados ni usar datos de evaluación para ajustar la solución. Los tests solo comprueban los casos que cubren.

### Si no sale

Si fallan casos borde, hacé primero funciones pequeñas sin archivos; si falla el entorno, recreá un venv y documentá la versión de Python.

### Retención

Cada tanto, retomá una variante sin mirar la solución. Si no sale, anotá ese punto como próximo ejercicio en [Mi seguimiento](../00-MOC/Estado%20actual.md), sin otra planilla ni fechas obligatorias. No hace falta reiniciar el módulo.

## Habilidades del camino Python

- Terminal: archivos, procesos, variables de entorno, permisos basicos.
- Python: tipos, funciones, clases basicas, modulos, excepciones, testing simple.
- Entornos: venv o uv, dependencias, notebooks y scripts.
- Git: commit, branch, diff, pull request, README.
- APIs: HTTP, JSON, autenticacion, rate limits.
- Bases de software: logging, configuracion, errores, estructura de proyecto.

## Práctica adicional opcional

La práctica guiada y la variante de arriba constituyen el ciclo principal. Elegí una de estas extensiones solo si aporta; no se suman todas al rango de horas.

- CLI que lee archivos, limpia texto y genera un reporte.
- Script que llama una API publica, guarda resultados y maneja errores.
- Repo con README, tests minimos y entorno reproducible.

## Referencias adicionales

Consulta estas fuentes solo si el recurso principal no alcanza; no son una lista de cursos obligatorios.

- Python Tutorial: <https://docs.python.org/3/tutorial/>
- Missing Semester: <https://missing.csail.mit.edu/>
- Git Book: <https://git-scm.com/book/en/v2>
- FastAPI docs: <https://fastapi.tiangolo.com/>

---
id: "01"
tags: [nivel, fundamentos]
revisado: 2026-09-06
---

# 01 - Computacion, Python, Git y entorno

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://cs50.harvard.edu/python/>

Qué estudiar: Funciones y variables, condicionales, bucles, excepciones, archivos y pruebas; OOP solo después de la CLI. Hacer ejercicios seleccionados, no completar dos cursos a la vez.

### Diagnóstico breve

En 30 minutos, escribí una función que lea filas válidas de un CSV, rechace datos inválidos y produzca un total. Corré una prueba y explicá un diff. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Resolvé el laboratorio 01 del índice de laboratorios: validación de datos sintéticos de piezas. Agregá una CLI que reciba la ruta del archivo y un README con el comando exacto.

Práctica ejecutable vinculada: [abrir laboratorio](../07-Laboratorios/01-python-csv/README.md). El [índice](../07-Laboratorios/README.md) reúne los demás. Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Procesá un archivo con columnas reordenadas, una fila vacía y un valor negativo. Elegí y documentá qué errores frenan todo y cuáles se reportan por fila.

### Rúbrica de salida

Pruebas del laboratorio aprobadas; ejecución desde una carpeta nueva; errores explicados sin ocultarlos; implementación esencial reproducida sin asistente.

Evaluá cuatro dimensiones: implementación correcta, comparación válida, explicación propia y transferencia a una variante. Cada una: 0 ausente/incorrecta, 1 con ayuda, 2 independiente. **Dominado:** al menos 7/8 y ninguna dimensión en 0; cualquier fuga de test o resultado inventado invalida la comparación. Los tests automáticos acreditan solo los casos que cubren.

### Si no sale

Si fallan casos borde, hacé primero funciones pequeñas sin archivos; si falla el entorno, recreá un venv y documentá la versión de Python.

### Retención

A los 7 días repetí una variante breve sin mirar la solución. A los 30 días reconstruí el razonamiento central. Si no sale, registrá qué olvidaste y volvé al ejercicio correspondiente; no reinicies todo el módulo. Guardá evidencia y fechas en tu [seguimiento personal](../00-MOC/Estado%20actual.md).

## Debes aprender

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

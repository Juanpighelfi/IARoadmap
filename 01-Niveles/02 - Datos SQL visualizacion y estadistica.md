---
id: "02"
tags: [nivel, fundamentos]
revisado: 2026-09-06
---

# 02 - Datos, SQL, visualizacion y estadistica practica

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://pandas.pydata.org/docs/getting_started/intro_tutorials/>

Qué estudiar: Lectura de tablas, selección, columnas derivadas, estadísticas, reshape y combinación; practicar JOIN y GROUP BY en SQLite de Python.

### Diagnóstico breve

Dadas dos tablas con un ID repetido, predecí cuántas filas devuelve el join y por qué una media podría quedar sesgada. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Tomá las filas sintéticas del laboratorio 01 y creá dos tablas SQLite: piezas e inspecciones. Consultá conteos por material y piezas sin inspección; registrá duplicados y ausentes.

Práctica ejecutable vinculada: [abrir laboratorio](../07-Laboratorios/01-python-csv/README.md). El [índice](../07-Laboratorios/README.md) reúne los demás. Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Agregá dos inspecciones de la misma pieza. Recalculá tasa de defectos por imagen y por pieza y explicá la diferencia.

### Rúbrica de salida

El reporte identifica unidad de análisis, denominador, ausentes y duplicados; entrega consulta SQL, gráfico legible y una conclusión con límites.

Evaluá cuatro dimensiones: implementación correcta, comparación válida, explicación propia y transferencia a una variante. Cada una: 0 ausente/incorrecta, 1 con ayuda, 2 independiente. **Dominado:** al menos 7/8 y ninguna dimensión en 0; cualquier fuga de test o resultado inventado invalida la comparación. Los tests automáticos acreditan solo los casos que cubren.

### Si no sale

Si cambia la conclusión al duplicar filas, repasar cardinalidad de joins y muestreo. No entrenar hasta fijar la unidad de análisis.

### Retención

A los 7 días repetí una variante breve sin mirar la solución. A los 30 días reconstruí el razonamiento central. Si no sale, registrá qué olvidaste y volvé al ejercicio correspondiente; no reinicies todo el módulo. Guardá evidencia y fechas en tu [seguimiento personal](../00-MOC/Estado%20actual.md).

## Debes aprender

- Pandas, NumPy, limpieza de datos, joins, missing values, tipos.
- SQL: SELECT, JOIN, GROUP BY, ventanas basicas.
- Visualizacion: distribuciones, outliers, correlaciones, series temporales.
- Estadistica practica: media, varianza, intervalos, muestreo, sesgo, leakage.
- Experimentacion: metricas, A/B testing basico, errores comunes.

## Práctica adicional opcional

La práctica guiada y la variante de arriba constituyen el ciclo principal. Elegí una de estas extensiones solo si aporta; no se suman todas al rango de horas.

- Analizar un dataset publico y guardar un notebook limpio.
- Crear un dashboard simple.
- Escribir un reporte: pregunta, datos, limpieza, hallazgos, limites.

## Referencias adicionales

Consulta estas fuentes solo si el recurso principal no alcanza; no son una lista de cursos obligatorios.

- Kaggle Learn: <https://www.kaggle.com/learn>
- Pandas docs: <https://pandas.pydata.org/docs/>
- Mode SQL Tutorial: <https://mode.com/sql-tutorial/>
- Seeing Theory: <https://seeing-theory.brown.edu/>

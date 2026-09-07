---
id: "02"
tags: [nivel, fundamentos]
revisado: 2026-09-06
---

# 02 - Datos, SQL, visualizacion y estadistica practica

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal de la ruta personal:** [tutorial de PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html). Para la rama de análisis con Python, se conservan los [tutoriales de Pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/). Elegí un camino; no sumes ambos al módulo.

Qué estudiar para el SaaS: tablas, tipos, claves, SELECT, JOIN, GROUP BY, valores ausentes, transacciones y cardinalidad. Escribir primero SQL sobre datos ficticios y después reconocer su equivalente en Drizzle. La alternativa Python usa lectura y combinación de tablas con Pandas/SQLite.

### Aplicación en la ruta personal

Usá el reporte administrativo de las [prácticas SaaS](../07-Laboratorios/Practicas%20SaaS.md) como práctica principal en lugar del caso de piezas de abajo. Crear tablas de profesionales, turnos y cobros ficticios. Consultar pendientes por profesional y turnos sin cobro; comprobar importes, duplicados y valores ausentes.

Para la variante, agregar dos pagos parciales a un turno y explicar por qué un JOIN puede duplicar su importe esperado. Distinguir cantidad de turnos de cantidad de pagos, calcular proporción de turnos pagados con denominador explícito y graficar cobros por profesional. Usar las mismas condiciones de salida; no sumar ambos proyectos como obligación.

El [mapa del SaaS real](../03-Proyectos/Estudiar%20con%20el%20SaaS%20real.md) enlaza el esquema existente. PostgreSQL y Drizzle son la aplicación principal; Pandas, NumPy y el caso de piezas de abajo quedan para la rama de análisis, no como prerrequisito del backend.

### Diagnóstico breve

Dadas dos tablas con un ID repetido, predecí cuántas filas devuelve el join y por qué una media podría quedar sesgada. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Tomá las filas sintéticas del laboratorio 01 y creá dos tablas SQLite: piezas e inspecciones. Consultá conteos por material y piezas sin inspección; registrá duplicados y ausentes.

Práctica ejecutable vinculada: [abrir laboratorio](../07-Laboratorios/01-python-csv/README.md). El [índice](../07-Laboratorios/README.md) reúne los demás. Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Agregá dos inspecciones de la misma pieza. Recalculá tasa de defectos por imagen y por pieza y explicá la diferencia.

### Cómo comprobar que aprendí

El reporte identifica unidad de análisis, denominador, ausentes y duplicados; entrega consulta SQL, gráfico legible y una conclusión con límites.

Comprobá que podés resolver el ejercicio, explicar el resultado y hacer una variante sin copiar. No hace falta puntuarte ni completar otra plantilla. Se mantienen los criterios técnicos anteriores: no inventar resultados ni usar datos de evaluación para ajustar la solución. Los tests solo comprueban los casos que cubren.

### Si no sale

Si cambia la conclusión al duplicar filas, repasar cardinalidad de joins y muestreo. No entrenar hasta fijar la unidad de análisis.

### Retención

Cada tanto, retomá una variante sin mirar la solución. Si no sale, anotá ese punto como próximo ejercicio en [Mi seguimiento](../00-MOC/Estado%20actual.md), sin otra planilla ni fechas obligatorias. No hace falta reiniciar el módulo.

## Debes aprender

- Limpieza de datos, joins, valores ausentes y tipos; Pandas/NumPy solo en el camino Python.
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

---
id: "10b"
tags: [nivel, transversal]
revisado: 2026-09-06
---

# 10b - Análisis de errores y evaluación desde trazas

[Abrir la hoja de ejercicios 10b, lista para completar](../08-Ejercicios/10b.md). Resolvé ahí el diagnóstico, la práctica y las variantes. Si hay código o laboratorio, la hoja indica qué probar y dónde anotar el resultado.

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://hamel.dev/blog/posts/field-guide/>

Qué estudiar: Lectura de trazas, taxonomía y evaluación dirigida por errores. Aplicar a pruebas propias o sesiones personales si no hay tráfico de usuarios.

### Aplicación en tu ruta personal

Retomá las consultas administrativas del [SaaS](../03-Proyectos/SaaS%20administrativo%20con%20IA.md). Una traza registra ID ficticio, entrada, etiqueta esperada, salida, validación, decisión de revisión, herramienta intentada, versión y latencia. Analizá los casos de desarrollo completos, agrupá causas y elegí una corrección por frecuencia y severidad. Conservá el conjunto reservado para el resultado final.

Podés ampliar la muestra de desarrollo a 30–50 interacciones si hace falta; no es obligatorio duplicar las prácticas de 06 y 08. Si hay menos casos, usá todos e indicá la limitación. Los datos sintéticos solo prueban ese escenario; no son tráfico real.

Para la especialización opcional de visión, usar registros por imagen con pieza, sesión, etiqueta, predicción y latencia, separando errores por iluminación o defecto. Usar las mismas condiciones de salida sobre esa evidencia sin cursar también el proyecto de conversaciones.

### Diagnóstico breve

Leé tres fallos completos y separá síntoma de causa; indicá qué dato falta para confirmar tu hipótesis. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Generá 30–50 interacciones propias o simuladas identificadas como tales. Anotá fallos, agrupá causas y elegí una por frecuencia y severidad; no necesitás otros estudiantes.

Los laboratorios numerados están en el [índice ejecutable](../07-Laboratorios/README.md). La hoja de este módulo reúne los espacios de respuesta; las referencias amplían el procedimiento.

### Práctica independiente

Repetí una muestra aleatoria distinta después del cambio, conservando los casos iniciales como regresión. Mostrá también un caso que todavía falla.

### Cómo comprobar que aprendí

Taxonomía con conteos y procedencia, cambio verificable y cobertura conocida; no llamar tráfico real a datos simulados.

Comprobá que podés resolver el ejercicio, explicar el resultado y hacer una variante sin copiar. No hace falta puntuarte ni completar otra plantilla. Se mantienen los criterios técnicos anteriores: no inventar resultados ni usar datos de evaluación para ajustar la solución. Los tests solo comprueban los casos que cubren.

### Si no sale

Si faltan trazas, instrumentar primero. Si la categoría es demasiado amplia, separar recuperación, razonamiento, herramientas y formato.

### Retención

Cada tanto, retomá una variante sin mirar la solución. Si no sale, anotá ese punto como próximo ejercicio en [Mi seguimiento](../00-MOC/Estado%20actual.md), sin otra planilla ni fechas obligatorias. No hace falta reiniciar el módulo.

[10 - Evaluacion seguridad gobernanza](10%20-%20Evaluacion%20seguridad%20gobernanza.md) ensena el bucle hacia adelante: escribis
casos, medis, bloqueas el deploy si baja la calidad. Este nivel ensena el bucle hacia
atras, que es el que usan los equipos que mejoran de verdad: **mirar lo que paso, armar
una taxonomia de fallas y recien entonces escribir los evals que importan**.

La diferencia practica: un eval harness escrito desde la imaginacion mide los errores
que vos supusiste. Uno escrito desde trazas mide los errores que tu sistema comete.

## Debes aprender

- Mirar los datos. Suena trivial y es el paso que casi todos saltan: leer 50 a 100
  interacciones completas de uso propio, pruebas o tráfico real, con procedencia identificada, una por una, sin agregar metricas todavia.
- Codificacion abierta: anotar en lenguaje natural que salio mal en cada caso, sin
  categorias previas.
- Codificacion axial: agrupar esas notas en una taxonomia de modos de falla, con
  frecuencia. Comprobá qué categorías explican los errores de tu muestra, sin imponer una cantidad de antemano.
- Priorizacion: frecuencia por severidad. Que arreglar primero y que ignorar a
  proposito.
- De taxonomía a evaluación: por cada modo de falla frecuente, un chequeo automático o una rúbrica manual reproducible. Primero
  deterministas (formato, esquema, presencia de cita, forma de la llamada a
  herramienta); LLM-as-judge solo donde no hay alternativa, y alineado contra tus
  propias etiquetas.
- Alinear al juez: medir el acuerdo con etiquetas humanas propias y revisar discrepancias. El acuerdo no elimina sesgos compartidos; un juez sin calibración no es evidencia suficiente.
- Instrumentacion: que loguear para que esto sea posible. Entrada, salida, contexto
  recuperado, llamadas a herramientas, version de prompt y de modelo, latencia, costo,
  feedback del usuario.
- Muestreo: aleatorio, estratificado por segmento, y dirigido a casos con senal
  negativa. Por que mirar solo las quejas sesga la vision.
- El ciclo completo: trazas, analisis, hipotesis, arreglo, eval que impide la
  regresion, vuelta a produccion.
- Datos sinteticos con criterio: generar variaciones de casos reales para ampliar
  cobertura, sin caer en un set que solo contiene errores imaginarios.
- Privacidad al mirar datos reales: minimizacion, anonimizacion, quien puede ver que.
  Critico si el dominio es sensible. Ver [Regulacion y cumplimiento](../04-Recursos/Regulacion%20y%20cumplimiento.md).

## Práctica adicional opcional

La práctica guiada y la variante de arriba constituyen el ciclo principal. Elegí una de estas extensiones solo si aporta; no se suman todas al rango de horas.

- Instrumentar una app tuya para guardar trazas completas, no solo entrada y salida.
- Leer una muestra inicial de 30–50 trazas propias o simuladas, identificando su procedencia; ampliar si siguen apareciendo modos de falla nuevos.
- Construir la taxonomia de fallas con frecuencias y guardar el gráfico.
- Escribir un eval automatico por cada una de las tres categorias mas frecuentes, y
  medir cuanto de la taxonomia queda cubierto.
- Si usás un juez LLM, validarlo contra una muestra etiquetada por vos. Reportar tamaño y acuerdo. Si es
  bajo, arreglar la rubrica antes que el sistema.
- Cerrar el ciclo: elegir la falla mas frecuente, arreglarla, y demostrar con el eval
  que bajo, sin que suban las otras.

## Advertencia

El error clasico es saltar directo a un dashboard de metricas genericas. Un numero
agregado te dice que algo empeoro; la lectura de trazas y la experimentación te dice que. El dashboard
viene despues de la taxonomia, no antes.

## Referencias adicionales

Consulta estas fuentes solo si el recurso principal no alcanza; no son una lista de cursos obligatorios.

- Hamel Husain, Your AI Product Needs Evals:
  <https://hamel.dev/blog/posts/evals/>
- Hamel Husain, Look at Your Data:
  <https://hamel.dev/blog/posts/field-guide/>
- Arize Phoenix, trazas y evaluacion: <https://phoenix.arize.com/>
- LangSmith docs: <https://docs.smith.langchain.com/>
- RAGAS: <https://docs.ragas.io/>
- OpenTelemetry, convenciones de trazas para GenAI:
  <https://opentelemetry.io/docs/specs/semconv/gen-ai/>

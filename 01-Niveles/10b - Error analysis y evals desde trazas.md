---
id: "10b"
tags: [nivel, transversal]
revisado: 2026-09-06
---

# 10b - Análisis de errores y evaluación desde trazas

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://hamel.dev/blog/posts/field-guide/>

Qué estudiar: Lectura de trazas, taxonomía y evaluación dirigida por errores. Aplicar a pruebas propias o sesiones personales si no hay tráfico de usuarios.

### Aplicación en tu ruta personal

En el proyecto de inspección visual, una traza es un registro por imagen: pieza y sesión, etiqueta real, predicción, confianza, versión del modelo, preprocesamiento y latencia. Analizá 30–50 predicciones propias de validación (o todas si tenés menos), separando errores por iluminación, orientación, tipo de defecto y pieza. Conservá el test reservado para la evaluación final. Si faltan imágenes reales, usá datos sintéticos únicamente para verificar el procedimiento y declaralo.

La práctica guiada y la variante se realizan con estos registros. Los ejemplos de conversaciones, herramientas y jueces LLM que siguen corresponden a la rama opcional de LLM; no hacen falta para completar este módulo en visión.

### Diagnóstico breve

Leé tres fallos completos y separá síntoma de causa; indicá qué dato falta para confirmar tu hipótesis. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Generá 30–50 interacciones propias o simuladas identificadas como tales. Anotá fallos, agrupá causas y elegí una por frecuencia y severidad; no necesitás otros estudiantes.

Los laboratorios numerados están en el [índice ejecutable](../07-Laboratorios/README.md). Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Repetí una muestra aleatoria distinta después del cambio, conservando los casos iniciales como regresión. Mostrá también un caso que todavía falla.

### Rúbrica de salida

Taxonomía con conteos y procedencia, cambio verificable y cobertura conocida; no llamar tráfico real a datos simulados.

Evaluá cuatro dimensiones: implementación correcta, comparación válida, explicación propia y transferencia a una variante. Cada una: 0 ausente/incorrecta, 1 con ayuda, 2 independiente. **Dominado:** al menos 7/8 y ninguna dimensión en 0; cualquier fuga de test o resultado inventado invalida la comparación. Los tests automáticos acreditan solo los casos que cubren.

### Si no sale

Si faltan trazas, instrumentar primero. Si la categoría es demasiado amplia, separar recuperación, razonamiento, herramientas y formato.

### Retención

A los 7 días repetí una variante breve sin mirar la solución. A los 30 días reconstruí el razonamiento central. Si no sale, registrá qué olvidaste y volvé al ejercicio correspondiente; no reinicies todo el módulo. Guardá evidencia y fechas en tu [seguimiento personal](../00-MOC/Estado%20actual.md).

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

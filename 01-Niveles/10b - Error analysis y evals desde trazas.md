---
tags:
  - nivel
  - evals
  - error-analysis
  - datos
duracion: 3-5 semanas
estado: pendiente
inicio:
fin:
---

# 10b - Error analysis y evals desde datos reales

[[10 - Evaluacion seguridad gobernanza]] ensena el bucle hacia adelante: escribis
casos, medis, bloqueas el deploy si baja la calidad. Este nivel ensena el bucle hacia
atras, que es el que usan los equipos que mejoran de verdad: **mirar lo que paso, armar
una taxonomia de fallas y recien entonces escribir los evals que importan**.

La diferencia practica: un eval harness escrito desde la imaginacion mide los errores
que vos supusiste. Uno escrito desde trazas mide los errores que tu sistema comete.

## Debes aprender

- Mirar los datos. Suena trivial y es el paso que casi todos saltan: leer 50 a 100
  interacciones reales completas, una por una, sin agregar metricas todavia.
- Codificacion abierta: anotar en lenguaje natural que salio mal en cada caso, sin
  categorias previas.
- Codificacion axial: agrupar esas notas en una taxonomia de modos de falla, con
  frecuencia. Casi siempre 3 o 4 categorias explican la mayoria de los errores.
- Priorizacion: frecuencia por severidad. Que arreglar primero y que ignorar a
  proposito.
- De taxonomia a eval: por cada modo de falla frecuente, un chequeo automatico. Primero
  deterministas (formato, esquema, presencia de cita, forma de la llamada a
  herramienta); LLM-as-judge solo donde no hay alternativa, y alineado contra tus
  propias etiquetas.
- Alinear al juez: medir el acuerdo entre el juez automatico y tu criterio humano sobre
  un set etiquetado. Un juez que no valida contra vos no mide nada.
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
  Critico si el dominio es sensible. Ver [[04-Recursos/Regulacion y cumplimiento]].

## Practica

- Instrumentar una app tuya para guardar trazas completas, no solo entrada y salida.
- Leer 100 trazas a mano y anotarlas en una planilla. Sin excepciones, sin muestrear a
  ojo. Este ejercicio es el nivel entero.
- Construir la taxonomia de fallas con frecuencias y publicar el grafico.
- Escribir un eval automatico por cada una de las tres categorias mas frecuentes, y
  medir cuanto de la taxonomia queda cubierto.
- Validar un juez LLM contra 50 casos que etiquetaste vos. Reportar el acuerdo. Si es
  bajo, arreglar la rubrica antes que el sistema.
- Cerrar el ciclo: elegir la falla mas frecuente, arreglarla, y demostrar con el eval
  que bajo, sin que suban las otras.

## Criterio de salida

Podes mostrar la taxonomia de fallas de tu sistema con frecuencias reales, senalar
cual arreglaste y presentar el eval que impide que vuelva.

## Advertencia

El error clasico es saltar directo a un dashboard de metricas genericas. Un numero
agregado te dice que algo empeoro; solo la lectura de trazas te dice que. El dashboard
viene despues de la taxonomia, no antes.

## Recursos

- Hamel Husain, Your AI Product Needs Evals:
  <https://hamel.dev/blog/posts/evals/>
- Hamel Husain, Look at Your Data:
  <https://hamel.dev/blog/posts/field-guide/>
- Arize Phoenix, trazas y evaluacion: <https://phoenix.arize.com/>
- LangSmith docs: <https://docs.smith.langchain.com/>
- RAGAS: <https://docs.ragas.io/>
- OpenTelemetry, convenciones de trazas para GenAI:
  <https://opentelemetry.io/docs/specs/semconv/gen-ai/>

## Siguiente

- [[11 - MLOps LLMOps despliegue]]
- [[11b - Inferencia costos y economia unitaria]]

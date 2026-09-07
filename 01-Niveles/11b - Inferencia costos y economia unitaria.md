---
id: "11b"
tags: [nivel, especializacion]
revisado: 2026-09-06
---

# 11b - Inferencia, latencia y economia unitaria

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://github.com/ggml-org/llama.cpp>

Qué estudiar: README, ejecución de inferencia y herramientas de benchmark; vLLM es referencia opcional para concurrencia en GPU. Medir en el equipo disponible.

### Diagnóstico breve

Diferenciá tiempo al primer token, tiempo total y throughput. Calculá memoria mínima de pesos como parámetros por bits/8 y nombrá costos adicionales. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Ejecutá un conjunto fijo de tareas con un modelo que quepa en tu equipo o una API ya disponible. Medí calentamiento por separado, p50/p95, calidad y costo por tarea completa.

Los laboratorios numerados están en el [índice ejecutable](../07-Laboratorios/README.md). Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Compará dos longitudes de contexto o precisiones con el mismo conjunto. Hacé al menos 30 repeticiones para una primera estimación, reportando tamaño de muestra y variabilidad.

### Cómo comprobar que aprendí

Hardware, runtime, modelo y precisión identificados; resultados sin confundir costo marginal de API con electricidad y tiempo de operación local; ninguna velocidad inventada.

Comprobá que podés resolver el ejercicio, explicar el resultado y hacer una variante sin copiar. No hace falta puntuarte ni completar otra plantilla. Se mantienen los criterios técnicos anteriores: no inventar resultados ni usar datos de evaluación para ajustar la solución. Los tests solo comprueban los casos que cubren.

### Si no sale

Si el benchmark incluye descarga/carga, separar etapas. Si falta memoria, reducir contexto/modelo antes de comprar hardware.

### Retención

Cada tanto, retomá una variante sin mirar la solución. Si no sale, anotá ese punto como próximo ejercicio en [Mi seguimiento](../00-MOC/Estado%20actual.md), sin otra planilla ni fechas obligatorias. No hace falta reiniciar el módulo.

[11 - MLOps LLMOps despliegue](11%20-%20MLOps%20LLMOps%20despliegue.md) menciona costos y GPU como dos vinetas. Merecen un
nivel: en un producto de IA, el costo por tarea y la latencia percibida deciden si el
negocio cierra, y son la primera cosa que un demo exitoso rompe cuando llegan usuarios
de verdad.

## Debes aprender

### Como se mide

- Metricas de latencia de un LLM: tiempo al primer token, tokens por segundo, tiempo
  total. Cual importa segun la interfaz: streaming en un chat, total en un batch.
- Percentiles, no promedios. Por que el p95 es el que define la experiencia.
- Costo por request, por tarea completa y por usuario activo. Una tarea con 12 pasos puede requerir varias llamadas, y eso no aparece en el precio por millon de tokens.
- Presupuesto: definir un techo de costo y latencia por tarea **antes** de construir, y
  tratarlo como un requisito y no como una sorpresa.

### Como se baja

- Eleccion de modelo y routing: modelo chico por defecto, escalada al grande solo
  cuando hace falta, con un criterio medible de cuando.
- Prompt caching: que parte del contexto es estable, como ordenarla, cuanto ahorra.
  Conecta con [06b - Context engineering](06b%20-%20Context%20engineering.md).
- Batching y procesamiento asincronico: que trabajo no necesita respuesta inmediata.
- Streaming: no baja el costo, cambia por completo la latencia percibida.
- Reduccion de contexto: recuperar menos y mejor suele ahorrar mas que cualquier truco
  de infraestructura.
- Destilacion y fine-tuning para bajar de tamano de modelo. Conecta con
  [05b - Post-training aplicado](05b%20-%20Post-training%20aplicado.md).
- Cache de resultados a nivel aplicacion para consultas repetidas.

### Si servis modelos propios

- Cuantizacion: int8, int4, que se degrada y como medirlo.
- KV cache: que es, cuanta memoria ocupa y por que limita el batch size.
- Continuous batching y throughput frente a latencia individual.
- Servidores de inferencia: comparar llama.cpp para modelos compatibles en local con vLLM cuando el hardware y la concurrencia lo justifiquen.
- Decoding especulativo, a nivel de que hace y cuando conviene.
- Dimensionamiento: memoria de GPU necesaria segun parametros y precision, y el calculo
  de cuantos usuarios concurrentes soporta.
- Comprar frente a alquilar frente a API: el punto de equilibrio real, incluyendo el
  costo de operarlo.

## Práctica adicional opcional

La práctica guiada y la variante de arriba constituyen el ciclo principal. Elegí una de estas extensiones solo si aporta; no se suman todas al rango de horas.

- Construir un tablero de costo por tarea para una app tuya, desglosado por paso.
  Identificá qué pasos dominan el costo y medí qué calidad se pierde al simplificarlos.
- Definir un presupuesto de latencia p95 y costo por tarea, e implementar routing entre
  dos modelos para cumplirlo. Medir que perdes en calidad.
- Medir el ahorro real de prompt caching sobre trafico realista, no sobre un caso ideal.
- Servir un modelo abierto chico local y comparar contra la API: calidad, p95, costo
  por 1000 requests y trabajo de operacion.
- Si el runtime lo permite, cuantizar ese modelo y medir el cambio de calidad con el eval de
  [10b - Error analysis y evals desde trazas](10b%20-%20Error%20analysis%20y%20evals%20desde%20trazas.md), no a ojo.
- Escribir la proyeccion: que pasa con tu factura si el uso se multiplica por 100.

## Referencias adicionales

Consulta estas fuentes solo si el recurso principal no alcanza; no son una lista de cursos obligatorios.

- vLLM docs: <https://docs.vllm.ai/>
- Elegir un runtime compatible con el modelo y hardware; comprobar su estado de mantenimiento antes de instalar.
- llama.cpp: <https://github.com/ggml-org/llama.cpp>
- Ollama: <https://ollama.com/>
- Transformer Inference Arithmetic, para el calculo de memoria y throughput:
  <https://kipp.ly/transformer-inference-arithmetic/>
- Chip Huyen, AI Engineering, capitulos de optimizacion de inferencia y costos:
  <https://huyenchip.com/books/>

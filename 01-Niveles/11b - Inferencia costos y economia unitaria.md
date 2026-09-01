---
tags:
  - nivel
  - inferencia
  - costos
  - latencia
duracion: 3-6 semanas
estado: pendiente
inicio:
fin:
---

# 11b - Inferencia, latencia y economia unitaria

[[11 - MLOps LLMOps despliegue]] menciona costos y GPU como dos vinetas. Merecen un
nivel: en un producto de IA, el costo por tarea y la latencia percibida deciden si el
negocio cierra, y son la primera cosa que un demo exitoso rompe cuando llegan usuarios
de verdad.

## Debes aprender

### Como se mide

- Metricas de latencia de un LLM: tiempo al primer token, tokens por segundo, tiempo
  total. Cual importa segun la interfaz: streaming en un chat, total en un batch.
- Percentiles, no promedios. Por que el p95 es el que define la experiencia.
- Costo por request, por tarea completa y por usuario activo. Una tarea con 12 pasos de
  agente cuesta 12 llamadas, y eso no aparece en el precio por millon de tokens.
- Presupuesto: definir un techo de costo y latencia por tarea **antes** de construir, y
  tratarlo como un requisito y no como una sorpresa.

### Como se baja

- Eleccion de modelo y routing: modelo chico por defecto, escalada al grande solo
  cuando hace falta, con un criterio medible de cuando.
- Prompt caching: que parte del contexto es estable, como ordenarla, cuanto ahorra.
  Conecta con [[06b - Context engineering]].
- Batching y procesamiento asincronico: que trabajo no necesita respuesta inmediata.
- Streaming: no baja el costo, cambia por completo la latencia percibida.
- Reduccion de contexto: recuperar menos y mejor suele ahorrar mas que cualquier truco
  de infraestructura.
- Destilacion y fine-tuning para bajar de tamano de modelo. Conecta con
  [[05b - Post-training aplicado]].
- Cache de resultados a nivel aplicacion para consultas repetidas.

### Si servis modelos propios

- Cuantizacion: int8, int4, que se degrada y como medirlo.
- KV cache: que es, cuanta memoria ocupa y por que limita el batch size.
- Continuous batching y throughput frente a latencia individual.
- Servidores de inferencia: vLLM, TGI, llama.cpp para local o edge.
- Decoding especulativo, a nivel de que hace y cuando conviene.
- Dimensionamiento: memoria de GPU necesaria segun parametros y precision, y el calculo
  de cuantos usuarios concurrentes soporta.
- Comprar frente a alquilar frente a API: el punto de equilibrio real, incluyendo el
  costo de operarlo.

## Practica

- Construir un tablero de costo por tarea para una app tuya, desglosado por paso.
  Casi siempre hay un paso que se lleva la mitad y no aporta la mitad del valor.
- Definir un presupuesto de latencia p95 y costo por tarea, e implementar routing entre
  dos modelos para cumplirlo. Medir que perdes en calidad.
- Medir el ahorro real de prompt caching sobre trafico realista, no sobre un caso ideal.
- Servir un modelo abierto chico local y comparar contra la API: calidad, p95, costo
  por 1000 requests y trabajo de operacion.
- Cuantizar ese modelo y medir la degradacion con el eval de
  [[10b - Error analysis y evals desde trazas]], no a ojo.
- Escribir la proyeccion: que pasa con tu factura si el uso se multiplica por 100.

## Criterio de salida

Podes decir cuanto cuesta una tarea de tu sistema, de que pasos se compone ese costo,
cual es tu p95, y que palanca usarias primero si manana tuvieras que bajar el costo a
la mitad sin perder calidad.

## Recursos

- vLLM docs: <https://docs.vllm.ai/>
- Hugging Face Text Generation Inference:
  <https://huggingface.co/docs/text-generation-inference>
- llama.cpp: <https://github.com/ggml-org/llama.cpp>
- Ollama: <https://ollama.com/>
- Transformer Inference Arithmetic, para el calculo de memoria y throughput:
  <https://kipp.ly/transformer-inference-arithmetic/>
- Chip Huyen, AI Engineering, capitulos de optimizacion de inferencia y costos:
  <https://huyenchip.com/books/>

## Siguiente

- [[12 - Profundizacion]]
- [[03-Proyectos/Capstone]]

---
tags:
  - nivel
  - fine-tuning
  - peft
  - post-training
duracion: 4-8 semanas
estado: pendiente
inicio:
fin:
---

# 05b - Post-training aplicado: fine-tuning, LoRA y preferencias

Llena el hueco entre consumir modelos por API ([[06 - LLMs aplicados]]) y construirlos
desde cero ([[12 - Profundizacion]]). El [[03-Proyectos/Portfolio minimo]] pide una
pieza de fine-tuning o PEFT: este es el nivel que la habilita.

Requiere [[05 - Deep learning y PyTorch]]. Sin training loop, dataloaders y debugging
de entrenamiento, un fine-tuning es una receta copiada que no vas a poder diagnosticar
cuando salga mal.

## Primero: cuando NO fine-tunear

Esta seccion va antes que el temario a proposito, porque la respuesta correcta suele
estar aca.

Antes de entrenar, agota en este orden:

1. Mejor prompt y mejores ejemplos en contexto.
2. Structured outputs con validacion y reintentos.
3. Recuperacion ([[07 - RAG busqueda embeddings]]) si el problema es que al modelo le
   falta informacion.
4. Un modelo mas capaz, si el costo lo permite.

Fine-tunear tiene sentido cuando queres **forma**, no **conocimiento**: un formato o un
estilo muy especifico, un dominio con jerga propia, una tarea de clasificacion o
extraccion muy repetida que queres correr barata en un modelo chico, o latencia y costo
que un modelo grande no te da. No sirve para meter hechos nuevos de forma confiable, y
sin evals previos no vas a poder demostrar que mejoro nada.

Regla: si no tenes un eval que corra antes y despues, no estas fine-tuneando, estas
adivinando. Ver [[10 - Evaluacion seguridad gobernanza]].

## Debes aprender

- Panorama del post-training: pretraining, SFT, alineamiento por preferencias,
  destilacion. Que hace cada etapa y con que datos.
- SFT (supervised fine-tuning): formato de datos, plantillas de chat, masking de la
  parte del prompt, empaquetado de secuencias.
- PEFT: LoRA y QLoRA. Que son rank y alpha, a que capas aplicar, cuanta memoria ahorran
  y que se pierde frente a un full fine-tune.
- Optimizacion por preferencias: DPO y variantes. Que forma tienen los datos de pares
  elegido/rechazado y de donde salen.
- Destilacion: usar un modelo grande para generar datos con los que entrenar uno chico.
  Limites legales y de licencia de esa practica.
- Datos: curacion, deduplicacion, contaminacion con el set de evaluacion, datos
  sinteticos y sus riesgos, cuantos ejemplos hacen falta de verdad (suelen ser cientos
  o pocos miles, no millones).
- Evaluacion del resultado: mismo eval antes y despues, y ademas un control de
  regresion sobre capacidades generales para detectar olvido catastrofico.
- Costos: horas de GPU, alquiler frente a API de fine-tuning gestionada, y el costo
  real de mantener un modelo propio cuando salga la proxima version base.
- Despliegue: adaptadores LoRA servidos sobre un modelo base, versionado de pesos y
  rollback. Conecta con [[11 - MLOps LLMOps despliegue]] y
  [[11b - Inferencia costos y economia unitaria]].

## Practica

- Tomar una tarea real donde el prompting ya llego a su techo, medirla con un eval de
  50 casos, y recien entonces fine-tunear. Reportar la diferencia con numeros.
- LoRA sobre un modelo abierto chico para una tarea de extraccion estructurada.
  Comparar contra el mismo modelo con prompting y contra un modelo grande por API:
  calidad, latencia y costo por 1000 requests.
- Construir el dataset a mano: 300 ejemplos curados, con criterio de anotacion escrito
  y revision de duplicados y contaminacion.
- Un experimento de DPO sobre pares de preferencia propios, aunque sea pequeno, para
  entender que los datos de preferencia son el cuello de botella y no el algoritmo.
- Documentar un caso donde el fine-tuning **no** mejoro nada. Es el resultado mas
  instructivo del nivel y va en el informe.

## Criterio de salida

Podes justificar con datos por que fine-tuneaste en lugar de las cuatro alternativas
mas baratas, mostrar la mejora medida sobre un eval fijo, y explicar que capacidad
perdio el modelo a cambio.

## Recursos

- Hugging Face, curso de LLMs y capitulo de fine-tuning:
  <https://huggingface.co/learn/llm-course>
- Hugging Face PEFT docs: <https://huggingface.co/docs/peft>
- Hugging Face TRL, SFT y DPO: <https://huggingface.co/docs/trl>
- Paper LoRA: <https://arxiv.org/abs/2106.09685>
- Paper QLoRA: <https://arxiv.org/abs/2305.14314>
- Paper DPO: <https://arxiv.org/abs/2305.18290>
- Sebastian Raschka sobre fine-tuning y post-training:
  <https://magazine.sebastianraschka.com/>
- Unsloth, recetas practicas de fine-tuning eficiente:
  <https://unsloth.ai/docs>

## Siguiente

- [[06 - LLMs aplicados]]
- [[11b - Inferencia costos y economia unitaria]]
- [[12 - Profundizacion]]

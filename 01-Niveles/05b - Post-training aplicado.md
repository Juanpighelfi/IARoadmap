---
id: "05b"
tags: [nivel, especializacion]
revisado: 2026-09-06
---

# 05b - Post-training aplicado: fine-tuning, LoRA y preferencias

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://huggingface.co/docs/trl/>

Qué estudiar: SFT Trainer y DPO Trainer como consulta; completar primero el experimento SFT. DPO es extensión optativa. Vincular con PEFT solo cuando la memoria lo requiera.

### Diagnóstico breve

Describí una tarea donde faltan hechos y otra donde falla el comportamiento. Diseñá una comparación justa entre prompt y ajuste. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Elegí una tarea de extracción. Curá un conjunto pequeño, separá entrenamiento/validación/test antes de generar variantes, medí prompting y solo entonces ensayá SFT o LoRA si hay presupuesto.

Los laboratorios numerados están en el [índice ejecutable](../07-Laboratorios/README.md). Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Probá formatos o ejemplos fuera de distribución y controles de capacidades generales. Si no entrenás, entregá un estudio de viabilidad con datos y baseline, sin marcar la práctica de entrenamiento como realizada.

### Cómo comprobar que aprendí

Informe de datos, costo, comparación fija y regresiones medidas; aprobar el experimento aunque no haya mejora o pérdida detectable. Para acreditar entrenamiento debe existir una corrida reproducible.

Comprobá que podés resolver el ejercicio, explicar el resultado y hacer una variante sin copiar. No hace falta puntuarte ni completar otra plantilla. Se mantienen los criterios técnicos anteriores: no inventar resultados ni usar datos de evaluación para ajustar la solución. Los tests solo comprueban los casos que cubren.

### Si no sale

Si el eval está contaminado, rehacer split por origen. Si el costo impide el experimento, reducir modelo/dataset o posponer el módulo con motivo.

### Retención

Cada tanto, retomá una variante sin mirar la solución. Si no sale, anotá ese punto como próximo ejercicio en [Mi seguimiento](../00-MOC/Estado%20actual.md), sin otra planilla ni fechas obligatorias. No hace falta reiniciar el módulo.

Llena el hueco entre consumir modelos por API ([06 - LLMs aplicados](06%20-%20LLMs%20aplicados.md)) y construirlos
desde cero ([12 - Profundizacion](12%20-%20Profundizacion.md)). El [Portfolio minimo](../03-Proyectos/Portfolio%20minimo.md) pide una
pieza de fine-tuning o PEFT: este es el nivel que la habilita.

Requiere [05 - Deep learning y PyTorch](05%20-%20Deep%20learning%20y%20PyTorch.md). Sin training loop, dataloaders y debugging
de entrenamiento, un fine-tuning es una receta copiada que no vas a poder diagnosticar
cuando salga mal.

## Primero: cuando NO fine-tunear

Esta seccion va antes que el temario a proposito, porque la respuesta correcta suele
estar aca.

Antes de entrenar, compará las alternativas pertinentes; no todas aplican a todos los problemas:

1. Mejor prompt y mejores ejemplos en contexto.
2. Structured outputs con validacion y reintentos.
3. Recuperacion ([07 - RAG busqueda embeddings](07%20-%20RAG%20busqueda%20embeddings.md)) si el problema es que al modelo le
   falta informacion.
4. Un modelo mas capaz, si el costo lo permite.

Fine-tunear puede adaptar comportamiento, estilo y desempeño en tareas de dominio; para hechos cambiantes, preferí recuperación verificable. Casos útiles: un formato o un
estilo muy especifico, un dominio con jerga propia, una tarea de clasificacion o
extraccion muy repetida que queres correr barata en un modelo chico, o latencia y costo
que un modelo grande no te da. No conviene tratarlo como una base de datos de hechos actualizables; además,
sin evals previos no vas a poder demostrar que mejoro nada.

Regla: si no tenes un eval que corra antes y despues, no estas fine-tuneando, estas
adivinando. Ver [10 - Evaluacion seguridad gobernanza](10%20-%20Evaluacion%20seguridad%20gobernanza.md).

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
  rollback. Conecta con [11 - MLOps LLMOps despliegue](11%20-%20MLOps%20LLMOps%20despliegue.md) y
  [11b - Inferencia costos y economia unitaria](11b%20-%20Inferencia%20costos%20y%20economia%20unitaria.md).

## Práctica adicional opcional

La práctica guiada y la variante de arriba constituyen el ciclo principal. Elegí una de estas extensiones solo si aporta; no se suman todas al rango de horas.

- Tomar una tarea con una limitación observada del prompting, medirla con un eval de
  50 casos, y recien entonces fine-tunear. Reportar la diferencia con numeros.
- LoRA sobre un modelo abierto chico para una tarea de extraccion estructurada.
  Comparar contra el mismo modelo con prompting y contra un modelo grande por API:
  calidad, latencia y costo por 1000 requests.
- Construir un piloto de dataset curado, con criterio de anotación escrito
  y revision de duplicados y contaminacion.
- Extensión opcional: un experimento de DPO sobre pares de preferencia propios para
  entender que los datos de preferencia son el cuello de botella y no el algoritmo.
- Documentar si el fine-tuning mejoró, no cambió o empeoró el resultado; no fabricar un resultado negativo para cumplir una consigna.

## Referencias adicionales

Consulta estas fuentes solo si el recurso principal no alcanza; no son una lista de cursos obligatorios.

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

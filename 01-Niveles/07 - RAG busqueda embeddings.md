---
id: "07"
tags: [nivel, especializacion]
revisado: 2026-09-06
---

# 07 - RAG, busqueda y embeddings

[Abrir la hoja de ejercicios 07, lista para completar](../08-Ejercicios/07.md). Resolvé ahí el diagnóstico, la práctica y las variantes. Si hay código o laboratorio, la hoja indica qué probar y dónde anotar el resultado.

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://qdrant.tech/documentation/>

Qué estudiar: Local Quickstart, Search, Filtering, BM25 y Hybrid Search with Reranking. Construí primero una búsqueda lexical simple; luego seguí el tutorial local para comparar. La documentación es consulta técnica y no sustituye las condiciones de salida del ejercicio.

### Diagnóstico breve

Separá un error de recuperación de uno de generación usando una pregunta y tres documentos. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Indexá diez notas técnicas propias o los módulos del vault. Creá 30 preguntas respondibles y 10 sin respuesta, con documento y fragmento de evidencia. Reservá test antes de ajustar chunking.

Los laboratorios numerados están en el [índice ejecutable](../07-Laboratorios/README.md). La hoja de este módulo reúne los espacios de respuesta; las referencias amplían el procedimiento.

### Práctica independiente

Agregá una nota que contradice una versión anterior y otra sin permisos. Compará búsqueda lexical y semántica con el mismo conjunto.

### Cómo comprobar que aprendí

Recall de documentos y fidelidad de citas evaluados por separado; abstención probada; sin documento retirado o no autorizado entre resultados; variantes elegidas con validación.

Comprobá que podés resolver el ejercicio, explicar el resultado y hacer una variante sin copiar. No hace falta puntuarte ni completar otra plantilla. Se mantienen los criterios técnicos anteriores: no inventar resultados ni usar datos de evaluación para ajustar la solución. Los tests solo comprueban los casos que cubren.

### Si no sale

Si no recupera la evidencia, corregir ingesta y retrieval antes del prompt. Si cita sin sustento, evaluar el fragmento y no solo la URL.

### Retención

Cada tanto, retomá una variante sin mirar la solución. Si no sale, anotá ese punto como próximo ejercicio en [Mi seguimiento](../00-MOC/Estado%20actual.md), sin otra planilla ni fechas obligatorias. No hace falta reiniciar el módulo.

## Debes aprender

- Arquitectura RAG: ingestion, chunking, embeddings, index, retrieval, reranking, generation, citations.
- Busqueda: keyword, BM25, semantic search, hybrid search.
- Vector DBs: Chroma, FAISS, Qdrant, Weaviate, Pinecone u otras.
- Chunking por estructura, metadata, permisos y freshness.
- Evaluacion RAG: retrieval recall, groundedness, answer relevance, citation accuracy.
- Fallos tipicos: contexto insuficiente, chunks malos, duplicados, datos viejos, respuestas sin evidencia.
- Borrado y correccion: como se elimina a una persona o un documento del indice, de los
  duplicados y de los sets de evaluacion. Ver [Regulacion y cumplimiento](../04-Recursos/Regulacion%20y%20cumplimiento.md).

## Práctica adicional opcional

La práctica guiada y la variante de arriba constituyen el ciclo principal. Elegí una de estas extensiones solo si aporta; no se suman todas al rango de horas.

- Chatbot sobre PDFs o docs propias con citas.
- Comparar chunking naive vs chunking por secciones.
- Crear un set de 50 preguntas con respuestas esperadas y documentos fuente.

## Referencias adicionales

Consulta estas fuentes solo si el recurso principal no alcanza; no son una lista de cursos obligatorios.

- DeepLearning.AI RAG course (acceso no confirmado en la revisión del 6 de septiembre; opcional): <https://www.deeplearning.ai/courses/retrieval-augmented-generation/>
- LlamaIndex docs: <https://docs.llamaindex.ai/>
- LangChain docs: <https://python.langchain.com/>
- Qdrant docs: <https://qdrant.tech/documentation/>
- Weaviate Academy: <https://weaviate.io/developers/academy>

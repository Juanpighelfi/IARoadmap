---
tags:
  - nivel
  - rag
  - retrieval
  - embeddings
duracion: 6-10 semanas
estado: pendiente
inicio:
fin:
---

# 07 - RAG, busqueda y embeddings

## Debes aprender

- Arquitectura RAG: ingestion, chunking, embeddings, index, retrieval, reranking, generation, citations.
- Busqueda: keyword, BM25, semantic search, hybrid search.
- Vector DBs: Chroma, FAISS, Qdrant, Weaviate, Pinecone u otras.
- Chunking por estructura, metadata, permisos y freshness.
- Evaluacion RAG: retrieval recall, groundedness, answer relevance, citation accuracy.
- Fallos tipicos: contexto insuficiente, chunks malos, duplicados, datos viejos, respuestas sin evidencia.
- Borrado y correccion: como se elimina a una persona o un documento del indice, de los
  duplicados y de los sets de evaluacion. Ver [[04-Recursos/Regulacion y cumplimiento]].

## Practica

- Chatbot sobre PDFs o docs propias con citas.
- Comparar chunking naive vs chunking por secciones.
- Crear un set de 50 preguntas con respuestas esperadas y documentos fuente.

## Criterio de salida

Puedes demostrar que tu RAG responde con evidencia y sabe no responder cuando no hay soporte.

## Recursos

- DeepLearning.AI RAG course: <https://www.deeplearning.ai/courses/retrieval-augmented-generation/>
- LlamaIndex docs: <https://docs.llamaindex.ai/>
- LangChain docs: <https://python.langchain.com/>
- Qdrant docs: <https://qdrant.tech/documentation/>
- Weaviate Academy: <https://weaviate.io/developers/academy>

## Siguiente

- [[08 - Agentes workflows automatizacion]]
- [[10 - Evaluacion seguridad gobernanza]]

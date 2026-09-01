---
tags:
  - recursos
  - herramientas
---

# Herramientas recomendadas

Aprende conceptos primero, herramientas despues.

## Lenguaje y entorno

- Python
- uv o venv
- Jupyter
- pytest
- ruff

## Datos

- SQL
- Pandas
- Polars opcional
- DuckDB
- Parquet

## ML clasico

- scikit-learn
- XGBoost o LightGBM opcional
- SHAP con cautela

## Deep learning

- PyTorch
- torchvision
- transformers
- accelerate

## LLMs

- Un proveedor API comercial
- Hugging Face para modelos open source
- Ollama o LM Studio para pruebas locales

## RAG

- BM25
- FAISS, Chroma, Qdrant, Weaviate o Pinecone
- Rerankers cuando el baseline lo justifique

## Agentes

- Primero codigo propio y state machines simples
- Luego LangGraph, CrewAI, AutoGen u otro framework si resuelve complejidad real
- MCP para exponer datos y acciones a un modelo sin integraciones a medida

## Fine-tuning y post-training

- Hugging Face PEFT para LoRA y QLoRA
- Hugging Face TRL para SFT y DPO
- Unsloth si la memoria de GPU es el limite
- Weights and Biases o MLflow para el tracking de experimentos

## Inferencia

- vLLM para servir modelos propios con throughput
- llama.cpp y Ollama para local, pruebas y edge
- Cuantizacion int8 o int4 cuando la calidad medida lo permita

## Codigo asistido

- Un asistente de codigo agentico, con un archivo de contexto del repo versionado
- Revision de diffs siempre, autocommit nunca

## Estudio y seguimiento

- Obsidian, este vault
- Dataview, opcional, para el tablero de [[00-MOC/Estado actual]]
- Anki o el plugin Spaced Repetition, ver [[Repaso espaciado]]

## Observabilidad y evals

- pytest para casos deterministas
- Phoenix
- LangSmith
- OpenTelemetry
- RAGAS o DeepEval segun stack

## Produccion

- FastAPI
- Docker
- GitHub Actions
- MLflow
- Prometheus y Grafana

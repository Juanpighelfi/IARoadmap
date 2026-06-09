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

---
tags:
  - recursos
  - herramientas
---

# Herramientas recomendadas

Aprende conceptos primero, herramientas después. Esta lista es un menú por especialidad, no una lista de instalaciones obligatorias.

## Selección para tu ruta personal

1. Empieza con Python, `venv`, Git y la biblioteca estándar: los cinco laboratorios no requieren paquetes externos.
2. En datos y ML, incorpora Pandas y scikit-learn cuando el ejercicio los necesite.
3. En deep learning y visión, añade PyTorch y torchvision. Trabaja primero con datos pequeños en CPU.
4. Para IA local y robótica, sigue las opciones y límites de [Hardware y presupuesto](Hardware%20y%20presupuesto.md); no compres equipo antes de medir una necesidad.

El resto sirve de consulta para las ramas opcionales. Elige una herramienta por función y mantén esa elección durante el proyecto.

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

- Un proveedor API comercial, opcional y con límite de gasto explícito
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
- Dataview, opcional, para el tablero de [Estado actual](../00-MOC/Estado%20actual.md)
- Anki o el plugin Spaced Repetition, ver [Repaso espaciado](Repaso%20espaciado.md)

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

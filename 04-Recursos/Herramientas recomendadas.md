---
tags:
  - recursos
  - herramientas
---

# Herramientas recomendadas

Aprende conceptos primero, herramientas después. Esta lista es un menú por especialidad, no una lista de instalaciones obligatorias.

## Selección para tu ruta personal

1. Empezá con Python, Git y un editor para el laboratorio 01. No instales todo el menú de especializaciones.
2. En web, aprendé HTML, JavaScript y HTTP; incorporá TypeScript si el SaaS lo usa. Consultá [MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development).
3. Inventariá el SaaS antes de elegir backend, base de datos o alojamiento. Conservá su stack cuando sea viable; todavía no se ha inspeccionado en esta adaptación.
4. Usá un solo asistente de código: pedir criterios, revisar cambios pequeños y probar. Una herramienta nueva necesita una limitación concreta que resolver.
5. Las primeras integraciones e IA se prueban con datos y servicios simulados; contratar un proveedor no es requisito para empezar.

El menú siguiente se conserva como consulta histórica por especialidad. No es una selección de versiones o proveedores para tu producto. Verificá documentación, compatibilidad, costo y condiciones al elegir una herramienta; no estudies frameworks en paralelo. Robótica y entrenamiento quedan fuera del recorrido principal.

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

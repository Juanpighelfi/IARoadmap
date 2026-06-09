# 🚀 Proyectos End-to-End — De Idea a Producción

> Cada proyecto simula un caso REAL de industria. No son ejercicios académicos — son portafolio profesional.

---

## Proyecto 1: Clasificador de Sentimiento en Reviews (NLP End-to-End)

**Cuándo hacerlo**: Después de completar Módulo 3  
**Duración estimada**: 8-12 horas  
**Skills**: Tokenización, fine-tuning, evaluación, API  

### Descripción
Construir un clasificador de sentimiento para reviews de productos en español.
Usar un dataset real, fine-tunear un modelo preentrenado, y desplegarlo como API.

### Fases

| Fase | Tarea | Herramientas |
|------|-------|-------------|
| 1. Datos | Cargar dataset `amazon_reviews_multi` (español) de HuggingFace | `datasets` |
| 2. EDA | Analizar distribución de clases, longitud de textos, wordclouds | `matplotlib`, `wordcloud` |
| 3. Baseline | TF-IDF + LogisticRegression (sklearn) | `sklearn` |
| 4. Fine-tune | BETO (BERT español) con HuggingFace Trainer | `transformers`, `peft` |
| 5. Evaluación | Confusion matrix, F1 por clase, errores más comunes | `sklearn.metrics` |
| 6. API | FastAPI + endpoint /predict | `fastapi`, `uvicorn` |
| 7. Docker | Dockerfile + docker-compose | `docker` |

### Criterio de éxito
- ✅ F1-macro > 0.75 en test set
- ✅ Baseline vs BETO comparativa documentada
- ✅ API funcional con /health y /predict
- ✅ Análisis de errores: ¿qué reviews confunde?
- ✅ README con instrucciones de reproducción

### Código inicial
```python
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
from sklearn.metrics import classification_report

# 1. Dataset
dataset = load_dataset("amazon_reviews_multi", "es", split="train[:5000]")

# 2. Tokenizar
tokenizer = AutoTokenizer.from_pretrained("dccuchile/bert-base-spanish-wwm-cased")
# TODO: tokenizar dataset, entrenar con Trainer, evaluar

# 3. Baseline comparativo
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
# TODO: TF-IDF pipeline
```

---

## Proyecto 2: Sistema de Búsqueda Semántica + RAG (GenAI End-to-End)

**Cuándo hacerlo**: Después de completar Módulo 5  
**Duración estimada**: 10-15 horas  
**Skills**: Embeddings, vector search, RAG, evaluación de RAG  

### Descripción
Construir un sistema RAG completo que responda preguntas sobre documentación técnica.
Usar tus propios study_docs como corpus.

### Fases

| Fase | Tarea | Herramientas |
|------|-------|-------------|
| 1. Indexación | Cargar .md, .py del curso → chunking → embeddings → ChromaDB | `langchain`, `chromadb` |
| 2. Retrieval | Buscar chunks relevantes con MMR | `sentence-transformers` |
| 3. Generation | Construir prompts RAG y generar respuestas | LLM local o API |
| 4. Evaluation | Implementar RAGAS-like eval (faithfulness, relevance, coverage) | Custom |
| 5. UI | Gradio chat interface | `gradio` |
| 6. Optimización | Comparar chunk_size, overlap, top_k, reranking | Experiment tracking |

### Criterio de éxito
- ✅ Chatbot funcional que responde sobre el curso de ML
- ✅ Comparativa: chunk_size 256 vs 512 vs 1024
- ✅ Evaluación cuantitativa de calidad de respuestas
- ✅ UI de chat con Gradio

### Preguntas de evaluación (para testear tu RAG):
1. "¿Qué es LoRA y cómo funciona?"
2. "¿Cuál es la diferencia entre MSE y cross-entropy para clasificación?"
3. "¿Cuántos parámetros tiene EfficientNet-B0?"
4. "¿Qué es vanishing gradient y cómo ResNet lo resuelve?"

---

## Proyecto 3: ML Pipeline Completo con Datos Tabulares (MLOps End-to-End)

**Cuándo hacerlo**: Después de completar Módulo 6  
**Duración estimada**: 12-16 horas  
**Skills**: Feature engineering, model selection, experiment tracking, deployment  

### Descripción
Resolver un problema de clasificación tabular end-to-end, como lo harías en industria.
Dataset sugerido: [Spaceship Titanic](https://www.kaggle.com/competitions/spaceship-titanic) (Kaggle).

### Fases

| Fase | Tarea | Herramientas |
|------|-------|-------------|
| 1. EDA | Distribuciones, correlaciones, datos faltantes, outliers | `pandas`, `seaborn` |
| 2. Feature Eng. | Encodings, interacciones, imputation, feature selection | `sklearn`, `category_encoders` |
| 3. Baselines | LogReg, RandomForest, XGBoost, LightGBM | `sklearn`, `xgboost`, `lightgbm` |
| 4. DNN | Red neuronal con embeddings para categoricals | `pytorch` |
| 5. Ensemble | Stacking/blending de mejores modelos | `sklearn` |
| 6. Tracking | Logear TODOS los experimentos con MLflow | `mlflow` |
| 7. API | Servir mejor modelo como API | `fastapi` |
| 8. CI/CD | Tests automáticos + GitHub Actions | `pytest`, `github actions` |

### Criterio de éxito
- ✅ Leaderboard Kaggle en top 30% (es realista para primer intento)
- ✅ MLflow con 10+ runs documentados
- ✅ Comparativa: ML clásico vs DNN en datos tabulares
- ✅ API dockerizada con tests
- ✅ README profesional con resultados

---

## Proyecto 4: Reproducir un Paper (Research End-to-End)

**Cuándo hacerlo**: Después de completar la lectura de papers (semana 2+)  
**Duración estimada**: 15-20 horas  
**Skills**: Lectura de papers, implementación desde descripción, experimentación  

### Papers sugeridos para reproducir (en orden de dificultad):

| Paper | Dificultad | Qué implementar |
|-------|-----------|-----------------|
| **Dropout** (2014) | ⭐⭐ | Implementar dropout from scratch y replicar Tabla 1 en MNIST |
| **ResNet** (2015) | ⭐⭐⭐ | ResNet-18 from scratch en CIFAR-10, replicar curvas de training |
| **Attention Is All You Need** (2017) | ⭐⭐⭐⭐ | Transformer encoder-decoder en WMT14 (subconjunto) |
| **LoRA** (2021) | ⭐⭐⭐ | Implementar LoRA y comparar con full fine-tuning en GLUE subset |

### Metodología
1. Lee el paper completo (2-3 veces si es necesario)
2. Identifica la tabla/figura que vas a replicar
3. Implementa el modelo siguiendo la Section 3 (Method)
4. Entrena y compara tus resultados con los del paper
5. Si difieren significativamente, diagnostica por qué
6. Escribe un mini-reporte de 1 página

---

## 📊 Rúbrica de Evaluación para Cada Proyecto

| Criterio | Peso | Descripción |
|----------|------|-------------|
| **Funcionalidad** | 30% | ¿El sistema funciona end-to-end? |
| **Calidad del código** | 20% | Modular, documentado, con type hints |
| **Experimentación** | 20% | ¿Probaste alternativas? ¿Documentaste resultados? |
| **Análisis de errores** | 15% | ¿Entiendes POR QUÉ falla? |
| **Reproducibilidad** | 15% | ¿Otro persona puede correrlo con tu README? |

> [!TIP]
> **Consejo**: Sube cada proyecto a GitHub como repositorio separado. Es tu portafolio profesional. Un recruiter quiere ver que podés ir de idea a producción, no que sabés usar `model.fit()`.

"""
=============================================================================
M5-CHALLENGE 2: RAG Pipeline Básico (sin frameworks)
=============================================================================
Construir un mini-RAG para entender cada pieza ANTES de usar LangChain.
DURACIÓN: ~2h | DIFICULTAD: ⭐⭐⭐

HINTS: Si te trabás, consultá modulo_5/hints/hint_challenge_2.md
=============================================================================
"""
import numpy as np
import os

print("=" * 60)
print("M5-CHALLENGE 2: RAG Pipeline Básico")
print("=" * 60)

try:
    from sentence_transformers import SentenceTransformer
    encoder = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    HAS_ENCODER = True
except ImportError:
    print("  pip install sentence-transformers")
    HAS_ENCODER = False


# --- Parte 1: Indexar documentos ---
print("\n--- Parte 1: Indexación ---")

documents = [
    "Las redes neuronales convolucionales (CNN) son especialmente efectivas para tareas de visión por computadora.",
    "El overfitting ocurre cuando un modelo se ajusta demasiado a los datos de entrenamiento.",
    "La regularización L2 (weight decay) penaliza pesos grandes, forzando soluciones más simples.",
    "Dropout desactiva aleatoriamente neuronas durante el entrenamiento, actuando como regularización.",
    "Transfer learning permite reutilizar un modelo preentrenado para una tarea nueva con pocos datos.",
    "El learning rate es el hiperparámetro más importante. Muy alto causa divergencia.",
    "Batch normalization normaliza las activaciones de cada capa, estabilizando el entrenamiento.",
    "Data augmentation genera variaciones artificiales de los datos para mejorar generalización.",
    "El gradiente descendente estocástico (SGD) actualiza pesos usando un subconjunto aleatorio.",
    "Adam combina momentum y learning rate adaptativo, siendo el optimizador más popular.",
    "Cross-entropy penaliza fuertemente las predicciones incorrectas confiadas.",
    "Las skip connections de ResNet permiten gradientes fluir directamente en redes profundas.",
]

"""
TODO: Implementa SimpleVectorStore con métodos:
  - add_documents(docs): encodea y almacena embeddings
  - search(query, top_k): busca los top_k documentos más similares
"""

class SimpleVectorStore:
    """TODO: Vector store mínimo: indexar, buscar, recuperar."""
    
    def __init__(self, encoder=None):
        self.documents = []
        self.embeddings = None
        self.encoder = encoder
    
    def add_documents(self, docs):
        """TODO: Almacena documentos y calcula sus embeddings."""
        self.documents = docs
        # TODO: self.embeddings = self.encoder.encode(docs) si hay encoder
        pass  # Tu código aquí
    
    def search(self, query, top_k=3):
        """
        TODO: Busca los top_k documentos más similares a la query.
        1. Encodea la query
        2. Calcula similitud coseno con cada documento
        3. Ordena y retorna los top_k
        """
        pass  # Tu código aquí


store = SimpleVectorStore(encoder if HAS_ENCODER else None)
store.add_documents(documents)
print(f"  Indexados {len(documents)} documentos")

queries = [
    "¿Cómo evitar que mi modelo memorice los datos?",
    "¿Qué optimizador debería usar?",
    "¿Cómo entrenar con pocos datos?",
]

for query in queries:
    print(f"\n  Query: '{query}'")
    results = store.search(query, top_k=3)
    for i, (doc, score) in enumerate(results):
        print(f"    {i+1}. [{score:.3f}] {doc[:80]}...")


# --- Parte 2: Formatear prompt con contexto ---
print(f"\n{'='*60}")
print("--- Parte 2: Formatear Prompt RAG ---")
print("=" * 60)

"""
TODO: Implementa una función que construya un prompt RAG con:
  - System prompt
  - Contexto recuperado
  - Pregunta del usuario
"""

def format_rag_prompt(query, context_docs, system_prompt=None):
    """TODO: Formatea un prompt RAG con contexto recuperado."""
    if system_prompt is None:
        system_prompt = "Eres un asistente experto en ML. Responde basándote SOLO en el contexto."
    
    # TODO: Construye el prompt con [SYSTEM], [CONTEXTO], [PREGUNTA], [RESPUESTA]
    prompt = ...  # Tu código aquí
    return prompt

query = "¿Cómo evitar que mi modelo memorice los datos?"
context = store.search(query, top_k=3)
prompt = format_rag_prompt(query, context)

print(f"\n  Prompt generado ({len(prompt)} chars):")
print(f"  {'-'*50}")
print(f"  {prompt}")
print(f"  {'-'*50}")


# --- Parte 3: MMR (Maximum Marginal Relevance) ---
print(f"\n{'='*60}")
print("--- Parte 3: MMR Ranking ---")
print("=" * 60)

print("""
  MMR selecciona documentos RELEVANTES pero DIVERSOS:
  
  Score_MMR = λ * sim(query, doc) - (1-λ) * max(sim(doc, selected))
  
  - λ=1.0: solo relevancia (puede traer docs repetitivos)
  - λ=0.0: solo diversidad (puede traer docs irrelevantes)
  - λ=0.5: balance (recomendado)
""")

"""
TODO: Implementa MMR search.
"""

def mmr_search(store, query, top_k=3, lambda_param=0.5, candidates=10):
    """TODO: Maximum Marginal Relevance search."""
    pass  # Tu código aquí

print("\nM5-Challenge 2 completado.")

"""
=============================================================================
M5-CHALLENGE 2: RAG Pipeline Basico (sin frameworks)
=============================================================================
Construir un mini-RAG para entender cada pieza ANTES de usar LangChain.
DURACION: ~2h | DIFICULTAD: 3/5
=============================================================================
"""
import numpy as np
import os

print("=" * 60)
print("M5-CHALLENGE 2: RAG Pipeline Basico")
print("=" * 60)

try:
    from sentence_transformers import SentenceTransformer
    encoder = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    HAS_ENCODER = True
except ImportError:
    print("  pip install sentence-transformers")
    HAS_ENCODER = False


# --- Parte 1: Indexar documentos ---
print("\n--- Parte 1: Indexacion ---")

# Base de conocimiento (apuntes de ML)
documents = [
    "Las redes neuronales convolucionales (CNN) son especialmente efectivas para tareas de vision por computadora como clasificacion de imagenes.",
    "El overfitting ocurre cuando un modelo se ajusta demasiado a los datos de entrenamiento y pierde capacidad de generalizacion.",
    "La regularizacion L2 (weight decay) penaliza pesos grandes, forzando al modelo a encontrar soluciones mas simples.",
    "Dropout desactiva aleatoriamente un porcentaje de neuronas durante el entrenamiento, actuando como regularizacion.",
    "Transfer learning permite reutilizar un modelo preentrenado en un dataset grande para una tarea nueva con pocos datos.",
    "El learning rate es el hiperparametro mas importante. Muy alto causa divergencia, muy bajo causa convergencia lenta.",
    "Batch normalization normaliza las activaciones de cada capa, estabilizando y acelerando el entrenamiento.",
    "Data augmentation genera variaciones artificiales de los datos de entrenamiento (rotacion, flip, crop) para mejorar generalizacion.",
    "El gradiente descendente estocastico (SGD) actualiza los pesos usando un subconjunto aleatorio de los datos en cada paso.",
    "Adam combina momentum y learning rate adaptativo, siendo el optimizador mas popular en deep learning.",
    "La funcion de perdida cross-entropy es estandar para clasificacion porque penaliza fuertemente las predicciones incorrectas confiadas.",
    "Las skip connections de ResNet permiten gradientes fluir directamente, resolviendo el problema de vanishing gradient en redes profundas.",
]

class SimpleVectorStore:
    """Vector store minimo: indexar, buscar, recuperar."""
    
    def __init__(self, encoder=None):
        self.documents = []
        self.embeddings = None
        self.encoder = encoder
    
    def add_documents(self, docs):
        self.documents = docs
        if self.encoder:
            self.embeddings = self.encoder.encode(docs)
        else:
            np.random.seed(42)
            self.embeddings = np.random.randn(len(docs), 384)
    
    def search(self, query, top_k=3):
        if self.encoder:
            q_emb = self.encoder.encode([query])[0]
        else:
            q_emb = np.random.randn(384)
        
        # Similitud coseno
        scores = []
        for i, emb in enumerate(self.embeddings):
            sim = np.dot(q_emb, emb) / (np.linalg.norm(q_emb) * np.linalg.norm(emb) + 1e-10)
            scores.append((sim, i))
        
        scores.sort(reverse=True)
        return [(self.documents[idx], score) for score, idx in scores[:top_k]]


# Indexar
store = SimpleVectorStore(encoder if HAS_ENCODER else None)
store.add_documents(documents)
print(f"  Indexados {len(documents)} documentos")

# Buscar
queries = [
    "Como evitar que mi modelo memorice los datos?",
    "Que optimizador deberia usar?",
    "Como entrenar con pocos datos?",
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

def format_rag_prompt(query, context_docs, system_prompt=None):
    """Formatea un prompt RAG con contexto recuperado."""
    if system_prompt is None:
        system_prompt = "Eres un asistente experto en machine learning. Responde basandote SOLO en el contexto proporcionado."
    
    context = "\n".join([f"- {doc}" for doc, _ in context_docs])
    
    prompt = f"""[SYSTEM]
{system_prompt}

[CONTEXTO RECUPERADO]
{context}

[PREGUNTA DEL USUARIO]
{query}

[RESPUESTA]"""
    return prompt

query = "Como evitar que mi modelo memorice los datos?"
context = store.search(query, top_k=3)
prompt = format_rag_prompt(query, context)

print(f"\n  Prompt generado ({len(prompt)} chars):")
print(f"  {'-'*50}")
print(f"  {prompt}")
print(f"  {'-'*50}")

print("""
  SIGUIENTE PASO (con un LLM):
  - Enviar este prompt a un LLM (local o API)
  - Comparar respuesta CON contexto vs SIN contexto
  - El modelo con RAG deberia dar respuestas mas especificas
""")


# --- Parte 3: MMR (Maximum Marginal Relevance) ---
print(f"\n{'='*60}")
print("--- Parte 3: MMR Ranking ---")
print("=" * 60)

print("""
  MMR selecciona documentos RELEVANTES pero DIVERSOS:
  
  Score_MMR = lambda * sim(query, doc) - (1-lambda) * max(sim(doc, selected))
  
  - lambda=1.0: solo relevancia (puede traer docs repetitivos)
  - lambda=0.0: solo diversidad (puede traer docs irrelevantes)
  - lambda=0.5: balance (recomendado)
""")

def mmr_search(store, query, top_k=3, lambda_param=0.5, candidates=10):
    """Maximum Marginal Relevance search."""
    # Obtener mas candidatos de los necesarios
    all_results = store.search(query, top_k=candidates)
    
    if not all_results:
        return []
    
    selected = [all_results[0]]  # El mas relevante siempre entra
    remaining = all_results[1:]
    
    while len(selected) < top_k and remaining:
        best_score = -float('inf')
        best_idx = 0
        
        for i, (doc, rel_score) in enumerate(remaining):
            # Calcular max similitud con los ya seleccionados
            max_sim = max(0.5 for _ in selected)  # Simplificado sin encoder
            mmr_score = lambda_param * rel_score - (1 - lambda_param) * max_sim
            
            if mmr_score > best_score:
                best_score = mmr_score
                best_idx = i
        
        selected.append(remaining.pop(best_idx))
    
    return selected

results_mmr = mmr_search(store, "Como regularizar mi modelo?")
print(f"\n  Resultados MMR (lambda=0.5):")
for i, (doc, score) in enumerate(results_mmr):
    print(f"    {i+1}. [{score:.3f}] {doc[:70]}...")

print("\nM5-Challenge 2 completado.")

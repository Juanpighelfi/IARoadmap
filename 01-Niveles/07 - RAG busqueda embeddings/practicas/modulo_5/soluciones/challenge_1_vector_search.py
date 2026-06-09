"""
=============================================================================
M5-CHALLENGE 1: Vector Search desde la Intuicion
=============================================================================
Embeddings semanticos, similitud coseno, busqueda semantica.
DURACION: ~1.5h | DIFICULTAD: 3/5
=============================================================================
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 60)
print("M5-CHALLENGE 1: Vector Search")
print("=" * 60)

try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    HAS_MODEL = True
except ImportError:
    print("  pip install sentence-transformers")
    print("  Continuando con embeddings simulados...")
    HAS_MODEL = False

# --- Parte 1: Embeddings semanticos ---
print("\n--- Parte 1: Embeddings Semanticos ---")

frases = [
    "El gato se sento en la alfombra",
    "El felino descanso sobre el tapete",
    "Python es un lenguaje de programacion",
    "Las redes neuronales aprenden representaciones",
    "Deep learning es un subcampo del machine learning",
]

if HAS_MODEL:
    embeddings = model.encode(frases)
else:
    np.random.seed(42)
    embeddings = np.random.randn(len(frases), 384)
    # Hacer que frases similares tengan embeddings similares (simulado)
    embeddings[1] = embeddings[0] + np.random.randn(384) * 0.3
    embeddings[4] = embeddings[3] + np.random.randn(384) * 0.3

print(f"  {len(frases)} frases codificadas a vectores de dim {embeddings.shape[1]}")

# Similitud coseno
def cosine_similarity_matrix(embs):
    norms = np.linalg.norm(embs, axis=1, keepdims=True)
    normalized = embs / norms
    return normalized @ normalized.T

sim_matrix = cosine_similarity_matrix(embeddings)

print(f"\n  Matriz de similitud coseno:")
print(f"  {'':30s}", end="")
for i in range(len(frases)):
    print(f"  F{i+1}", end="")
print()
for i in range(len(frases)):
    label = frases[i][:28] + ".." if len(frases[i]) > 30 else frases[i]
    print(f"  {label:30s}", end="")
    for j in range(len(frases)):
        val = sim_matrix[i, j]
        print(f"  {val:.2f}", end="")
    print()

# Heatmap
fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(sim_matrix, cmap='YlOrRd', aspect='auto', vmin=0, vmax=1)
labels = [f[:20]+"..." if len(f) > 20 else f for f in frases]
ax.set_xticks(range(len(frases))); ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=8)
ax.set_yticks(range(len(frases))); ax.set_yticklabels(labels, fontsize=8)
plt.colorbar(im, ax=ax, label='Similitud Coseno')
ax.set_title('Similitud Semantica entre Frases', fontweight='bold')
plt.tight_layout()
plt.savefig('challenges/m5_ch1_similarity.png', dpi=100, bbox_inches='tight')
plt.close()
print("\n  Heatmap guardado.")


# --- Parte 2: Busqueda semantica ---
print(f"\n{'='*60}")
print("--- Parte 2: Busqueda Semantica ---")
print("=" * 60)

query = "Los modelos de ML extraen features automaticamente"
if HAS_MODEL:
    q_emb = model.encode([query])[0]
else:
    q_emb = embeddings[3] + np.random.randn(384) * 0.5

# Calcular similitud con cada frase
scores = []
for i, emb in enumerate(embeddings):
    sim = np.dot(q_emb, emb) / (np.linalg.norm(q_emb) * np.linalg.norm(emb))
    scores.append((sim, frases[i]))

scores.sort(reverse=True)

print(f"\n  Query: '{query}'")
print(f"  Resultados ordenados por similitud:")
for i, (score, frase) in enumerate(scores):
    marker = "<-- MEJOR" if i == 0 else ""
    print(f"    {i+1}. [{score:.4f}] {frase} {marker}")


# --- Parte 3: Chunking experiment ---
print(f"\n{'='*60}")
print("--- Parte 3: Chunking ---")
print("=" * 60)

texto_largo = """
Machine learning es un subcampo de la inteligencia artificial que se centra en el desarrollo
de algoritmos y modelos estadisticos que permiten a los sistemas informaticos mejorar su
rendimiento en una tarea especifica a traves de la experiencia, sin ser programados
explicitamente. Los algoritmos de machine learning construyen un modelo matematico basado
en datos de entrenamiento para hacer predicciones o tomar decisiones. El deep learning es
una rama del machine learning que utiliza redes neuronales con multiples capas para aprender
representaciones jerarquicas de los datos. Las redes neuronales profundas han logrado
avances significativos en vision por computadora, procesamiento del lenguaje natural y
otros dominios.
"""

def chunk_text(text, chunk_size, overlap=0):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunks.append(" ".join(words[start:end]))
        start += chunk_size - overlap
    return chunks

for chunk_size in [10, 25, 50]:
    for overlap in [0, 5]:
        chunks = chunk_text(texto_largo, chunk_size, overlap)
        print(f"  chunk_size={chunk_size:3d}, overlap={overlap}: {len(chunks)} chunks")

print("""
  OBSERVACION:
  - Chunks muy chicos: pierden contexto ("deep learning es una" sin explicar que)
  - Chunks muy grandes: meten ruido (info irrelevante)
  - Overlap: evita cortar ideas a la mitad
  - Sweet spot: 500-1000 tokens con 10-20% overlap
""")

print("M5-Challenge 1 completado.")

"""
=============================================================================
M5-CHALLENGE 1: Vector Search desde la Intuición
=============================================================================
Embeddings semánticos, similitud coseno, búsqueda semántica.
DURACIÓN: ~1.5h | DIFICULTAD: ⭐⭐⭐

HINTS: Si te trabás, consultá modulo_5/hints/hint_challenge_1.md
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

# --- Parte 1: Embeddings semánticos ---
print("\n--- Parte 1: Embeddings Semánticos ---")

frases = [
    "El gato se sentó en la alfombra",
    "El felino descansó sobre el tapete",
    "Python es un lenguaje de programación",
    "Las redes neuronales aprenden representaciones",
    "Deep learning es un subcampo del machine learning",
]

if HAS_MODEL:
    embeddings = model.encode(frases)
else:
    np.random.seed(42)
    embeddings = np.random.randn(len(frases), 384)
    embeddings[1] = embeddings[0] + np.random.randn(384) * 0.3
    embeddings[4] = embeddings[3] + np.random.randn(384) * 0.3

print(f"  {len(frases)} frases codificadas a vectores de dim {embeddings.shape[1]}")

"""
TODO: Implementa una función que calcule la matriz de similitud coseno.
  1. Normaliza cada embedding: emb / ||emb||
  2. Multiplica: normalized @ normalized.T
"""

def cosine_similarity_matrix(embs):
    """TODO: Calcula la matriz de similitud coseno entre todos los embeddings."""
    pass  # Tu código aquí

sim_matrix = cosine_similarity_matrix(embeddings)

# Imprimir matriz
print(f"\n  Matriz de similitud coseno:")
for i in range(len(frases)):
    label = frases[i][:28] + ".." if len(frases[i]) > 30 else frases[i]
    print(f"  {label:30s}", end="")
    for j in range(len(frases)):
        print(f"  {sim_matrix[i, j]:.2f}", end="")
    print()

# Heatmap
fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(sim_matrix, cmap='YlOrRd', aspect='auto', vmin=0, vmax=1)
labels = [f[:20]+"..." if len(f) > 20 else f for f in frases]
ax.set_xticks(range(len(frases))); ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=8)
ax.set_yticks(range(len(frases))); ax.set_yticklabels(labels, fontsize=8)
plt.colorbar(im, ax=ax, label='Similitud Coseno')
ax.set_title('Similitud Semántica entre Frases', fontweight='bold')
plt.tight_layout()
plt.savefig('challenges/m5_ch1_similarity.png', dpi=100, bbox_inches='tight')
plt.close()


# --- Parte 2: Búsqueda semántica ---
print(f"\n{'='*60}")
print("--- Parte 2: Búsqueda Semántica ---")
print("=" * 60)

query = "Los modelos de ML extraen features automáticamente"
if HAS_MODEL:
    q_emb = model.encode([query])[0]
else:
    q_emb = embeddings[3] + np.random.randn(384) * 0.5

"""
TODO: Para cada frase, calcula la similitud coseno con la query y ordena.
  sim = dot(q, emb) / (||q|| * ||emb||)
"""
scores = []
for i, emb in enumerate(embeddings):
    sim = ...  # Tu código aquí
    scores.append((sim, frases[i]))

scores.sort(reverse=True)

print(f"\n  Query: '{query}'")
print(f"  Resultados ordenados por similitud:")
for i, (score, frase) in enumerate(scores):
    marker = "<-- MEJOR" if i == 0 else ""
    print(f"    {i+1}. [{score:.4f}] {frase} {marker}")


# --- Parte 3: Chunking ---
print(f"\n{'='*60}")
print("--- Parte 3: Chunking ---")
print("=" * 60)

texto_largo = """
Machine learning es un subcampo de la inteligencia artificial que se centra en el desarrollo
de algoritmos y modelos estadísticos que permiten a los sistemas informáticos mejorar su
rendimiento en una tarea específica a través de la experiencia, sin ser programados
explícitamente. Los algoritmos de machine learning construyen un modelo matemático basado
en datos de entrenamiento para hacer predicciones o tomar decisiones.
"""

"""
TODO: Implementa una función de chunking con overlap.
"""

def chunk_text(text, chunk_size, overlap=0):
    """TODO: Divide texto en chunks de chunk_size palabras con overlap."""
    words = text.split()
    chunks = []
    start = 0
    # TODO: Itera creando chunks con overlap
    while start < len(words):
        pass  # Tu código aquí
    return chunks

for chunk_size in [10, 25, 50]:
    for overlap in [0, 5]:
        chunks = chunk_text(texto_largo, chunk_size, overlap)
        print(f"  chunk_size={chunk_size:3d}, overlap={overlap}: {len(chunks)} chunks")

print("\nM5-Challenge 1 completado.")

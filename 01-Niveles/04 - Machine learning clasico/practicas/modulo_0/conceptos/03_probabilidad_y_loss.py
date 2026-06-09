"""
=============================================================================
📐 PROBABILIDAD Y LOSS FUNCTIONS — Guía Conceptual Interactiva
=============================================================================

PROPÓSITO: Entender la conexión profunda entre probabilidad, teoría de la
           información y las loss functions que usamos en ML.

           La mayoría de tutoriales dicen "usa cross-entropy" sin explicar
           POR QUÉ. Aquí vas a entender la razón matemática e intuitiva.

DURACIÓN: ~40 minutos
PRERREQUISITO: Entender sigmoid, gradientes (guías anteriores)
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'figure.figsize': (10, 6),
    'font.size': 11,
    'axes.grid': True,
    'grid.alpha': 0.3
})


# =============================================================================
# 1️⃣ PROBABILIDAD: Lo que tu modelo realmente predice
# =============================================================================
"""
Tu modelo de clasificación NO predice una clase. Predice una
DISTRIBUCIÓN DE PROBABILIDAD sobre las clases posibles.

Para un clasificador de gatos/perros:
  - model(imagen) = [0.85, 0.15]   → "85% gato, 15% perro"

La pregunta que la loss function responde es:
  "¿Qué tan LEJOS está la distribución predicha de la real?"
"""

print("=" * 60)
print("1️⃣  DISTRIBUCIONES DE PROBABILIDAD")
print("=" * 60)

# Ejemplo: clasificador de 4 clases
clases = ['Gato', 'Perro', 'Pájaro', 'Pez']

# Distribución real (la imagen ES un gato)
p_real = np.array([1.0, 0.0, 0.0, 0.0])  # one-hot

# Predicciones de 3 modelos diferentes
q_bueno = np.array([0.85, 0.05, 0.05, 0.05])   # Modelo confiado y correcto
q_medio = np.array([0.40, 0.30, 0.20, 0.10])    # Modelo inseguro
q_malo  = np.array([0.05, 0.60, 0.25, 0.10])    # Modelo confiado e INCORRECTO

print(f"\n  Distribución real (one-hot): {dict(zip(clases, p_real))}")
print(f"\n  Modelo bueno:  {dict(zip(clases, q_bueno))}")
print(f"  Modelo medio:  {dict(zip(clases, q_medio))}")
print(f"  Modelo malo:   {dict(zip(clases, q_malo))}")

# Visualizar
fig, axes = plt.subplots(1, 4, figsize=(16, 4), sharey=True)
distribuciones = [('Real (p)', p_real, '#4CAF50'), 
                  ('Modelo Bueno', q_bueno, '#2196F3'),
                  ('Modelo Medio', q_medio, '#FFC107'),
                  ('Modelo Malo', q_malo, '#F44336')]

for ax, (nombre, dist, color) in zip(axes, distribuciones):
    ax.bar(clases, dist, color=color, alpha=0.8, edgecolor='white')
    ax.set_title(nombre, fontweight='bold', fontsize=12)
    ax.set_ylim(0, 1.1)

plt.suptitle('¿Qué distribución se parece más a la real?', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('conceptos/03_distribuciones.png', dpi=100, bbox_inches='tight')
plt.show()

input("\n[Presiona Enter para continuar...]\n")


# =============================================================================
# 2️⃣ ENTROPÍA: Cuánta "sorpresa" tiene una distribución
# =============================================================================
"""
La ENTROPÍA mide la incertidumbre de una distribución.

    H(p) = -Σ p(x) · log₂(p(x))

- Distribución uniforme (máxima incertidumbre) → entropía ALTA
- Distribución puntual [1, 0, 0, 0] (certeza total) → entropía BAJA = 0

Analogía: Cuántos bits necesitas para transmitir un resultado.
- Moneda justa (50/50): 1 bit (cara/cruz)
- Dado de 6 caras: 2.58 bits
- Resultado seguro: 0 bits (no necesitas decir nada, ya lo sabes)
"""

print("\n" + "=" * 60)
print("2️⃣  ENTROPÍA")
print("=" * 60)

def entropia(p, base=2):
    """Calcula la entropía de una distribución p."""
    p = np.array(p, dtype=float)
    p = p[p > 0]  # Evitar log(0)
    return -np.sum(p * np.log(p) / np.log(base))

# Ejemplos
distribuciones_entropia = {
    "Certeza total [1,0,0,0]": [1.0, 0.0, 0.0, 0.0],
    "Casi seguro [0.95, 0.02, 0.02, 0.01]": [0.95, 0.02, 0.02, 0.01],
    "Inseguro [0.4, 0.3, 0.2, 0.1]": [0.4, 0.3, 0.2, 0.1],
    "Uniforme [0.25, 0.25, 0.25, 0.25]": [0.25, 0.25, 0.25, 0.25],
}

print(f"\n  {'Distribución':45s} | {'Entropía (bits)':>15s}")
print(f"  {'-'*45} | {'-'*15}")
for nombre, dist in distribuciones_entropia.items():
    H = entropia(dist)
    bar = "█" * int(H * 10)
    print(f"  {nombre:45s} | {H:10.4f} bits  {bar}")

print("""
  🔑 OBSERVA: La entropía máxima para 4 clases es log₂(4) = 2 bits.
     Eso ocurre con la distribución uniforme (máxima incertidumbre).
     
     En ML, queremos que nuestro modelo tenga BAJA entropía en sus
     predicciones → que esté "seguro" de su respuesta.
""")

input("\n[Presiona Enter para continuar...]\n")


# =============================================================================
# 3️⃣ CROSS-ENTROPY: ¿Qué tan lejos estás de la realidad?
# =============================================================================
"""
La CROSS-ENTROPY mide cuánta "sorpresa" genera la distribución q
cuando la realidad es p:

    H(p, q) = -Σ p(x) · log(q(x))

Propiedades importantes:
- H(p, q) ≥ H(p) siempre (la cross-entropy siempre es ≥ la entropía)
- H(p, q) = H(p) sólo cuando q = p (predicción perfecta)
- La diferencia H(p,q) - H(p) = KL(p||q) (divergencia KL)

Para clasificación con labels one-hot [1, 0, 0, 0]:
    H(p, q) = -1·log(q₁) - 0·log(q₂) - 0·log(q₃) - 0·log(q₄)
            = -log(q₁)

¡Solo importa la probabilidad asignada a la clase CORRECTA!
Cuanto más alta sea q_correcta, menor la loss.
"""

print("\n" + "=" * 60)
print("3️⃣  CROSS-ENTROPY")
print("=" * 60)

def cross_entropy(p, q, epsilon=1e-15):
    """Cross-entropy H(p, q) = -Σ p(x) log(q(x))"""
    q = np.clip(q, epsilon, 1 - epsilon)  # Evitar log(0)
    return -np.sum(p * np.log(q))

# Calcular cross-entropy para cada modelo
for nombre, q in [("Bueno", q_bueno), ("Medio", q_medio), ("Malo", q_malo)]:
    ce = cross_entropy(p_real, q)
    print(f"  H(p, q_{nombre:5s}) = -log({q[0]:.2f}) = {ce:.4f}")

print("""
  🔑 OBSERVA:
  - Modelo bueno (q[gato]=0.85): loss = 0.16 (baja)
  - Modelo medio (q[gato]=0.40): loss = 0.92 (media)
  - Modelo malo  (q[gato]=0.05): loss = 3.00 (¡MUY alta!)
  
  Cross-entropy penaliza MUCHO las predicciones incorrectas y confiadas.
  Esto es exactamente lo que queremos: que el modelo aprenda rápido de sus
  peores errores.
""")

# Visualización de la penalización
q_range = np.linspace(0.01, 0.99, 200)
loss_ce = -np.log(q_range)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(q_range, loss_ce, linewidth=2.5, color='#F44336', label='-log(q) = Cross-Entropy Loss')
ax.fill_between(q_range, loss_ce, alpha=0.1, color='#F44336')
ax.set_xlabel('Probabilidad asignada a la clase correcta (q)', fontsize=12)
ax.set_ylabel('Cross-Entropy Loss', fontsize=12)
ax.set_title('Cross-Entropy: Penalización por confianza equivocada', fontweight='bold', fontsize=14)

# Marcar zonas
ax.annotate('Baja confianza correcta\n→ Loss ALTA', 
            xy=(0.1, -np.log(0.1)), xytext=(0.3, 3.5),
            fontsize=11, arrowprops=dict(arrowstyle='->', color='gray'),
            bbox=dict(facecolor='#FFCDD2', edgecolor='none', alpha=0.8))

ax.annotate('Alta confianza correcta\n→ Loss BAJA', 
            xy=(0.9, -np.log(0.9)), xytext=(0.5, 1.5),
            fontsize=11, arrowprops=dict(arrowstyle='->', color='gray'),
            bbox=dict(facecolor='#C8E6C9', edgecolor='none', alpha=0.8))

ax.legend(fontsize=12)
plt.tight_layout()
plt.savefig('conceptos/03_cross_entropy.png', dpi=100, bbox_inches='tight')
plt.show()

input("\n[Presiona Enter para continuar...]\n")


# =============================================================================
# 4️⃣ KL DIVERGENCE: La "distancia" entre distribuciones
# =============================================================================
"""
KL Divergence mide cuánta información se PIERDE al usar q para aproximar p:

    KL(P || Q) = Σ P(x) · log(P(x) / Q(x))
               = H(P, Q) - H(P)

Propiedades importantes:
- KL(P||Q) ≥ 0 siempre
- KL(P||Q) = 0 sólo si P = Q
- ¡NO es simétrica! KL(P||Q) ≠ KL(Q||P)

En ML aparece en:
- VAEs: KL(q(z|x) || p(z)) — regularización del espacio latente
- Destilación de conocimiento: KL(teacher || student)
- RLHF: KL penalty para que el modelo no se desvíe del base
"""

print("\n" + "=" * 60)
print("4️⃣  KL DIVERGENCE")
print("=" * 60)

def kl_divergence(p, q, epsilon=1e-15):
    """KL(P || Q) = Σ P(x) · log(P(x) / Q(x))"""
    p = np.array(p, dtype=float)
    q = np.array(q, dtype=float)
    q = np.clip(q, epsilon, None)
    mask = p > 0
    return np.sum(p[mask] * np.log(p[mask] / q[mask]))

# Ejemplo
P = np.array([0.7, 0.2, 0.1])
Q1 = np.array([0.6, 0.3, 0.1])  # Cercana a P
Q2 = np.array([0.1, 0.1, 0.8])  # Lejos de P

print(f"\n  P =  {P}")
print(f"  Q1 = {Q1} (cercana)")
print(f"  Q2 = {Q2} (lejana)")

kl_pq1 = kl_divergence(P, Q1)
kl_pq2 = kl_divergence(P, Q2)
kl_q1p = kl_divergence(Q1, P)

print(f"\n  KL(P || Q1) = {kl_pq1:.4f}  (Q1 ≈ P → KL bajo)")
print(f"  KL(P || Q2) = {kl_pq2:.4f}  (Q2 ≠ P → KL alto)")
print(f"\n  KL(Q1 || P) = {kl_q1p:.4f}")
print(f"  ¿KL(P||Q1) == KL(Q1||P)? {'Sí' if np.isclose(kl_pq1, kl_q1p) else 'NO — ¡KL no es simétrica!'}")

print("""
  🔑 ¿Por qué la asimetría importa?
     
     KL(P || Q) penaliza cuando Q asigna BAJA probabilidad donde P asigna ALTA.
     → "No te olvides de lo importante" (mode-covering)
     
     KL(Q || P) penaliza cuando Q asigna ALTA probabilidad donde P asigna BAJA.
     → "No inventes cosas falsas" (mode-seeking)
     
     En VAEs se usa KL(Q || P) porque queremos que el encoder
     no "invente" regiones del espacio latente que el prior no cubre.
""")


# =============================================================================
# 5️⃣ SOFTMAX: De logits a probabilidades
# =============================================================================
"""
Los modelos de clasificación producen "logits" (números sin restricción).
Softmax los convierte en una distribución de probabilidad:

    softmax(zᵢ) = exp(zᵢ) / Σⱼ exp(zⱼ)

Propiedades:
- Todos los valores son > 0
- Suman exactamente 1
- Preserva el orden (el logit más alto → la probabilidad más alta)
- Amplifica las diferencias (funciona como un "argmax suave")
"""

print("\n" + "=" * 60)
print("5️⃣  SOFTMAX")
print("=" * 60)

def softmax(logits):
    """Softmax numéricamente estable."""
    # Truco: restar el máximo para evitar overflow de exp()
    shifted = logits - np.max(logits)
    exp_vals = np.exp(shifted)
    return exp_vals / np.sum(exp_vals)

logits = np.array([2.0, 1.0, 0.1])
probs = softmax(logits)

print(f"\n  Logits:         {logits}")
print(f"  Softmax:        {probs.round(4)}")
print(f"  Suma:           {probs.sum():.6f}")

# Efecto de la "temperatura"
print(f"\n  --- Efecto de la Temperatura ---")
print(f"  temperature < 1: más confiado (más pico)")
print(f"  temperature > 1: más uniforme (más suave)")

for T in [0.1, 0.5, 1.0, 2.0, 10.0]:
    scaled = softmax(logits / T)
    bar = "".join(["█" * int(p * 30) for p in scaled])
    print(f"  T={T:4.1f}: {scaled.round(3)} {bar}")


# =============================================================================
# RESUMEN
# =============================================================================
print(f"""
{'=' * 60}
📋 RESUMEN — PROBABILIDAD Y LOSS FUNCTIONS
{'=' * 60}

┌──────────────────────────────────────────────────────────┐
│ CONCEPTO         │ EN ML SIGNIFICA...                     │
├──────────────────────────────────────────────────────────┤
│ Entropía H(p)    │ Incertidumbre de la distribución real  │
│ Cross-Entropy     │ Loss function para clasificación       │
│ KL Divergence     │ "Distancia" entre distribuciones       │
│ Softmax           │ Convertir logits → probabilidades      │
│ Temperatura       │ Controlar "confianza" del modelo       │
│ One-hot encoding  │ Distribución real para labels          │
│ -log(q_correcto)  │ Simplificación de CE con one-hot       │
└──────────────────────────────────────────────────────────┘

Relación: H(p,q) = H(p) + KL(p||q)
  → Minimizar cross-entropy = Minimizar KL divergence
    (porque H(p) es constante para los datos de entrenamiento)

🎯 SIGUIENTE: challenges 7, 8, 9
""")

"""
=============================================================================
🏆 CHALLENGE 9: KL Divergence
=============================================================================

OBJETIVO: Calcular KL divergence manualmente, entender su asimetría,
          y conectar con aplicaciones en ML (VAEs, destilación).

DURACIÓN: ~25 minutos
DIFICULTAD: ⭐⭐ (Intermedia)
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


print("=" * 60)
print("🏆 CHALLENGE 9: KL Divergence")
print("=" * 60)


# =============================================================================
# PARTE 1: Cálculo Manual
# =============================================================================
"""
KL(P || Q) = Σ P(x) · log(P(x) / Q(x))
           = Σ P(x) · [log P(x) - log Q(x)]

Interpretación intuitiva:
  "Cuánta información EXTRA necesitas para codificar datos de P
   si tu código fue diseñado para Q"

TODO: Calcula KL(P||Q1), KL(P||Q2) y KL(Q1||P) manualmente.
"""

P  = np.array([0.7, 0.2, 0.1])
Q1 = np.array([0.6, 0.3, 0.1])  # Cercana a P
Q2 = np.array([0.1, 0.1, 0.8])  # Lejos de P

print("\n--- PARTE 1: Cálculo paso a paso ---")
print(f"\n  P  = {P}")
print(f"  Q1 = {Q1}")
print(f"  Q2 = {Q2}")

# KL(P || Q1) paso a paso
print(f"\n  KL(P || Q1) paso a paso:")
total = 0
for i in range(len(P)):
    term = P[i] * np.log(P[i] / Q1[i])
    total += term
    print(f"    P[{i}]·log(P[{i}]/Q1[{i}]) = {P[i]}·log({P[i]}/{Q1[i]}) = {P[i]}·{np.log(P[i]/Q1[i]):.4f} = {term:.4f}")
print(f"    TOTAL: KL(P||Q1) = {total:.4f}")

# KL(P || Q2) paso a paso
print(f"\n  KL(P || Q2) paso a paso:")
total2 = 0
for i in range(len(P)):
    term = P[i] * np.log(P[i] / Q2[i])
    total2 += term
    print(f"    P[{i}]·log(P[{i}]/Q2[{i}]) = {P[i]}·log({P[i]}/{Q2[i]}) = {P[i]}·{np.log(P[i]/Q2[i]):.4f} = {term:.4f}")
print(f"    TOTAL: KL(P||Q2) = {total2:.4f}")

# KL(Q1 || P) — para mostrar asimetría
print(f"\n  KL(Q1 || P) paso a paso:")
total3 = 0
for i in range(len(P)):
    term = Q1[i] * np.log(Q1[i] / P[i])
    total3 += term
    print(f"    Q1[{i}]·log(Q1[{i}]/P[{i}]) = {Q1[i]}·log({Q1[i]}/{P[i]}) = {Q1[i]}·{np.log(Q1[i]/P[i]):.4f} = {term:.4f}")
print(f"    TOTAL: KL(Q1||P) = {total3:.4f}")

print(f"""
  RESULTADOS:
    KL(P || Q1) = {total:.4f}  ← Q1 aproxima bien a P
    KL(P || Q2) = {total2:.4f}  ← Q2 aproxima mal a P
    KL(Q1 || P) = {total3:.4f}  ← ¡Diferente de KL(P||Q1)!
    
  ¿KL(P||Q1) == KL(Q1||P)? {'SÍ' if np.isclose(total, total3) else 'NO ← ¡KL NO es simétrica!'}
""")

input("\n[Presiona Enter para continuar...]\n")


# =============================================================================
# PARTE 2: Asimetría visualizada
# =============================================================================
"""
KL(P||Q) ≠ KL(Q||P) porque:

KL(P||Q) — "Forward KL" — Mode Covering:
  Penaliza cuando Q asigna BAJA probabilidad donde P asigna ALTA.
  → "No te olvides de nada importante"
  → Tiende a "cubrir" todos los modos de P (spread out)

KL(Q||P) — "Reverse KL" — Mode Seeking:
  Penaliza cuando Q asigna ALTA probabilidad donde P asigna BAJA.
  → "No inventes cosas falsas"
  → Tiende a concentrarse en UN solo modo de P (collapse)
"""

print(f"\n{'=' * 60}")
print("PARTE 2: Forward KL vs Reverse KL")
print("=" * 60)

# Crear una distribución bimodal P
x = np.linspace(-5, 5, 500)
P_bimodal = 0.5 * np.exp(-0.5 * (x + 2)**2) + 0.5 * np.exp(-0.5 * (x - 2)**2)
P_bimodal = P_bimodal / np.sum(P_bimodal)

# Q que "cubre" ambos modos (forward KL optimal)
Q_covering = np.exp(-0.5 * (x / 2.5)**2)
Q_covering = Q_covering / np.sum(Q_covering)

# Q que se "concentra" en un modo (reverse KL optimal)
Q_seeking = np.exp(-0.5 * (x - 2)**2)
Q_seeking = Q_seeking / np.sum(Q_seeking)

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# P original
axes[0].fill_between(x, P_bimodal * 500, alpha=0.3, color='#4CAF50')
axes[0].plot(x, P_bimodal * 500, linewidth=2, color='#4CAF50', label='P (real)')
axes[0].set_title('P: Distribución Real\n(bimodal)', fontweight='bold')
axes[0].legend()

# Forward KL → mode covering
axes[1].fill_between(x, P_bimodal * 500, alpha=0.2, color='#4CAF50')
axes[1].plot(x, P_bimodal * 500, linewidth=2, color='#4CAF50', label='P')
axes[1].fill_between(x, Q_covering * 500, alpha=0.2, color='#2196F3')
axes[1].plot(x, Q_covering * 500, linewidth=2, color='#2196F3', label='Q (mode covering)')
axes[1].set_title('Forward KL: min KL(P||Q)\n"Cubre" todos los modos', fontweight='bold', color='#2196F3')
axes[1].legend()

# Reverse KL → mode seeking
axes[2].fill_between(x, P_bimodal * 500, alpha=0.2, color='#4CAF50')
axes[2].plot(x, P_bimodal * 500, linewidth=2, color='#4CAF50', label='P')
axes[2].fill_between(x, Q_seeking * 500, alpha=0.2, color='#FF5722')
axes[2].plot(x, Q_seeking * 500, linewidth=2, color='#FF5722', label='Q (mode seeking)')
axes[2].set_title('Reverse KL: min KL(Q||P)\n"Busca" un solo modo', fontweight='bold', color='#FF5722')
axes[2].legend()

plt.suptitle('Asimetría de KL Divergence', fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('challenges/challenge_9_kl_asimetria.png', dpi=100, bbox_inches='tight')
plt.show()


# =============================================================================
# PARTE 3: KL en la práctica — VAEs
# =============================================================================
"""
En un VAE (Variational Autoencoder):
  - El encoder produce q(z|x) ≈ N(μ, σ²) para cada input x
  - Queremos que q(z|x) sea cercana al prior p(z) = N(0, 1)
  - Usamos KL(q(z|x) || p(z)) como regularización

La fórmula cerrada para KL entre dos Gaussianas:
    KL(N(μ, σ²) || N(0, 1)) = -0.5 * Σ(1 + log(σ²) - μ² - σ²)
"""

print(f"\n{'=' * 60}")
print("PARTE 3: KL en VAEs")
print("=" * 60)

def kl_gaussians(mu, log_var):
    """KL divergence entre N(mu, exp(log_var)) y N(0, 1)."""
    return -0.5 * np.sum(1 + log_var - mu**2 - np.exp(log_var))

# Simular diferentes distribuciones del encoder
casos = [
    ("μ=0, σ=1 (exacto al prior)", 0.0, 0.0),          # log(1) = 0
    ("μ=0, σ=0.5 (más estrecha)", 0.0, np.log(0.25)),   # log(0.25)
    ("μ=2, σ=1 (desplazada)", 2.0, 0.0),
    ("μ=0, σ=3 (más ancha)", 0.0, np.log(9)),
    ("μ=3, σ=0.1 (desplazada + estrecha)", 3.0, np.log(0.01)),
]

print(f"\n  {'Caso':45s} | {'KL':>8s}")
print(f"  {'-'*45} | {'-'*8}")
for nombre, mu, lv in casos:
    kl = kl_gaussians(np.array([mu]), np.array([lv]))
    bar = "█" * min(int(kl * 3), 40)
    print(f"  {nombre:45s} | {kl:8.4f}  {bar}")

print("""
  🔑 OBSERVA:
  - KL = 0 cuando q = p exactamente (μ=0, σ=1)
  - Desplazar la media (μ ≠ 0) aumenta KL mucho
  - Cambiar la varianza (σ ≠ 1) también aumenta KL
  - En VAEs, este término "tira" de q hacia N(0,1),
    forzando un espacio latente organizado y continuo
""")


# =============================================================================
# PARTE 4: Relación CE = H + KL
# =============================================================================
"""
Teorema fundamental:
    H(P, Q) = H(P) + KL(P || Q)

Esto significa:
    Cross-Entropy = Entropía + KL Divergence

Como H(P) es constante (depende solo de los datos),
minimizar cross-entropy es EQUIVALENTE a minimizar KL divergence.
"""

print(f"\n{'=' * 60}")
print("PARTE 4: H(P,Q) = H(P) + KL(P||Q)")
print("=" * 60)

def entropia(p):
    p = p[p > 0]
    return -np.sum(p * np.log(p))

def cross_entropy_fn(p, q, eps=1e-15):
    q = np.clip(q, eps, None)
    return -np.sum(p * np.log(q))

def kl_div(p, q, eps=1e-15):
    q = np.clip(q, eps, None)
    mask = p > 0
    return np.sum(p[mask] * np.log(p[mask] / q[mask]))

# Verificar
H_P = entropia(P)
CE_PQ1 = cross_entropy_fn(P, Q1)
KL_PQ1 = kl_div(P, Q1)

print(f"\n  H(P)      = {H_P:.6f}")
print(f"  KL(P||Q1) = {KL_PQ1:.6f}")
print(f"  H(P,Q1)   = {CE_PQ1:.6f}")
print(f"  H(P) + KL = {H_P + KL_PQ1:.6f}")
print(f"\n  ¿H(P,Q) == H(P) + KL(P||Q)? {np.isclose(CE_PQ1, H_P + KL_PQ1)} ← ¡✅ Verificado!")


# =============================================================================
# REFLEXIÓN
# =============================================================================
print(f"""
{'=' * 60}
🧠 REFLEXIÓN
{'=' * 60}

1. ¿Por qué la asimetría de KL importa en la práctica?
   → forward KL (KL(P||Q)): Usado en entrenamiento de modelos generativos
     cuando quieres cubrir TODA la distribución real.
   → reverse KL (KL(Q||P)): Usado en VAEs y destilación, donde prefieres
     que Q sea precisa aunque no cubra todo P.

2. ¿KL puede ser negativa?
   → NO. KL ≥ 0 siempre (desigualdad de Gibbs).
   → Si tu implementación da KL < 0, hay un bug de precisión numérica.

3. ¿Cuándo usar KL vs cross-entropy?
   → Para ENTRENAMIENTO: da igual, son equivalentes.
   → Para COMPARACIÓN entre modelos: KL es más interpretable 
     (0 = perfecto, más alto = peor).
   → Para REGULARIZACIÓN (VAEs): KL directamente.

4. Conexión con RLHF (Fine-tuning de LLMs):
   → Al hacer RLHF, se añade un término KL(π_RL || π_base)
   → Esto evita que el modelo RL se desvíe mucho del modelo base
   → Sin este término, el modelo "olvida" el lenguaje natural

✅ Challenge 9 completado.
   
🎯 ¡Semana 3 completada! Siguiente: proyecto/backprop_from_scratch.py
""")

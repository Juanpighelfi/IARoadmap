"""
=============================================================================
🏆 M3-CHALLENGE 1: Self-Attention Paso a Paso
=============================================================================
Implementar self-attention manualmente con una frase real.
DURACIÓN: ~1.5h | DIFICULTAD: ⭐⭐⭐
=============================================================================
"""
import torch
import torch.nn.functional as F
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 60)
print("🏆 M3-CHALLENGE 1: Self-Attention Paso a Paso")
print("=" * 60)

# --- Setup ---
tokens = ["El", "gato", "se", "sentó", "en", "la", "alfombra", "porque", "estaba", "cansado"]
seq_len = len(tokens)
d_model = 8

torch.manual_seed(42)
embeddings = torch.randn(seq_len, d_model)  # (10, 8)

# Proyecciones Q, K, V
W_q = torch.randn(d_model, d_model) * 0.1
W_k = torch.randn(d_model, d_model) * 0.1
W_v = torch.randn(d_model, d_model) * 0.1

# --- PASO 1: Calcular Q, K, V ---
print("\n--- Paso 1: Q, K, V ---")
Q = embeddings @ W_q  # (10, 8)
K = embeddings @ W_k  # (10, 8)
V = embeddings @ W_v  # (10, 8)
print(f"  Q shape: {Q.shape}")
print(f"  K shape: {K.shape}")
print(f"  V shape: {V.shape}")

# --- PASO 2: Attention scores ---
print("\n--- Paso 2: Attention Scores = softmax(QK^T / √d_k) ---")
d_k = d_model

# CON scaling
scores_scaled = (Q @ K.T) / np.sqrt(d_k)  # (10, 10)
weights_scaled = F.softmax(scores_scaled, dim=-1)

# SIN scaling
scores_raw = Q @ K.T
weights_raw = F.softmax(scores_raw, dim=-1)

print(f"  Score matrix shape: {scores_scaled.shape}")
print(f"  Con √d_k: weights max={weights_scaled.max():.4f}, min={weights_scaled.min():.4f}")
print(f"  Sin √d_k: weights max={weights_raw.max():.4f}, min={weights_raw.min():.4f}")
print(f"  → Sin scaling, softmax se SATURA (un peso ≈ 1, resto ≈ 0)")

# Visualizar
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
for ax, w, title in [(axes[0], weights_scaled, 'Con √d_k (correcto)'),
                       (axes[1], weights_raw, 'Sin √d_k (saturado)')]:
    im = ax.imshow(w.detach().numpy(), cmap='Blues', aspect='auto')
    ax.set_xticks(range(seq_len)); ax.set_xticklabels(tokens, rotation=45, ha='right', fontsize=8)
    ax.set_yticks(range(seq_len)); ax.set_yticklabels(tokens, fontsize=8)
    ax.set_title(title, fontweight='bold')
    plt.colorbar(im, ax=ax, shrink=0.8)

plt.suptitle('Self-Attention Weights', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('challenges/m3_ch1_attention.png', dpi=100, bbox_inches='tight')
plt.close()

# --- PASO 3: Output ---
print("\n--- Paso 3: Output = weights @ V ---")
output = weights_scaled @ V  # (10, 8)
print(f"  Output shape: {output.shape}")
print(f"  ¿Misma dimensión que input? {output.shape == embeddings.shape}")

# --- PASO 4: Causal Mask (para decoders) ---
print(f"\n{'='*60}")
print("--- Paso 4: Causal Mask (Decoder) ---")
print("=" * 60)

mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1).bool()
scores_masked = scores_scaled.clone()
scores_masked.masked_fill_(mask, float('-inf'))
weights_causal = F.softmax(scores_masked, dim=-1)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].imshow(mask.float().numpy(), cmap='Reds', aspect='auto')
axes[0].set_title('Causal Mask (rojo = bloqueado)', fontweight='bold')
axes[0].set_xticks(range(seq_len)); axes[0].set_xticklabels(tokens, rotation=45, ha='right', fontsize=8)
axes[0].set_yticks(range(seq_len)); axes[0].set_yticklabels(tokens, fontsize=8)

im = axes[1].imshow(weights_causal.detach().numpy(), cmap='Blues', aspect='auto')
axes[1].set_title('Masked Self-Attention', fontweight='bold')
axes[1].set_xticks(range(seq_len)); axes[1].set_xticklabels(tokens, rotation=45, ha='right', fontsize=8)
axes[1].set_yticks(range(seq_len)); axes[1].set_yticklabels(tokens, fontsize=8)
plt.colorbar(im, ax=axes[1], shrink=0.8)

plt.tight_layout()
plt.savefig('challenges/m3_ch1_causal.png', dpi=100, bbox_inches='tight')
plt.close()
print("  Causal mask: cada token solo atiende a los ANTERIORES ← AUTOREGRESIVO")

print(f"""
{'='*60}
🧠 REFLEXIÓN
{'='*60}
  1. ¿Por qué dividir por √d_k?
     → QK^T tiene varianza ∝ d_k. Sin normalizar, softmax se satura
       y los gradientes se hacen muy pequeños.
  
  2. ¿Self-attention tiene parámetros que aprender?
     → SÍ: W_q, W_k, W_v (3 × d_model × d_model parámetros)
  
  3. ¿Cuál es la complejidad de self-attention?
     → O(n² · d) donde n=seq_len. Para GPT-4 con 128K tokens: ¡ENORME!
     → Soluciones: Flash Attention, Sparse Attention, Sliding Window.

✅ M3-Challenge 1 completado.
""")

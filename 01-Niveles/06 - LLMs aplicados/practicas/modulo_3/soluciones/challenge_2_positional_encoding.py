"""
=============================================================================
🏆 M3-CHALLENGE 2: Positional Encoding y Masked Attention
=============================================================================
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
print("🏆 M3-CHALLENGE 2: Positional Encoding")
print("=" * 60)

# --- Positional Encoding sinusoidal ---
def positional_encoding(max_len, d_model):
    """
    PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
    PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
    """
    pe = torch.zeros(max_len, d_model)
    pos = torch.arange(0, max_len).unsqueeze(1).float()
    div_term = torch.exp(torch.arange(0, d_model, 2).float() * -(np.log(10000.0) / d_model))
    
    pe[:, 0::2] = torch.sin(pos * div_term)  # dimensiones pares
    pe[:, 1::2] = torch.cos(pos * div_term)  # dimensiones impares
    return pe

PE = positional_encoding(100, 64)
print(f"  PE shape: {PE.shape} (100 posiciones × 64 dimensiones)")

# Visualizar como heatmap
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].imshow(PE[:50, :].numpy(), aspect='auto', cmap='RdBu_r')
axes[0].set_xlabel('Dimensión'); axes[0].set_ylabel('Posición')
axes[0].set_title('Positional Encoding (50 posiciones)', fontweight='bold')

# Similitud coseno entre posiciones
cos_sim = F.cosine_similarity(PE.unsqueeze(1), PE.unsqueeze(0), dim=2)
axes[1].imshow(cos_sim[:30, :30].numpy(), cmap='viridis', aspect='equal')
axes[1].set_xlabel('Posición'); axes[1].set_ylabel('Posición')
axes[1].set_title('Similitud Coseno entre Posiciones', fontweight='bold')
plt.colorbar(axes[1].images[0], ax=axes[1], shrink=0.8)

plt.tight_layout()
plt.savefig('challenges/m3_ch2_pe.png', dpi=100, bbox_inches='tight')
plt.close()

# Similitudes específicas
pairs = [(0, 1), (0, 5), (0, 50), (0, 99)]
print(f"\n  Similitud coseno entre posiciones:")
for i, j in pairs:
    sim = F.cosine_similarity(PE[i].unsqueeze(0), PE[j].unsqueeze(0)).item()
    print(f"    pos({i}, {j}): {sim:.4f}")
print("  → Posiciones cercanas: alta similitud. Lejanas: baja.")

# --- Sin PE, mismo significado ---
print(f"\n{'='*60}")
print("--- Sin PE: el orden se pierde ---")
print("=" * 60)

tokens_1 = torch.randn(3, 8)  # "ABC"
tokens_2 = tokens_1[[2, 0, 1]]  # "CAB" (permutado)

W_q = torch.randn(8, 8) * 0.1
W_k = torch.randn(8, 8) * 0.1

scores_1 = F.softmax(tokens_1 @ W_q @ (tokens_1 @ W_k).T / np.sqrt(8), dim=-1)
scores_2 = F.softmax(tokens_2 @ W_q @ (tokens_2 @ W_k).T / np.sqrt(8), dim=-1)

# Los scores SON DISTINTOS en posición, pero la "relación" entre tokens es la misma
print(f"  Sin PE: attention de 'ABC':")
print(f"  {scores_1.detach().numpy().round(3)}")
print(f"  Sin PE: attention de 'CAB':")
print(f"  {scores_2.detach().numpy().round(3)}")
print(f"  → Sin PE, self-attention es permutation EQUIVARIANT")
print(f"  → CON PE, cada posición tiene una identidad única")

print("\n✅ M3-Challenge 2 completado.")

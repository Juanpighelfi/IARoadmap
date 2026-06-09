"""
=============================================================================
🏆 M3-CHALLENGE 3: Multi-Head Attention desde Cero
=============================================================================
Implementar MHA y verificar contra nn.MultiheadAttention.
DURACIÓN: ~2h | DIFICULTAD: ⭐⭐⭐⭐

HINTS: Si te trabás, consultá modulo_3/hints/hint_challenge_3.md
=============================================================================
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

print("=" * 60)
print("🏆 M3-CHALLENGE 3: Multi-Head Attention desde Cero")
print("=" * 60)

class MyMultiHeadAttention(nn.Module):
    """
    TODO: Implementa Multi-Head Attention desde cero.
    
    Pasos:
    1. Proyectar input a Q, K, V con matrices lineales (W_q, W_k, W_v)
    2. Split Q, K, V en n_heads cabezas
    3. Calcular atención escalada por cada cabeza
    4. Concatenar salidas + proyección final (W_o)
    
    Shapes:
      Input:  (batch, seq_len, d_model)
      Q,K,V:  (batch, n_heads, seq_len, d_k)  donde d_k = d_model / n_heads
      Output: (batch, seq_len, d_model)
    """
    def __init__(self, d_model, n_heads, dropout=0.0):
        super().__init__()
        assert d_model % n_heads == 0, "d_model debe ser divisible por n_heads"
        
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_model // n_heads
        
        # TODO: Crea las 4 proyecciones lineales
        self.W_q = ...  # nn.Linear(d_model, d_model)
        self.W_k = ...
        self.W_v = ...
        self.W_o = ...  # Proyección de salida
        
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, query, key, value, mask=None):
        batch_size = query.size(0)
        seq_len = query.size(1)
        
        # TODO 1: Proyectar
        Q = ...  # self.W_q(query)
        K = ...
        V = ...
        
        # TODO 2: Split en cabezas: (B, seq, d_model) → (B, n_heads, seq, d_k)
        # Q = Q.view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)
        Q = ...
        K = ...
        V = ...
        
        # TODO 3: Scaled Dot-Product Attention
        # scores = Q @ K^T / √d_k
        scores = ...
        
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float('-inf'))
        
        attn_weights = F.softmax(scores, dim=-1)
        attn_weights = self.dropout(attn_weights)
        
        # context = weights @ V
        context = ...  # torch.matmul(attn_weights, V)
        
        # TODO 4: Concatenar cabezas: (B, n_heads, seq, d_k) → (B, seq, d_model)
        # context = context.transpose(1, 2).contiguous().view(batch_size, -1, self.d_model)
        context = ...
        
        # TODO 5: Proyección final
        output = ...  # self.W_o(context)
        
        return output, attn_weights

# --- Test ---
d_model, n_heads = 64, 8
batch_size, seq_len = 2, 10

mha = MyMultiHeadAttention(d_model, n_heads)
x = torch.randn(batch_size, seq_len, d_model)

output, attn_weights = mha(x, x, x)  # Self-attention
print(f"\n  Config: d_model={d_model}, n_heads={n_heads}, d_k={d_model//n_heads}")
print(f"  Input:   {x.shape}")
print(f"  Output:  {output.shape}")
print(f"  Weights: {attn_weights.shape}  (B, heads, seq, seq)")
print(f"  Params:  {sum(p.numel() for p in mha.parameters()):,}")

# --- Comparar con PyTorch oficial ---
print(f"\n{'='*60}")
print("--- Comparación con nn.MultiheadAttention ---")
print("=" * 60)

official = nn.MultiheadAttention(d_model, n_heads, batch_first=True)
out_official, weights_official = official(x, x, x)

print(f"  Oficial output:  {out_official.shape}")
print(f"  Mi output:       {output.shape} ✅ shapes coinciden")

# --- Con causal mask ---
print(f"\n{'='*60}")
print("--- Con Causal Mask (Decoder) ---")
print("=" * 60)

causal_mask = torch.tril(torch.ones(seq_len, seq_len)).unsqueeze(0).unsqueeze(0)
output_masked, weights_masked = mha(x, x, x, mask=causal_mask)
print(f"  Masked output: {output_masked.shape}")

# --- TODO: Transformer Encoder Layer completo ---
print(f"\n{'='*60}")
print("--- TransformerEncoderLayer ---")
print("=" * 60)

class MyTransformerEncoderLayer(nn.Module):
    """
    TODO: Implementa: Self-Attn → Add&Norm → FFN → Add&Norm
    
    FFN = Linear(d_model, d_ff) → GELU → Dropout → Linear(d_ff, d_model) → Dropout
    """
    def __init__(self, d_model, n_heads, d_ff, dropout=0.1):
        super().__init__()
        # TODO: Implementa los componentes
        self.self_attn = ...  # MyMultiHeadAttention(...)
        self.norm1 = ...      # nn.LayerNorm(d_model)
        self.norm2 = ...      # nn.LayerNorm(d_model)
        self.ffn = ...        # nn.Sequential(Linear, GELU, Dropout, Linear, Dropout)
    
    def forward(self, x):
        # TODO: Self-attention + residual + norm
        # attn_out, _ = self.self_attn(x, x, x)
        # x = self.norm1(x + attn_out)
        # FFN + residual + norm
        # ffn_out = self.ffn(x)
        # x = self.norm2(x + ffn_out)
        pass  # Tu código aquí

encoder_layer = MyTransformerEncoderLayer(d_model=64, n_heads=8, d_ff=256)
x_enc = torch.randn(2, 10, 64)
out_enc = encoder_layer(x_enc)
print(f"  Input:  {x_enc.shape}")
print(f"  Output: {out_enc.shape}")
print(f"  Params: {sum(p.numel() for p in encoder_layer.parameters()):,}")

print(f"""
{'='*60}
🧠 REFLEXIÓN
{'='*60}
  1. Multi-Head: 8 cabezas × d_k=8 = d_model=64

  2. Params: MHA tiene 4×d_model² (Q, K, V, Output)

  3. Pre-norm vs Post-norm

  4. FFN es donde el modelo "procesa" la información

✅ M3-Challenge 3 completado. → Proyecto: Transformer completo
""")

"""
=============================================================================
M4-CHALLENGE 2: LoRA Manual
=============================================================================
Implementar LoRA desde cero (sin peft), entender la matemática.
DURACIÓN: ~1.5h | DIFICULTAD: ⭐⭐⭐⭐

HINTS: Si te trabás, consultá modulo_4/hints/hint_challenge_2.md
=============================================================================
"""
import torch
import torch.nn as nn
import numpy as np

print("=" * 60)
print("M4-CHALLENGE 2: LoRA Manual")
print("=" * 60)

# --- Parte 1: Matemática de LoRA ---
print("\n--- Parte 1: Matemática de LoRA ---")

"""
TODO: Calcula cuántos parámetros tiene LoRA vs fine-tuning completo.
  Full Linear(d, d): d² parámetros
  LoRA con rango r:  d*r + r*d = 2*d*r parámetros
"""

d = 4096  # dimensión típica de un LLM
r_values = [1, 4, 8, 16, 64, 256, 4096]

print(f"\n  Full Linear({d},{d}): {d*d:,} params")
print(f"\n  {'r':>6s} | {'LoRA params':>12s} | {'% del full':>10s} | {'Compresión':>10s}")
print(f"  {'-'*6} | {'-'*12} | {'-'*10} | {'-'*10}")
for r in r_values:
    lora_params = ...  # Tu cálculo: d*r + r*d
    pct = ...          # lora_params / (d*d) * 100
    print(f"  {r:6d} | {lora_params:>12,} | {pct:>9.2f}% | {d*d/lora_params:>9.0f}x")


# --- Parte 2: Implementación ---
print(f"\n{'='*60}")
print("--- Parte 2: LoRALinear desde cero ---")
print("=" * 60)

class LoRALinear(nn.Module):
    """
    TODO: Implementa Linear layer con adaptador LoRA.
    
    Original:  y = Wx
    Con LoRA:  y = Wx + (alpha/r) * BAx
    
    Donde:
    - W: pesos originales CONGELADOS (no se entrenan)
    - A: (d_in, r) inicializado con valores pequeños
    - B: (r, d_out) inicializado con ZEROS
    - alpha: factor de escala
    
    ¿Por qué B se inicializa con zeros?
    → Al inicio, BA = 0, así que y = Wx (sin cambio)
    → El modelo empieza idéntico al preentrenado
    """
    def __init__(self, original_linear, r=8, alpha=16):
        super().__init__()
        self.original = original_linear
        # TODO: Congela los pesos originales
        # self.original.weight.requires_grad = False
        
        d_in = original_linear.in_features
        d_out = original_linear.out_features
        self.r = r
        self.alpha = alpha
        self.scaling = alpha / r
        
        # TODO: Crea las matrices LoRA A y B
        self.A = ...  # nn.Parameter(torch.randn(d_in, r) * 0.01)
        self.B = ...  # nn.Parameter(torch.zeros(r, d_out))  ← ¡ZEROS!
    
    def forward(self, x):
        """
        TODO: Implementa el forward pass.
        y = original(x) + (x @ A @ B) * scaling
        """
        pass  # Tu código aquí
    
    def merge(self):
        """
        TODO: Fusiona LoRA en los pesos originales (para inferencia sin overhead).
        W_new = W + (B^T @ A^T) * scaling
        """
        pass  # Tu código aquí


# --- Test ---
print("\n  Creando LoRA...")
original = nn.Linear(512, 512)
lora = LoRALinear(original, r=8, alpha=16)

# Verificar que output es idéntico al inicio (B=0)
x = torch.randn(4, 512)
with torch.no_grad():
    out_original = original(x)
    out_lora = lora(x)

print(f"  Output idéntico al inicio (B=0)? {torch.allclose(out_original, out_lora, atol=1e-6)}")

# Contar parámetros
total = sum(p.numel() for p in lora.parameters())
trainable = sum(p.numel() for p in lora.parameters() if p.requires_grad)
frozen = total - trainable

print(f"\n  Total params:       {total:>10,}")
print(f"  Entrenables (LoRA): {trainable:>10,}  (A + B)")
print(f"  Congelados (W):     {frozen:>10,}")
print(f"  Ratio:              {trainable/total*100:.2f}%")

# Simular "entrenamiento"
print(f"\n--- Simulando entrenamiento ---")
optimizer = torch.optim.AdamW([p for p in lora.parameters() if p.requires_grad], lr=1e-3)
target = torch.randn(4, 512)

for step in range(100):
    optimizer.zero_grad()
    out = lora(x)
    loss = nn.MSELoss()(out, target)
    loss.backward()
    optimizer.step()
    if step % 25 == 0:
        print(f"  Step {step}: loss = {loss.item():.4f}")

print(f"\n  B ya no es zero: max(|B|) = {lora.B.abs().max().item():.6f}")

# Merge para inferencia
print(f"\n--- Merge para inferencia ---")
merged = lora.merge()
out_merged = merged(x)
print(f"  Merged output shape: {out_merged.shape}")
print(f"  Ahora es un nn.Linear normal, sin overhead de LoRA")

print("\nM4-Challenge 2 completado.")

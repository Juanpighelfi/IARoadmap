"""
=============================================================================
M4-CHALLENGE 2: LoRA Manual
=============================================================================
Implementar LoRA desde cero (sin peft), entender la matematica.
DURACION: ~1.5h | DIFICULTAD: 4/5
=============================================================================
"""
import torch
import torch.nn as nn
import numpy as np

print("=" * 60)
print("M4-CHALLENGE 2: LoRA Manual")
print("=" * 60)

# --- Calculo de parametros ---
print("\n--- Parte 1: Matematica de LoRA ---")

d = 4096  # dimension tipica de un LLM
r_values = [1, 4, 8, 16, 64, 256, 4096]

print(f"\n  Full Linear({d},{d}): {d*d:,} params")
print(f"\n  {'r':>6s} | {'LoRA params':>12s} | {'% del full':>10s} | {'Compresion':>10s}")
print(f"  {'-'*6} | {'-'*12} | {'-'*10} | {'-'*10}")
for r in r_values:
    lora_params = d * r + r * d  # A: d*r + B: r*d
    pct = lora_params / (d * d) * 100
    print(f"  {r:6d} | {lora_params:>12,} | {pct:>9.2f}% | {d*d/lora_params:>9.0f}x")

print(f"\n  Cuando r=d, LoRA params = 2*d^2 > d^2  (PEOR que full!)")
print(f"  Sweet spot: r=8-16 para la mayoria de tareas")


# --- Implementacion ---
print(f"\n{'='*60}")
print("--- Parte 2: LoRALinear desde cero ---")
print("=" * 60)

class LoRALinear(nn.Module):
    """
    Linear layer con adaptador LoRA.
    
    Original:  y = Wx
    Con LoRA:  y = Wx + (alpha/r) * BAx
    
    Donde:
    - W: pesos originales CONGELADOS (no se entrenan)
    - A: (d_in, r) inicializado con Kaiming normal
    - B: (r, d_out) inicializado con ZEROS
    - alpha: factor de escala
    
    Por que B se inicializa con zeros?
    -> Al inicio, BA = 0, asi que y = Wx (sin cambio)
    -> El modelo empieza identico al preentrenado
    -> Gradualmente aprende el "delta" necesario
    """
    def __init__(self, original_linear, r=8, alpha=16):
        super().__init__()
        self.original = original_linear
        self.original.weight.requires_grad = False  # Congelar W
        if self.original.bias is not None:
            self.original.bias.requires_grad = False
        
        d_in = original_linear.in_features
        d_out = original_linear.out_features
        self.r = r
        self.alpha = alpha
        self.scaling = alpha / r
        
        # LoRA matrices
        self.A = nn.Parameter(torch.randn(d_in, r) * 0.01)   # Kaiming-like
        self.B = nn.Parameter(torch.zeros(r, d_out))           # Zeros!
    
    def forward(self, x):
        # Original output (no gradients for W)
        original_out = self.original(x)
        # LoRA delta
        lora_out = (x @ self.A @ self.B) * self.scaling
        return original_out + lora_out
    
    def merge(self):
        """Fusionar LoRA en los pesos originales (para inferencia sin overhead)."""
        with torch.no_grad():
            self.original.weight += (self.B.T @ self.A.T) * self.scaling
        return self.original


# --- Test ---
print("\n  Creando LoRA...")
original = nn.Linear(512, 512)
lora = LoRALinear(original, r=8, alpha=16)

# Verificar que output es identico al inicio (B=0)
x = torch.randn(4, 512)
with torch.no_grad():
    out_original = original(x)
    out_lora = lora(x)

print(f"  Output identico al inicio (B=0)? {torch.allclose(out_original, out_lora, atol=1e-6)}")

# Contar parametros
total = sum(p.numel() for p in lora.parameters())
trainable = sum(p.numel() for p in lora.parameters() if p.requires_grad)
frozen = total - trainable

print(f"\n  Total params:      {total:>10,}")
print(f"  Entrenables (LoRA): {trainable:>10,}  (A + B)")
print(f"  Congelados (W):    {frozen:>10,}")
print(f"  Ratio:             {trainable/total*100:.2f}%")

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

# Verificar que B ya no es zero
print(f"\n  B ya no es zero: max(|B|) = {lora.B.abs().max().item():.6f}")

# Merge para inferencia
print(f"\n--- Merge para inferencia ---")
merged = lora.merge()
out_merged = merged(x)
print(f"  Merged output shape: {out_merged.shape}")
print(f"  Ahora es un nn.Linear normal, sin overhead de LoRA")


# --- Que capas reciben LoRA? ---
print(f"\n{'='*60}")
print("--- Parte 3: Que capas reciben LoRA? ---")
print("=" * 60)

print("""
  En la practica (LLaMA, Mistral, etc.):
  
  Capas que SIEMPRE reciben LoRA:
    - q_proj (Query projection)    -> afecta QUE busca el modelo
    - v_proj (Value projection)    -> afecta QUE informacion extrae
  
  Capas que A VECES reciben LoRA:
    - k_proj (Key projection)      -> afecta COMO se indexa
    - o_proj (Output projection)   -> afecta COMO se combina
    - gate_proj, up_proj, down_proj -> FFN layers
  
  Capas que NUNCA reciben LoRA:
    - Embeddings (son lookup tables, no lineales)
    - LayerNorm (pocos parametros, ya se entrenan rapido)
  
  Regla: mas capas con LoRA = mas capacidad = mas VRAM
""")

print("\nM4-Challenge 2 completado.")

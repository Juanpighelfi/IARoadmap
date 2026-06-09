"""
=============================================================================
🏆 CHALLENGE 2 (M1): nn.Module y Custom Layers
=============================================================================
DURACIÓN: ~1.5h | DIFICULTAD: ⭐⭐⭐

HINTS: Si te trabás, consultá modulo_1/hints/hint_challenge_2.md
=============================================================================
"""
import torch
import torch.nn as nn
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 60)
print("🏆 M1-CHALLENGE 2: nn.Module y Custom Layers")
print("=" * 60)

# --- DESAFÍO 1: Activación Swish custom ---
print("\n--- Desafío 1: SwishActivation ---")

"""
TODO: Implementa Swish(x) = x * sigmoid(x)
Swish fue usada en EfficientNet y reemplaza a ReLU en muchos modelos modernos.
"""

class SwishActivation(nn.Module):
    """TODO: Implementa forward(self, x) que retorne x * sigmoid(x)."""
    def forward(self, x):
        pass  # Tu código aquí

# Visualizar Swish vs ReLU
x = torch.linspace(-5, 5, 200)
swish = SwishActivation()
relu = nn.ReLU()

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(x.numpy(), swish(x).detach().numpy(), label='Swish', linewidth=2)
axes[0].plot(x.numpy(), relu(x).detach().numpy(), label='ReLU', linewidth=2)
axes[0].legend(); axes[0].set_title('Función')
axes[0].axhline(y=0, color='k', linewidth=0.3)

x_g = x.clone().requires_grad_(True)
s_out = swish(x_g).sum(); s_out.backward()
s_grad = x_g.grad.clone()
x_g2 = x.clone().requires_grad_(True)
r_out = relu(x_g2).sum(); r_out.backward()
r_grad = x_g2.grad.clone()

axes[1].plot(x.numpy(), s_grad.numpy(), label="Swish'", linewidth=2)
axes[1].plot(x.numpy(), r_grad.numpy(), label="ReLU'", linewidth=2)
axes[1].legend(); axes[1].set_title('Derivada')
plt.tight_layout()
plt.savefig('challenges/m1_ch2_activations.png', dpi=100, bbox_inches='tight')
plt.close()
print("  Gráfico guardado.")

# --- DESAFÍO 2: ResidualBlock ---
print("\n--- Desafío 2: ResidualBlock ---")

"""
TODO: Implementa un bloque residual:
  Input → Linear → BN → ReLU → Linear → BN → (+Input) → ReLU
  
La skip connection (+Input) es lo que hace a ResNet tan poderosa.
"""

class ResidualBlock(nn.Module):
    """TODO: Implementa __init__ y forward con skip connection."""
    def __init__(self, dim):
        super().__init__()
        # TODO: Crea el bloque secuencial: Linear → BN → ReLU → Linear → BN
        self.block = ...  # Tu código aquí
        self.relu = nn.ReLU()
    
    def forward(self, x):
        # TODO: return self.relu(self.block(x) + x)  ← la skip connection!
        pass  # Tu código aquí

"""
TODO: Implementa MiniResNet que apila 3 ResidualBlocks.
Arquitectura: project(input→hidden) → 3×ResidualBlock → classifier(hidden→classes)
"""

class MiniResNet(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_classes):
        super().__init__()
        # TODO: Implementa la arquitectura
        self.project = ...  # nn.Linear(input_dim, hidden_dim)
        self.blocks = ...   # nn.Sequential(3 ResidualBlocks)
        self.classifier = ...  # nn.Linear(hidden_dim, num_classes)
    
    def forward(self, x):
        # TODO: project → blocks → classifier
        pass  # Tu código aquí

model = MiniResNet(784, 128, 10)
print(f"  MiniResNet params: {sum(p.numel() for p in model.parameters()):,}")

# Test forward
dummy = torch.randn(4, 784)
out = model(dummy)
print(f"  Forward test: input={dummy.shape} → output={out.shape}")

# --- DESAFÍO 3: Inspección de parámetros ---
print("\n--- Desafío 3: Inspección de modelos ---")
total = 0
for name, p in model.named_parameters():
    total += p.numel()
    print(f"  {name:45s} {str(list(p.shape)):20s} → {p.numel():>8,}")
print(f"  {'TOTAL':45s} {'':20s} → {total:>8,}")

print("\n✅ M1-Challenge 2 completado.")

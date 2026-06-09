"""
=============================================================================
🏆 CHALLENGE 2 (M1): nn.Module y Custom Layers
=============================================================================
DURACIÓN: ~1.5h | DIFICULTAD: ⭐⭐⭐
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

class SwishActivation(nn.Module):
    """Swish(x) = x * sigmoid(x) — usada en EfficientNet."""
    def forward(self, x):
        return x * torch.sigmoid(x)

# Visualizar Swish vs ReLU
x = torch.linspace(-5, 5, 200)
swish = SwishActivation()
relu = nn.ReLU()

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(x.numpy(), swish(x).detach().numpy(), label='Swish', linewidth=2)
axes[0].plot(x.numpy(), relu(x).detach().numpy(), label='ReLU', linewidth=2)
axes[0].legend(); axes[0].set_title('Función')
axes[0].axhline(y=0, color='k', linewidth=0.3)

# Derivadas
x_g = x.clone().requires_grad_(True)
s_out = swish(x_g).sum(); s_out.backward()
s_grad = x_g.grad.clone()
x_g2 = x.clone().requires_grad_(True)
r_out = relu(x_g2).sum(); r_out.backward()
r_grad = x_g2.grad.clone()

axes[1].plot(x.numpy(), s_grad.numpy(), label="Swish'", linewidth=2)
axes[1].plot(x.numpy(), r_grad.numpy(), label="ReLU'", linewidth=2)
axes[1].legend(); axes[1].set_title('Derivada')
axes[1].axhline(y=0, color='k', linewidth=0.3)
plt.tight_layout()
plt.savefig('challenges/m1_ch2_activations.png', dpi=100, bbox_inches='tight')
plt.close()
print("  Swish es suave, permite gradientes negativos pequeños. Guardado gráfico.")

# --- DESAFÍO 2: ResidualBlock ---
print("\n--- Desafío 2: ResidualBlock ---")

class ResidualBlock(nn.Module):
    """Input → Linear → BN → ReLU → Linear → BN → (+Input) → ReLU"""
    def __init__(self, dim):
        super().__init__()
        self.block = nn.Sequential(
            nn.Linear(dim, dim),
            nn.BatchNorm1d(dim),
            nn.ReLU(),
            nn.Linear(dim, dim),
            nn.BatchNorm1d(dim),
        )
        self.relu = nn.ReLU()
    
    def forward(self, x):
        return self.relu(self.block(x) + x)  # Skip connection

class MiniResNet(nn.Module):
    """3 ResidualBlocks apilados."""
    def __init__(self, input_dim, hidden_dim, num_classes):
        super().__init__()
        self.project = nn.Linear(input_dim, hidden_dim)
        self.blocks = nn.Sequential(
            ResidualBlock(hidden_dim),
            ResidualBlock(hidden_dim),
            ResidualBlock(hidden_dim),
        )
        self.classifier = nn.Linear(hidden_dim, num_classes)
    
    def forward(self, x):
        x = self.project(x)
        x = self.blocks(x)
        return self.classifier(x)

model = MiniResNet(784, 128, 10)
print(f"  Restricción: input_dim == output_dim en cada bloque (para el +x)")
print(f"  MiniResNet params: {sum(p.numel() for p in model.parameters()):,}")

# Test forward
dummy = torch.randn(4, 784)
out = model(dummy)
print(f"  Forward test: input={dummy.shape} → output={out.shape}")

# --- DESAFÍO 3: Inspección ---
print("\n--- Desafío 3: Inspección de modelos ---")
total = 0
for name, p in model.named_parameters():
    total += p.numel()
    print(f"  {name:45s} {str(list(p.shape)):20s} → {p.numel():>8,}")
print(f"  {'TOTAL':45s} {'':20s} → {total:>8,}")

print("\n✅ M1-Challenge 2 completado.")

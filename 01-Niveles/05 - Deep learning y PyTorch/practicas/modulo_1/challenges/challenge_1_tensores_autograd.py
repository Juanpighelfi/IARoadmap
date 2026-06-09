"""
=============================================================================
🏆 CHALLENGE 1 (M1): Tensores y Autograd
=============================================================================
DURACIÓN: ~1.5h | DIFICULTAD: ⭐⭐

HINTS: Si te trabás, consultá modulo_1/hints/hint_challenge_1.md
=============================================================================
"""
import torch
import numpy as np

print("=" * 60)
print("🏆 M1-CHALLENGE 1: Tensores y Autograd")
print("=" * 60)

# --- DESAFÍO 1: Operaciones con tensores ---
print("\n--- Desafío 1: Operaciones con tensores ---")

# TODO a) Crea un tensor 3D de shape (2, 3, 4) con valores aleatorios
t3d = ...  # Tu código aquí
print(f"  a) Tensor 3D: shape={t3d.shape}")

# TODO b) Haz reshape a (6, 4) y a (2, 12)
r1 = ...  # Tu código aquí
r2 = ...  # Tu código aquí
print(f"  b) Reshape (6,4): {r1.shape}, (2,12): {r2.shape}")

# TODO c) Calcula la media por cada dimensión (dim=0, 1, 2)
for dim in range(3):
    m = ...  # Tu código aquí: t3d.mean(dim=dim)
    print(f"  c) mean(dim={dim}): shape={m.shape}")

# TODO d) Demuestra broadcasting: suma un tensor (3,1) + (1,4)
a = torch.randn(3, 1)
b = torch.randn(1, 4)
c = ...  # Tu código aquí
print(f"  d) Broadcasting (3,1)+(1,4) = {c.shape}")

# --- DESAFÍO 2: Autograd manual vs automático ---
print("\n--- Desafío 2: f(x,y) = x²y + sin(y) ---")

"""
TODO: 
  1. Crea tensores x=3.0, y=2.0 con requires_grad=True
  2. Calcula f = x²y + sin(y)
  3. Llama f.backward()
  4. Compara con derivadas analíticas:
     ∂f/∂x = 2xy = 12
     ∂f/∂y = x² + cos(y) ≈ 9.584
"""

x = ...  # torch.tensor([3.0], requires_grad=True)
y = ...  # torch.tensor([2.0], requires_grad=True)
f = ...  # x**2 * y + torch.sin(y)
# TODO: f.backward()

df_dx_expected = 2 * 3.0 * 2.0
df_dy_expected = 9.0 + np.cos(2.0)

print(f"  f(3,2) = {f.item():.4f}")
print(f"  ∂f/∂x: analítico={df_dx_expected:.4f}, autograd={x.grad.item():.4f} ✅={np.isclose(df_dx_expected, x.grad.item())}")
print(f"  ∂f/∂y: analítico={df_dy_expected:.4f}, autograd={y.grad.item():.4f} ✅={np.isclose(df_dy_expected, y.grad.item())}")

# TODO: Derivada segunda de f(x) = x³ + 2x → f''(2) = 6x = 12
# Usa torch.autograd.grad con create_graph=True
x2 = torch.tensor([2.0], requires_grad=True)
f2 = x2**3 + 2*x2
grad1 = ...  # torch.autograd.grad(f2, x2, create_graph=True)[0]
grad2 = ...  # torch.autograd.grad(grad1, x2)[0]
print(f"\n  f''(2) analítico = 12, autograd = {grad2.item()}")

# --- DESAFÍO 3: Trampas de autograd ---
print("\n--- Desafío 3: ¿Cuándo se rompe autograd? ---")

# TODO a) Demuestra que operaciones in-place rompen el grafo
try:
    xi = torch.tensor([2.0], requires_grad=True)
    yi = xi ** 2
    xi.add_(1)  # in-place
    yi.backward()
except RuntimeError:
    print("  a) In-place: ✅ RuntimeError (esperado)")

# TODO b) Demuestra la acumulación de gradientes (bug más común)
xa = torch.tensor([2.0], requires_grad=True)
for i in range(3):
    ya = xa ** 2
    ya.backward()
print(f"  b) Sin zero_grad, grad acumula: {xa.grad.item()} (debería ser 4, es {4*(3)})")

# TODO c) Demuestra .detach()
xd = torch.tensor([2.0], requires_grad=True)
yd = xd ** 2
zd = yd.detach()
print(f"  c) detach(): zd.requires_grad = {zd.requires_grad} (desconectado)")

print("\n✅ M1-Challenge 1 completado.")

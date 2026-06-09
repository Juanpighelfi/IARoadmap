"""
=============================================================================
🏆 CHALLENGE 1 (M1): Tensores y Autograd
=============================================================================
DURACIÓN: ~1.5h | DIFICULTAD: ⭐⭐
=============================================================================
"""
import torch
import numpy as np

print("=" * 60)
print("🏆 M1-CHALLENGE 1: Tensores y Autograd")
print("=" * 60)

# --- DESAFÍO 1: Operaciones con tensores ---
print("\n--- Desafío 1: Operaciones con tensores ---")

# a) Tensor 3D
t3d = torch.randn(2, 3, 4)
print(f"  a) Tensor 3D: shape={t3d.shape}")

# b) Reshape
r1 = t3d.reshape(6, 4)
r2 = t3d.reshape(2, 12)
print(f"  b) Reshape (6,4): {r1.shape}, (2,12): {r2.shape}")

# c) Media por dimensión
for dim in range(3):
    m = t3d.mean(dim=dim)
    print(f"  c) mean(dim={dim}): shape={m.shape}")

# d) Broadcasting
a = torch.randn(3, 1)
b = torch.randn(1, 4)
c = a + b
print(f"  d) Broadcasting (3,1)+(1,4) = {c.shape}")

# --- DESAFÍO 2: Autograd manual vs automático ---
print("\n--- Desafío 2: f(x,y) = x²y + sin(y) ---")

x = torch.tensor([3.0], requires_grad=True)
y = torch.tensor([2.0], requires_grad=True)
f = x**2 * y + torch.sin(y)
f.backward()

# Analítico: df/dx = 2xy, df/dy = x² + cos(y)
df_dx_expected = 2 * 3.0 * 2.0
df_dy_expected = 9.0 + np.cos(2.0)

print(f"  f(3,2) = {f.item():.4f}")
print(f"  ∂f/∂x: analítico={df_dx_expected:.4f}, autograd={x.grad.item():.4f} ✅={np.isclose(df_dx_expected, x.grad.item())}")
print(f"  ∂f/∂y: analítico={df_dy_expected:.4f}, autograd={y.grad.item():.4f} ✅={np.isclose(df_dy_expected, y.grad.item())}")

# Derivada segunda
x2 = torch.tensor([2.0], requires_grad=True)
f2 = x2**3 + 2*x2
grad1 = torch.autograd.grad(f2, x2, create_graph=True)[0]
grad2 = torch.autograd.grad(grad1, x2)[0]
print(f"\n  f(x) = x³+2x → f''(2) = 6x = 12")
print(f"  autograd f''(2) = {grad2.item()}")

# --- DESAFÍO 3: Trampas de autograd ---
print("\n--- Desafío 3: ¿Cuándo se rompe autograd? ---")

# In-place ops
try:
    xi = torch.tensor([2.0], requires_grad=True)
    yi = xi ** 2
    xi.add_(1)
    yi.backward()
except RuntimeError:
    print("  a) In-place: ✅ RuntimeError (esperado)")

# Acumulación de gradientes
xa = torch.tensor([2.0], requires_grad=True)
for i in range(3):
    ya = xa ** 2
    ya.backward()

print(f"  b) Sin zero_grad, grad acumula: {xa.grad.item()} (debería ser 4, es {4*(3)})")

# detach
xd = torch.tensor([2.0], requires_grad=True)
yd = xd ** 2
zd = yd.detach()
print(f"  c) detach(): zd.requires_grad = {zd.requires_grad} (desconectado)")

print("\n✅ M1-Challenge 1 completado.")

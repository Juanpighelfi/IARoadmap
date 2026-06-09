"""
=============================================================================
🏆 CHALLENGE 5: Verificación con PyTorch Autograd
=============================================================================

OBJETIVO: Verificar tus gradientes manuales del Challenge 4 usando PyTorch
          autograd. Aprender cómo funciona el sistema de diferenciación
          automática.

CONCEPTO: PyTorch construye un grafo computacional dinámico (DAG).
          Cada operación sobre tensores con requires_grad=True se registra.
          Al llamar .backward(), recorre el grafo en reversa calculando gradientes.

DURACIÓN: ~30 minutos
DIFICULTAD: ⭐⭐ (Intermedia)

PRERREQUISITO: Challenge 4 (gradientes manuales)
=============================================================================
"""

import numpy as np
import torch


print("=" * 60)
print("🏆 CHALLENGE 5: Verificación con PyTorch Autograd")
print("=" * 60)

# =============================================================================
# PARTE 1: Misma red del Challenge 4, ahora con PyTorch
# =============================================================================
"""
Red: input (2) → linear → sigmoid → MSE loss
Mismos valores que el Challenge 4 para comparar.
"""

print("\n--- PARTE 1: Reproducir el Challenge 4 con PyTorch ---")

# Crear tensores (mismos valores que Challenge 4)
x_t = torch.tensor([1.0, 2.0])                    # input
W_t = torch.tensor([[0.5, -0.3]], requires_grad=True)  # pesos (necesitan gradiente)
b_t = torch.tensor([0.1], requires_grad=True)          # bias (necesita gradiente)
y_true_t = torch.tensor([0.8])                          # target

# Forward pass
z_t = W_t @ x_t + b_t
a_t = torch.sigmoid(z_t)
loss_t = (a_t - y_true_t) ** 2

print(f"Forward pass (PyTorch):")
print(f"  z = {z_t.item():.6f}")
print(f"  a = {a_t.item():.6f}")
print(f"  L = {loss_t.item():.6f}")

# Backward pass (PyTorch lo hace automáticamente)
loss_t.backward()

print(f"\nGradientes (PyTorch autograd):")
print(f"  dL/dW = {W_t.grad}")
print(f"  dL/db = {b_t.grad}")

# Comparar con gradientes manuales del Challenge 4
print(f"\n--- COMPARACIÓN con gradientes manuales ---")

# Recalcular manualmente (copiado del Challenge 4)
x_np = np.array([1.0, 2.0])
W_np = np.array([[0.5, -0.3]])
b_np = np.array([0.1])
y_true_np = 0.8

z_np = W_np @ x_np + b_np
a_np = 1 / (1 + np.exp(-z_np))
dL_da = 2 * (a_np - y_true_np)
da_dz = a_np * (1 - a_np)
dL_dz = dL_da * da_dz
dL_dW_manual = dL_dz.reshape(-1, 1) @ x_np.reshape(1, -1)
dL_db_manual = dL_dz

print(f"  dL/dW (manual)  = {dL_dW_manual}")
print(f"  dL/dW (PyTorch) = {W_t.grad.numpy()}")
print(f"  ¿Coinciden? {np.allclose(dL_dW_manual, W_t.grad.numpy())}")

print(f"\n  dL/db (manual)  = {dL_db_manual}")
print(f"  dL/db (PyTorch) = {b_t.grad.numpy()}")
print(f"  ¿Coinciden? {np.allclose(dL_db_manual, b_t.grad.numpy())}")


# =============================================================================
# PARTE 2: Función compuesta — f(x, y) = x²y + sin(y)
# =============================================================================
"""
TODO: Calcula las derivadas parciales analíticamente y verifica con autograd.

f(x, y) = x²y + sin(y)

Derivadas analíticas:
  ∂f/∂x = 2xy
  ∂f/∂y = x² + cos(y)
"""

print(f"\n{'=' * 60}")
print("PARTE 2: Función compuesta f(x,y) = x²y + sin(y)")
print("=" * 60)

x2 = torch.tensor([3.0], requires_grad=True)
y2 = torch.tensor([2.0], requires_grad=True)

# Forward
f = x2**2 * y2 + torch.sin(y2)

# Backward
f.backward()

# Analítico
df_dx_analitico = 2 * 3.0 * 2.0  # 2xy
df_dy_analitico = 3.0**2 + np.cos(2.0)  # x² + cos(y)

print(f"\n  f(3, 2) = {f.item():.6f}")
print(f"\n  ∂f/∂x:")
print(f"    Analítico: 2xy = 2·3·2 = {df_dx_analitico}")
print(f"    Autograd:  {x2.grad.item():.6f}")
print(f"    ¿Coinciden? {np.isclose(df_dx_analitico, x2.grad.item())}")

print(f"\n  ∂f/∂y:")
print(f"    Analítico: x²+cos(y) = 9+cos(2) = {df_dy_analitico:.6f}")
print(f"    Autograd:  {y2.grad.item():.6f}")
print(f"    ¿Coinciden? {np.isclose(df_dy_analitico, y2.grad.item())}")


# =============================================================================
# PARTE 3: Derivada segunda (Hessiano)
# =============================================================================
"""
La derivada segunda contiene información sobre la CURVATURA de la loss.
- Curvatura alta = el gradiente cambia rápido = necesitas lr más bajo
- Curvatura baja = el gradiente cambia lento = puedes usar lr más alto

Para calcular ∂²f/∂x² con autograd, necesitas create_graph=True
en el primer .backward() para que el grafo se mantenga.
"""

print(f"\n{'=' * 60}")
print("PARTE 3: Derivada segunda con create_graph=True")
print("=" * 60)

x3 = torch.tensor([2.0], requires_grad=True)

# f(x) = x³ + 2x
f3 = x3**3 + 2*x3
# f'(x) = 3x² + 2
# f''(x) = 6x

# Primera derivada — mantener el grafo para segunda derivada
grad1 = torch.autograd.grad(f3, x3, create_graph=True)[0]

# Segunda derivada
grad2 = torch.autograd.grad(grad1, x3)[0]

print(f"\n  f(x) = x³ + 2x")
print(f"  f(2) = {f3.item()}")

print(f"\n  f'(x) = 3x² + 2")
print(f"  f'(2) analítico = {3*4 + 2}")
print(f"  f'(2) autograd  = {grad1.item()}")

print(f"\n  f''(x) = 6x")
print(f"  f''(2) analítico = {6*2}")
print(f"  f''(2) autograd  = {grad2.item()}")


# =============================================================================
# PARTE 4: ¿Cuándo se rompe autograd?
# =============================================================================
"""
TODO: Experimenta con cada caso y documenta qué pasa.
"""

print(f"\n{'=' * 60}")
print("PARTE 4: Trampas de Autograd — ¡Cuidado!")
print("=" * 60)

# CASO 1: Operaciones in-place
print("\n  CASO 1: Operaciones in-place")
try:
    x_ip = torch.tensor([2.0], requires_grad=True)
    y_ip = x_ip ** 2
    x_ip.add_(1)  # in-place: modifica x directamente
    y_ip.backward()
    print(f"    ❌ Esto NO debería funcionar sin error")
except RuntimeError as e:
    print(f"    ✅ Error esperado: operación in-place rompe el grafo")
    print(f"    Mensaje: {str(e)[:80]}...")

# CASO 2: .numpy() en medio del cómputo
print("\n  CASO 2: .numpy() desconecta del grafo")
x_np2 = torch.tensor([2.0], requires_grad=True)
y_np2 = x_np2 ** 2
try:
    z_np2 = y_np2.detach().numpy()  # Necesitas .detach() primero
    print(f"    ✅ .detach().numpy() funciona: {z_np2}")
    print(f"    PERO: z_np2 ya no está conectado al grafo → no recibirá gradientes")
except RuntimeError as e:
    print(f"    Error: {e}")

# CASO 3: .detach() — desconexión intencional
print("\n  CASO 3: .detach() — desconexión intencional")
x_det = torch.tensor([2.0], requires_grad=True)
y_det = x_det ** 2
z_det = y_det.detach()  # Desconecta del grafo
w_det = z_det * 3       # Esta operación NO se registra para x_det

print(f"    y = x² = {y_det.item()}")
print(f"    z = y.detach() = {z_det.item()} (desconectado)")
print(f"    w = z * 3 = {w_det.item()}")
print(f"    z.requires_grad = {z_det.requires_grad}")  # False
print(f"""
    ¿Cuándo usar .detach()?
    - Para usar un tensor como "constante" en un cómputo
    - Para ahorrar memoria (no registrar operaciones innecesarias)
    - En GANs: para no propagar gradientes al generator cuando entrenas el discriminator
    """)

# CASO 4: Acumulación de gradientes (¡el bug más común!)
print("  CASO 4: Acumulación de gradientes — EL BUG MÁS COMÚN")
x_ac = torch.tensor([2.0], requires_grad=True)

for i in range(3):
    y_ac = x_ac ** 2  # y = 4
    y_ac.backward()
    print(f"    Iteración {i}: grad = {x_ac.grad.item()}")
    # ⚠️ ¡El gradiente se ACUMULA! 4, 8, 12 en vez de 4, 4, 4

# La solución:
print("\n    SOLUCIÓN: usar grad.zero_() al inicio de cada iteración")
x_ac2 = torch.tensor([2.0], requires_grad=True)
for i in range(3):
    if x_ac2.grad is not None:
        x_ac2.grad.zero_()  # ← ESTO ES CRUCIAL
    y_ac2 = x_ac2 ** 2
    y_ac2.backward()
    print(f"    Iteración {i}: grad = {x_ac2.grad.item()}")


# =============================================================================
# REFLEXIÓN
# =============================================================================
print(f"""
{'=' * 60}
🧠 REFLEXIÓN
{'=' * 60}

1. ¿Por qué PyTorch acumula gradientes por defecto?
   → Para soportar mini-batches: puedes hacer forward + backward
     varias veces y LUEGO actualizar (gradient accumulation).
   → Útil cuando tu batch no cabe en memoria de GPU.

2. ¿Qué diferencia hay entre .backward() y torch.autograd.grad()?
   → .backward() acumula gradientes en .grad de cada tensor
   → torch.autograd.grad() retorna los gradientes directamente
   → .grad() es más limpio para cálculos específicos

3. ¿Cuándo NO necesitas tracking de gradientes?
   → Durante evaluación (inference): usa torch.no_grad()
   → Para métricas y logging
   → Esto ahorra memoria y es más rápido

✅ Challenge 5 completado.
   Siguiente: challenge_6_vanishing_gradient.py
""")

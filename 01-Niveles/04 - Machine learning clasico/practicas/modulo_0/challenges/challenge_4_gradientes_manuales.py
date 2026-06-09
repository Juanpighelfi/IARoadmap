"""
=============================================================================
🏆 CHALLENGE 4: Gradientes Manuales — Forward y Backward a Mano
=============================================================================

OBJETIVO: Calcular gradientes manualmente para una red simple de 1 capa
          y verificar que entiendes CADA paso del backward pass.

CONCEPTO: Si no puedes calcular gradientes a mano, no entiendes backprop.
          Este es el ejercicio más importante del módulo.

DURACIÓN: ~45 minutos
DIFICULTAD: ⭐⭐⭐ (Avanzada)

PRERREQUISITO: Guía conceptual 02_calculo_y_gradientes.py

RED: input (2) → linear → sigmoid → MSE loss

HINTS: Si te trabás, consultá modulo_0/hints/hint_challenge_4.md
=============================================================================
"""

from numpy import number
import numpy as np


print("=" * 60)
print("🏆 CHALLENGE 4: Gradientes Manuales")
print("=" * 60)

# =============================================================================
# SETUP: Red de 1 neurona con 2 inputs
# =============================================================================
"""
Arquitectura:
    z = W @ x + b       (transformación lineal)
    a = sigmoid(z)       (activación)
    L = (a - y_true)²   (MSE loss)

Donde:
    x = [1.0, 2.0]      (input, 2 features)
    W = [[0.5, -0.3]]   (pesos, shape 1×2)
    b = [0.1]            (bias)
    y_true = 0.8         (label)
"""

x = np.array([1.0, 2.0])
W = np.array([[0.5, -0.3]])  # shape (1, 2)
b = np.array([0.1])
y_true = 0.8
sigmoid = lambda z: 1 / (1 + np.exp(-z))


# =============================================================================
# PASO 1: FORWARD PASS — Calcula cada valor
# =============================================================================
"""
TODO: Calcula z, a, y loss paso a paso.
  z = W @ x + b
  a = sigmoid(z)
  L = (a - y_true)²
"""

print("\n--- FORWARD PASS ---")

# TODO: z = W @ x + b
z:number = W @ x + b  # Tu código aquí

print(f"z = W @ x + b = {W} @ {x} + {b}")
print(f"  = {z}")

# TODO: a = sigmoid(z)
a = 1 / (1 + np.exp(-z))  # Tu código aquí

print(f"\na = sigmoid(z) = {a}")

# TODO: L = (a - y_true)²
L = np.square(a - y_true)  # Tu código aquí

print(f"\nL = (a - y_true)² = {L}")


# =============================================================================
# PASO 2: BACKWARD PASS — La regla de la cadena, paso a paso
# =============================================================================
"""
Para calcular dL/dW, aplicamos la regla de la cadena:
    dL/dW = dL/da · da/dz · dz/dW

Cada derivada parcial:

1. dL/da = d/da [(a - y)²] = 2(a - y)

2. da/dz = d/dz [sigmoid(z)] = sigmoid(z) · (1 - sigmoid(z)) = a · (1 - a)

3. dz/dW = d/dW [W @ x + b] = x^T
   (la derivada de Wx respecto a W es x)

4. dz/db = d/db [W @ x + b] = 1

TODO: Calcula CADA derivada parcial y luego combínalas.
"""

print("\n--- BACKWARD PASS ---")
print("\nPaso a paso con la regla de la cadena:")

# TODO: dL/da = 2(a - y_true)
dL_da =  2(a - y_true) # Tu código aquí
print(f"\n  1) dL/da = 2(a - y_true) = {dL_da}")

# TODO: da/dz = a * (1 - a)   ← derivada de sigmoid
da_dz = a * (1 - a)  # Tu código aquí
print(f"\n  2) da/dz = a · (1 - a) = {da_dz}")

# TODO: dL/dz = dL/da * da/dz  ← combinar con regla de la cadena
dL_dz = dL_da * da_dz  # Tu código aquí
print(f"\n  3) dL/dz = dL/da · da/dz = {dL_dz}")

# TODO: dL/dW = dL/dz · x^T   ← outer product
# Para cada peso: dL/dW[0,j] = dL/dz · x[j]
dL_dW = dL_da * x.T  # Tu código aquí (pista: dL_dz.reshape(-1, 1) @ x.reshape(1, -1))
print(f"\n  4) dL/dW = {dL_dW}")

# TODO: dL/db = dL/dz
dL_db = dL_dz  # Tu código aquí
print(f"\n  5) dL/db = {dL_db}")


# =============================================================================
# PASO 3: ACTUALIZACIÓN DE PESOS
# =============================================================================

lr = 0.1
W_nuevo = W - lr * dL_dW
b_nuevo = b - lr * dL_db

print(f"\n--- ACTUALIZACIÓN (lr={lr}) ---")
print(f"  W_nuevo = W - lr·dL/dW = {W_nuevo}")
print(f"  b_nuevo = b - lr·dL/db = {b_nuevo}")

# Verificar que la loss baja
z_new = W_nuevo @ x + b_nuevo
a_new = sigmoid(z_new)
L_new = (a_new - y_true) ** 2
print(f"\n  Loss anterior: {L[0]:.6f}")
print(f"  Loss nueva:    {L_new[0]:.6f}")
print(f"  ¿La loss bajó? {'✅ SÍ' if L_new < L else '❌ NO'}")


# =============================================================================
# PASO 4: ENTRENAMIENTO COMPLETO
# =============================================================================
"""
TODO: Implementa un loop de entrenamiento usando tus gradientes manuales.
Repite el forward → backward → update por 1000 epochs.

Para cada epoch:
  1. Forward: z → a → loss
  2. Backward: calcular gradientes
  3. Update: W -= lr * dL_dW, b -= lr * dL_db
"""

print(f"\n{'=' * 60}")
print("ENTRENAMIENTO COMPLETO (gradientes manuales)")
print("=" * 60)

# Reset
W_train = np.array([[0.5, -0.3]])
b_train = np.array([0.1])
lr = 0.5
losses = []

for epoch in range(1000):
    # TODO: Forward
    z = ...
    a = ...
    loss = ...
    losses.append(loss[0])
    
    # TODO: Backward
    dL_da = ...
    da_dz = ...
    dL_dz = ...
    dL_dW = ...
    dL_db = ...
    
    # TODO: Update
    W_train -= lr * dL_dW
    b_train -= lr * dL_db
    
    if epoch < 5 or epoch % 200 == 0 or epoch == 999:
        print(f"  Epoch {epoch:4d}: loss = {loss[0]:.8f}, a = {a[0]:.6f}, W = {W_train[0]}")

print(f"\n  Predicción final: {sigmoid(W_train @ x + b_train)[0]:.6f}")
print(f"  Target: {y_true}")

# Graficar la loss
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(losses, linewidth=2, color='#2196F3')
ax.set_xlabel('Epoch', fontsize=12)
ax.set_ylabel('MSE Loss', fontsize=12)
ax.set_title('Entrenamiento con Gradientes Manuales', fontweight='bold', fontsize=14)
ax.set_yscale('log')
plt.tight_layout()
plt.savefig('challenges/challenge_4_training.png', dpi=100, bbox_inches='tight')
plt.show()


# =============================================================================
# REFLEXIÓN
# =============================================================================
print(f"""
{'=' * 60}
🧠 REFLEXIÓN
{'=' * 60}

1. ¿Qué pasaría si usaras lr=10? ¿Y lr=0.001?

2. ¿Por qué dz/dW = x y no W?

3. ¿Cuántas multiplicaciones hace el backward pass vs el forward pass?

4. En una red de N capas, ¿cuántas reglas de la cadena se aplican?

✅ Challenge 4 completado.
   Siguiente: challenge_5_autograd_verify.py
""")

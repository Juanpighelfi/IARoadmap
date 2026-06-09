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
=============================================================================
"""

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
Llena los valores y verifica que coinciden.
"""

print("\n--- FORWARD PASS ---")

# z = W @ x + b
z = W @ x + b
print(f"z = W @ x + b = {W} @ {x} + {b}")
print(f"  = {W[0,0]}*{x[0]} + {W[0,1]}*{x[1]} + {b[0]}")
print(f"  = {W[0,0]*x[0]} + {W[0,1]*x[1]} + {b[0]}")
print(f"  = {z}")

# a = sigmoid(z)
a = sigmoid(z)
print(f"\na = sigmoid(z) = 1 / (1 + exp(-{z[0]:.4f}))")
print(f"  = {a}")

# L = (a - y_true)²
L = (a - y_true) ** 2
print(f"\nL = (a - y_true)² = ({a[0]:.6f} - {y_true})²")
print(f"  = {L}")


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

# dL/da
dL_da = 2 * (a - y_true)
print(f"\n  1) dL/da = 2(a - y_true) = 2({a[0]:.6f} - {y_true})")
print(f"     = {dL_da}")

# da/dz (derivada de sigmoid)
da_dz = a * (1 - a)
print(f"\n  2) da/dz = sigmoid(z) · (1 - sigmoid(z)) = {a[0]:.6f} · {1-a[0]:.6f}")
print(f"     = {da_dz}")

# dL/dz (combinando 1 y 2)
dL_dz = dL_da * da_dz
print(f"\n  3) dL/dz = dL/da · da/dz = {dL_da[0]:.6f} · {da_dz[0]:.6f}")
print(f"     = {dL_dz}")

# dL/dW = dL/dz · dz/dW = dL/dz · x^T
# Para cada peso: dL/dW[0,j] = dL/dz · x[j]
dL_dW = dL_dz.reshape(-1, 1) @ x.reshape(1, -1)  # outer product
print(f"\n  4) dL/dW = dL/dz · x^T")
print(f"     dL/dW[0,0] = {dL_dz[0]:.6f} · {x[0]} = {dL_dW[0,0]:.6f}")
print(f"     dL/dW[0,1] = {dL_dz[0]:.6f} · {x[1]} = {dL_dW[0,1]:.6f}")
print(f"     dL/dW = {dL_dW}")

# dL/db = dL/dz · 1 = dL/dz
dL_db = dL_dz
print(f"\n  5) dL/db = dL/dz = {dL_db}")


# =============================================================================
# PASO 3: ACTUALIZACIÓN DE PESOS
# =============================================================================

lr = 0.1
W_nuevo = W - lr * dL_dW
b_nuevo = b - lr * dL_db

print(f"\n--- ACTUALIZACIÓN (lr={lr}) ---")
print(f"  W_nuevo = W - lr·dL/dW = {W} - {lr}·{dL_dW}")
print(f"         = {W_nuevo}")
print(f"  b_nuevo = b - lr·dL/db = {b} - {lr}·{dL_db}")
print(f"         = {b_nuevo}")

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
    # Forward
    z = W_train @ x + b_train
    a = sigmoid(z)
    loss = (a - y_true) ** 2
    losses.append(loss[0])
    
    # Backward
    dL_da = 2 * (a - y_true)
    da_dz = a * (1 - a)
    dL_dz = dL_da * da_dz
    dL_dW = dL_dz.reshape(-1, 1) @ x.reshape(1, -1)
    dL_db = dL_dz
    
    # Update
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
   → lr=10: La loss probablemente OSCILA porque los pasos son demasiado grandes
   → lr=0.001: Converge pero MUY lento

2. ¿Por qué dz/dW = x y no W?
   → Porque z = W·x + b. La derivada de W·x respecto a W es x.
   → Piénsalo así: z es una función LINEAL de W, con "pendiente" x.

3. ¿Cuántas multiplicaciones hace el backward pass vs el forward pass?
   → Aproximadamente la misma cantidad. Backprop es eficiente porque
     reutiliza los valores calculados en el forward (z, a).

4. En una red de N capas, ¿cuántas reglas de la cadena se aplican?
   → N reglas de la cadena encadenadas. Si la derivada de cada paso
     es < 1, el gradiente final puede ser 0.25^N → ¡vanishing gradient!

✅ Challenge 4 completado.
   Siguiente: challenge_5_autograd_verify.py
""")

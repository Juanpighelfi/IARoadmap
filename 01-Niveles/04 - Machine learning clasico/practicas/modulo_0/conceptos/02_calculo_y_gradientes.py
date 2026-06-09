"""
=============================================================================
📐 CÁLCULO Y GRADIENTES PARA ML — Guía Conceptual Interactiva
=============================================================================

PROPÓSITO: Reforzar los conceptos de "La Esencia del Cálculo" (3Blue1Brown)
           con aplicaciones directas a redes neuronales.

PRERREQUISITO: Haber visto "La Esencia del Cálculo" de 3Blue1Brown
DURACIÓN: ~45 minutos

Después de esta guía, estarás preparado para challenges 4-6.
=============================================================================
"""

import os
import numpy as np
import matplotlib.pyplot as plt

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({
    'figure.figsize': (10, 6),
    'font.size': 11,
    'axes.grid': True,
    'grid.alpha': 0.3
})


# =============================================================================
# 1️⃣ DERIVADAS: La tasa de cambio instantánea
# =============================================================================
"""
La derivada f'(x) te dice: "Si muevo x un poquito, ¿cuánto cambia f?"

En ML, esto es EXACTAMENTE lo que necesitamos:
  "Si cambio un peso w un poquito, ¿cuánto cambia la loss?"
  
Si dL/dw > 0: aumentar w aumenta la loss → HAY QUE DISMINUIR w
Si dL/dw < 0: aumentar w disminuye la loss → HAY QUE AUMENTAR w
Si dL/dw = 0: estamos en un punto estacionario (mínimo, máximo o silla)

La regla de actualización: w_nuevo = w_viejo - lr * dL/dw
"""

print("=" * 60)
print("1️⃣  DERIVADAS Y GRADIENT DESCENT")
print("=" * 60)

# Ejemplo visual: Minimizar una función simple
def f(x):
    return x**2 + 2*np.sin(3*x)

def df(x):
    """Derivada analítica: f'(x) = 2x + 6cos(3x)"""
    return 2*x + 6*np.cos(3*x)

# Visualizar la función y su derivada
x = np.linspace(-3, 3, 300)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Función
axes[0].plot(x, f(x), 'b-', linewidth=2.5, label='f(x) = x² + 2sin(3x)')
axes[0].set_title('La función (landscape de la loss)', fontweight='bold')
axes[0].set_xlabel('x (un peso del modelo)')
axes[0].set_ylabel('f(x) (la loss)')
axes[0].legend()

# Derivada
axes[1].plot(x, df(x), 'r-', linewidth=2.5, label="f'(x) = 2x + 6cos(3x)")
axes[1].axhline(y=0, color='k', linewidth=0.5)
axes[1].set_title('El gradiente (dirección de actualización)', fontweight='bold')
axes[1].set_xlabel('x')
axes[1].set_ylabel("f'(x)")
axes[1].legend()

# Marcar dónde la derivada es 0 (puntos estacionarios)
from scipy.optimize import brentq
# Encontrar raíces de f'(x) en intervalos
roots = []
for a, b in zip(np.arange(-3, 3, 0.5), np.arange(-2.5, 3.5, 0.5)):
    try:
        root = brentq(df, a, b)
        if -3 <= root <= 3:
            roots.append(root)
    except ValueError:
        pass

for root in roots:
    axes[0].plot(root, f(root), 'ro', markersize=10, zorder=5)
    axes[1].plot(root, 0, 'ro', markersize=10, zorder=5)

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, '02_derivada.png'), dpi=100, bbox_inches='tight')
plt.show()

# Simulación de Gradient Descent
print("\n--- Gradient Descent en acción ---")
w = 2.5  # Punto de inicio
lr = 0.05  # Learning rate
historia = [w]

for step in range(30):
    grad = df(w)
    w = w - lr * grad
    historia.append(w)
    if step < 5 or step % 5 == 4:
        print(f"  Step {step:2d}: w = {w:7.4f}, f(w) = {f(w):7.4f}, grad = {grad:7.4f}")

# Visualizar el camino del gradient descent
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, f(x), 'b-', linewidth=2, alpha=0.5)
ax.scatter(historia, [f(w) for w in historia], c=range(len(historia)), 
           cmap='hot', s=50, zorder=5, edgecolors='black', linewidth=0.5)
ax.plot(historia, [f(w) for w in historia], 'k--', alpha=0.3)
ax.set_title('Gradient Descent: Camino de actualización de w', fontweight='bold', fontsize=14)
ax.set_xlabel('w')
ax.set_ylabel('f(w) = Loss')
plt.colorbar(ax.scatter(historia, [f(w) for w in historia], c=range(len(historia)), 
             cmap='hot', s=0), label='Step')
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, '02_gradient_descent.png'), dpi=100, bbox_inches='tight')
plt.show()

input("\n[Presiona Enter para continuar...]\n")


# =============================================================================
# 2️⃣ LA REGLA DE LA CADENA: El corazón de Backpropagation
# =============================================================================
"""
Si f(x) = h(g(x)), entonces:
    f'(x) = h'(g(x)) · g'(x)

Esto se extiende a múltiples funciones encadenadas:
    f = f₃(f₂(f₁(x)))
    f'(x) = f₃'(f₂(f₁(x))) · f₂'(f₁(x)) · f₁'(x)

¡Esto es EXACTAMENTE lo que hace backpropagation!

Una red neuronal es una cadena de funciones:
    loss = L(σ(W₂ · relu(W₁ · x + b₁) + b₂))

Para calcular ∂loss/∂W₁, necesitamos la regla de la cadena
aplicada paso a paso desde el final (loss) hasta W₁.
"""

print("\n" + "=" * 60)
print("2️⃣  LA REGLA DE LA CADENA")
print("=" * 60)

# Ejemplo concreto con una "mini red" de 1 neurona
print("""
Mini red neuronal: x → (W·x + b) → sigmoid → MSE Loss

Funciones encadenadas:
  z = W·x + b         (transformación lineal)
  a = σ(z)            (activación sigmoid)
  L = (a - y)²        (loss MSE)

Para actualizar W, necesitamos dL/dW:
  dL/dW = dL/da · da/dz · dz/dW
""")

# Valores concretos
x_val = 2.0
W_val = 0.5
b_val = -0.1
y_true = 1.0

# Forward pass (paso a paso)
z = W_val * x_val + b_val
a = 1 / (1 + np.exp(-z))  # sigmoid
L = (a - y_true) ** 2

print(f"Forward pass:")
print(f"  z = W·x + b = {W_val}·{x_val} + {b_val} = {z}")
print(f"  a = σ(z) = σ({z}) = {a:.6f}")
print(f"  L = (a - y)² = ({a:.6f} - {y_true})² = {L:.6f}")

# Backward pass (paso a paso)
dL_da = 2 * (a - y_true)           # dL/da = 2(a - y)
da_dz = a * (1 - a)                # da/dz = σ(z)(1 - σ(z))  ← derivada de sigmoid
dz_dW = x_val                      # dz/dW = x

dL_dW = dL_da * da_dz * dz_dW      # Regla de la cadena completa

print(f"\nBackward pass (Regla de la Cadena):")
print(f"  dL/da = 2(a - y) = 2({a:.6f} - {y_true}) = {dL_da:.6f}")
print(f"  da/dz = σ(z)(1 - σ(z)) = {a:.6f}·{1-a:.6f} = {da_dz:.6f}")
print(f"  dz/dW = x = {dz_dW}")
print(f"  dL/dW = dL/da · da/dz · dz/dW = {dL_da:.6f} · {da_dz:.6f} · {dz_dW} = {dL_dW:.6f}")

# Actualización
lr = 0.1
W_nuevo = W_val - lr * dL_dW
print(f"\n  W_nuevo = W - lr·dL/dW = {W_val} - {lr}·{dL_dW:.6f} = {W_nuevo:.6f}")

# Visualizar el grafo computacional
print("""
    ┌───────────────────────────────────────────────────────────┐
    │                GRAFO COMPUTACIONAL                        │
    │                                                           │
    │   x ─────┐                                                │
    │           ├─→ [z = W·x + b] ──→ [a = σ(z)] ──→ [L=(a-y)²]│
    │   W ─────┘        │                  │              │     │
    │   b ─────┘        │                  │              │     │
    │                   │                  │              │     │
    │   BACKWARD:       │                  │              │     │
    │   ←── dz/dW=x ←── da/dz=σ'(z) ←── dL/da=2(a-y) ←──│     │
    └───────────────────────────────────────────────────────────┘
""")

input("\n[Presiona Enter para continuar...]\n")


# =============================================================================
# 3️⃣ FUNCIONES DE ACTIVACIÓN Y SUS DERIVADAS
# =============================================================================
"""
Las funciones de activación añaden NO LINEALIDAD a la red.
Para backpropagation, necesitamos sus derivadas.

🔑 La elección de activación afecta el flujo de gradientes:
  - Sigmoid: gradiente máximo = 0.25 → los gradientes se hacen PEQUEÑOS
  - ReLU: gradiente = 0 o 1 → no hay vanishing gradient (pero sí "neuronas muertas")
"""

print("\n" + "=" * 60)
print("3️⃣  FUNCIONES DE ACTIVACIÓN")
print("=" * 60)

x = np.linspace(-5, 5, 500)

# Sigmoid
sigmoid = lambda z: 1 / (1 + np.exp(-z))
sigmoid_deriv = lambda z: sigmoid(z) * (1 - sigmoid(z))

# Tanh
tanh = lambda z: np.tanh(z)
tanh_deriv = lambda z: 1 - np.tanh(z)**2

# ReLU
relu = lambda z: np.maximum(0, z)
relu_deriv = lambda z: (z > 0).astype(float)

# Swish (x * sigmoid(x)) — usado en EfficientNet
swish = lambda z: z * sigmoid(z)
swish_deriv = lambda z: sigmoid(z) + z * sigmoid_deriv(z)

activaciones = [
    ("Sigmoid", sigmoid, sigmoid_deriv, "σ(z) = 1/(1+e⁻ᶻ)"),
    ("Tanh", tanh, tanh_deriv, "tanh(z) = (eᶻ - e⁻ᶻ)/(eᶻ + e⁻ᶻ)"),
    ("ReLU", relu, relu_deriv, "relu(z) = max(0, z)"),
    ("Swish", swish, swish_deriv, "swish(z) = z·σ(z)")
]

fig, axes = plt.subplots(2, 4, figsize=(20, 8))

for idx, (nombre, func, deriv, formula) in enumerate(activaciones):
    # Función
    axes[0, idx].plot(x, func(x), linewidth=2.5, color='#2196F3')
    axes[0, idx].set_title(f'{nombre}\n{formula}', fontweight='bold')
    axes[0, idx].axhline(y=0, color='k', linewidth=0.3)
    axes[0, idx].axvline(x=0, color='k', linewidth=0.3)
    axes[0, idx].set_ylim(-2, 5)
    
    # Derivada
    axes[1, idx].plot(x, deriv(x), linewidth=2.5, color='#FF5722')
    axes[1, idx].set_title(f"Derivada de {nombre}", fontweight='bold')
    axes[1, idx].axhline(y=0, color='k', linewidth=0.3)
    axes[1, idx].axvline(x=0, color='k', linewidth=0.3)
    axes[1, idx].set_ylim(-0.5, 1.5)
    
    # Marcar gradiente máximo de sigmoid
    if nombre == "Sigmoid":
        axes[1, idx].axhline(y=0.25, color='gray', linestyle='--', alpha=0.5)
        axes[1, idx].annotate('max = 0.25', xy=(2, 0.25), fontsize=10, color='gray')

plt.suptitle('Funciones de Activación y sus Derivadas', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, '02_activaciones.png'), dpi=100, bbox_inches='tight')
plt.show()

print("""
🔑 OBSERVACIONES CLAVE:

1. SIGMOID: La derivada máxima es 0.25. Si apilamos 10 sigmoid,
   el gradiente se multiplica: 0.25^10 = 0.0000009536 → ¡DESAPARECE!
   Esto es el "vanishing gradient problem".

2. ReLU: La derivada es 0 o 1. No hay multiplicación de fracciones pequeñas. 
   PERO si z < 0, la derivada es 0 → la neurona "muere" y nunca más recibe gradientes.

3. SWISH: Balance entre sigmoid (suave) y ReLU (eficiente).
   Tiene un pequeño dip negativo que funciona como regularización.
""")

input("\n[Presiona Enter para continuar...]\n")


# =============================================================================
# 4️⃣ GRADIENTE EN MÚLTIPLES DIMENSIONES
# =============================================================================
"""
Para funciones de múltiples variables f(x₁, x₂, ..., xₙ), el gradiente
es un VECTOR de derivadas parciales:

    ∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]

El gradiente apunta en la dirección de MAYOR CRECIMIENTO de f.
Para minimizar f (nuestra loss), vamos en la dirección OPUESTA: -∇f.
"""

print("\n" + "=" * 60)
print("4️⃣  GRADIENTE EN MÚLTIPLES DIMENSIONES")
print("=" * 60)

# Función de 2 variables: f(x, y) = x² + 3y²
# El gradiente es: ∇f = [2x, 6y]
def f2d(x, y):
    return x**2 + 3*y**2

def grad_f2d(x, y):
    return np.array([2*x, 6*y])

# Visualización: Mapa de contorno + flechas de gradiente
xx = np.linspace(-3, 3, 100)
yy = np.linspace(-3, 3, 100)
XX, YY = np.meshgrid(xx, yy)
ZZ = f2d(XX, YY)

fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Contorno + gradientes
axes[0].contourf(XX, YY, ZZ, levels=20, cmap='viridis', alpha=0.8)
axes[0].contour(XX, YY, ZZ, levels=20, colors='white', linewidths=0.5, alpha=0.3)

# Flechas de gradiente negativo (dirección de descenso)
gx, gy = np.meshgrid(np.linspace(-2.5, 2.5, 8), np.linspace(-2.5, 2.5, 8))
grad_x, grad_y = grad_f2d(gx, gy)
axes[0].quiver(gx, gy, -grad_x, -grad_y, color='white', alpha=0.7, scale=50)
axes[0].set_title('Mapa de contorno + Gradiente negativo\n(dirección de descenso)', fontweight='bold', fontsize=13)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
plt.colorbar(axes[0].contourf(XX, YY, ZZ, levels=20, cmap='viridis', alpha=0.0), ax=axes[0])

# Gradient descent 2D
w = np.array([2.5, -2.0])
lr = 0.05
path = [w.copy()]

for _ in range(50):
    g = grad_f2d(w[0], w[1])
    w = w - lr * g
    path.append(w.copy())

path = np.array(path)

axes[1].contourf(XX, YY, ZZ, levels=20, cmap='viridis', alpha=0.8)
axes[1].contour(XX, YY, ZZ, levels=20, colors='white', linewidths=0.5, alpha=0.3)
axes[1].plot(path[:, 0], path[:, 1], 'r.-', linewidth=1.5, markersize=5, alpha=0.8)
axes[1].plot(path[0, 0], path[0, 1], 'wo', markersize=12, markeredgecolor='red', markeredgewidth=2, label='Inicio')
axes[1].plot(path[-1, 0], path[-1, 1], 'w*', markersize=15, markeredgecolor='red', markeredgewidth=2, label='Final')
axes[1].set_title('Gradient Descent en 2D\n(el camino de optimización)', fontweight='bold', fontsize=13)
axes[1].set_xlabel('w₁')
axes[1].set_ylabel('w₂')
axes[1].legend(fontsize=11)

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, '02_gradiente_2d.png'), dpi=100, bbox_inches='tight')
plt.show()

print("""
🔑 OBSERVA:
  - El gradiente desciende MÁS RÁPIDO en la dirección de y (la "pendiente" es mayor)
  - Esto causa un camino "zigzagueante" — por eso Adam/AdamW adaptan el lr por parámetro
  - El learning rate controla el tamaño de cada paso:
    • lr muy alto → oscila y no converge
    • lr muy bajo → converge pero muy lento
""")


# =============================================================================
# 5️⃣ RESUMEN
# =============================================================================

print(f"""
{'=' * 60}
📋 RESUMEN — CÁLCULO PARA ML
{'=' * 60}

┌────────────────────────────────────────────────────────────┐
│ CONCEPTO              │ EN ML SIGNIFICA...                  │
├────────────────────────────────────────────────────────────┤
│ Derivada f'(x)        │ ¿Cuánto cambia la loss si muevo w? │
│ Regla de la cadena    │ = Backpropagation                   │
│ Gradiente ∇f          │ Dirección de mayor cambio           │
│ -∇f                   │ Dirección para reducir la loss      │
│ Learning rate         │ Tamaño del paso en esa dirección    │
│ Sigmoid'              │ max 0.25 → vanishing gradient       │
│ ReLU'                 │ 0 o 1 → no vanishing, pero muertas │
│ Computational Graph   │ DAG de operaciones para autograd    │
└────────────────────────────────────────────────────────────┘

🎯 SIGUIENTE PASO: Ve a challenges/ y completa:
   - challenge_4_gradientes_manuales.py
   - challenge_5_autograd_verify.py
   - challenge_6_vanishing_gradient.py
""")

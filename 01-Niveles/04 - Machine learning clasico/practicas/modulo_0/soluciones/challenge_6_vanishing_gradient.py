"""
=============================================================================
🏆 CHALLENGE 6: Demostrar Vanishing Gradient
=============================================================================

OBJETIVO: Experimentar y visualizar el problema de vanishing gradient
          apilando múltiples funciones sigmoid.

CONCEPTO: La derivada de sigmoid tiene un máximo de 0.25.
          Cuando apilas N sigmoids, el gradiente se multiplica:
          grad ≈ 0.25^N → para N=20, grad ≈ 10^{-12} → ¡prácticamente 0!

          Este es EL problema que motivó:
          - El uso de ReLU en lugar de sigmoid
          - Las skip connections (ResNet)
          - Técnicas como BatchNorm
          - Inicialización cuidadosa (He, Xavier)

DURACIÓN: ~30 minutos
DIFICULTAD: ⭐⭐⭐ (Avanzada)
=============================================================================
"""

import numpy as np
import torch
import matplotlib.pyplot as plt

plt.rcParams.update({
    'figure.figsize': (12, 6),
    'font.size': 11,
    'axes.grid': True,
    'grid.alpha': 0.3
})

print("=" * 60)
print("🏆 CHALLENGE 6: Vanishing Gradient")
print("=" * 60)


# =============================================================================
# PARTE 1: Apilar sigmoids con NumPy
# =============================================================================
"""
Implementa: x → sigmoid → sigmoid → ... → sigmoid (N veces)
Calcula el gradiente de la salida respecto a x.

El gradiente se calcula con la regla de la cadena:
    dout/dx = σ'(z₁) · σ'(z₂) · ... · σ'(zₙ)
    
donde σ'(z) = σ(z)(1 - σ(z)) y cada zᵢ es la salida de la sigmoid anterior.
"""

print("\n--- PARTE 1: Apilar sigmoids (NumPy) ---")

sigmoid = lambda z: 1 / (1 + np.exp(-z))
sigmoid_deriv = lambda z: sigmoid(z) * (1 - sigmoid(z))

def forward_stacked_sigmoids(x, n_layers):
    """Forward pass: apilar n_layers sigmoids."""
    activations = [x]
    z = x
    for _ in range(n_layers):
        z = sigmoid(z)
        activations.append(z)
    return z, activations

def gradient_stacked_sigmoids(activations):
    """
    Calcula el gradiente total multiplicando las derivadas intermedias.
    grad = π σ'(aᵢ) para cada capa.
    
    NOTA: la derivada de sigmoid evaluada en la ACTIVACIÓN a es a·(1-a)
    (porque a ya pasó por sigmoid, así que σ(z) = a).
    """
    grad = 1.0
    # Empezamos desde la primera activación (antes de la primera sigmoid)
    for i in range(len(activations) - 1):
        a = activations[i + 1]  # Salida de la sigmoid
        local_grad = a * (1 - a)  # σ'(z) evaluada
        grad *= local_grad
    return grad

# Probar con diferentes cantidades de capas
x_val = 0.5
capas = [1, 2, 5, 10, 15, 20, 30, 50]
gradientes = []

print(f"\n  x = {x_val}")
print(f"  {'Capas':>6s} | {'Salida':>12s} | {'Gradiente':>15s} | {'log10(grad)':>12s}")
print(f"  {'-'*6} | {'-'*12} | {'-'*15} | {'-'*12}")

for n in capas:
    output, activations = forward_stacked_sigmoids(x_val, n)
    grad = gradient_stacked_sigmoids(activations)
    gradientes.append(grad)
    log_grad = np.log10(abs(grad) + 1e-300)
    print(f"  {n:6d} | {output:12.8f} | {grad:15.2e} | {log_grad:12.1f}")

print("""
  🔑 OBSERVA: Con 20 capas, el gradiente es ~10⁻¹²
     → Los pesos de las primeras capas NUNCA se actualizan
     → La red no puede aprender features profundas
     → ¡Esta es la razón por la que las redes profundas no funcionaban antes de 2010!
""")


# =============================================================================
# PARTE 2: Verificar con PyTorch autograd
# =============================================================================

print(f"\n{'=' * 60}")
print("PARTE 2: Verificación con PyTorch Autograd")
print("=" * 60)

for n in [1, 5, 10, 20, 50]:
    x_t = torch.tensor([0.5], requires_grad=True)
    z_t = x_t
    for _ in range(n):
        z_t = torch.sigmoid(z_t)
    z_t.backward()
    print(f"  {n:2d} sigmoids: grad = {x_t.grad.item():.2e}")


# =============================================================================
# PARTE 3: Comparación Sigmoid vs ReLU vs Tanh
# =============================================================================
"""
TODO: Repite el experimento con ReLU y Tanh.
¿Cómo se comporta el gradiente en cada caso?
"""

print(f"\n{'=' * 60}")
print("PARTE 3: Sigmoid vs ReLU vs Tanh — Flujo de Gradientes")
print("=" * 60)

capas_test = list(range(1, 51))

def gradient_experiment(activation_fn, n_layers, x_val=0.5):
    """Calcula el gradiente a través de n_layers de activation_fn usando PyTorch."""
    x_t = torch.tensor([x_val], requires_grad=True)
    z = x_t
    for _ in range(n_layers):
        z = activation_fn(z)
    z.backward()
    return x_t.grad.item()

# Calcular gradientes para cada activación
grads_sigmoid = []
grads_tanh = []
grads_relu = []

for n in capas_test:
    grads_sigmoid.append(abs(gradient_experiment(torch.sigmoid, n, 0.5)))
    grads_tanh.append(abs(gradient_experiment(torch.tanh, n, 0.5)))
    # ReLU con x=0.5 siempre da 1.0 (trivial), vamos a usar una red con pesos
    # Para ReLU usamos un valor positivo donde la derivada es 1
    grads_relu.append(abs(gradient_experiment(torch.relu, n, 0.5)))

# Visualizar
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Escala logarítmica
axes[0].semilogy(capas_test, grads_sigmoid, 'r-', linewidth=2, label='Sigmoid', marker='o', markersize=3)
axes[0].semilogy(capas_test, grads_tanh, 'b-', linewidth=2, label='Tanh', marker='s', markersize=3)
axes[0].semilogy(capas_test, grads_relu, 'g-', linewidth=2, label='ReLU', marker='^', markersize=3)
axes[0].set_xlabel('Número de capas', fontsize=12)
axes[0].set_ylabel('|Gradiente| (log scale)', fontsize=12)
axes[0].set_title('Vanishing Gradient: Comparación de Activaciones', fontweight='bold', fontsize=13)
axes[0].legend(fontsize=12)
axes[0].axhline(y=1e-7, color='gray', linestyle='--', alpha=0.5, label='Umbral práctico')

# Zoom en sigmoid
axes[1].plot(capas_test, [np.log10(g + 1e-300) for g in grads_sigmoid], 'r-', linewidth=2, marker='o', markersize=3)
axes[1].set_xlabel('Número de capas', fontsize=12)
axes[1].set_ylabel('log₁₀(|gradiente|)', fontsize=12)
axes[1].set_title('Sigmoid: Gradiente decae exponencialmente', fontweight='bold', fontsize=13)
axes[1].axhline(y=-7, color='gray', linestyle='--', alpha=0.5)
axes[1].annotate('Float32 pierde precisión', xy=(20, -7), fontsize=10, color='gray')

plt.tight_layout()
plt.savefig('challenges/challenge_6_vanishing.png', dpi=100, bbox_inches='tight')
plt.show()


# =============================================================================
# PARTE 4: Red neuronal real — Inicialización importa
# =============================================================================
"""
Vamos a crear una red profunda REAL y medir los gradientes en cada capa.
Compararemos:
  a) Red con sigmoid → vanishing gradient
  b) Red con ReLU + He init → gradientes saludables
"""

print(f"\n{'=' * 60}")
print("PARTE 4: Red real — Sigmoid vs ReLU")
print("=" * 60)

import torch.nn as nn

def build_deep_net(activation, n_layers=15, hidden_dim=64, init='default'):
    """Construye una red profunda con la activación especificada."""
    layers = []
    for i in range(n_layers):
        linear = nn.Linear(hidden_dim, hidden_dim)
        if init == 'he':
            nn.init.kaiming_normal_(linear.weight, nonlinearity='relu')
        layers.append(linear)
        layers.append(activation())
    return nn.Sequential(*layers)

def measure_gradients(model, input_dim=64):
    """Mide la norma del gradiente en cada capa lineal."""
    x = torch.randn(32, input_dim)  # Batch de 32
    output = model(x)
    loss = output.sum()
    loss.backward()
    
    grad_norms = []
    for i, layer in enumerate(model):
        if isinstance(layer, nn.Linear):
            grad_norms.append(layer.weight.grad.norm().item())
    return grad_norms

# Red con Sigmoid
net_sigmoid = build_deep_net(nn.Sigmoid, n_layers=15)
grads_sig = measure_gradients(net_sigmoid)

# Red con ReLU + He init
net_relu = build_deep_net(nn.ReLU, n_layers=15, init='he')
grads_relu_net = measure_gradients(net_relu)

# Visualizar
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

layers_idx = list(range(1, len(grads_sig) + 1))

axes[0].bar(layers_idx, grads_sig, color='#F44336', alpha=0.8, edgecolor='white')
axes[0].set_xlabel('Capa (1=más profunda, N=más cercana a input)')
axes[0].set_ylabel('Norma del Gradiente')
axes[0].set_title('Red con Sigmoid\n(Vanishing Gradient)', fontweight='bold', color='#F44336')
axes[0].set_yscale('log')

axes[1].bar(layers_idx, grads_relu_net, color='#4CAF50', alpha=0.8, edgecolor='white')
axes[1].set_xlabel('Capa')
axes[1].set_ylabel('Norma del Gradiente')
axes[1].set_title('Red con ReLU + He Init\n(Gradientes Saludables)', fontweight='bold', color='#4CAF50')
axes[1].set_yscale('log')

plt.suptitle('Gradientes por Capa en una Red de 15 Capas', fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('challenges/challenge_6_red_real.png', dpi=100, bbox_inches='tight')
plt.show()


# =============================================================================
# REFLEXIÓN
# =============================================================================
print(f"""
{'=' * 60}
🧠 REFLEXIÓN
{'=' * 60}

1. ¿Por qué 20 sigmoids apiladas causan vanishing gradient?
   → σ'(z) ∈ (0, 0.25]. Al multiplicar N veces: 0.25^N → 0 rápidamente.
   → A las 12 capas ya estamos en ~10⁻⁷, la precisión de float32.

2. ¿ReLU resuelve completamente el problema?
   → Para gradientes positivos, sí: la derivada es exactamente 1.
   → PERO: si la entrada es negativa, la derivada es 0 → "neurona muerta"
   → Soluciones: LeakyReLU, ELU, GELU (usada en Transformers).

3. ¿Qué más ayuda contra vanishing gradient?
   → Skip connections (ResNet): grad = ∂f/∂x + 1 (el +1 evita que desaparezca)
   → BatchNorm: normaliza activaciones → mantiene gradientes en rango útil
   → Inicialización correcta (He/Xavier): empieza con gradientes de escala 1
   → Gradient clipping: pone un tope superior (contra exploding gradient)

4. ¿El exploding gradient es el problema opuesto?
   → Sí: si los eigenvalores del Jacobiano son > 1, los gradientes CRECEN.
   → El gradiente se va a infinito → NaN en los pesos → modelo roto.
   → Solución: gradient clipping con clip_grad_norm_().

✅ Challenge 6 completado.
   Siguiente: challenge_7_cross_entropy.py (Semana 3: Probabilidad)
""")

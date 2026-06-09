"""
=============================================================================
🏆 CHALLENGE 8: MSE vs Cross-Entropy para Clasificación
=============================================================================

OBJETIVO: Demostrar empíricamente POR QUÉ NO usar MSE para clasificación.
          Comparar gradientes de ambas funciones de loss.

CONCEPTO: MSE tiene "saturación" cuando la predicción es muy incorrecta:
          el gradiente se hace PEQUEÑO justo cuando debería ser GRANDE.
          Cross-entropy no tiene este problema.

DURACIÓN: ~30 minutos
DIFICULTAD: ⭐⭐⭐ (Avanzada)

HINTS: Si te trabás, consultá modulo_0/hints/hint_challenge_8.md
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'figure.figsize': (12, 6),
    'font.size': 11,
    'axes.grid': True,
    'grid.alpha': 0.3
})


print("=" * 60)
print("🏆 CHALLENGE 8: MSE vs Cross-Entropy")
print("=" * 60)


# =============================================================================
# PARTE 1: La loss y sus gradientes
# =============================================================================
"""
Para clasificación binaria con sigmoid:
    ŷ = sigmoid(z) = σ(z)

MSE Loss: L_mse = (ŷ - y)² = (σ(z) - y)²
    dL/dz = 2(σ(z) - y) · σ'(z) = 2(σ(z) - y) · σ(z)(1-σ(z))

BCE Loss: L_bce = -[y·log(σ(z)) + (1-y)·log(1-σ(z))]
    dL/dz = σ(z) - y    ← ¡Mucho más simple!

El truco: la derivada de sigmoid se CANCELA con la derivada de log.
Por eso BCE + sigmoid es una combinación natural.

TODO: Calcula y compara loss y gradientes para ambas funciones.
"""

sigmoid = lambda z: 1 / (1 + np.exp(-z))

z = np.linspace(-6, 6, 500)
y_hat = sigmoid(z)

# Caso: y_true = 1
y_true = 1
epsilon = 1e-15

# TODO: MSE loss y gradiente respecto a z
mse_loss = ...  # (y_hat - y_true) ** 2
mse_grad = ...  # 2 * (y_hat - y_true) * y_hat * (1 - y_hat)

# TODO: BCE loss y gradiente respecto a z
bce_loss = ...  # -(y_true * log(y_hat) + (1-y_true) * log(1-y_hat))
bce_grad = ...  # y_hat - y_true (simplificación con sigmoid)

# Tabla comparativa
print("\n--- Comparación de Loss y Gradientes (y_true = 1) ---")
print(f"  {'z':>5s} | {'ŷ=σ(z)':>8s} | {'MSE Loss':>10s} | {'BCE Loss':>10s} | {'MSE grad':>10s} | {'BCE grad':>10s}")
print(f"  {'-'*5} | {'-'*8} | {'-'*10} | {'-'*10} | {'-'*10} | {'-'*10}")
for z_val in [-5, -3, -1, 0, 1, 3, 5]:
    idx = np.argmin(np.abs(z - z_val))
    print(f"  {z_val:5.1f} | {y_hat[idx]:8.4f} | {mse_loss[idx]:10.4f} | {bce_loss[idx]:10.4f} | {mse_grad[idx]:10.6f} | {bce_grad[idx]:10.6f}")


# =============================================================================
# PARTE 2: Visualización
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

axes[0, 0].plot(z, mse_loss, linewidth=2.5, color='#FF5722', label='MSE Loss')
axes[0, 0].plot(z, bce_loss, linewidth=2.5, color='#2196F3', label='BCE Loss')
axes[0, 0].set_xlabel('z (logit)', fontsize=12)
axes[0, 0].set_ylabel('Loss', fontsize=12)
axes[0, 0].set_title('Loss (y_true = 1)', fontweight='bold', fontsize=13)
axes[0, 0].legend(fontsize=12)
axes[0, 0].set_ylim(0, 5)

axes[0, 1].plot(z, np.abs(mse_grad), linewidth=2.5, color='#FF5722', label='|dL/dz| MSE')
axes[0, 1].plot(z, np.abs(bce_grad), linewidth=2.5, color='#2196F3', label='|dL/dz| BCE')
axes[0, 1].set_xlabel('z (logit)', fontsize=12)
axes[0, 1].set_ylabel('|Gradiente|', fontsize=12)
axes[0, 1].set_title('Magnitud del Gradiente (y_true = 1)', fontweight='bold', fontsize=13)
axes[0, 1].legend(fontsize=12)
axes[0, 1].axvspan(-6, -2, color='#FFCDD2', alpha=0.2)
axes[0, 1].annotate('ZONA CRÍTICA\nMSE grad ≈ 0 ← ¡PROBLEMA!\nBCE grad ≈ 1 ← ¡OK!', 
                     xy=(-5, 0.5), fontsize=10,
                     bbox=dict(facecolor='white', edgecolor='red', alpha=0.9))

# TODO: Repite para y_true = 0
y_true_0 = 0
mse_loss_0 = ...  # Tu código aquí
mse_grad_0 = ...  # Tu código aquí
bce_loss_0 = ...  # Tu código aquí
bce_grad_0 = ...  # Tu código aquí

axes[1, 0].plot(z, mse_loss_0, linewidth=2.5, color='#FF5722', label='MSE Loss')
axes[1, 0].plot(z, bce_loss_0, linewidth=2.5, color='#2196F3', label='BCE Loss')
axes[1, 0].set_xlabel('z (logit)'); axes[1, 0].set_ylabel('Loss')
axes[1, 0].set_title('Loss (y_true = 0)', fontweight='bold', fontsize=13)
axes[1, 0].legend(fontsize=12); axes[1, 0].set_ylim(0, 5)

axes[1, 1].plot(z, np.abs(mse_grad_0), linewidth=2.5, color='#FF5722', label='|dL/dz| MSE')
axes[1, 1].plot(z, np.abs(bce_grad_0), linewidth=2.5, color='#2196F3', label='|dL/dz| BCE')
axes[1, 1].set_xlabel('z (logit)'); axes[1, 1].set_ylabel('|Gradiente|')
axes[1, 1].set_title('Magnitud del Gradiente (y_true = 0)', fontweight='bold', fontsize=13)
axes[1, 1].legend(fontsize=12)

plt.suptitle('MSE vs Cross-Entropy: ¿Por qué MSE es MALO para clasificación?', 
             fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('challenges/challenge_8_mse_vs_ce.png', dpi=100, bbox_inches='tight')
plt.show()

input("\n[Presiona Enter para continuar...]\n")


# =============================================================================
# PARTE 3: Entrenamiento comparativo
# =============================================================================
"""
TODO: Implementa train_classifier que entrene un clasificador de 1 neurona
con la loss especificada (MSE o BCE).

Para cada epoch:
  1. Forward: z = X * w + b, a = sigmoid(z)
  2. Calcular loss (MSE o BCE)
  3. Calcular gradiente dL/dz:
     - BCE: dz = a - y
     - MSE: dz = 2 * (a - y) * a * (1 - a)
  4. Actualizar pesos: w -= lr * mean(dz * X), b -= lr * mean(dz)
"""

print(f"\n{'=' * 60}")
print("PARTE 3: Entrenamiento comparativo")
print("=" * 60)

np.random.seed(42)

# Dataset simple: clasificar si x > 0
n_samples = 200
X = np.random.randn(n_samples, 1) * 2
y = (X > 0).astype(float).flatten()

def train_classifier(X, y, loss_type='bce', lr=0.1, epochs=500):
    """TODO: Entrena un clasificador de 1 neurona con la loss especificada."""
    w = np.random.randn(1) * 0.1
    b = np.zeros(1)
    losses = []
    
    for epoch in range(epochs):
        # TODO: Forward
        z = ...  # X.flatten() * w + b
        a = ...  # sigmoid(z)
        
        if loss_type == 'bce':
            # TODO: Loss BCE y gradiente
            loss = ...
            dz = ...  # a - y
        elif loss_type == 'mse':
            # TODO: Loss MSE y gradiente
            loss = ...
            dz = ...  # 2 * (a - y) * a * (1 - a)
        
        losses.append(loss)
        
        # TODO: Gradientes y update
        dw = np.mean(dz * X.flatten())
        db = np.mean(dz)
        w -= lr * dw
        b -= lr * db
    
    # Accuracy final
    preds = (1 / (1 + np.exp(-(X.flatten() * w + b))) > 0.5).astype(float)
    accuracy = np.mean(preds == y)
    
    return losses, accuracy, w, b

# Entrenar con ambas loss
losses_bce, acc_bce, _, _ = train_classifier(X, y, 'bce', lr=0.5, epochs=300)
losses_mse, acc_mse, _, _ = train_classifier(X, y, 'mse', lr=0.5, epochs=300)

print(f"\n  Accuracy final:")
print(f"    BCE: {acc_bce*100:.1f}%")
print(f"    MSE: {acc_mse*100:.1f}%")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(losses_bce, linewidth=2.5, color='#2196F3', label=f'BCE (acc final: {acc_bce*100:.0f}%)')
ax.plot(losses_mse, linewidth=2.5, color='#FF5722', label=f'MSE (acc final: {acc_mse*100:.0f}%)')
ax.set_xlabel('Epoch'); ax.set_ylabel('Loss')
ax.set_title('Velocidad de Convergencia: BCE vs MSE', fontweight='bold', fontsize=14)
ax.legend(fontsize=12)
plt.tight_layout()
plt.savefig('challenges/challenge_8_training.png', dpi=100, bbox_inches='tight')
plt.show()


# =============================================================================
# REFLEXIÓN
# =============================================================================
print(f"""
{'=' * 60}
🧠 REFLEXIÓN
{'=' * 60}

1. ¿Entonces MSE nunca sirve?

2. ¿Hay casos donde BCE no es ideal?

3. ¿Qué loss usa PyTorch internamente?

✅ Challenge 8 completado.
   Siguiente: challenge_9_kl_divergence.py
""")

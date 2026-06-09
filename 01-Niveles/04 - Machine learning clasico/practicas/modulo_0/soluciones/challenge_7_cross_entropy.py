"""
=============================================================================
🏆 CHALLENGE 7: Implementar y Visualizar Cross-Entropy
=============================================================================

OBJETIVO: Implementar binary cross-entropy desde cero, visualizarla,
          y entender intuitivamente por qué penaliza los errores confiados.

DURACIÓN: ~30 minutos
DIFICULTAD: ⭐⭐ (Intermedia)

PRERREQUISITO: Guía conceptual 03_probabilidad_y_loss.py
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'figure.figsize': (10, 6),
    'font.size': 11,
    'axes.grid': True,
    'grid.alpha': 0.3
})


print("=" * 60)
print("🏆 CHALLENGE 7: Cross-Entropy")
print("=" * 60)


# =============================================================================
# PARTE 1: Implementar Binary Cross-Entropy
# =============================================================================
"""
Binary Cross-Entropy (para clasificación binaria):

    BCE(y, ŷ) = -[y·log(ŷ) + (1-y)·log(1-ŷ)]

Donde:
  - y ∈ {0, 1}   → label real
  - ŷ ∈ (0, 1)   → predicción del modelo (después de sigmoid)

Si y=1: BCE = -log(ŷ)       → queremos ŷ alto (cercano a 1)
Si y=0: BCE = -log(1-ŷ)     → queremos ŷ bajo (cercano a 0)

TODO: Implementa la función con clipping para evitar log(0).
"""

def binary_cross_entropy(y_true, y_pred, epsilon=1e-15):
    """
    Binary Cross-Entropy Loss.
    
    Args:
        y_true: labels reales (0 o 1), puede ser un array
        y_pred: predicciones del modelo (entre 0 y 1)
        epsilon: valor pequeño para evitar log(0)
    
    Returns:
        Loss promedio sobre todas las muestras
    """
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    loss = -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return np.mean(loss)


# Verificar con casos simples
print("\n--- Verificación ---")
print(f"  BCE(y=1, ŷ=0.99) = {binary_cross_entropy(1, 0.99):.6f}  (baja: confiado y correcto)")
print(f"  BCE(y=1, ŷ=0.50) = {binary_cross_entropy(1, 0.50):.6f}  (media: indeciso)")
print(f"  BCE(y=1, ŷ=0.01) = {binary_cross_entropy(1, 0.01):.6f}  (¡ALTA: confiado e incorrecto!)")
print(f"  BCE(y=0, ŷ=0.01) = {binary_cross_entropy(0, 0.01):.6f}  (baja: confiado y correcto)")
print(f"  BCE(y=0, ŷ=0.99) = {binary_cross_entropy(0, 0.99):.6f}  (¡ALTA: confiado e incorrecto!)")


# =============================================================================
# PARTE 2: Visualizar la asimetría de la penalización
# =============================================================================
"""
Grafica: eje X = predicción del modelo (0.01 a 0.99)
         eje Y = loss
Haz dos curvas: cuando y_true=1 y cuando y_true=0
"""

y_pred_range = np.linspace(0.01, 0.99, 200)

# Loss para cada caso
loss_y1 = -np.log(y_pred_range)           # y_true = 1
loss_y0 = -np.log(1 - y_pred_range)       # y_true = 0

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Gráfico 1: Ambas curvas juntas
axes[0].plot(y_pred_range, loss_y1, linewidth=2.5, color='#2196F3', label='y_true = 1')
axes[0].plot(y_pred_range, loss_y0, linewidth=2.5, color='#FF5722', label='y_true = 0')
axes[0].set_xlabel('Predicción del modelo (ŷ)', fontsize=12)
axes[0].set_ylabel('Binary Cross-Entropy Loss', fontsize=12)
axes[0].set_title('BCE Loss: Cuánto penaliza cada predicción', fontweight='bold', fontsize=13)
axes[0].legend(fontsize=12)
axes[0].set_ylim(0, 5)

# Marcar la zona de error confiado
axes[0].axvspan(0, 0.2, color='#FFCDD2', alpha=0.3)
axes[0].annotate('Zona peligrosa\n(y=1 pero ŷ≈0)', xy=(0.05, 4), fontsize=10, 
                 bbox=dict(facecolor='white', edgecolor='red', alpha=0.8))
axes[0].axvspan(0.8, 1.0, color='#BBDEFB', alpha=0.3)
axes[0].annotate('Zona peligrosa\n(y=0 pero ŷ≈1)', xy=(0.82, 4), fontsize=10,
                 bbox=dict(facecolor='white', edgecolor='blue', alpha=0.8))

# Gráfico 2: Gradiente de BCE
# d/dŷ BCE = -y/ŷ + (1-y)/(1-ŷ)
grad_y1 = -1 / y_pred_range                    # Para y=1
grad_y0 = 1 / (1 - y_pred_range)               # Para y=0

axes[1].plot(y_pred_range, np.abs(grad_y1), linewidth=2.5, color='#2196F3', label='|dBCE/dŷ| con y=1')
axes[1].plot(y_pred_range, np.abs(grad_y0), linewidth=2.5, color='#FF5722', label='|dBCE/dŷ| con y=0')
axes[1].set_xlabel('Predicción del modelo (ŷ)', fontsize=12)
axes[1].set_ylabel('|Gradiente|', fontsize=12)
axes[1].set_title('Gradiente de BCE: Error confiado → gradiente GRANDE', fontweight='bold', fontsize=13)
axes[1].legend(fontsize=12)
axes[1].set_ylim(0, 20)

plt.tight_layout()
plt.savefig('challenges/challenge_7_bce_curves.png', dpi=100, bbox_inches='tight')
plt.show()

print("""
  🔑 OBSERVACIÓN CRUCIAL:
  
  Cuando el modelo está muy equivocado Y confiado (ej: y=1, ŷ=0.01),
  el gradiente es ENORME. Esto significa que:
  
  1. El modelo aprende MÁS RÁPIDO de sus peores errores
  2. Los errores confiados son los que más "tiran" de los pesos
  3. Esto es DESEABLE: queremos corregir los errores graves primero
  
  Compara esto con MSE en el siguiente challenge...
""")

input("\n[Presiona Enter para continuar...]\n")


# =============================================================================
# PARTE 3: Categorical Cross-Entropy (multiclase)
# =============================================================================
"""
Para K clases:
    CCE = -Σₖ yₖ · log(ŷₖ)

Con labels one-hot, esto se simplifica a:
    CCE = -log(ŷ_correcto)
"""

print(f"\n{'=' * 60}")
print("PARTE 3: Categorical Cross-Entropy")
print("=" * 60)

def categorical_cross_entropy(y_true_onehot, y_pred, epsilon=1e-15):
    """
    Categorical Cross-Entropy para clasificación multiclase.
    
    Args:
        y_true_onehot: labels one-hot, shape (n_samples, n_classes)
        y_pred: predicciones (probabilidades), shape (n_samples, n_classes)
    """
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    loss = -np.sum(y_true_onehot * np.log(y_pred), axis=-1)
    return np.mean(loss)


# Ejemplo con 4 clases
y_real = np.array([1, 0, 0, 0])  # Clase 0 (Gato)

predicciones = {
    "Perfecta":      np.array([0.99, 0.003, 0.003, 0.004]),
    "Buena":         np.array([0.85, 0.05, 0.05, 0.05]),
    "Mediocre":      np.array([0.40, 0.30, 0.20, 0.10]),
    "Mala":          np.array([0.05, 0.60, 0.25, 0.10]),
    "Desastrosa":    np.array([0.01, 0.01, 0.01, 0.97]),
}

print(f"\n  Label real: {y_real}")
print(f"  {'Predicción':15s} | {'q_correcto':>12s} | {'CCE Loss':>10s}")
print(f"  {'-'*15} | {'-'*12} | {'-'*10}")
for nombre, q in predicciones.items():
    loss = categorical_cross_entropy(y_real, q)
    bar = "█" * min(int(loss * 5), 40)
    print(f"  {nombre:15s} | {q[0]:12.4f} | {loss:10.4f}  {bar}")


# =============================================================================
# PARTE 4: BCE con batch de datos
# =============================================================================
"""
En la práctica, calculamos la loss sobre un BATCH de muestras.
La loss del batch es el PROMEDIO de las losses individuales.
"""

print(f"\n{'=' * 60}")
print("PARTE 4: BCE con batch")
print("=" * 60)

# Simular un mini-batch de 8 muestras
np.random.seed(42)
batch_y_true = np.array([1, 0, 1, 1, 0, 0, 1, 0])
batch_y_pred = np.array([0.9, 0.1, 0.7, 0.3, 0.2, 0.8, 0.95, 0.05])

# Calcular loss individual y promedio
losses_individuales = -(batch_y_true * np.log(np.clip(batch_y_pred, 1e-15, None)) + 
                        (1 - batch_y_true) * np.log(np.clip(1 - batch_y_pred, 1e-15, None)))

print(f"\n  {'Muestra':>7s} | {'y_true':>6s} | {'y_pred':>6s} | {'Loss':>8s} | {'Notas':>20s}")
print(f"  {'-'*7} | {'-'*6} | {'-'*6} | {'-'*8} | {'-'*20}")
for i in range(len(batch_y_true)):
    nota = ""
    if batch_y_true[i] == 1 and batch_y_pred[i] < 0.5:
        nota = "❌ Error confiado!"
    elif batch_y_true[i] == 0 and batch_y_pred[i] > 0.5:
        nota = "❌ Error confiado!"
    else:
        nota = "✅ Correcto"
    print(f"  {i:7d} | {batch_y_true[i]:6.0f} | {batch_y_pred[i]:6.2f} | {losses_individuales[i]:8.4f} | {nota}")

print(f"\n  Loss promedio del batch: {np.mean(losses_individuales):.4f}")
print(f"  Loss máx (peor error):  {np.max(losses_individuales):.4f} ← muestra {np.argmax(losses_individuales)}")

"""
  🔑 En el entrenamiento real:
  - optimizer.zero_grad()     → resetear gradientes
  - loss = criterion(pred, y) → calcular loss del batch (ya promediada)
  - loss.backward()           → calcular gradientes
  - optimizer.step()          → actualizar pesos
"""


# =============================================================================
# REFLEXIÓN
# =============================================================================
print(f"""
{'=' * 60}
🧠 REFLEXIÓN
{'=' * 60}

1. ¿Qué pasa si la predicción es EXACTAMENTE 0 o 1?
   → log(0) = -∞ → loss infinita → gradientes NaN → modelo roto
   → Por eso usamos clipping: np.clip(y_pred, epsilon, 1-epsilon)

2. ¿Por qué se usa log en la loss y no simplemente |y - ŷ|?
   → log penaliza exponencialmente los errores confiados
   → |y - ŷ| = 0.99 si ŷ=0.01, pero -log(0.01) = 4.6
   → La penalización logarítmica es mucho más agresiva con errores graves

3. ¿Cross-entropy y negative log-likelihood son lo mismo?
   → SÍ (para clasificación con softmax + one-hot labels)
   → Minimizar CE = Maximizar la likelihood de los datos
   → Es el principio de Maximum Likelihood Estimation (MLE)

✅ Challenge 7 completado.
   Siguiente: challenge_8_mse_vs_ce.py
""")

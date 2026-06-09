import numpy as np
import matplotlib.pyplot as plt

# 1. Grafica las 3 funciones de activación (sigmoid, relu, tanh) en un solo subplot
#    con leyenda, grilla, y colores distintos. Rango x: [-6, 6]

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
# axes es un array de 3 ejes

x = np.linspace(-5, 5, 100)

# Subplot 1: Sigmoid
axes[0].plot(x, 1 / (1 + np.exp(-x)), color='blue', linewidth=2)
axes[0].set_title('Sigmoid')
axes[0].axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)

# Subplot 2: ReLU
axes[1].plot(x, np.maximum(0, x), color='green', linewidth=2)
axes[1].set_title('ReLU')

# Subplot 3: Tanh
axes[2].plot(x, np.tanh(x), color='red', linewidth=2)
axes[2].set_title('Tanh')

for ax in axes:
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('x')

plt.suptitle('Funciones de Activación', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
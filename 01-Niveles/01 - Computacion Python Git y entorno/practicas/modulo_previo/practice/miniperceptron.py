# desafio_previo_4_integrador.py
# Combina TODO lo aprendido: NumPy + Matplotlib + OOP

import numpy as np
import matplotlib.pyplot as plt

# OBJETIVO: Implementar un Perceptrón (la neurona más simple)
# que clasifique un dataset linealmente separable

class Perceptron:
    def __init__(self, n_features):
        """Inicializa pesos y bias en cero"""
        self.weights = np.zeros(n_features)
        self.bias = 0.0
        self.history = {"accuracy": []}
    
    def predict(self, X):
        """Predicción: 1 si w·x + b > 0, sino 0"""
        if ((self.weights @ X) + self.bias) > 0:
            return 1
        else:
            return 0
        
    
    def train(self, X, y, epochs=100, lr=0.01):
        for epoch in range(epochs):
            # 1. Ajustar pesos muestra por muestra
            for xi, target in zip(X, y):
                prediction = self.predict(xi)
                error = target - prediction
                # RECUERDA: usa self.weights y self.bias para actualizar
                self.weights = self.weights + lr * error * xi
                self.bias = self.bias + lr * error
            
            # 2. Calcular Accuracy de la época
            # (Predice todo X y compara con y)
            preds = np.array([self.predict(xi) for xi in X])
            acc = np.mean(preds == y)
            self.history["accuracy"].append(acc)
    
    def plot_decision_boundary(self, X, y, ax):
    # 1. Graficar los puntos de datos (puedes usar ax.scatter)
        ax.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', alpha=0.7)
        
        # 2. Definir el rango de x1
        x1_min, x1_max = X[:, 0].min(), X[:, 0].max()
        x1_values = np.linspace(x1_min, x1_max, 100)
        
        # 3. Calcular x2_values usando los pesos del modelo
        # w1 = self.weights[0], w2 = self.weights[1], b = self.bias
        x2_values = -(self.weights[0] * x1_values + self.bias) / self.weights[1]
        
        # 4. Graficar la línea
        ax.plot(x1_values, x2_values, 'k-', lw=2)
        ax.set_title("Frontera de Decisión")
        ax.set_xlabel("Característica 1")
        ax.set_ylabel("Característica 2")
        ax.grid(True)

# Crear dataset
np.random.seed(42)
X_pos = np.random.randn(100, 2) + np.array([2, 2])
X_neg = np.random.randn(100, 2) + np.array([-2, -2])
X = np.vstack([X_pos, X_neg])
y = np.array([1]*100 + [0]*100)

# Entrenar
p = Perceptron(n_features=2)
p.train(X, y, epochs=50, lr=0.1)

# Visualizar
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Subplot 1: Frontera de decisión
p.plot_decision_boundary(X, y, axes[0])

# Subplot 2: Accuracy por epoch
axes[1].plot(p.history["accuracy"], marker='o', markersize=3)
axes[1].set_title("Accuracy por Epoch")
axes[1].set_xlabel("Epoch")
axes[1].set_ylabel("Accuracy")
axes[1].grid(True)

plt.tight_layout()
plt.show()
print(f"Accuracy final: {p.history['accuracy'][-1]:.2%}")
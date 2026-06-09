"""
=============================================================================
🔨 PROYECTO INTEGRADOR: Backpropagation desde Cero
=============================================================================

OBJETIVO: Implementar una red neuronal de 3 capas SIN frameworks (solo NumPy).
          Entender CADA línea del forward pass, backward pass y training loop.

ESTE ES EL HITO DEL MÓDULO 0:
  ✅ Cuando este proyecto funcione y puedas explicar cada línea,
     habrás desbloqueado la capacidad de depurar problemas de
     entrenamiento a nivel de gradientes.

ARQUITECTURA:
  Input (2) → Dense(16, ReLU) → Dense(8, ReLU) → Dense(1, Sigmoid)

DATASET: make_moons (clasificación binaria no lineal)

DURACIÓN: ~2-3 horas (el ejercicio más largo del módulo)
DIFICULTAD: ⭐⭐⭐⭐ (Desafiante)
=============================================================================
"""

import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

plt.rcParams.update({
    'figure.figsize': (10, 6),
    'font.size': 11,
    'axes.grid': True,
    'grid.alpha': 0.3
})


# =============================================================================
# DATASET
# =============================================================================

# Generar dataset no-lineal (dos lunas entrelazadas)
X, y = make_moons(n_samples=1000, noise=0.2, random_state=42)
y = y.reshape(-1, 1)  # Shape: (1000, 1)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("=" * 60)
print("🔨 PROYECTO: Backpropagation desde Cero")
print("=" * 60)
print(f"\n  Dataset: make_moons")
print(f"  Train: {X_train.shape[0]} muestras")
print(f"  Test:  {X_test.shape[0]} muestras")
print(f"  Features: {X_train.shape[1]}")

# Visualizar el dataset
fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train.ravel(), 
                     cmap='RdYlBu', s=15, alpha=0.7, edgecolors='none')
ax.set_title('Dataset: Make Moons (Dos Lunas Entrelazadas)', fontweight='bold', fontsize=14)
ax.set_xlabel('x₁')
ax.set_ylabel('x₂')
plt.colorbar(scatter, label='Clase')
plt.tight_layout()
plt.savefig('proyecto/dataset.png', dpi=100, bbox_inches='tight')
plt.show()


# =============================================================================
# RED NEURONAL DESDE CERO
# =============================================================================

class NeuralNetworkFromScratch:
    """
    Red neuronal fully-connected implementada solo con NumPy.
    
    Arquitectura configurable via layer_sizes.
    Ejemplo: [2, 16, 8, 1] → input=2, hidden1=16, hidden2=8, output=1
    
    Capas ocultas: ReLU
    Capa de salida: Sigmoid (clasificación binaria)
    Loss: Binary Cross-Entropy
    """
    
    def __init__(self, layer_sizes):
        """
        Inicializa los pesos con He initialization.
        
        He init: W ~ N(0, sqrt(2/n_in))
        ¿Por qué sqrt(2/n_in)?
          - Con ReLU, la mitad de las neuronas se "apagan" (output=0).
          - Necesitamos escalar por un factor extra de 2 para compensar.
          - Sin esto, las activaciones se harían cada vez más pequeñas
            capa a capa → gradientes desaparecen.
        """
        self.weights = []
        self.biases = []
        self.n_layers = len(layer_sizes) - 1
        
        for i in range(self.n_layers):
            # He initialization
            w = np.random.randn(layer_sizes[i], layer_sizes[i+1]) * np.sqrt(2.0 / layer_sizes[i])
            b = np.zeros((1, layer_sizes[i+1]))
            self.weights.append(w)
            self.biases.append(b)
        
        # Caches para el backward pass
        self.activations = []
        self.z_values = []
    
    # ----- Funciones de activación -----
    
    def relu(self, z):
        """ReLU: max(0, z). Usada en capas ocultas."""
        return np.maximum(0, z)
    
    def relu_derivative(self, z):
        """
        Derivada de ReLU:
          - 1 si z > 0
          - 0 si z ≤ 0
        """
        return (z > 0).astype(float)
    
    def sigmoid(self, z):
        """Sigmoid: 1/(1+exp(-z)). Usada en la capa de salida."""
        return 1 / (1 + np.exp(-np.clip(z, -500, 500)))  # Clip para estabilidad
    
    # ----- Forward Pass -----
    
    def forward(self, X):
        """
        Forward pass completo.
        
        Almacena las activaciones y los valores z para el backward pass.
        
        Para cada capa oculta i:
            z_i = a_{i-1} @ W_i + b_i    (transformación lineal)
            a_i = relu(z_i)               (activación)
        
        Para la última capa:
            z_last = a_{n-1} @ W_last + b_last
            a_last = sigmoid(z_last)
        """
        self.activations = [X]  # a_0 = input
        self.z_values = []
        
        a = X
        # Capas ocultas (ReLU)
        for i in range(self.n_layers - 1):
            z = a @ self.weights[i] + self.biases[i]
            self.z_values.append(z)
            a = self.relu(z)
            self.activations.append(a)
        
        # Última capa (Sigmoid)
        z = a @ self.weights[-1] + self.biases[-1]
        self.z_values.append(z)
        a = self.sigmoid(z)
        self.activations.append(a)
        
        return a
    
    # ----- Loss Function -----
    
    def compute_loss(self, y_pred, y_true):
        """
        Binary Cross-Entropy Loss:
            L = -(1/m) * Σ [y·log(ŷ) + (1-y)·log(1-ŷ)]
        
        Promediada sobre las m muestras del batch.
        """
        m = y_true.shape[0]
        epsilon = 1e-15
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
        loss = -(1/m) * np.sum(
            y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred)
        )
        return loss
    
    # ----- Backward Pass -----
    
    def backward(self, y_true, learning_rate=0.01):
        """
        Backward pass: calcula gradientes y actualiza pesos.
        
        ALGORITMO:
        
        1. Empezar por la última capa:
           dz_last = a_last - y_true
           (Esta es la derivada simplificada de BCE + Sigmoid combinadas)
        
        2. Para la última capa:
           dW_last = (1/m) * a_{n-1}.T @ dz_last
           db_last = (1/m) * sum(dz_last, axis=0)
        
        3. Propagar hacia atrás:
           da_{i} = dz_{i+1} @ W_{i+1}.T
           dz_{i} = da_{i} * relu'(z_{i})
           dW_{i} = (1/m) * a_{i-1}.T @ dz_{i}
           db_{i} = (1/m) * sum(dz_{i}, axis=0)
        
        4. Actualizar todos los pesos:
           W -= lr * dW
           b -= lr * db
        
        ¿POR QUÉ se transpone a_{prev} y no dz?
        → dW tiene shape (n_in, n_out). 
        → a_prev tiene shape (m, n_in) y dz tiene shape (m, n_out).
        → a_prev.T @ dz = (n_in, m) @ (m, n_out) = (n_in, n_out) ← ¡correcto!
        → Si transpusiéramos dz: dz.T @ a_prev = (n_out, m) @ (m, n_in) = (n_out, n_in) ← ¡incorrecto!
        """
        m = y_true.shape[0]
        
        # Último layer: derivada de BCE + Sigmoid
        # dL/dz_last = a_last - y_true
        # (Demostración: dL/da = -y/a + (1-y)/(1-a), da/dz = a(1-a))
        # (Al multiplicar: dL/dz = a - y)
        dz = self.activations[-1] - y_true
        
        # Recorrer capas de atrás hacia adelante
        for i in range(self.n_layers - 1, -1, -1):
            a_prev = self.activations[i]  # Activación de la capa anterior
            
            # Gradientes de pesos y biases
            dW = (1/m) * a_prev.T @ dz
            db = (1/m) * np.sum(dz, axis=0, keepdims=True)
            
            # Propagar el gradiente a la capa anterior (si no es la primera)
            if i > 0:
                da_prev = dz @ self.weights[i].T
                dz = da_prev * self.relu_derivative(self.z_values[i-1])
            
            # Actualizar pesos (Gradient Descent)
            self.weights[i] -= learning_rate * dW
            self.biases[i] -= learning_rate * db
    
    # ----- Training Loop -----
    
    def train(self, X, y, epochs=1000, lr=0.01, verbose=True):
        """
        Training loop con tracking de métricas.
        
        Cada época:
        1. Forward pass → calcular predicciones
        2. Calcular loss
        3. Backward pass → calcular gradientes y actualizar pesos
        4. Registrar métricas
        """
        history = {"loss": [], "accuracy": []}
        
        for epoch in range(epochs):
            # Forward
            y_pred = self.forward(X)
            loss = self.compute_loss(y_pred, y)
            
            # Backward
            self.backward(y, learning_rate=lr)
            
            # Métricas
            accuracy = np.mean((y_pred > 0.5).astype(int) == y)
            history["loss"].append(loss)
            history["accuracy"].append(accuracy)
            
            if verbose and (epoch < 5 or epoch % 200 == 0 or epoch == epochs - 1):
                print(f"  Epoch {epoch:4d} | Loss: {loss:.4f} | Acc: {accuracy:.4f}")
        
        return history
    
    # ----- Visualización -----
    
    def plot_decision_boundary(self, X, y, title="Decision Boundary"):
        """Visualiza la frontera de decisión aprendida por la red."""
        x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
        y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
        xx, yy = np.meshgrid(
            np.arange(x_min, x_max, 0.02),
            np.arange(y_min, y_max, 0.02)
        )
        
        grid = np.c_[xx.ravel(), yy.ravel()]
        Z = self.forward(grid)
        Z = Z.reshape(xx.shape)
        
        plt.figure(figsize=(10, 8))
        plt.contourf(xx, yy, Z, levels=50, cmap='RdYlBu', alpha=0.6)
        plt.contour(xx, yy, Z, levels=[0.5], colors='black', linewidths=2)
        plt.scatter(X[:, 0], X[:, 1], c=y.ravel(), cmap='RdYlBu', 
                    edgecolors='black', s=25, linewidth=0.5)
        plt.title(title, fontweight='bold', fontsize=14)
        plt.xlabel("x₁")
        plt.ylabel("x₂")
        plt.colorbar(label='P(clase 1)')
        plt.tight_layout()


# =============================================================================
# 🚀 EJECUTAR
# =============================================================================

if __name__ == "__main__":
    print(f"\n{'=' * 60}")
    print("🚀 ENTRENAMIENTO")
    print("=" * 60)
    
    # Crear la red
    np.random.seed(42)
    nn = NeuralNetworkFromScratch([2, 16, 8, 1])
    
    print(f"\n  Arquitectura: Input(2) → Dense(16, ReLU) → Dense(8, ReLU) → Dense(1, Sigmoid)")
    print(f"  Parámetros totales: {sum(w.size + b.size for w, b in zip(nn.weights, nn.biases))}")
    
    # Entrenar
    print(f"\n  Entrenando por 2000 epochs con lr=0.05...")
    history = nn.train(X_train, y_train, epochs=2000, lr=0.05)
    
    # Evaluar en test
    y_test_pred = nn.forward(X_test)
    test_acc = np.mean((y_test_pred > 0.5).astype(int) == y_test)
    test_loss = nn.compute_loss(y_test_pred, y_test)
    
    print(f"\n{'=' * 60}")
    print("📊 RESULTADOS")
    print("=" * 60)
    print(f"\n  Test Accuracy: {test_acc:.4f}")
    print(f"  Test Loss:     {test_loss:.4f}")
    print(f"  {'✅ OBJETIVO CUMPLIDO' if test_acc > 0.95 else '❌ Objetivo no cumplido (>95%)'}")
    
    # Visualizar frontera de decisión
    nn.plot_decision_boundary(X_test, y_test, 
                              f"Frontera de Decisión (Test Acc: {test_acc:.1%})")
    plt.savefig('proyecto/decision_boundary.png', dpi=100, bbox_inches='tight')
    plt.show()
    
    # Graficar curvas de entrenamiento
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    axes[0].plot(history["loss"], linewidth=2, color='#F44336')
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('BCE Loss')
    axes[0].set_title('Training Loss', fontweight='bold')
    
    axes[1].plot(history["accuracy"], linewidth=2, color='#4CAF50')
    axes[1].set_xlabel('Epoch')
    axes[1].set_ylabel('Accuracy')
    axes[1].set_title('Training Accuracy', fontweight='bold')
    axes[1].set_ylim(0.4, 1.05)
    
    plt.suptitle('Curvas de Entrenamiento', fontsize=15, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('proyecto/training_curves.png', dpi=100, bbox_inches='tight')
    plt.show()
    
    # Inspeccionar pesos
    print(f"\n{'=' * 60}")
    print("🔍 INSPECCIÓN DE PESOS")
    print("=" * 60)
    for i, (w, b) in enumerate(zip(nn.weights, nn.biases)):
        print(f"\n  Capa {i}: W{w.shape}, b{b.shape}")
        print(f"    |W| medio: {np.abs(w).mean():.4f}")
        print(f"    |b| medio: {np.abs(b).mean():.4f}")
        print(f"    W rango:   [{w.min():.4f}, {w.max():.4f}]")
    

    # =============================================================================
    # VERIFICACIÓN DE GRADIENTES (Gradient Checking)
    # =============================================================================
    """
    Para verificar que nuestro backward pass es correcto, comparamos
    nuestros gradientes analíticos con gradientes NUMÉRICOS (finite differences):
    
        dL/dw ≈ [L(w + ε) - L(w - ε)] / (2ε)
    
    Si la diferencia relativa es < 1e-5, nuestros gradientes son correctos.
    """
    
    print(f"\n{'=' * 60}")
    print("🧪 GRADIENT CHECKING")
    print("=" * 60)
    
    # Resetear la red para gradient checking
    np.random.seed(123)
    nn_check = NeuralNetworkFromScratch([2, 4, 1])  # Red pequeña para velocidad
    
    # Un mini-batch pequeño
    X_mini = X_train[:5]
    y_mini = y_train[:5]
    
    # Forward + backward para obtener gradientes analíticos
    y_pred = nn_check.forward(X_mini)
    loss = nn_check.compute_loss(y_pred, y_mini)
    
    # Guardar gradientes analíticos (antes de que backward() actualice)
    # Necesitamos recalcular sin actualizar
    m = y_mini.shape[0]
    dz = nn_check.activations[-1] - y_mini
    
    analytical_dW = []
    for i in range(nn_check.n_layers - 1, -1, -1):
        a_prev = nn_check.activations[i]
        dW = (1/m) * a_prev.T @ dz
        analytical_dW.insert(0, dW.copy())
        if i > 0:
            da_prev = dz @ nn_check.weights[i].T
            dz = da_prev * nn_check.relu_derivative(nn_check.z_values[i-1])
    
    # Gradientes numéricos (finite differences)
    epsilon = 1e-5
    print(f"\n  Usando ε = {epsilon}")
    
    for layer_idx in range(nn_check.n_layers):
        W = nn_check.weights[layer_idx]
        numerical_dW = np.zeros_like(W)
        
        # Solo verificar unos pocos pesos para velocidad
        n_checks = min(5, W.size)
        indices = [(np.random.randint(W.shape[0]), np.random.randint(W.shape[1])) 
                   for _ in range(n_checks)]
        
        max_diff = 0
        for i, j in indices:
            # L(w + ε)
            W[i, j] += epsilon
            y_plus = nn_check.forward(X_mini)
            loss_plus = nn_check.compute_loss(y_plus, y_mini)
            
            # L(w - ε)  
            W[i, j] -= 2 * epsilon
            y_minus = nn_check.forward(X_mini)
            loss_minus = nn_check.compute_loss(y_minus, y_mini)
            
            # Restaurar
            W[i, j] += epsilon
            
            # Gradiente numérico
            num_grad = (loss_plus - loss_minus) / (2 * epsilon)
            ana_grad = analytical_dW[layer_idx][i, j]
            
            diff = abs(num_grad - ana_grad) / (abs(num_grad) + abs(ana_grad) + 1e-15)
            max_diff = max(max_diff, diff)
        
        status = "✅" if max_diff < 1e-5 else "❌"
        print(f"  Capa {layer_idx}: max diff relativa = {max_diff:.2e} {status}")
    
    print(f"""
{'=' * 60}
🏆 RESUMEN DEL PROYECTO
{'=' * 60}

Lo que has implementado:
  ✅ Forward pass con ReLU + Sigmoid
  ✅ Binary Cross-Entropy Loss
  ✅ Backward pass completo con regla de la cadena
  ✅ He initialization
  ✅ Gradient checking numérico
  ✅ Visualización de frontera de decisión

Lo que deberías poder explicar:
  ❓ ¿Por qué se transpone a_prev y no dz en dW = a_prev.T @ dz?
  ❓ ¿Qué pasaría con pesos iniciales todos 0?
  ❓ ¿Por qué ReLU en capas ocultas y Sigmoid en la salida?
  ❓ ¿Qué es He init y por qué sqrt(2/n_in)?
  ❓ ¿Cómo se relaciona cada línea del backward con la regla de la cadena?

🎯 HITO DE CARRERA DESBLOQUEADO:
   Capacidad de depurar problemas de entrenamiento a nivel de gradientes.
   Entender vanishing/exploding gradients.
   Leer secciones matemáticas de papers sin bloqueo.
   
🏁 ¡MÓDULO 0 COMPLETADO! → Siguiente: Módulo 1 (DNN con PyTorch)
""")

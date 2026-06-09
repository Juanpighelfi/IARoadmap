# desafio_previo_3_oop.py
import numpy as np

# DESAFÍO: Construir un mini-framework de "capas" similar a PyTorch

# 1. Crea una clase base Layer con método forward(x) que lanza NotImplementedError

# 2. Crea LinearLayer(Layer) que:
#    - En __init__: recibe in_features, out_features
#    - Inicializa weight y bias con random
#    - forward(x): retorna x @ weight + bias

# 3. Crea ReLULayer(Layer) que:
#    - forward(x): retorna np.maximum(0, x)

# 4. Crea Sequential que:
#    - En __init__: recibe una lista de layers
#    - forward(x): pasa x por cada layer en orden y retorna el resultado final

class Layer:
    def __init__(self):
        self._parameters = {}

    def register_parameter(self, name, value):
        self._parameters[name] = value
    
    def parameters(self):
        return self._parameters.values()
    
    def forward(self, x):
        raise NotImplementedError

    def __call__(self, x):
        return self.forward(x)

class Sequential(Layer):
    def __init__(self, layers):
        super().__init__()
        # Guardamos la lista de capas en el estado del objeto 📦
        self.layers = layers

    def forward(self, x):
        # El truco: pasamos x por cada capa y actualizamos su valor 
        for layer in self.layers:
            x = layer(x) # La salida de una capa es la entrada de la siguiente
        return x

class LinearLayer(Layer):
    # ¡Importante! Ahora sí recibe el tamaño de entrada y salida
    def __init__(self, in_features, out_features):
        super().__init__()
        self.register_parameter('weight', np.random.randn(in_features, out_features) * 0.01)
        self.register_parameter('bias', np.zeros(out_features))

    def forward(self, x):
        return x @ self._parameters['weight'] + self._parameters['bias']

class ReLULayer(Layer):
    def __init__(self):
        super().__init__()
        # ReLU no tiene parámetros (pesos), así que el init queda vacío ✨

    def forward(self, x):
        return np.maximum(0, x)

# 5. Usa tu framework:
model = Sequential([
    LinearLayer(2, 16),
    ReLULayer(),
    LinearLayer(16, 8),
    ReLULayer(),
    LinearLayer(8, 1),
])

x = np.random.randn(5, 2)   # 5 muestras, 2 features
output = model.forward(x)
print(f"Input shape: {x.shape}")
print(f"Output shape: {output.shape}")  # Debería ser (5, 1)

# 6. Añade un método count_parameters() a Sequential
#    que cuente el total de parámetros entrenables (weight + bias de cada LinearLayer)
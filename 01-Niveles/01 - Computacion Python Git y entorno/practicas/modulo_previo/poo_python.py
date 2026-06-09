import numpy as np
class MiniModule:
    """Simulación simplificada de nn.Module para entender el patrón"""
    
    def __init__(self):
        self._parameters = {}   # Almacena los parámetros entrenables
    
    def register_parameter(self, name, value):
        """Registra un parámetro (como nn.Module hace automáticamente)"""
        self._parameters[name] = value
    
    def parameters(self):
        """Devuelve todos los parámetros (lo que pasas al optimizer)"""
        return self._parameters.values()
    
    def forward(self, x):
        raise NotImplementedError
    
    def __call__(self, x):
        """Permite hacer model(x) en vez de model.forward(x)"""
        return self.forward(x)


class MiniLinear(MiniModule):
    """Simulación de nn.Linear"""
    
    def __init__(self, in_features, out_features):
        super().__init__()
        import numpy as np
        # Inicializar pesos aleatorios
        self.register_parameter('weight', np.random.randn(in_features, out_features) * 0.01)
        self.register_parameter('bias', np.zeros(out_features))
    
    def forward(self, x):
        import numpy as np
        return x @ self._parameters['weight'] + self._parameters['bias']


# Usar exactamente como PyTorch:
layer = MiniLinear(5, 3)         # 5 inputs → 3 outputs
import numpy as np
x = np.random.randn(1, 5)       # 1 muestra, 5 features
output = layer(x)                # Llama a __call__ → forward
print(output.shape)   
print(layer.parameters())           # (1, 3)
print(f"Parámetros: {len(list(layer.parameters()))}")  # 2 (weight + bias)



# --- List Comprehensions ---
# Forma compacta de crear listas
cuadrados = [x**2 for x in range(10)]           # [0,1,2,3,4,5,6,7,8,9] -> [0, 1, 4, 9, 16, ...]
cuadrados_numpy = np.arange(0,10,1)**2
print(f"Cuadrados desde Numpy: {cuadrados_numpy}")

pares = [x for x in range(20) if x % 2 == 0]    # [0, 2, 4, 6, ...]

# En ML: crear listas de capas, filtrar datos, etc.

# --- Unpacking ---
a, b, c = [1, 2, 3]
primera, *resto = [1, 2, 3, 4, 5]   # primera=1, resto=[2,3,4,5]
# En ML: desempaquetar batches, datasets splits, etc.

# --- Diccionarios como configuración ---
config = {
    "lr": 0.001,
    "batch_size": 32,
    "epochs": 100,
    "hidden_dims": [256, 128, 64]
}
# Acceso: config["lr"], config.get("dropout", 0.5)  ← con default

# --- F-strings para logging ---
epoch, loss, acc = 42, 0.234, 0.956
print(f"Epoch {epoch:4d} | Loss: {loss:.4f} | Acc: {acc:.2%}")
# "Epoch   42 | Loss: 0.2340 | Acc: 95.60%"

# --- Context Managers (with) ---
# En ML: torch.no_grad(), open(), dispositivos
# with torch.no_grad():    ← desactiva autograd (para inferencia)
#     output = model(input)

# --- enumerate y zip ---
nombres = ["Adam", "SGD", "RMSprop"]
lrs = [0.001, 0.01, 0.0001]

for i, nombre in enumerate(nombres):    # índice + valor
    print(f"{i}: {nombre}")

for nombre, lr in zip(nombres, lrs):    # iterar en paralelo
    print(f"{nombre}: lr={lr}")

# --- Lambda functions ---
# Función anónima de una línea
relu = lambda x: max(0, x) # Definimos una funcion efimera. lambda quiere decir que vamos a usar una funcion. x actua como def(x) y despues de los : va lo que debe realizar.
print(relu(-5))   # 0
print(relu(3))    # 3

# --- Type hints (buena práctica) ---
def entrenar(modelo, datos: list, epochs: int = 10, lr: float = 0.01) -> dict:
    """Los type hints documentan qué espera y devuelve la función"""
    resultados = {"loss": [], "accuracy": []}
    # ...
    return resultados
import numpy as np
datos = np.random.randn(2, 5)          # 100 muestras, 5 features
print(f"Datos: {datos}")
media = datos.mean(axis=0)               # Shape: (5,) — media de cada feature
print(f"Media: {media}")
datos_centrados = datos - media           # Broadcasting: (100, 5) - (5,) → (100, 5)
print(f"Datos Centrados: {datos_centrados}")

print("-" * 30)
x = np.linspace(-5, 5, 100)
print(x)

print(f"{"-"*5}Sigmoide de x")
sigmoid = 1 / (1 + np.exp(-x))
print(sigmoid)

print(f"{"-"*5}ReLU de x")
relu = np.maximum(0, x)
print(relu)

print(f"{"-"*5}Softmax")
def softmax_debug(z):
    print(f"1. Logits originales: {z}")
    
    # Estabilidad
    z_stable = z - np.max(z)
    print(f"2. Tras restar el máximo ({np.max(z)}): {z_stable}")
    
    # Exponencial
    exp_z = np.exp(z_stable)
    print(f"3. Tras aplicar exponencial (e^z): {exp_z}")
    
    # Suma y división
    sum_exp = np.sum(exp_z)
    probabilidades = exp_z / sum_exp
    print(f"4. Suma total de exp: {sum_exp}")
    
    return probabilidades

logits = np.array([2.0, 1.0, 0.5])
resultado = softmax_debug(logits)
print(f"\n--- Resultado Final ---\n{resultado}")
print(f"Suma total: {np.sum(resultado)}")
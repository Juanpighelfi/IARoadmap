import numpy as np
import matplotlib.pyplot as plt

print("1. *"*10)
# 1. Crea una matriz de 5×5 con los números del 1 al 25
#    Extrae: la diagonal, la segunda fila, la última columna
arr = np.arange(25).reshape(5,5)
print(arr.shape)
print(arr)
print(f"La segunda fila: {arr[1,:]}")
print(f"La primera columna: {arr[:, 0]}")
print(f"Diagonal: {arr.diagonal()}")

print("2. *"*10)
# 2. Genera 1000 números aleatorios con distribución normal (media=5, std=2)
#    a) Calcula media y desviación estándar (¿se acercan a 5 y 2?)
#    b) ¿Cuántos caen dentro de ±1 std de la media? (debería ser ~68%)
#    c) Grafica un histograma con 30 bins
normal_dist = np.random.normal(5,2,1000)
print(normal_dist)
media = normal_dist.mean()
stdeviation = normal_dist.std()
print(f"Media={media}, Desviacion Estandar={stdeviation}")
mask = (normal_dist >(media-stdeviation)) & (normal_dist < media+stdeviation) 
print(mask)
print(f"La cantidad que caen en una std son: {mask.sum()}")
plt.hist(normal_dist,30)
plt.show()

print("3. *"*10)
# 3. Simula un dataset de ML:
#    - 500 muestras, cada una con 3 features
#    - Normaliza cada feature: (x - media) / std  (usa axis=0)
#    - Verifica que después de normalizar, media≈0 y std≈1 por feature
dataset = np.random.randint(100, 1800, 1500).reshape(500,3)
print(dataset.shape)
norm_dataset_mean = dataset.mean(axis=0)
norm_dataset_std = dataset.std(axis=0)
norm_dataset = (dataset - norm_dataset_mean) / norm_dataset_std
print(f"Dataset normalizado: {norm_dataset}")
print(f"Media={norm_dataset.mean(axis=0)}, Desviacion Estandar={norm_dataset.std(axis=0)}")

print("*"*10)
print("4.")

# 4. Implementa estas funciones SIN usar las de NumPy:
def mi_mean(arr):
    """Calcula la media de un array 1D"""
    sum = 0
    n = 0
    for items in arr:
        sum += items
        n += 1
    print(f"La cantidad de items es: {n}, la suma es: {sum}, la media es: {sum/n}")
    return sum/n
    

my_arr = np.random.randint(1, 10000, 100000)
mi_mean(my_arr)
print(my_arr.mean())

def mi_std(arr):
    """Calcula la desviación estándar de un array 1D"""
    media = mi_mean(arr)
    numerador_sum = 0
    n = 0
    for i in arr:
        numerador_sum += ((i-media)**2)
        n += 1

    desviacion = (numerador_sum / n)**(1/2)
    print(f"La desviación estándar es: {desviacion}")

    pass
mi_std(my_arr)
print(my_arr.std())

def mi_argmax(arr):
    """Devuelve el índice del valor máximo"""
    n = 0
    max_value = [0, None] # Primer valor es índice, segundo el numero
    for i in arr:
        if n == 0: max_value[1] = i
        if max_value[1] < i: 
            max_value[1] = i
            max_value[0] = n

        n+=1
    print(f"El valor máximo es: {max_value[1]} y está en la posición {max_value[0]}")
        
    pass
mi_argmax(my_arr)
print(my_arr.argmax())


# 5. Multiplicación de matrices:
#    A = [[1, 2], [3, 4]]
#    B = [[5, 6], [7, 8]]
#    a) Calcula A @ B a mano (en papel o con tu función mi_matmul)
#    b) Verifica con NumPy
#    c) ¿A @ B == B @ A? ¿Por qué importa esto en redes neuronales?
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"Son iguales! Vamos todavía") if ((A @ B) == (B @ A)).all() else print(f"LPM, no son iguales")
print(f"A @ B es: {A @ B} y B @ A es: {B @ A}")
import numpy as np

# ESTO ES TREMENDO, SE PUEDE SOLICITAR UNA SERIE DE NÚMEROS DE UN ÍNDICE USANDO ARRAYS

a = np.arange(12)**2  # the first 12 square numbers
print(a)
i = np.array([1, 1, 3, 8, 5])  # an array of indices
print(a[i])  # the elements of `a` at the positions `i`

j = np.array([[3, 4], [9, 7]])  # a bidimensional array of indices
print(a[j])  # the same shape as `j`

print("\n*** Accediendo a arrays multidimensionales ***")

# Accediendo a arrays multidimensionales con otros arrays
palette = np.array([[0, 0, 0],         # black
                    [255, 0, 0],       # red
                    [0, 255, 0],       # green
                    [0, 0, 255],       # blue
                    [255, 255, 255]])  # white
image = np.array([[0, 1, 2, 0],  # each value corresponds to a color in the palette
                  [0, 3, 4, 0]])
print(palette[image])  # the (2, 4, 3) color image

h = np.arange(12).reshape(3, 4)
print(h)

i = np.array([[0, 1],  # indices for the first dim of `a`
              [1, 2]])
k = np.array([[2, 1],  # indices for the second dim
              [3, 3]])
 

print(h[i, k])  # i and j must have equal shape
print(f"Uepaa\n {h[i, 2]}")
print(h[:, k])



# --- 1. TUPLA VS ARRAY (Coordenadas vs Selección) ---
print("--- 1. Tupla vs Array ---")
a = np.array([[10, 20, 30], 
              [40, 50, 60], 
              [70, 80, 90]])

# Una tupla es UNA coordenada: fila 0, columna 2
idx_tupla = (0, 2)
print(f"Coordenada {idx_tupla}:", a[idx_tupla]) # 30

# Un array es una LISTA DE FILAS: fila 0 y fila 2
idx_array = np.array([0, 2])
print("Filas seleccionadas:\n", a[idx_array]) 
# Resultado: la fila [10,20,30] y la [70,80,90]

print("-" * 30)

# --- 2. EL TRUCO DEL ARGMAX (Series de tiempo) ---
print("--- 2. Argmax y Mapeo ---")
# Imagina 3 sensores con 4 lecturas cada uno
lecturas = np.array([
    [0.1, 0.8, 0.2], # Tiempo 0
    [0.9, 0.2, 0.7], # Tiempo 1
    [0.3, 0.4, 0.9], # Tiempo 2
    [0.5, 0.6, 0.1]  # Tiempo 3
])
horas = np.array([10, 11, 12, 13]) # Las horas de cada fila

# ¿En qué FILA está el máximo de cada COLUMNA (sensor)?
indices_max = lecturas.argmax(axis=0) 
print("Índices de los máximos:", indices_max) # [1, 0, 2]

# Ahora usamos esos índices para saber A QUÉ HORA ocurrió
horas_max = horas[indices_max]
print("Horas en que ocurrieron los máximos:", horas_max)

print("-" * 30)

# --- 3. EL "TRUCO" DEL += (Asignación repetida) ---
print("--- 3. El peligro de los índices repetidos ---")
b = np.zeros(5)
indices_repetidos = [0, 0, 0]

# Intento 1: Sumar 1 tres veces a la posición 0
b[indices_repetidos] += 1

print("Resultado de b[[0,0,0]] += 1:", b) 
# ¡Sorpresa! b[0] es 1, no 3.

# EXPLICACIÓN:
# b[indices] += 1 se traduce como:
# b[indices] = b[indices] + 1
# 1. Extrae los valores: [0, 0, 0]
# 2. Les suma 1: [1, 1, 1]
# 3. Los asigna: b[0]=1, luego b[0]=1, luego b[0]=1. El resultado final es 1.

# SOLUCIÓN si quieres que sume de verdad:
np.add.at(b, indices_repetidos, 1)
print("Resultado usando np.add.at:", b) # Ahora sí: [3, 0, 0, 0, 0]


print("--- Indexing Booleanos Arrays ---")
a = np.arange(12).reshape(3,4) # 3 filas, 4 columnas
print(a) 

b = a > 4
print(b)

print(a[b])
a[b]=0
print(a)

a = np.arange(12).reshape(3, 4)
b1 = np.array([False, True, True])         # first dim selection
b2 = np.array([True, False, True, False])  # second dim selection

a[b1, :] # Imprimimos solo las filas 2 y 3 que son las que tienen true                      
a[b1]                                      # same thing que arriba
a[:, b2]                                   # selecting columns, solo la 1era y 3era columna
a[b1, b2]                                  # a weird thing to do

# Imagina que 'a' son tipos de pan, 'b' son rellenos y 'c' son salsas
panes = np.array([1, 2])          # 2 tipos
rellenos = np.array([10, 20, 30]) # 3 tipos
salsas = np.array([100, 200])     # 2 tipos

# Creamos la "malla" (mesh)
px, rx, sx = np.ix_(panes, rellenos, salsas)

# Calculamos todas las combinaciones posibles de una:
# px + rx + sx
menu_total = px + rx + sx

print("Forma del menú final:", menu_total.shape) # (2, 3, 2)
print("---")

# Si quiero la combinación: Pan índice 0, Relleno índice 2, Salsa índice 1
print("Resultado manual:", panes[0] + rellenos[2] + salsas[1])
print("Resultado en la matriz:", menu_total[0, 2, 1]) 
print(menu_total)
# ¡Ambos dan 231!
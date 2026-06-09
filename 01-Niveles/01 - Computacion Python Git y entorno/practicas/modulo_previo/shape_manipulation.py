import numpy as np

# Uno puede manipular la forma de los arrays de distintas formas
a = np.arange(3,128,2)
print(a)

print(a.ravel())  # returns the array, flattened
print(a.reshape(3, -1))  # returns the array with a modified shape, el -1 calcula automáticamente la otra dimensión para que concuerde
print(a.T)  # returns the array, transposed


# Diferencias entre reshape y resize
# La diferencia fundamental es: reshape es conservador (solo cambia la vista), mientras que resize es transformador (puede alterar el contenido).
# Si necesita más elementos, al usar resize numpy va a llenar automáticamente los huecos vacíos con datos originales

# Apilando arrays
print("\n*** Podemos apilar arrays de manera simple, siempre que sean del mismo tamaño ***")
c = np.floor(10 * rg.random((2, 2)))
d = np.floor(10 * rg.random((2, 2)))
np.vstack((a, b)) # Verticalmente
np.hstack((a, b)) # Horizontalmente

a = np.array([1, 2])
b = np.array([3, 4])

print(f"Array A: {a}")
print(f"Array B: {b}\n")

# 1. HSTACK: Pega uno al lado del otro (Horizontal)
# Resultado: Una sola fila larga
h = np.hstack((a, b))
print("--- hstack ---")
print(h)  # [1 2 3 4]

# 2. VSTACK: Pega uno ENCIMA del otro (Vertical)
# Resultado: Una matriz de 2 filas y 2 columnas
v = np.vstack((a, b))
print("\n--- vstack ---")
print(v)
# [[1 2]
#  [3 4]]

# 3. COLUMN_STACK: Pega como si cada array fuera una columna
# Resultado: Una matriz de 2 filas y 2 columnas (pero rotada)
c = np.column_stack((a, b))
print("\n--- column_stack ---")
print(c)
# [[1 3]
#  [2 4]]


# Dividiendo un array en multiples chiquitos
# HSPLIT
# vsplit splits along the vertical axis, and array_split allows one to specify along which axis to split.


a = np.arrayarray([[6., 7., 6., 9., 0., 5., 4., 0., 6., 8., 5., 2.],
       [8., 5., 5., 7., 1., 8., 6., 7., 1., 8., 1., 0.]])

# Split `a` into 3
np.hsplit(a, 3)
# Split `a` after the third and the fourth column
np.hsplit(a, (3, 4))
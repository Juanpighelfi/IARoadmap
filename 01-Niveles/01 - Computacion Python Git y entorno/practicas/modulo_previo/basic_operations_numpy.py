import numpy as np

a = np.array([20, 30, 40, 50])
b = np.arange(4)

c = a - b

print(f"Resta de {a} con {b} es igual a {c}")

print(b**2)

print(10 * np.sin(a))
print(a < 35)

print("\n*** Multiplicacion de Matrices ***")

A = np.array([[1, 1],
              [0, 1]])

B = np.array([[2, 0],
              [3, 4]])

print(A * B)    # elementwise product
print(A @ B)     # matrix product

print("\n*** Usando asignadores y acumuladores ***")

rg = np.random.default_rng(1)  # create instance of default random number generator
f = np.ones((2, 3), dtype=int)
g = rg.random((2, 3))
f *= 3
print(f)

print(a.sum())
print(a.min())
print(a.max())

b = np.arange(12).reshape(3, 4)

b.sum(axis=0)     # sum of each column
b.min(axis=1)     # min of each row
b.cumsum(axis=1)  # cumulative sum along each row



print("\n*** Funciones universales ***")


C = np.arange(3)
print(C)

np.exp(C)
np.sqrt(C)
D = np.array([2., -1., 4.])
np.add(C, D)

# Caso con +=
x = np.array([1, 2], dtype=int)
x += 1  # Funciona, x ahora es [2, 3]
# x += 1.5  <-- ¡Esto daría ERROR! No puede convertir float a int in-place.

# Caso con np.add
y = np.array([1, 2], dtype=int)
z = np.add(y, 1.5) # Funciona perfectamente, z es float64: [2.5, 3.5]
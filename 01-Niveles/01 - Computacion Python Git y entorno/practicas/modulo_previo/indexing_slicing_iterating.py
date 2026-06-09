import numpy as np


print("\n*** Seleccionando un elemento en un array unidimensional ***")

a = np.arange(10)
print(a)
a = a**3
print(f"Todos los elementos son: \n {a} \n Seleccionar un elemento se hace con a[elemento], por ejemplo: {a[3]}")

print("\n*** np.fromFunction un elemento en un array multidimensional ***")

def distancia_al_centro(x, y):
    centro = 2  # Para una matriz de 5x5
    return np.sqrt((x - centro)**2 + (y - centro)**2)

capa = np.fromfunction(distancia_al_centro, (5, 5))
print(capa)

print("\n*** Slicing y seleccionando un elemento en un array multidimensional ***")

print(capa[2,3])
print(capa[0:5, 2]) # Es lo mismo que usar capa[:, 2]
print(capa[1:3, :]) # Si no hay indice, por ejemplo capa[1], se considera que el segundo índice es : y trae todo

# x[1, 2, ...] is equivalent to x[1, 2, :, :, :],
# x[..., 3] to x[:, :, :, :, 3] and
# x[4, ..., 5, :] to x[4, :, :, 5, :].

print("\n*** Iterando ***")
b = np.arange(6).reshape(2,3)
print(b)

for row in b:
    print(row)

# Para operar individualmente en cada item del array multidimensional, podemos usar flat
for element in b.flat:
    print(element+1)
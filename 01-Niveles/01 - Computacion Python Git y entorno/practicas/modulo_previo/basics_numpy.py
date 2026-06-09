import numpy as np 


print("*** Reshape y arange ***")
a = np.arange(1,12,2)
a = a.reshape(int(a.size/3), a.size//2)

print(a)

print("\n*** Array Creation ***")

b = np.array([2,5,6,7,1])
print(b)

c = np.array([[(2, 3), (4,5)], [(6,7), (8,9)]])
print(f"El array es: {c} y el tamaño es: {c.size} con {c.ndim} dimensiones")

print("\n*** Creando Arrays Predefinidos ***")

z=np.zeros((3,3, 3, 4)) # Creamos una matriz que tiene 3 filas con 4 items cada una
o=np.ones((2, 3, 4), dtype=np.int16) # Creamos dos matrices que tienen 3 filas y 4 items cada una
e=np.empty((2, 3)) # Creamos una matriz fcon dos filas y tres items cada una donde el valor de cada item es aleatorio

print(z)
print("\n")
print(o)
print("\n")

print(e)
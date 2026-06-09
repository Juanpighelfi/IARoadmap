import numpy as np

# ****** No se copian de esta forma
a = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11]])
b=a # No se crea nuevo objeto, se vuelven dos nombres para el mismo objeto ndarray


# ****** Vista, comparten la data, crea un nuevo array que ve a la misma data
c = a.view()
print(f"c.base is a nos devuelve si se usa la misma base. Es la misma base? {c.base is a}")

c = c.reshape((2, 6))  # a's shape doesn't change, reassigned c is still a view of a
c[0, 4] = 1234         # los datos de a SÍ CAMBIAN!
print(a)

# Lo mismo pasa si hacemos un slicing

# ******* Copia profunda, copia todo el array y sus datos

d = a.copy()
print(d is a)
print(d.base is a)
d[0,0] = 9999
print(a) # a se mantiene como estaba

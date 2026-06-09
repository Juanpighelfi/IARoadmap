# desafio_semana1.py — Álgebra Lineal operativa
import numpy as np

# DESAFÍO 1: Implementa la multiplicación de matrices "a mano" (sin np.matmul)
def mi_matmul(A, B):
    """Multiplica matrices A (m×n) y B (n×p) devolviendo C (m×p)"""
    C = np.zeros((A.shape[0], B.shape[1]))
    for column in range(B.shape[1]):
        B_column = B[:, column]
        column_c = np.zeros((A.shape[0]))
        for a_columns in range(A.shape[1]):
            column_c += B_column[a_columns] * A[:, a_columns]

        C[:, column] = column_c
    print(f"El producto con la función custom es: {C}")
    pass

A = np.random.randint(0, 100, (2,2))
B = np.random.randint(0, 100, (2,2))
mi_matmul(A, B)
dot_product = A @ B
print(f"El producto con numpy es: {dot_product}")
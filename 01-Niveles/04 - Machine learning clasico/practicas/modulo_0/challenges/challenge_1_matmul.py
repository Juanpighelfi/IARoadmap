"""
=============================================================================
🏆 CHALLENGE 1: Implementar Multiplicación de Matrices desde Cero
=============================================================================

OBJETIVO: Entender qué sucede "debajo del capó" cuando hacemos W @ x.
          No usar np.matmul, np.dot, ni el operador @.

CONCEPTO: La multiplicación de matrices es la BASE de toda red neuronal.
          Cada forward pass es una cadena de multiplicaciones de matrices.

DURACIÓN: ~30 minutos
DIFICULTAD: ⭐⭐ (Intermedia)

DESPUÉS DE COMPLETAR: Deberías poder explicar:
  1. Por qué las dimensiones internas deben coincidir (n)
  2. Qué representa cada elemento c_ij del resultado
  3. Al menos DOS formas de pensar la multiplicación:
     - Fila por columna (producto punto)
     - Combinación lineal de columnas
=============================================================================
"""

import numpy as np
import time


# =============================================================================
# PARTE 1: Implementación "fila × columna" (la más intuitiva)
# =============================================================================
"""
c_ij = Σ_k  A[i,k] * B[k,j]

Cada elemento del resultado es el PRODUCTO PUNTO de:
  - la fila i de A
  - la columna j de B
"""

def matmul_filas_columnas(A, B):
    """
    Multiplica A (m×n) y B (n×p) usando el enfoque fila × columna.
    
    INSTRUCCIONES:
    - Verifica que las dimensiones sean compatibles
    - Usa 3 loops anidados: i (filas de A), j (columnas de B), k (dimensión interna)
    - NO uses np.dot, np.matmul, ni @
    """
    m, n = A.shape
    n2, p = B.shape
    
    assert n == n2, f"Dimensiones incompatibles: A es {A.shape}, B es {B.shape}. A.columns ({n}) != B.rows ({n2})"
    
    C = np.zeros((m, p))
    
    # TODO: tu implementación aquí
    # Hint: C[i, j] = sum(A[i, k] * B[k, j] for k in range(n))
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]
    
    return C


# =============================================================================
# PARTE 2: Implementación "combinación lineal de columnas"
# =============================================================================
"""
Esta es la visión de 3Blue1Brown:

  A @ B = [A @ b₁ | A @ b₂ | ... | A @ bₚ]

Cada columna del resultado es A multiplicado por una columna de B.
Y cada A @ bⱼ es una COMBINACIÓN LINEAL de las columnas de A,
con los coeficientes dados por bⱼ.

TU IMPLEMENTACIÓN ORIGINAL está basada en esta idea (¡bien hecho!).
"""

def matmul_combinacion_columnas(A, B):
    """
    Multiplica A (m×n) y B (n×p) usando combinaciones lineales de columnas.
    
    INSTRUCCIONES:
    - Para cada columna j de B:
      - La columna j del resultado = combinación lineal de columnas de A
      - Los coeficientes son los elementos de la columna j de B
    """
    m, n = A.shape
    n2, p = B.shape
    assert n == n2, f"Dimensiones incompatibles"
    
    C = np.zeros((m, p))
    
    # TODO: tu implementación aquí
    for j in range(p):  # Para cada columna del resultado
        for k in range(n):  # Combinación lineal
            C[:, j] += B[k, j] * A[:, k]
    
    return C


# =============================================================================
# PARTE 3: Implementación vectorizada (sin loops en k)
# =============================================================================
"""
Podemos eliminar el loop interno usando el producto punto de NumPy
sobre filas/columnas individuales. Esto es MÁS RÁPIDO porque NumPy
ejecuta operaciones vectorizadas en C bajo el capó.
"""

def matmul_semi_vectorizada(A, B):
    """
    Multiplica A (m×n) y B (n×p) usando solo 2 loops.
    Usa np.sum() o np.dot() solo para el loop interno.
    
    INSTRUCCIONES:
    - Usa 2 loops (i, j) pero reemplaza el loop k con np.sum
    """
    m, n = A.shape
    n2, p = B.shape
    assert n == n2, f"Dimensiones incompatibles"
    
    C = np.zeros((m, p))
    
    # TODO: tu implementación aquí
    for i in range(m):
        for j in range(p):
            C[i, j] = np.sum(A[i, :] * B[:, j])
    
    return C


# =============================================================================
# VERIFICACIÓN Y BENCHMARK
# =============================================================================

print("=" * 60)
print("🧪 VERIFICACIÓN DE IMPLEMENTACIONES")
print("=" * 60)

# Test con matrices pequeñas
np.random.seed(42)
A = np.random.randint(0, 10, (3, 4))
B = np.random.randint(0, 10, (4, 2))

print(f"\nA ({A.shape}):\n{A}")
print(f"\nB ({B.shape}):\n{B}")

# Resultado correcto (NumPy)
expected = A @ B
print(f"\n✅ NumPy (A @ B):\n{expected}")

# Verificar cada implementación
implementations = [
    ("Fila × Columna", matmul_filas_columnas),
    ("Combinación Columnas", matmul_combinacion_columnas),
    ("Semi-vectorizada", matmul_semi_vectorizada),
]

for name, func in implementations:
    result = func(A, B)
    is_correct = np.allclose(result, expected)
    status = "✅ CORRECTO" if is_correct else "❌ INCORRECTO"
    print(f"\n  {name}: {status}")
    if not is_correct:
        print(f"    Tu resultado:\n{result}")

# Benchmark de velocidad
print(f"\n{'=' * 60}")
print("⏱️  BENCHMARK DE VELOCIDAD")
print("=" * 60)

sizes = [5, 10, 30, 1000]  # Mantenemos chico porque los loops de Python son lentos
for size in sizes:
    A_bench = np.random.randn(size, size)
    B_bench = np.random.randn(size, size)
    
    print(f"\n  Matrices {size}×{size}:")
    
    for name, func in implementations:
        start = time.time()
        _ = func(A_bench, B_bench)
        elapsed = time.time() - start
        print(f"    {name:25s}: {elapsed:.4f}s")
    
    start = time.time()
    _ = A_bench @ B_bench
    elapsed = time.time() - start
    print(f"    {'NumPy (@)':25s}: {elapsed:.6f}s")

print(f"""
{'=' * 60}
🧠 REFLEXIÓN
{'=' * 60}

1. ¿Por qué NumPy @ es MILES de veces más rápido que los loops de Python?
   → NumPy usa BLAS (Basic Linear Algebra Subprograms) implementado en C/Fortran
   → Accede a la memoria de forma contigua (cache-friendly)
   → Puede usar instrucciones SIMD del procesador (SSE, AVX)

2. ¿Cuántas operaciones de multiplicación hace matmul para matrices n×n?
   → n³ multiplicaciones. Para n=1000: ¡mil millones de multiplicaciones!
   → Por eso las GPUs son esenciales: están diseñadas para matmul masivo.

3. ¿Qué enfoque (fila×columna vs combinación de columnas) te parece 
   más intuitivo para entender redes neuronales?
   → La combinación de columnas es la visión de 3Blue1Brown y es más
     geométrica: cada columna del resultado es un punto transformado.
""")

# =============================================================================
# BONUS: Verificar dimensiones edge cases
# =============================================================================
print("\n🏋️ BONUS: Tests de edge cases")

# Vector × Matriz
v = np.array([[1, 2, 3]])  # (1, 3) — vector fila
M = np.array([[4, 5], [6, 7], [8, 9]])  # (3, 2)
result = matmul_filas_columnas(v, M)
expected_vm = v @ M
print(f"  Vector(1×3) × Matriz(3×2) = {result.flatten()} | expected: {expected_vm.flatten()} | ✅ {np.allclose(result, expected_vm)}")

# Matriz × Vector
M2 = np.array([[1, 2], [3, 4], [5, 6]])  # (3, 2)
v2 = np.array([[7], [8]])  # (2, 1)
result = matmul_filas_columnas(M2, v2)
expected_mv = M2 @ v2
print(f"  Matriz(3×2) × Vector(2×1) = {result.flatten()} | expected: {expected_mv.flatten()} | ✅ {np.allclose(result, expected_mv)}")

print("\n✅ Challenge 1 completado!")

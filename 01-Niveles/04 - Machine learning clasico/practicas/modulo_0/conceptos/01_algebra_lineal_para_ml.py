"""
=============================================================================
📐 ÁLGEBRA LINEAL PARA ML — Guía Conceptual Interactiva
=============================================================================

PROPÓSITO: Reforzar los conceptos de 3Blue1Brown con código ejecutable.
           Ejecuta este archivo sección por sección, o todo de una vez.

PRERREQUISITO: Haber visto "La Esencia del Álgebra Lineal" de 3Blue1Brown
DURACIÓN: ~45 minutos de lectura activa + experimentación

Después de esta guía, estarás preparado para hacer los challenges 1-3.
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# Configuración global de matplotlib para gráficos bonitos
plt.rcParams.update({
    'figure.figsize': (8, 6),
    'font.size': 11,
    'axes.grid': True,
    'grid.alpha': 0.3
})


# =============================================================================
# 1️⃣ VECTORES: La unidad fundamental
# =============================================================================
"""
En ML, un vector es una LISTA DE NÚMEROS que representa algo:
  - Un punto de datos (features de una casa: [metros², habitaciones, precio])
  - Un peso del modelo (los parámetros que ajustamos)
  - Un gradiente (la dirección de mayor cambio)

Geométricamente, un vector es una FLECHA desde el origen hasta un punto.
"""

print("=" * 60)
print("1️⃣  VECTORES")
print("=" * 60)

# Un vector en NumPy
v = np.array([3, 2])
w = np.array([1, 4])

# Operaciones fundamentales
print(f"\nv = {v}")
print(f"w = {w}")
print(f"v + w = {v + w}")           # Suma: punta-cola
print(f"2 * v = {2 * v}")     
print(f"1/2 * v = {(1/2) * v}")           # Escalado: estira/encoge
print(f"v · w = {np.dot(v, w)}")
print(f"v * w = {v * w}")    # Producto matricial
print(f"|v| = {np.linalg.norm(v):.4f}")  # Norma: longitud del vector

"""
🔑 CONCEPTO CLAVE PARA ML:
El producto punto v·w mide "cuánto se parecen las direcciones" de v y w.
- Si v·w > 0: apuntan en dirección similar
- Si v·w = 0: son perpendiculares (ortogonales)
- Si v·w < 0: apuntan en direcciones opuestas

En una neurona: output = dot(weights, inputs) + bias
El producto punto mide cuánto los inputs "coinciden" con lo que la neurona busca.
"""

# Visualización de vectores
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Subplot 1: Vectores originales
ax = axes[0]
ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='#2196F3', label='v', linewidth=2)
ax.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='#FF5722', label='w', linewidth=2)
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
ax.legend(fontsize=12)
ax.set_title('Vectores v y w')

# Subplot 2: Suma de vectores (regla del paralelogramo)
ax = axes[1]
ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='#2196F3', label='v', linewidth=2)
ax.quiver(v[0], v[1], w[0], w[1], angles='xy', scale_units='xy', scale=1, color='#FF5722', label='w', linewidth=2, alpha=0.7)
suma = v + w
ax.quiver(0, 0, suma[0], suma[1], angles='xy', scale_units='xy', scale=1, color='#4CAF50', label='v+w', linewidth=2.5)
ax.set_xlim(0, 6)
ax.set_ylim(0, 7)
ax.set_aspect('equal')
ax.legend(fontsize=12)
ax.set_title('Suma: v + w (punta-cola)')

# Subplot 3: Producto punto como proyección
ax = axes[2]
ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='#2196F3', label='v', linewidth=2)
ax.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='#FF5722', label='w', linewidth=2)
# Proyección de w sobre v
proj_scalar = np.dot(w, v) / np.dot(v, v)
proj_vector = proj_scalar * v
ax.quiver(0, 0, proj_vector[0], proj_vector[1], angles='xy', scale_units='xy', scale=1, 
          color='#9C27B0', label=f'proj_v(w) = {proj_scalar:.2f}·v', linewidth=2.5)
ax.plot([w[0], proj_vector[0]], [w[1], proj_vector[1]], 'k--', alpha=0.3)
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
ax.legend(fontsize=10)
ax.set_title('Producto punto como proyección')

plt.tight_layout()
plt.show()

input("\n[Presiona Enter para continuar a la siguiente sección...]\n")


# =============================================================================
# 2️⃣ MATRICES COMO TRANSFORMACIONES LINEALES
# =============================================================================
"""
Esta es LA idea más importante de 3Blue1Brown:

    Una MATRIZ es una TRANSFORMACIÓN del espacio.

Cuando multiplicamos un vector por una matriz:
    y = A · x

Estamos TRANSFORMANDO x: lo rotamos, lo escalamos, lo deformamos.

En ML, cada capa de una red neuronal es exactamente esto:
    output = W · input + bias

W es una transformación que aprende a extraer las features útiles.
"""

print("\n" + "=" * 60)
print("2️⃣  MATRICES COMO TRANSFORMACIONES LINEALES")
print("=" * 60)

# Función helper para visualizar transformaciones
def plot_transformation(A, title="Transformación", ax=None):
    """Visualiza cómo una matriz A transforma una grilla 2D."""
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    
    # Crear grilla de puntos
    t = np.linspace(-2, 2, 20)
    
    # Líneas horizontales y verticales de la grilla
    colors_h = plt.cm.Blues(np.linspace(0.3, 0.9, len(t)))
    colors_v = plt.cm.Reds(np.linspace(0.3, 0.9, len(t)))
    
    for i, val in enumerate(t):
        # Línea horizontal: y = val, x varía
        line_h = np.array([[x, val] for x in t])
        transformed_h = (A @ line_h.T).T
        ax.plot(transformed_h[:, 0], transformed_h[:, 1], color=colors_h[i], alpha=0.5, linewidth=0.8)
        
        # Línea vertical: x = val, y varía
        line_v = np.array([[val, y] for y in t])
        transformed_v = (A @ line_v.T).T
        ax.plot(transformed_v[:, 0], transformed_v[:, 1], color=colors_v[i], alpha=0.5, linewidth=0.8)
    
    # Vectores base transformados
    e1_transformed = A @ np.array([1, 0])
    e2_transformed = A @ np.array([0, 1])
    
    ax.quiver(0, 0, e1_transformed[0], e1_transformed[1], angles='xy', scale_units='xy', scale=1, 
              color='#2196F3', linewidth=3, label=f'Ae₁ = [{e1_transformed[0]:.1f}, {e1_transformed[1]:.1f}]')
    ax.quiver(0, 0, e2_transformed[0], e2_transformed[1], angles='xy', scale_units='xy', scale=1, 
              color='#FF5722', linewidth=3, label=f'Ae₂ = [{e2_transformed[0]:.1f}, {e2_transformed[1]:.1f}]')
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.legend(fontsize=10)
    ax.set_title(title, fontsize=13, fontweight='bold')
    return ax

# Mostrar varias transformaciones
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Identidad
I = np.eye(2)
plot_transformation(I, "Identidad\n[[1,0],[0,1]]", axes[0, 0])

# Escala
S = np.array([[2, 0], [0, 0.5]])
plot_transformation(S, "Escala\n[[2,0],[0,0.5]]", axes[0, 1])

# Rotación 45°
theta = np.pi / 4
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
plot_transformation(R, f"Rotación {np.degrees(theta):.0f}°", axes[0, 2])

# Shear (cizalla)
Sh = np.array([[1, 1], [0, 1]])
plot_transformation(Sh, "Shear (Cizalla)\n[[1,1],[0,1]]", axes[1, 0])

# Reflexión
Ref = np.array([[1, 0], [0, -1]])
plot_transformation(Ref, "Reflexión eje X\n[[1,0],[0,-1]]", axes[1, 1])

# Compresión a 1D (rango 1 — pierde información)
Comp = np.array([[1, 1], [0, 0]])
plot_transformation(Comp, "Rango 1 (pierde dim)\n[[1,1],[0,0]]", axes[1, 2])

plt.suptitle("Matrices = Transformaciones del Espacio", fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()

plt.show()

"""
🔑 CONCEPTOS CLAVE:
- Las COLUMNAS de la matriz te dicen a dónde van los vectores base e₁ y e₂
- El DETERMINANTE te dice cuánto cambia el área (det > 0: conserva orientación, det < 0: la invierte)
- Si det = 0, la transformación "aplasta" el espacio a una dimensión menor (pierde información)
- El RANGO de la matriz = dimensión del espacio de salida
"""

print("\nDeterminantes de cada transformación:")
for name, M in [("Identidad", I), ("Escala", S), ("Rotación", R), 
                ("Shear", Sh), ("Reflexión", Ref), ("Compresión", Comp)]:
    det = np.linalg.det(M)
    rank = np.linalg.matrix_rank(M)
    print(f"  {name:15s}: det = {det:6.2f}, rango = {rank}")

input("\n[Presiona Enter para continuar...]\n")


# =============================================================================
# 3️⃣ MULTIPLICACIÓN DE MATRICES = COMPOSICIÓN DE TRANSFORMACIONES
# =============================================================================
"""
Si A y B son transformaciones, entonces A·B significa:
    "Primero aplica B, luego aplica A"

Esto es EXACTAMENTE lo que pasa en una red neuronal:
    y = W₃ · (relu(W₂ · (relu(W₁ · x + b₁)) + b₂)) + b₃

Cada Wᵢ es una transformación. La red compone transformaciones apiladas.
"""

print("\n" + "=" * 60)
print("3️⃣  COMPOSICIÓN DE TRANSFORMACIONES")
print("=" * 60)

# Ejemplo: Rotar 30° y luego escalar 2x en X
theta = np.pi / 6  # 30°
R_30 = np.array([[np.cos(theta), -np.sin(theta)],
                 [np.sin(theta),  np.cos(theta)]])
S_2x = np.array([[2, 0], [0, 1]])

# Composición: primero rotar, luego escalar
compuesta = S_2x @ R_30  # "S_2x después de R_30"

print(f"R_30 (rotación 30°):\n{R_30.round(3)}\n")
print(f"S_2x (escala 2x en X):\n{S_2x}\n")
print(f"S_2x @ R_30 (primero rotar, luego escalar):\n{compuesta.round(3)}")

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
plot_transformation(R_30, "Paso 1: Rotar 30°", axes[0])
plot_transformation(S_2x, "Paso 2: Escalar 2x en X", axes[1])
plot_transformation(compuesta, "Composición: S₂ₓ · R₃₀", axes[2])
plt.tight_layout()
plt.show()

"""
⚠️ ¡OJO! El orden importa: A·B ≠ B·A (en general)
Esto es por qué en redes neuronales el orden de las capas importa.
"""

# Demostrar no conmutatividad
AB = S_2x @ R_30
BA = R_30 @ S_2x
print(f"\n¿S·R == R·S? {np.allclose(AB, BA)} ← ¡NO conmutan!")
print(f"S·R =\n{AB.round(3)}")
print(f"R·S =\n{BA.round(3)}")

input("\n[Presiona Enter para continuar...]\n")


# =============================================================================
# 4️⃣ EIGENVALORES Y EIGENVECTORES
# =============================================================================
"""
Para una transformación A, un eigenvector v es un vector que NO cambia de dirección
cuando A lo transforma. Solo se ESCALA por un factor λ (el eigenvalor):

    A · v = λ · v

¿Por qué importa en ML?

1. PCA (Análisis de Componentes Principales):
   Los eigenvectores de la matriz de covarianza son las DIRECCIONES de
   máxima varianza en tus datos. Los eigenvalores te dicen CUÁNTA varianza
   hay en cada dirección.

2. Estabilidad de redes:
   Si los eigenvalores de los Jacobianos son > 1: gradientes explotan
   Si son < 1: gradientes desaparecen (vanishing gradient)

3. SVD y LoRA:
   Descomposición en valores singulares usa eigenvalores para comprimir matrices.
"""

print("\n" + "=" * 60)
print("4️⃣  EIGENVALORES Y EIGENVECTORES")
print("=" * 60)

# Ejemplo concreto
A = np.array([[3, 1],
              [0, 2]])

eigenvalores, eigenvectores = np.linalg.eig(A)

print(f"\nMatriz A:\n{A}")
print(f"\nEigenvalores: {eigenvalores}")
print(f"\nEigenvectores (columnas):\n{eigenvectores}")

# Verificación: A·v = λ·v
for i in range(len(eigenvalores)):
    v = eigenvectores[:, i]
    lam = eigenvalores[i]
    Av = A @ v
    lam_v = lam * v
    print(f"\n  Eigenvector v{i+1} = {v.round(4)}")
    print(f"  λ{i+1} = {lam}")
    print(f"  A·v{i+1} = {Av.round(4)}")
    print(f"  λ{i+1}·v{i+1} = {lam_v.round(4)}")
    print(f"  ¿A·v = λ·v? {np.allclose(Av, lam_v)}")

# Visualización
fig, ax = plt.subplots(1, 1, figsize=(8, 8))
plot_transformation(A, f"Transformación A con eigenvectores", ax)

for i in range(len(eigenvalores)):
    v = eigenvectores[:, i]
    lam = eigenvalores[i]
    color = '#4CAF50' if i == 0 else '#FFC107'
    # Vector original
    ax.quiver(0, 0, v[0]*2, v[1]*2, angles='xy', scale_units='xy', scale=1, 
              color=color, linewidth=3, alpha=0.8, 
              label=f'eigenvector v{i+1}, λ={lam:.1f}')
    # Vector transformado (escalado por lambda)
    Av = A @ (v * 2)
    ax.quiver(0, 0, Av[0], Av[1], angles='xy', scale_units='xy', scale=1, 
              color=color, linewidth=3, alpha=0.4, linestyle='dashed')

ax.legend(fontsize=11, loc='upper left')
plt.show()

input("\n[Presiona Enter para continuar...]\n")


# =============================================================================
# 5️⃣ RANGO DE UNA MATRIZ Y PÉRDIDA DE INFORMACIÓN
# =============================================================================
"""
El RANGO de una matriz = el número de dimensiones independientes de la salida.

Si tienes una matriz W de forma (m × n):
- rango(W) ≤ min(m, n)
- Si rango(W) = min(m, n): la transformación es "completa", no pierde dimensiones
- Si rango(W) < min(m, n): la transformación APLASTA datos a menos dimensiones

En ML esto aparece en:
- LoRA: ΔW = A·B donde A es (d×r) y B es (r×d) con r << d
  El rango de ΔW es como máximo r. Esto funciona porque los cambios
  necesarios para fine-tuning viven en un subespacio de bajo rango.

- Bottleneck layers: Una capa de 768→64→768 fuerza a la red a comprimir
  la representación a 64 dimensiones.
"""

print("\n" + "=" * 60)
print("5️⃣  RANGO DE UNA MATRIZ")
print("=" * 60)

# Rango completo vs bajo rango
W_full = np.array([[1, 2],
                   [3, 5]])

W_low = np.array([[1, 2],
                  [2, 4]])  # fila 2 = 2 × fila 1 SON LINEALMENTE DEPENDIENTES PORQUE UNA ES EL DOBLE DE LA OTRA

print(f"W_full:\n{W_full}")
print(f"  Rango: {np.linalg.matrix_rank(W_full)}")
print(f"  Determinante: {np.linalg.det(W_full):.2f}")

print(f"\nW_low (fila 2 = 2 × fila 1):\n{W_low}")
print(f"  Rango: {np.linalg.matrix_rank(W_low)}")
print(f"  Determinante: {np.linalg.det(W_low):.2f}")

# Demostración: W_low aplasta todo a una línea
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
plot_transformation(W_full, f"Rango completo (rango={np.linalg.matrix_rank(W_full)})\ndet={np.linalg.det(W_full):.1f}", axes[0])
plot_transformation(W_low, f"Rango deficiente (rango={np.linalg.matrix_rank(W_low)})\ndet={np.linalg.det(W_low):.1f}\n¡Todo colapsa a una línea!", axes[1])
plt.tight_layout()
plt.show()

"""
🧠 SIMULACIÓN LoRA: Cómo funciona la actualización de bajo rango

En LoRA, en lugar de actualizar toda la matriz W (que puede ser enorme),
actualizamos con ΔW = A·B donde A y B tienen rango r << d.
"""

print("\n--- Simulación LoRA ---")
d = 100  # dimensión original (ej: 768 en un modelo real)
r = 4    # rango bajo para la actualización

W_original = np.random.randn(d, d) * 0.1  # Pesos originales
A = np.random.randn(d, r) * 0.01          # Matriz A (d×r)
B = np.random.randn(r, d) * 0.01          # Matriz B (r×d)
delta_W = A @ B                            # Actualización de bajo rango

print(f"W_original: shape={W_original.shape}, rango={np.linalg.matrix_rank(W_original)}")
print(f"A: shape={A.shape}")
print(f"B: shape={B.shape}")
print(f"ΔW = A·B: shape={delta_W.shape}, rango={np.linalg.matrix_rank(delta_W)}")
print(f"\nParámetros W completo: {d*d:,} ({d}×{d})")
print(f"Parámetros LoRA: {d*r + r*d:,} ({d}×{r} + {r}×{d})")
print(f"Reducción: {(d*r + r*d) / (d*d) * 100:.1f}% de los parámetros originales")

input("\n[Presiona Enter para continuar...]\n")


# =============================================================================
# 6️⃣ RESUMEN Y CONEXIÓN CON ML
# =============================================================================

print("\n" + "=" * 60)
print("📋 RESUMEN — ÁLGEBRA LINEAL PARA ML")
print("=" * 60)

resumen = """
┌─────────────────────────────────────────────────────────────────┐
│  CONCEPTO              │  EN ML SIGNIFICA...                    │
├─────────────────────────────────────────────────────────────────┤
│  Vector                │  Un punto de datos o un peso           │
│  Producto punto        │  "Cuánto coinciden" input y pesos      │
│  Matriz                │  Una transformación (capa de la red)   │
│  Multiplicación mat.   │  Composición de capas (forward pass)   │
│  Determinante          │  ¿La transformación pierde info?       │
│  Rango                 │  Dimensionalidad útil de la salida     │
│  Eigenvalores          │  Estabilidad de gradientes / PCA       │
│  Eigenvectores         │  Direcciones "naturales" de los datos  │
│  Matriz de covarianza  │  Estructura/correlación de features    │
│  SVD                   │  Compresión de matrices (LoRA)         │
└─────────────────────────────────────────────────────────────────┘

🎯 SIGUIENTE PASO: Ve a challenges/ y completa:
   - challenge_1_matmul.py     (ya hecho ✅)
   - challenge_2_pca_manual.py
   - challenge_3_transformaciones.py
"""

print(resumen)

print("✅ Guía conceptual completada. ¡A los challenges!")

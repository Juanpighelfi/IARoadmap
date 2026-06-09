"""
=============================================================================
🏆 CHALLENGE 3: Visualización de Transformaciones Lineales
=============================================================================

OBJETIVO: Demostrar visualmente que multiplicar por una matriz es
          una transformación geométrica del espacio.

          Este es el ejercicio que te va a hacer "sentir" lo que 3Blue1Brown
          te enseñó en video.

CONCEPTO: Cada capa de una red neuronal (y = Wx + b) transforma el espacio
          de representación de tus datos. Entender CÓMO se transforma te
          permite diagnosticar problemas y diseñar mejores arquitecturas.

DURACIÓN: ~40 minutos
DIFICULTAD: ⭐⭐ (Intermedia)

LO QUE VAS A HACER:
  a) Crear una grilla 2D de puntos + una forma reconocible
  b) Aplicar distintas matrices de transformación
  c) Visualizar antes/después
  d) Interpretar qué hace cada matriz geométricamente
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import matplotlib.colors as mcolors

plt.rcParams.update({
    'font.size': 11,
    'axes.grid': True,
    'grid.alpha': 0.3
})


# =============================================================================
# HELPER: Crear formas para visualizar transformaciones
# =============================================================================

def crear_forma_L():
    """
    Crea una forma de 'L' usando puntos.
    La L es fácil de ver si se rota, escala o refleja.
    """
    # Barra vertical de la L
    puntos_v = np.array([[0, y] for y in np.linspace(0, 2, 30)])
    # Barra horizontal de la L  
    puntos_h = np.array([[x, 0] for x in np.linspace(0, 1.5, 20)])
    
    return np.vstack([puntos_v, puntos_h])

def crear_circulo_con_flecha():
    """
    Crea un círculo con una 'flecha' para ver rotaciones.
    """
    # Círculo
    theta = np.linspace(0, 2 * np.pi, 80)
    circulo = np.column_stack([np.cos(theta), np.sin(theta)])
    
    # Flecha (una línea desde el centro hacia la derecha)
    flecha = np.array([[x, 0] for x in np.linspace(0, 1.2, 15)])
    
    return np.vstack([circulo, flecha])

def crear_grilla(n=10, lim=2):
    """Crea una grilla regular de puntos."""
    x = np.linspace(-lim, lim, n)
    y = np.linspace(-lim, lim, n)
    xx, yy = np.meshgrid(x, y)
    return np.column_stack([xx.ravel(), yy.ravel()])


# =============================================================================
# HELPER: Visualizar transformación
# =============================================================================

def visualizar_transformacion(puntos, A, titulo, ax_antes, ax_despues, 
                               color_original='#2196F3', color_transformado='#FF5722'):
    """Muestra los puntos antes y después de aplicar la transformación A."""
    puntos_transformados = (A @ puntos.T).T
    
    # Antes
    ax_antes.scatter(puntos[:, 0], puntos[:, 1], c=color_original, s=8, alpha=0.6)
    ax_antes.set_xlim(-4, 4)
    ax_antes.set_ylim(-4, 4)
    ax_antes.set_aspect('equal')
    ax_antes.set_title('ANTES', fontweight='bold', color='gray')
    ax_antes.axhline(y=0, color='k', linewidth=0.3)
    ax_antes.axvline(x=0, color='k', linewidth=0.3)
    
    # Vectores base originales
    ax_antes.quiver(0, 0, 1, 0, angles='xy', scale_units='xy', scale=1, color='red', 
                    linewidth=2, alpha=0.8, label='e₁')
    ax_antes.quiver(0, 0, 0, 1, angles='xy', scale_units='xy', scale=1, color='green', 
                    linewidth=2, alpha=0.8, label='e₂')
    ax_antes.legend(fontsize=9)
    
    # Después
    ax_despues.scatter(puntos_transformados[:, 0], puntos_transformados[:, 1], 
                       c=color_transformado, s=8, alpha=0.6)
    ax_despues.set_xlim(-4, 4)
    ax_despues.set_ylim(-4, 4)
    ax_despues.set_aspect('equal')
    ax_despues.set_title(f'DESPUÉS: {titulo}', fontweight='bold', color='#FF5722')
    ax_despues.axhline(y=0, color='k', linewidth=0.3)
    ax_despues.axvline(x=0, color='k', linewidth=0.3)
    
    # Vectores base transformados
    e1_t = A @ np.array([1, 0])
    e2_t = A @ np.array([0, 1])
    ax_despues.quiver(0, 0, e1_t[0], e1_t[1], angles='xy', scale_units='xy', scale=1, 
                      color='red', linewidth=2, alpha=0.8, label=f'Ae₁=[{e1_t[0]:.1f},{e1_t[1]:.1f}]')
    ax_despues.quiver(0, 0, e2_t[0], e2_t[1], angles='xy', scale_units='xy', scale=1, 
                      color='green', linewidth=2, alpha=0.8, label=f'Ae₂=[{e2_t[0]:.1f},{e2_t[1]:.1f}]')
    ax_despues.legend(fontsize=9)


# =============================================================================
# PARTE 1: Transformaciones Básicas
# =============================================================================

print("=" * 60)
print("🏆 CHALLENGE 3: Transformaciones Lineales Visuales")
print("=" * 60)

# Crear la forma (L + grilla)
forma = crear_forma_L()
grilla = crear_grilla(n=12, lim=2.5)
puntos = np.vstack([forma, grilla])

"""
INSTRUCCIÓN: Para cada transformación:
  1. Observa la matriz A y trata de PREDECIR qué va a pasar
  2. Ejecuta el código y verifica tu predicción
  3. Fíjate en qué pasa con e₁ y e₂ (las columnas de A)
"""

# Definir transformaciones
transformaciones = {
    "Escala Uniforme (2x)": np.array([[2, 0], [0, 2]]),
    "Escala No-Uniforme": np.array([[2, 0], [0, 0.5]]),
    "Rotación 45°": np.array([
        [np.cos(np.pi/4), -np.sin(np.pi/4)],
        [np.sin(np.pi/4),  np.cos(np.pi/4)]
    ]),
    "Rotación 90°": np.array([
        [np.cos(np.pi/2), -np.sin(np.pi/2)],
        [np.sin(np.pi/2),  np.cos(np.pi/2)]
    ]),
    "Shear (Cizalla)": np.array([[1, 1], [0, 1]]),
    "Reflexión (eje X)": np.array([[1, 0], [0, -1]]),
}

fig, axes = plt.subplots(len(transformaciones), 2, figsize=(12, 4 * len(transformaciones)))

for idx, (nombre, A) in enumerate(transformaciones.items()):
    det = np.linalg.det(A)
    titulo = f"{nombre}\ndet={det:.2f}"
    visualizar_transformacion(puntos, A, titulo, axes[idx, 0], axes[idx, 1])

plt.suptitle("Transformaciones Lineales Básicas", fontsize=16, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig('challenges/challenge_3_basicas.png', dpi=100, bbox_inches='tight')
plt.show()

input("\n[Presiona Enter para continuar...]\n")


# =============================================================================
# PARTE 2: Matrices de Rotación — Implementación Manual
# =============================================================================
"""
TODO: Implementa una función que genere la matriz de rotación para
      cualquier ángulo θ.

La matriz de rotación 2D es:
    R(θ) = [[cos(θ), -sin(θ)],
            [sin(θ),  cos(θ)]]

PREGUNTA: ¿Qué propiedades tiene esta matriz?
  - det(R) = ?
  - R @ R^T = ?
  - R^(-1) = ?
"""

print("\n" + "=" * 60)
print("PARTE 2: Matrices de Rotación")
print("=" * 60)

def matriz_rotacion(angulo_grados):
    """
    Genera la matriz de rotación 2D para un ángulo dado en grados.
    
    IMPLEMENTA ESTA FUNCIÓN.
    """
    theta = np.radians(angulo_grados)
    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

# Verificar propiedades
R = matriz_rotacion(30)

print(f"\nR(30°) =\n{R.round(4)}")
print(f"\ndet(R) = {np.linalg.det(R):.6f}  (debería ser 1.0)")
print(f"\nR @ R^T =\n{(R @ R.T).round(6)}  (debería ser Identidad)")
print(f"\nR^(-1) =\n{np.linalg.inv(R).round(4)}")
print(f"\nR^T =\n{R.T.round(4)}")
print(f"\n¿R^(-1) == R^T? {np.allclose(np.linalg.inv(R), R.T)}  ← Matrices ortogonales!")

# Animar rotaciones (como una secuencia de imágenes)
circulo_flecha = crear_circulo_con_flecha()
angulos = [0, 30, 60, 90, 120, 180, 270, 360]

fig, axes = plt.subplots(2, 4, figsize=(16, 8))
for idx, angulo in enumerate(angulos):
    ax = axes[idx // 4, idx % 4]
    R_a = matriz_rotacion(angulo)
    transformado = (R_a @ circulo_flecha.T).T
    
    ax.scatter(transformado[:, 0], transformado[:, 1], c='#FF5722', s=5, alpha=0.8)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.set_title(f'{angulo}°', fontsize=14, fontweight='bold')
    ax.axhline(y=0, color='k', linewidth=0.3)
    ax.axvline(x=0, color='k', linewidth=0.3)

plt.suptitle("Rotación progresiva", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('challenges/challenge_3_rotaciones.png', dpi=100, bbox_inches='tight')
plt.show()

input("\n[Presiona Enter para continuar...]\n")


# =============================================================================
# PARTE 3: Composición de Transformaciones (¡el orden importa!)
# =============================================================================
"""
En una red neuronal:  y = W₂ @ (ReLU(W₁ @ x + b₁)) + b₂

Esto es una COMPOSICIÓN de transformaciones:
  1. Primero W₁ transforma x
  2. Luego ReLU (no lineal) deforma el espacio
  3. Luego W₂ transforma de nuevo

IMPORTANTE: W₂ @ W₁ ≠ W₁ @ W₂ (en general)

TODO: Verifica esto con las siguientes matrices:
"""

print("\n" + "=" * 60)
print("PARTE 3: Composición — El Orden Importa")
print("=" * 60)

# Rotar 45° y luego escalar
R45 = matriz_rotacion(45)
S = np.array([[2, 0], [0, 0.5]])

AB = S @ R45   # Primero rotar, luego escalar
BA = R45 @ S   # Primero escalar, luego rotar

print(f"S @ R45 (rotar, luego escalar):\n{AB.round(3)}\n")
print(f"R45 @ S (escalar, luego rotar):\n{BA.round(3)}\n")
print(f"¿Son iguales? {np.allclose(AB, BA)}")

# Visualizar la diferencia
forma = crear_forma_L()

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Original
axes[0].scatter(forma[:, 0], forma[:, 1], c='#2196F3', s=12, alpha=0.8)
axes[0].set_xlim(-4, 4)
axes[0].set_ylim(-4, 4)
axes[0].set_aspect('equal')
axes[0].set_title('Original', fontweight='bold', fontsize=14)
axes[0].axhline(y=0, color='k', linewidth=0.3)
axes[0].axvline(x=0, color='k', linewidth=0.3)

# S @ R45 (rotar primero)
t1 = (AB @ forma.T).T
axes[1].scatter(t1[:, 0], t1[:, 1], c='#FF5722', s=12, alpha=0.8)
axes[1].set_xlim(-4, 4)
axes[1].set_ylim(-4, 4)
axes[1].set_aspect('equal')
axes[1].set_title('Rotar 45° → Escalar\n(S @ R)', fontweight='bold', fontsize=14, color='#FF5722')
axes[1].axhline(y=0, color='k', linewidth=0.3)
axes[1].axvline(x=0, color='k', linewidth=0.3)

# R45 @ S (escalar primero)
t2 = (BA @ forma.T).T
axes[2].scatter(t2[:, 0], t2[:, 1], c='#4CAF50', s=12, alpha=0.8)
axes[2].set_xlim(-4, 4)
axes[2].set_ylim(-4, 4)
axes[2].set_aspect('equal')
axes[2].set_title('Escalar → Rotar 45°\n(R @ S)', fontweight='bold', fontsize=14, color='#4CAF50')
axes[2].axhline(y=0, color='k', linewidth=0.3)
axes[2].axvline(x=0, color='k', linewidth=0.3)

plt.suptitle("Composición NO conmuta: A·B ≠ B·A", fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('challenges/challenge_3_composicion.png', dpi=100, bbox_inches='tight')
plt.show()

input("\n[Presiona Enter para continuar...]\n")


# =============================================================================
# PARTE 4: Transformación como la ve una Red Neuronal
# =============================================================================
"""
Simulemos lo que hace UNA CAPA de una red neuronal en 2D:
    y = relu(W @ x + b)

La parte W @ x es lineal (transformación geométrica).
La parte relu() es NO lineal (corta los negativos → deforma el espacio).

Vamos a visualizar ambas:
"""

print("\n" + "=" * 60)
print("PARTE 4: Una Capa de Red Neuronal en 2D")
print("=" * 60)

# Generar datos 2D (un dataset circular)
np.random.seed(42)
n = 500
theta_data = np.random.uniform(0, 2 * np.pi, n)
r_data = np.random.uniform(0.5, 2, n)
datos = np.column_stack([r_data * np.cos(theta_data), r_data * np.sin(theta_data)])

# Pesos de la "capa"
W = np.array([[1.5, -0.5],
              [0.5,  1.2]])
b = np.array([0.3, -0.2])

# Forward pass
z = (W @ datos.T).T + b
a = np.maximum(0, z)  # ReLU

# Colorear por distancia al origen para tracking
colores = np.sqrt(datos[:, 0]**2 + datos[:, 1]**2)

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Input
sc1 = axes[0].scatter(datos[:, 0], datos[:, 1], c=colores, cmap='viridis', s=5, alpha=0.7)
axes[0].set_xlim(-3, 3)
axes[0].set_ylim(-3, 3)
axes[0].set_aspect('equal')
axes[0].set_title('INPUT: x', fontweight='bold', fontsize=14)
axes[0].axhline(y=0, color='k', linewidth=0.3)
axes[0].axvline(x=0, color='k', linewidth=0.3)

# Después de W @ x + b (lineal)
axes[1].scatter(z[:, 0], z[:, 1], c=colores, cmap='viridis', s=5, alpha=0.7)
axes[1].set_xlim(-4, 5)
axes[1].set_ylim(-3, 4)
axes[1].set_aspect('equal')
axes[1].set_title('LINEAL: W·x + b', fontweight='bold', fontsize=14)
axes[1].axhline(y=0, color='k', linewidth=0.3)
axes[1].axvline(x=0, color='k', linewidth=0.3)

# Después de ReLU (no lineal)
axes[2].scatter(a[:, 0], a[:, 1], c=colores, cmap='viridis', s=5, alpha=0.7)
axes[2].set_xlim(-1, 5)
axes[2].set_ylim(-1, 4)
axes[2].set_aspect('equal')
axes[2].set_title('ReLU: max(0, W·x + b)', fontweight='bold', fontsize=14, color='#FF5722')
axes[2].axhline(y=0, color='k', linewidth=0.3)
axes[2].axvline(x=0, color='k', linewidth=0.3)

plt.suptitle("Lo que hace UNA CAPA de una red neuronal", fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('challenges/challenge_3_red_neuronal.png', dpi=100, bbox_inches='tight')
plt.show()

"""
🔑 OBSERVA:
  1. W·x + b deforma el espacio (rotación + escala + traslación)
  2. ReLU "corta" todo lo negativo → colapsa parte del espacio a 0
  3. ¡Esta deformación no-lineal es lo que permite a las redes 
     separar datos que no son linealmente separables!

Sin ReLU (u otra no-linealidad), apilar capas sería inútil:
  W₃ @ W₂ @ W₁ = W_total (sigue siendo UNA transformación lineal)
  Con ReLU, cada capa puede "doblar" el espacio de una forma nueva.
"""


# =============================================================================
# PARTE 5: Tu Turno — Experimenta
# =============================================================================
"""
TODO: Crea tus propias matrices de transformación y observa qué hacen.

Ideas para experimentar:
  1. ¿Qué pasa con una matriz donde todos los valores son iguales?
  2. ¿Qué pasa si los eigenvalores son negativos?
  3. ¿Puedes crear una matriz que haga un "espejo" en una diagonal?
  4. ¿Cómo se ve una transformación con determinante = 0?
"""

print(f"""
{'=' * 60}
🧠 REFLEXIÓN FINAL
{'=' * 60}

1. ¿Qué pasa geométricamente cuando det(A) = 0?
   → El espacio se "aplasta" a una dimensión menor.
   → Se PIERDE información (no se puede invertir A).
   → Conexión ML: una capa con pesos de rango bajo pierde representaciones.

2. ¿Qué pasa cuando det(A) < 0?
   → La transformación INVIERTE la orientación (como un espejo).

3. ¿Por qué las no-linealidades (ReLU, sigmoid) son necesarias?
   → Sin ellas, N capas lineales = 1 capa lineal.
   → La no-linealidad permite "doblar" el espacio para crear
     fronteras de decisión complejas.

4. ¿Cómo se conecta esto con el entrenamiento?
   → El SGD ajusta W para que la transformación lleve los datos
     a un espacio donde sean fácilmente separables.
   → Cada iteración "mejora" la transformación un poquito.

✅ Challenge 3 completado.
   
🎯 Has terminado la Semana 1 (Álgebra Lineal para Redes).
   Criterio de éxito: ¿Puedes explicar qué hace geométricamente
   W·x para cualquier matriz W de 2×2?
""")

"""
=============================================================================
🏆 CHALLENGE 2: PCA Manual con Eigenvectores
=============================================================================

OBJETIVO: Implementar PCA (Análisis de Componentes Principales) desde cero
          usando eigenvectores de la matriz de covarianza.

CONCEPTO PREVIO (de la guía conceptual):
  - Los eigenvectores de la matriz de covarianza son las DIRECCIONES de
    máxima varianza en tus datos.
  - Los eigenvalores te dicen CUÁNTA varianza hay en esa dirección.
  - PCA = Proyectar los datos sobre los eigenvectores más importantes.

POR QUÉ IMPORTA EN ML:
  - Reducción de dimensionalidad (menos features, menos cómputo)
  - Visualización de datos de alta dimensión
  - Eliminación de ruido (las componentes de menor varianza suelen ser ruido)
  - Decorrelación de features (las componentes son ortogonales)

DURACIÓN: ~45 minutos
DIFICULTAD: ⭐⭐⭐ (Avanzada)

PRERREQUISITO: Haber leído la sección de eigenvectores en la guía conceptual

HINTS: Si te trabás, consultá modulo_0/hints/hint_challenge_2.md
=============================================================================
"""

from re import subn
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'figure.figsize': (10, 8),
    'font.size': 11,
    'axes.grid': True,
    'grid.alpha': 0.3
})

# =============================================================================
# PASO 1: Generar datos de ejemplo con estructura clara
# =============================================================================
"""
Creamos datos de 5 dimensiones donde:
  - 2 dimensiones tienen ALTA varianza (señal)
  - 3 dimensiones tienen BAJA varianza (ruido)
  
PCA debería "descubrir" que los datos son esencialmente 2D.
"""

print("=" * 60)
print("🏆 CHALLENGE 2: PCA Manual")
print("=" * 60)

np.random.seed(42)

# Datos originales en 2D con correlación
n_samples = 200
t = np.random.randn(n_samples)
x1 = 3 * t + np.random.randn(n_samples) * 0.3    # Alta varianza
x2 = 2 * t + np.random.randn(n_samples) * 0.3    # Alta varianza, correlacionada con x1
x3 = np.random.randn(n_samples) * 0.5              # Ruido
x4 = np.random.randn(n_samples) * 0.3              # Ruido
x5 = np.random.randn(n_samples) * 0.1              # Poco ruido

data = np.column_stack([x1, x2, x3, x4, x5])  # (200, 5)

print(f"\nDatos originales: {data.shape} → {n_samples} muestras, 5 features")
print(f"Media por feature: {data.mean(axis=0).round(3)}")
print(f"Std por feature:   {data.std(axis=0).round(3)}")


# =============================================================================
# PASO 2: Centrar los datos (PASO CRÍTICO)
# =============================================================================
"""
PCA requiere datos CENTRADOS (media = 0). Si no centras, las componentes 
principales se ven afectadas por la media y no representan la varianza real.

🔑 En ML, normalizar/estandarizar los datos es SIEMPRE el primer paso.
"""

# TODO: Centra los datos restando la media de cada feature
# 1. Calcula la media por columna (cada feature)
# 2. Resta la media a los datos
mean = data.mean(axis=0)  # Tu código aquí
print(f"La media de cada columna es: {mean}")
data_centered = data - mean  # Tu código aquí
print(f"\n✅ Datos centrados. Nueva media: {data_centered.mean(axis=0).round(10)}")


# =============================================================================
# PASO 3: Calcular la Matriz de Covarianza
# =============================================================================
"""
La matriz de covarianza Σ es una matriz (n_features × n_features) donde:
  - Σ[i,i] = varianza de la feature i
  - Σ[i,j] = covarianza entre features i y j 
              (cuánto varían juntas)

Si Σ[i,j] > 0: cuando feature i sube, feature j tiende a subir
Si Σ[i,j] < 0: cuando feature i sube, feature j tiende a bajar
Si Σ[i,j] ≈ 0: features i y j son independientes

Fórmula: Σ = (1/(m-1)) * Xᵀ · X    (con X centrado, m-1 para muestra)
"""

# TODO: Calcula la matriz de covarianza manualmente
# Fórmula: cov_matrix = (1 / (n_samples - 1)) * data_centered.T @ data_centered
cov_matrix = (1/(n_samples-1)) * data_centered.T @ data_centered  # Tu código aquí

# Verificar con NumPy
cov_numpy = np.cov(data_centered, rowvar=False)
print(f"\n¿Covarianza manual ≈ NumPy? {np.allclose(cov_matrix, cov_numpy)}")

print(f"\nMatriz de Covarianza ({cov_matrix.shape}):")
print(np.array2string(cov_matrix, precision=3, suppress_small=True))

# Visualizar la matriz de covarianza como heatmap
fig, ax = plt.subplots(figsize=(7, 6))
im = ax.imshow(cov_matrix, cmap='RdBu_r', vmin=-np.max(np.abs(cov_matrix)), 
               vmax=np.max(np.abs(cov_matrix)))
ax.set_xticks(range(5))
ax.set_yticks(range(5))
ax.set_xticklabels([f'x{i+1}' for i in range(5)])
ax.set_yticklabels([f'x{i+1}' for i in range(5)])
for i in range(5):
    for j in range(5):
        ax.text(j, i, f'{cov_matrix[i, j]:.2f}', ha='center', va='center', fontsize=10,
                color='white' if abs(cov_matrix[i, j]) > np.max(np.abs(cov_matrix)) * 0.5 else 'black')
plt.colorbar(im)
ax.set_title('Matriz de Covarianza', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

"""
🔑 OBSERVA: x1 y x2 están MUY correlacionadas (covarianza alta).
   x3, x4, x5 tienen poca varianza y poca correlación con el resto.
"""

input("\n[Presiona Enter para continuar...]\n")


# =============================================================================
# PASO 4: Calcular Eigenvalores y Eigenvectores
# =============================================================================
"""
Los eigenvectores de Σ son las COMPONENTES PRINCIPALES.
Los eigenvalores son la VARIANZA EXPLICADA por cada componente.

IMPORTANTE: Usamos np.linalg.eigh() (no eig()) porque:
  - La matriz de covarianza es SIMÉTRICA: Σ = Σᵀ
  - eigh() es más rápido y numéricamente estable para matrices simétricas
  - eigh() devuelve eigenvalores ordenados de menor a mayor
"""

# TODO: Calcula eigenvalores y eigenvectores de la matriz de covarianza
# Usa np.linalg.eigh() y luego ordena de MAYOR a MENOR
eigen = np.linalg.eigh(cov_matrix)
print(f"Eigen: {eigen}")
eigenvalores, eigenvectores = eigen
print(f"Imprimimos los dos juntos: {eigenvalores, eigenvectores}")

# TODO: Ordena de mayor a menor (eigh devuelve de menor a mayor)
# Pista: usa np.argsort()[::-1] para obtener los índices en orden descendente
idx_sorted = np.argsort(eigenvalores)[::-1]
eigenvalores = eigenvalores[idx_sorted]
eigenvectores = eigenvectores[:, idx_sorted]

print(f"\nEigenvalores (varianza por componente):")
for i, val in enumerate(eigenvalores):
    print(f"  PC{i+1}: λ = {val:.4f}")

print(f"\nEigenvectores (componentes principales, por columnas):")
print(np.array2string(eigenvectores, precision=3, suppress_small=True))


# =============================================================================
# PASO 5: Calcular la Varianza Explicada
# =============================================================================
"""
La varianza explicada te dice qué porcentaje de la información total
captura cada componente.

varianza_explicada_i = λ_i / Σ λ_j

Si PC1 y PC2 juntas capturan >95% de la varianza, puedes reducir
de 5 dimensiones a 2 ¡perdiendo menos del 5% de información!
"""

# TODO: Calcula el porcentaje de varianza explicada por cada componente
# 1. Suma total de eigenvalores
# 2. Cada eigenvalor / total = porcentaje
# 3. Acumulado con np.cumsum()
varianza_total = np.sum(eigenvalores)  # Tu código aquí
varianza_explicada = eigenvalores / varianza_total  # Tu código aquí
varianza_acumulada = np.cumsum(varianza_explicada)  # Tu código aquí

print(f"\nVarianza explicada por componente:")
for i, (ve, va) in enumerate(zip(varianza_explicada, varianza_acumulada)):
    bar = "█" * int(ve * 50)
    print(f"  PC{i+1}: {ve*100:5.1f}% | acumulada: {va*100:5.1f}% | {bar}")

# Gráfico de varianza explicada (Scree plot)
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].bar(range(1, 6), varianza_explicada * 100, color='#2196F3', alpha=0.8, edgecolor='white')
axes[0].set_xlabel('Componente Principal')
axes[0].set_ylabel('Varianza Explicada (%)')
axes[0].set_title('Scree Plot — Varianza por Componente', fontweight='bold')
axes[0].set_xticks(range(1, 6))

axes[1].plot(range(1, 6), varianza_acumulada * 100, 'o-', color='#FF5722', linewidth=2, markersize=8)
axes[1].axhline(y=95, color='gray', linestyle='--', alpha=0.7, label='95% umbral')
axes[1].fill_between(range(1, 6), varianza_acumulada * 100, alpha=0.1, color='#FF5722')
axes[1].set_xlabel('Número de Componentes')
axes[1].set_ylabel('Varianza Acumulada (%)')
axes[1].set_title('Varianza Acumulada', fontweight='bold')
axes[1].set_xticks(range(1, 6))
axes[1].legend()

plt.tight_layout()
plt.show()

input("\n[Presiona Enter para continuar...]\n")


# =============================================================================
# PASO 6: Proyectar los Datos a 2D
# =============================================================================
"""
Proyección = multiplicar los datos centrados por los eigenvectores seleccionados.

Si tomamos los primeros k eigenvectores como columnas de W (n_features × k):
    datos_proyectados = datos_centrados @ W    →  shape: (n_samples, k)

Esto transforma datos de 5D → 2D, conservando la mayor varianza posible.
"""

# TODO: Proyecta los datos a las 2 primeras componentes principales
# 1. Selecciona las primeras 2 columnas de eigenvectores como W
# 2. Multiplica data_centered @ W
n_components = 2
W = eigenvectores[:,:n_components]  # Acá guardamos los Loading Scores, básicamente, cuáles son las proporciones para construir cada PC
print(f"W tiene una forma de {W.shape} y sus valores son: {W}")
data_2d = data_centered @ W  # Pasamos de tener 200 datos en 5 dimensiones a tener 200 datos en 2 dimensiones. Esto es gracias al poder de la multiplicación donde (200, 5) x (5, 2) = (200,2)

print(f"\nProyección: {data_centered.shape} → {data_2d.shape}")
print(f"Varianza capturada: {varianza_acumulada[n_components-1]*100:.1f}%")

# Visualización de la proyección
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Datos originales (solo las 2 primeras features)
axes[0].scatter(data[:, 0], data[:, 1], c='#2196F3', alpha=0.5, s=15, edgecolors='none')
axes[0].set_xlabel('Feature x1')
axes[0].set_ylabel('Feature x2')
axes[0].set_title('Datos Originales (x1 vs x2)', fontweight='bold')
axes[0].set_aspect('equal')

# Datos proyectados con PCA
axes[1].scatter(data_2d[:, 0], data_2d[:, 1], c='#FF5722', alpha=0.5, s=15, edgecolors='none')
axes[1].set_xlabel('PC1')
axes[1].set_ylabel('PC2')
axes[1].set_title(f'PCA: 5D → 2D ({varianza_acumulada[1]*100:.1f}% varianza)', fontweight='bold')
axes[1].set_aspect('equal')

plt.tight_layout()
plt.show()


# =============================================================================
# PASO 7: Verificar con sklearn
# =============================================================================

print(f"\n{'=' * 60}")
print("🧪 VERIFICACIÓN CON SKLEARN")
print("=" * 60)

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
data_2d_sklearn = pca.fit_transform(data)

# Los signos de los eigenvectores pueden ser opuestos (ambos son válidos)
# Comparamos la varianza explicada que es invariante al signo
print(f"\nVarianza explicada (nuestro PCA): {varianza_explicada[:2].round(4)}")
print(f"Varianza explicada (sklearn):    {pca.explained_variance_ratio_.round(4)}")
print(f"\n¿Coinciden? {np.allclose(varianza_explicada[:2], pca.explained_variance_ratio_, atol=1e-3)}")


# =============================================================================
# BONUS: Reconstrucción de datos
# =============================================================================

print(f"\n{'=' * 60}")
print("🏋️  BONUS: Reconstrucción de datos")
print("=" * 60)

"""
Si PCA proyecta datos de 5D → 2D, podemos RECONSTRUIR una aproximación
de los datos originales volviendo a 5D:

    datos_reconstruidos = datos_2d @ W.T + mean

El error de reconstrucción nos dice cuánta información perdimos.
"""

# TODO (BONUS): Reconstruye los datos desde la proyección 2D
# data_reconstruido = data_2d @ W.T + mean
data_reconstruido = data_2d @ W.T + mean  # Tu código aquí

# Error de reconstrucción
error = np.mean((data - data_reconstruido) ** 2)
print(f"\nError cuadrático medio de reconstrucción: {error:.6f}")
print(f"Comparado con la varianza total de los datos: {np.var(data):.6f}")
print(f"Ratio de compresión: {n_components}/{data.shape[1]} = {n_components/data.shape[1]*100:.0f}% de las dimensiones originales")


# =============================================================================
# REFLEXIÓN FINAL
# =============================================================================
print(f"""
{'=' * 60}
🧠 REFLEXIÓN
{'=' * 60}

1. ¿Cuántas componentes necesitarías para capturar el 99% de la varianza?
   → Mira el scree plot.

2. ¿Qué pasa si tus datos NO están centrados antes de PCA?

3. ¿PCA funciona bien con datos no lineales?

4. ¿Cuándo usar PCA en un pipeline de ML?

✅ Challenge 2 completado.
   Siguiente: challenge_3_transformaciones.py
""")

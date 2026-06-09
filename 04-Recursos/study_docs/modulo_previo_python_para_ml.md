# 🐍 Módulo Previo: Python para Machine Learning

> **Prerrequisito**: Conocer la sintaxis básica de Python (variables, funciones, loops, condicionales).
> **Objetivo**: Dominar las herramientas y patrones de Python que se usan constantemente en ML.
> **Duración estimada**: 1-2 semanas (según dedicación).

---

## ¿Por qué este módulo?

Saber Python "básico" y saber Python "para ML" son niveles distintos. En ML vas a manipular datos como **matrices multidimensionales**, no como listas. Vas a trabajar con **clases** que heredan de `nn.Module`, no solo con funciones sueltas. Y vas a necesitar **visualizar** datos y resultados constantemente.

Este módulo cubre exactamente lo que necesitas para que el Módulo 0 (Matemáticas) y el resto del plan fluyan sin fricción con el código.

```
Python básico (lo que ya sabes)
├── Variables, tipos, strings
├── Listas, diccionarios, tuplas
├── for/while, if/else
├── Funciones (def, args, return)
└── Lectura/escritura de archivos

Python para ML (lo que aprenderás aquí)         ← ESTÁS AQUÍ
├── NumPy: arrays, broadcasting, vectorización
├── Matplotlib: gráficas profesionales
├── Pandas: DataFrames, exploración y preprocesamiento
├── Clases y OOP para ML (nn.Module pattern)
├── Manejo del entorno (venv, pip, proyecto)
├── List comprehensions y expresiones avanzadas
├── Jupyter Notebooks como herramienta de trabajo
└── Debugging eficaz de código numérico
```

---

## 📚 Recursos de Referencia

| Recurso | Tipo | Enlace | Prioridad |
|---------|------|--------|-----------|
| **Python para todos (Univ. Michigan)** | Libro ES gratuito | [py4e.com/book](https://www.py4e.com/book) (versión ES disponible) | 🟢 Si necesitas repasar base |
| **Tutorial NumPy oficial** | Docs interactivos | [numpy.org/doc/stable/user/quickstart](https://numpy.org/doc/stable/user/quickstart.html) | 🔴 Obligatorio |
| **Scientific Python Lectures** | Notebooks | [lectures.scientific-python.org](https://lectures.scientific-python.org/) | 🟡 Referencia completa |
| **Matplotlib Tutorial** | Docs | [matplotlib.org/stable/tutorials](https://matplotlib.org/stable/tutorials/index.html) | 🟡 Consulta |
| **Real Python - OOP** | Artículos (EN, claro) | [realpython.com/python3-object-oriented-programming](https://realpython.com/python3-object-oriented-programming/) | 🟡 Si OOP no te queda claro |
| **Ringa Tech - Python para Data Science** | Videos (ES) | [YouTube Ringa Tech](https://www.youtube.com/@RingaTech) | 🟢 Apoyo visual |

---

## Parte 1: Setup del Entorno de Trabajo

Antes de escribir una línea de código, configura tu espacio de trabajo correctamente. Esto te ahorrará **horas** de dolores de cabeza.

### 1.1 Entorno virtual (venv)

Un entorno virtual aísla las librerías de tu proyecto. Sin esto, distintos proyectos pueden tener conflictos de versiones.

```powershell
# En tu terminal (PowerShell en Windows):

# 1. Navega a tu directorio de trabajo
cd c:\Users\agusm\Downloads\proyectos\ml-course

# 2. Crea un entorno virtual
python -m venv .venv

# 3. Actívalo
.venv\Scripts\Activate.ps1
# Verás (.venv) al inicio de la línea → estás dentro del entorno

# 4. Instala las librerías base del curso
pip install numpy pandas matplotlib jupyter ipykernel scikit-learn

# 5. Registra el kernel para Jupyter
python -m ipykernel install --user --name=ml-course --display-name="ML Course"

# 6. (Opcional) Guarda las dependencias
pip freeze > requirements.txt
```

> [!TIP]
> **Siempre activa el entorno antes de trabajar.** Si ves que `import numpy` falla, probablemente no activaste el venv. En VS Code, puedes seleccionar el intérprete de Python con `Ctrl+Shift+P → Python: Select Interpreter → .venv`.

### 1.2 Estructura del proyecto

```
ml-course/
├── .venv/                  # Entorno virtual (no lo toques)
├── study_docs/             # Plan de estudio y documentación
├── modulo_previo/          # ← Tus ejercicios de este módulo
│   ├── 01_numpy_basics.py
│   ├── 02_matplotlib_vis.py
│   ├── 03_oop_para_ml.py
│   └── 04_desafio_integrador.py
├── modulo0/                # Ejercicios del Módulo 0
├── modulo1/                # ...y así sucesivamente
├── notebooks/              # Jupyter notebooks de experimentación
└── requirements.txt
```

### 1.3 Jupyter Notebooks

Los notebooks son tu "laboratorio". Permiten ejecutar código celda por celda y ver resultados al instante.

```powershell
# Iniciar Jupyter (desde el directorio del proyecto, con venv activado)
jupyter notebook
# O para JupyterLab (más moderno):
pip install jupyterlab
jupyter lab
```

Atajos esenciales de Jupyter:
| Atajo | Acción |
|-------|--------|
| `Shift+Enter` | Ejecutar celda y avanzar |
| `Ctrl+Enter` | Ejecutar celda sin avanzar |
| `Esc + A` | Insertar celda arriba |
| `Esc + B` | Insertar celda abajo |
| `Esc + DD` | Eliminar celda |
| `Esc + M` | Convertir celda a Markdown |
| `Tab` | Autocompletar |
| `Shift+Tab` | Ver documentación de función |

---

## Parte 2: NumPy — El Corazón del Cómputo Numérico

NumPy es **LA** librería fundamental. Todo en ML pasa por arrays de NumPy (o tensores de PyTorch, que tienen la misma API). Si dominas NumPy, PyTorch será natural.

### 2.1 Arrays vs Listas

```python
import numpy as np

# ❌ Python puro: lento, verboso
lista = [1, 2, 3, 4, 5]
resultado = []
for x in lista:
    resultado.append(x * 2 + 1)
# resultado = [3, 5, 7, 9, 11]

# ✅ NumPy: rápido, limpio (VECTORIZADO)
arr = np.array([1, 2, 3, 4, 5])
resultado = arr * 2 + 1
# array([3, 5, 7, 9, 11])  ← opera sobre TODO el array de una vez
```

**¿Por qué es rápido?** NumPy está escrito en C por debajo. Cuando haces `arr * 2`, no hay un loop de Python — se ejecuta un loop optimizado en C sobre bloques contiguos de memoria. Esto es **vectorización**.

> [!IMPORTANT]
> **Regla de oro de ML**: Si te encuentras escribiendo un `for` loop sobre datos numéricos, probablemente hay una operación vectorizada de NumPy que lo hace 100x más rápido. Busca siempre la versión vectorizada primero.

### 2.2 Creación de Arrays

```python
import numpy as np

# Desde una lista
a = np.array([1, 2, 3])                    # 1D: vector
b = np.array([[1, 2], [3, 4], [5, 6]])     # 2D: matriz (3 filas, 2 columnas)

# Funciones de creación
zeros   = np.zeros((3, 4))        # Matriz 3×4 de ceros
ones    = np.ones((2, 3))         # Matriz 2×3 de unos
eye     = np.eye(3)               # Matriz identidad 3×3
rango   = np.arange(0, 10, 2)    # [0, 2, 4, 6, 8] (como range pero devuelve array)
lineal  = np.linspace(0, 1, 5)   # [0, 0.25, 0.5, 0.75, 1.0] (5 puntos equiespaciados)

# Aleatorios (MUY usado en ML para inicializar pesos)
random_uniform = np.random.rand(3, 4)       # Uniforme [0, 1), shape (3, 4)
random_normal  = np.random.randn(3, 4)      # Normal (media=0, std=1), shape (3, 4)
random_int     = np.random.randint(0, 10, (3, 4))  # Enteros [0, 10), shape (3, 4)

# Semilla para REPRODUCIBILIDAD (crucial en ML)
np.random.seed(42)  # Siempre obtener los mismos "aleatorios"
```

### 2.3 Shape, Reshape y Dimensiones

Este es el concepto que más confusión causa al principio, y el que MÁS usarás en todo el curso.

```python
import numpy as np

# Shape = la "forma" del array (dimensiones)
a = np.array([1, 2, 3])
print(a.shape)  # (3,) ← 1D, 3 elementos

b = np.array([[1, 2, 3],
              [4, 5, 6]])
print(b.shape)  # (2, 3) ← 2D, 2 filas × 3 columnas

# Reshape: cambiar la forma SIN cambiar los datos
c = np.arange(12)         # [0, 1, 2, ..., 11], shape (12,)
d = c.reshape(3, 4)       # Ahora es 3×4
e = c.reshape(2, 2, 3)    # Ahora es 3D: 2×2×3
f = c.reshape(-1, 4)      # -1 = "calcula tú esta dimensión" → (3, 4)

# ¡Los datos son los MISMOS! Solo cambia la interpretación
print(c)  # [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(d)  # [[ 0  1  2  3]
          #  [ 4  5  6  7]
          #  [ 8  9 10 11]]

# Dimensiones típicas en ML:
# Datos tabulares:  (n_samples, n_features)         ej: (1000, 10)
# Imágenes:         (batch, channels, height, width) ej: (32, 3, 224, 224)
# Texto/secuencias: (batch, sequence_length)          ej: (64, 128)
# Embeddings:       (batch, seq_len, d_model)         ej: (64, 128, 512)
```

### 2.4 Indexación y Slicing

```python
import numpy as np

a = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

# Acceso por posición
a[0, 0]     # 10 (fila 0, columna 0)
a[1, 2]     # 60 (fila 1, columna 2)

# Slicing [inicio:fin:paso] — fin NO está incluido
a[0, :]     # [10, 20, 30] ← fila 0, todas las columnas
a[:, 1]     # [20, 50, 80] ← todas las filas, columna 1
a[0:2, :]   # [[10,20,30], [40,50,60]] ← filas 0 y 1
a[:, 1:]    # [[20,30], [50,60], [80,90]] ← desde columna 1

# Indexación booleana (MUY útil en ML para filtrar datos)
mask = a > 50
# [[False, False, False],
#  [False, False,  True],
#  [ True,  True,  True]]
a[mask]  # [60, 70, 80, 90] ← solo los elementos > 50

# Ejemplo práctico: filtrar predicciones correctas
predicciones = np.array([0.1, 0.8, 0.3, 0.9, 0.6])
correctas = predicciones > 0.5  # [False, True, False, True, True]
print(f"Accuracy: {correctas.mean():.0%}")  # Accuracy: 60%
```

### 2.5 Operaciones Vectorizadas y Broadcasting

```python
import numpy as np

# Operaciones elemento a elemento
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)   # [5, 7, 9]
print(a * b)   # [4, 10, 18]  ← ELEMENTO por ELEMENTO, NO es producto punto
print(a ** 2)  # [1, 4, 9]

# Producto punto (dot product) — lo más usado en ML
print(np.dot(a, b))  # 32 = 1*4 + 2*5 + 3*6
print(a @ b)         # 32 ← notación con @ (idéntico a np.dot para 1D y 2D)

# Multiplicación de matrices
A = np.array([[1, 2], [3, 4]])   # 2×2
B = np.array([[5, 6], [7, 8]])   # 2×2
print(A @ B)  # [[19, 22], [43, 50]]  ← multiplicación de matrices
# RECORDAR: (m×n) @ (n×p) = (m×p) — las dimensiones internas deben coincidir

# BROADCASTING: operar arrays de shapes diferentes
# NumPy "estira" automáticamente la dimensión más pequeña
matriz = np.array([[1, 2, 3],
                   [4, 5, 6]])     # Shape: (2, 3)
vector = np.array([10, 20, 30])    # Shape: (3,)
print(matriz + vector)
# [[11, 22, 33],
#  [14, 25, 36]]
# ← el vector se "copió" a cada fila automáticamente

# Broadcasting en ML: restar la media por feature
datos = np.random.randn(100, 5)          # 100 muestras, 5 features
media = datos.mean(axis=0)               # Shape: (5,) — media de cada feature
datos_centrados = datos - media           # Broadcasting: (100, 5) - (5,) → (100, 5)
```

**Regla de broadcasting**: NumPy compara shapes de derecha a izquierda. Dos dimensiones son compatibles si:
1. Son iguales, o
2. Una de ellas es 1 (se "estira")

```
(100, 5)  + (5,)     → ✅ (100, 5)     # (5,) se trata como (1, 5)
(3, 1)    + (1, 4)   → ✅ (3, 4)       # cada dim 1 se estira
(3, 4)    + (3,)     → ❌ ERROR        # 4 ≠ 3 y ninguno es 1
```

### 2.6 Funciones Matemáticas Esenciales para ML

```python
import numpy as np

# Funciones sobre arrays
a = np.array([1, -2, 3, -4, 5])
np.sum(a)       # 3
np.mean(a)      # 0.6
np.std(a)       # ~3.26
np.max(a)       # 5
np.min(a)       # -4
np.abs(a)       # [1, 2, 3, 4, 5]
np.argmax(a)    # 4 ← ÍNDICE del máximo (muy usado en clasificación)

# Funciones por eje
b = np.array([[1, 2, 3],
              [4, 5, 6]])

np.sum(b, axis=0)   # [5, 7, 9]  ← suma por columna (colapsa filas)
np.sum(b, axis=1)   # [6, 15]    ← suma por fila (colapsa columnas)
np.mean(b, axis=0)  # [2.5, 3.5, 4.5]

# Funciones que usarás CONSTANTEMENTE en ML:
x = np.linspace(-5, 5, 100)

# Sigmoid: σ(x) = 1 / (1 + e^(-x)) — mapea cualquier valor a (0, 1)
sigmoid = 1 / (1 + np.exp(-x))

# ReLU: max(0, x) — la activación más usada
relu = np.maximum(0, x)

# Softmax: convierte vector de scores a probabilidades
def softmax(z):
    exp_z = np.exp(z - np.max(z))  # restar max para estabilidad numérica
    return exp_z / np.sum(exp_z)

logits = np.array([2.0, 1.0, 0.5])
print(softmax(logits))  # [0.59, 0.24, 0.13] — suman ~1.0
```

---

## Parte 3: Matplotlib — Visualización que Importa

Ver los datos y resultados es esencial para entender qué está pasando. En ML, siempre graficarás: datos, curvas de loss, fronteras de decisión, distribuciones, etc.

### 3.1 Gráficas Básicas

```python
import numpy as np
import matplotlib.pyplot as plt

# Gráfica simple de línea
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, np.cos(x), label='cos(x)', color='red', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funciones Trigonométricas')
plt.legend()         # Mostrar leyenda
plt.grid(True)       # Activar grilla
plt.tight_layout()   # Ajustar márgenes
plt.show()

# Scatter plot (gráfico de dispersión — muy usado para datos 2D)
np.random.seed(42)
x1 = np.random.randn(100) + 2    # Clase 0: centrada en (2, 2)
y1 = np.random.randn(100) + 2
x2 = np.random.randn(100) - 2    # Clase 1: centrada en (-2, -2)
y2 = np.random.randn(100) - 2

plt.scatter(x1, y1, c='blue', label='Clase 0', alpha=0.6, edgecolors='black', s=30)
plt.scatter(x2, y2, c='red', label='Clase 1', alpha=0.6, edgecolors='black', s=30)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Datos de Dos Clases')
plt.legend()
plt.show()
```

### 3.2 Subplots y Figuras con Múltiples Gráficas

```python
import numpy as np
import matplotlib.pyplot as plt

# Subplots: múltiples gráficas en una figura
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
# axes es un array de 3 ejes

x = np.linspace(-5, 5, 100)

# Subplot 1: Sigmoid
axes[0].plot(x, 1 / (1 + np.exp(-x)), color='blue', linewidth=2)
axes[0].set_title('Sigmoid')
axes[0].axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)

# Subplot 2: ReLU
axes[1].plot(x, np.maximum(0, x), color='green', linewidth=2)
axes[1].set_title('ReLU')

# Subplot 3: Tanh
axes[2].plot(x, np.tanh(x), color='red', linewidth=2)
axes[2].set_title('Tanh')

for ax in axes:
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('x')

plt.suptitle('Funciones de Activación', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### 3.3 Heatmaps (esenciales para matrices de atención y confusion matrices)

```python
import numpy as np
import matplotlib.pyplot as plt

# Heatmap de una matriz
matrix = np.random.randn(5, 5)
plt.imshow(matrix, cmap='RdBu_r', aspect='auto')
plt.colorbar(label='Valor')
plt.title('Heatmap de una Matriz')
plt.xlabel('Columna')
plt.ylabel('Fila')

# Añadir números en cada celda
for i in range(5):
    for j in range(5):
        plt.text(j, i, f'{matrix[i,j]:.2f}', ha='center', va='center', fontsize=8)

plt.tight_layout()
plt.show()
```

---

## Parte 4: Pandas — Datos Tabulares y Exploración

En Deep Learning, los datos suelen llegar como tensores (imágenes, texto). Pero en la **práctica diaria** de un ML Engineer usarás pandas constantemente para:
- **Explorar datasets** antes de entrenarlos (EDA — Exploratory Data Analysis)
- **Preprocesar datos tabulares** (CSV, bases de datos) antes de convertirlos a tensores
- **Analizar resultados** de experimentos (métricas, logs, comparaciones)
- **Preparar datos para RAG** (Módulo 5): limpiar documentos, metadatos, etc.

### 4.1 DataFrame: La Estructura Central

```python
import pandas as pd
import numpy as np

# Crear un DataFrame desde un diccionario
datos = {
    "nombre": ["Modelo_A", "Modelo_B", "Modelo_C", "Modelo_D"],
    "accuracy": [0.92, 0.88, 0.95, 0.91],
    "params_M": [7.0, 1.1, 25.0, 3.5],       # Millones de parámetros
    "tiempo_entrenamiento_h": [2.5, 0.5, 8.0, 1.2],
    "arquitectura": ["ResNet50", "MobileNet", "EfficientNet-B4", "ResNet18"]
}
df = pd.DataFrame(datos)
print(df)
#       nombre  accuracy  params_M  tiempo_entrenamiento_h    arquitectura
# 0   Modelo_A      0.92       7.0                     2.5        ResNet50
# 1   Modelo_B      0.88       1.1                     0.5       MobileNet
# 2   Modelo_C      0.95      25.0                     8.0  EfficientNet-B4
# 3   Modelo_D      0.91       3.5                     1.2        ResNet18

# Cargar desde CSV (lo más común)
# df = pd.read_csv("resultados_experimentos.csv")
# df = pd.read_csv("dataset.csv", sep=";", encoding="utf-8")
```

### 4.2 Exploración Rápida (EDA)

```python
import pandas as pd

# Estas funciones son lo PRIMERO que ejecutas con cualquier dataset nuevo:
df.shape          # (4, 5) → 4 filas, 5 columnas
df.info()         # Tipos de dato, valores no-nulos por columna
df.describe()     # Estadísticas: media, std, min, max, quartiles (solo numéricas)
df.head(3)        # Primeras 3 filas
df.dtypes         # Tipo de dato por columna
df.isnull().sum() # Valores faltantes por columna ← CRÍTICO antes de entrenar

# Valores únicos (útil para features categóricas)
df["arquitectura"].unique()        # Array de valores únicos
df["arquitectura"].value_counts()  # Conteo por valor
```

### 4.3 Selección y Filtrado

```python
import pandas as pd

# Seleccionar columnas
df["accuracy"]                    # Una columna → Series
df[["nombre", "accuracy"]]        # Varias columnas → DataFrame

# Filtrar filas (como WHERE en SQL)
df[df["accuracy"] > 0.90]                    # Modelos con accuracy > 90%
df[df["arquitectura"].str.contains("Res")]   # Arquitecturas que contienen "Res"
df[(df["accuracy"] > 0.90) & (df["params_M"] < 10)]  # Combinar condiciones con &

# Ordenar
df.sort_values("accuracy", ascending=False)  # Mejor accuracy primero

# Agregar columna calculada
df["eficiencia"] = df["accuracy"] / df["params_M"]  # accuracy por millón de params
```

### 4.4 Operaciones Comunes para ML

```python
import pandas as pd
import numpy as np

# --- Manejar valores faltantes ---
df_con_nulos = pd.DataFrame({
    "feature_1": [1.0, 2.0, np.nan, 4.0],
    "feature_2": [np.nan, 5.0, 6.0, 7.0],
    "label": [0, 1, 1, 0]
})

# Opción 1: Eliminar filas con nulos
df_limpio = df_con_nulos.dropna()

# Opción 2: Rellenar con la media (más común en ML)
df_con_nulos["feature_1"].fillna(df_con_nulos["feature_1"].mean(), inplace=True)

# --- One-hot encoding (para features categóricas) ---
df_encoded = pd.get_dummies(df, columns=["arquitectura"], prefix="arch")
# Agrega columnas: arch_ResNet50, arch_MobileNet, arch_EfficientNet-B4, arch_ResNet18

# --- GroupBy (agrupar y agregar) ---
# Ejemplo: si tuvieras múltiples runs por arquitectura
resultados = pd.DataFrame({
    "arquitectura": ["ResNet", "ResNet", "EfficientNet", "EfficientNet"],
    "run": [1, 2, 1, 2],
    "accuracy": [0.92, 0.93, 0.95, 0.94],
    "loss": [0.25, 0.22, 0.18, 0.19]
})
resumen = resultados.groupby("arquitectura").agg({
    "accuracy": ["mean", "std"],
    "loss": "mean"
})
print(resumen)
# Muestra media y std de accuracy por arquitectura

# --- Train/test split info ---
from sklearn.model_selection import train_test_split
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
print(f"Train: {len(train_df)}, Test: {len(test_df)}")
```

### 4.5 El Puente: DataFrame → NumPy → PyTorch Tensor

Esta es la conexión clave que justifica aprender pandas para Deep Learning:

```python
import pandas as pd
import numpy as np
# import torch  # Lo usarás desde el Módulo 1

# 1. Datos en CSV → DataFrame
df = pd.read_csv("mi_dataset.csv")  # o pd.DataFrame({...})

# 2. Separar features y labels
feature_cols = ["feature_1", "feature_2", "feature_3"]
X = df[feature_cols].values    # .values → NumPy array
y = df["label"].values          # .values → NumPy array

print(type(X))   # <class 'numpy.ndarray'>
print(X.shape)   # (n_samples, 3)

# 3. (Módulo 1) NumPy → PyTorch Tensor
# X_tensor = torch.tensor(X, dtype=torch.float32)
# y_tensor = torch.tensor(y, dtype=torch.long)  # para clasificación
# dataset = TensorDataset(X_tensor, y_tensor)
# dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# El flujo completo en producción:
# CSV → pd.read_csv → DataFrame → preprocesar → .values → np.array → torch.tensor
```

> [!TIP]
> **¿Cuándo usar pandas vs NumPy directamente?**
> - **Pandas**: Cuando tus datos tienen columnas con nombres, tipos mixtos (texto + números), o necesitas explorar/filtrar datos. Datos tabulares.
> - **NumPy**: Cuando ya tienes datos numéricos puros y necesitas operaciones matemáticas rápidas. Tensores.
> - En la práctica: pandas para **cargar y explorar**, NumPy/PyTorch para **entrenar**.

---

## Parte 5: POO (Programación Orientada a Objetos) para ML

En PyTorch, TODO modelo se construye como una clase que hereda de `nn.Module`. Si no estás cómodo con clases, herencia y métodos, el Módulo 1 será confuso. Aquí lo dominarás.

### 4.1 Clases: Lo Básico

```python
# Una clase es un "molde" para crear objetos con datos (atributos) y comportamiento (métodos)

class Rectangulo:
    def __init__(self, ancho, alto):
        """Constructor: se ejecuta al crear un objeto"""
        self.ancho = ancho    # atributo de instancia
        self.alto = alto
    
    def area(self):
        """Método: función que pertenece al objeto"""
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)
    
    def __repr__(self):
        """Cómo se muestra el objeto al imprimirlo"""
        return f"Rectangulo({self.ancho}, {self.alto})"

# Crear objetos (instancias)
r1 = Rectangulo(3, 5)
r2 = Rectangulo(10, 2)
print(r1)            # Rectangulo(3, 5)
print(r1.area())     # 15
print(r1.ancho)      # 3
```

### 4.2 Herencia: El Patrón de PyTorch

```python
# Herencia: crear una clase que EXTIENDE otra clase existente
# En PyTorch: tu modelo HEREDA de nn.Module

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        raise NotImplementedError("Las subclases deben implementar hablar()")

class Perro(Animal):                    # Perro HEREDA de Animal
    def __init__(self, nombre, raza):
        super().__init__(nombre)        # Llama al __init__ del padre
        self.raza = raza
    
    def hablar(self):                   # SOBREESCRIBE el método del padre
        return f"{self.nombre} dice: ¡Guau!"

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Miau!"

# Ahora veamos el MISMO patrón en PyTorch:
# import torch.nn as nn
#
# class MiModelo(nn.Module):            ← HEREDA de nn.Module
#     def __init__(self, input_size):
#         super().__init__()             ← Llama al __init__ de nn.Module
#         self.linear = nn.Linear(input_size, 10)
#
#     def forward(self, x):              ← SOBREESCRIBE forward()
#         return self.linear(x)
```

> [!IMPORTANT]
> **El patrón es siempre el mismo**:
> 1. Heredar de `nn.Module`
> 2. En `__init__`: llamar `super().__init__()` y definir capas
> 3. En `forward`: definir cómo fluyen los datos por las capas

### 4.3 El Patrón `nn.Module` Simulado (sin PyTorch)

Vamos a construir una "mini-versión" de `nn.Module` para entender qué hace por dentro:

```python
class MiniModule:
    """Simulación simplificada de nn.Module para entender el patrón"""
    
    def __init__(self):
        self._parameters = {}   # Almacena los parámetros entrenables
    
    def register_parameter(self, name, value):
        """Registra un parámetro (como nn.Module hace automáticamente)"""
        self._parameters[name] = value
    
    def parameters(self):
        """Devuelve todos los parámetros (lo que pasas al optimizer)"""
        return self._parameters.values()
    
    def forward(self, x):
        raise NotImplementedError
    
    def __call__(self, x):
        """Permite hacer model(x) en vez de model.forward(x)"""
        return self.forward(x)


class MiniLinear(MiniModule):
    """Simulación de nn.Linear"""
    
    def __init__(self, in_features, out_features):
        super().__init__()
        import numpy as np
        # Inicializar pesos aleatorios
        self.register_parameter('weight', np.random.randn(in_features, out_features) * 0.01)
        self.register_parameter('bias', np.zeros(out_features))
    
    def forward(self, x):
        import numpy as np
        return x @ self._parameters['weight'] + self._parameters['bias']


# Usar exactamente como PyTorch:
layer = MiniLinear(5, 3)         # 5 inputs → 3 outputs
import numpy as np
x = np.random.randn(1, 5)       # 1 muestra, 5 features
output = layer(x)                # Llama a __call__ → forward
print(output.shape)              # (1, 3)
print(f"Parámetros: {len(list(layer.parameters()))}")  # 2 (weight + bias)
```

### 4.4 Otros Patrones de Python que Verás en ML

```python
# --- List Comprehensions ---
# Forma compacta de crear listas
cuadrados = [x**2 for x in range(10)]           # [0, 1, 4, 9, 16, ...]
pares = [x for x in range(20) if x % 2 == 0]    # [0, 2, 4, 6, ...]
# En ML: crear listas de capas, filtrar datos, etc.

# --- Unpacking ---
a, b, c = [1, 2, 3]
primera, *resto = [1, 2, 3, 4, 5]   # primera=1, resto=[2,3,4,5]
# En ML: desempaquetar batches, datasets splits, etc.

# --- Diccionarios como configuración ---
config = {
    "lr": 0.001,
    "batch_size": 32,
    "epochs": 100,
    "hidden_dims": [256, 128, 64]
}
# Acceso: config["lr"], config.get("dropout", 0.5)  ← con default

# --- F-strings para logging ---
epoch, loss, acc = 42, 0.234, 0.956
print(f"Epoch {epoch:4d} | Loss: {loss:.4f} | Acc: {acc:.2%}")
# "Epoch   42 | Loss: 0.2340 | Acc: 95.60%"

# --- Context Managers (with) ---
# En ML: torch.no_grad(), open(), dispositivos
# with torch.no_grad():    ← desactiva autograd (para inferencia)
#     output = model(input)

# --- enumerate y zip ---
nombres = ["Adam", "SGD", "RMSprop"]
lrs = [0.001, 0.01, 0.0001]

for i, nombre in enumerate(nombres):    # índice + valor
    print(f"{i}: {nombre}")

for nombre, lr in zip(nombres, lrs):    # iterar en paralelo
    print(f"{nombre}: lr={lr}")

# --- Lambda functions ---
# Función anónima de una línea
relu = lambda x: max(0, x)
print(relu(-5))   # 0
print(relu(3))    # 3

# --- Type hints (buena práctica) ---
def entrenar(modelo, datos: list, epochs: int = 10, lr: float = 0.01) -> dict:
    """Los type hints documentan qué espera y devuelve la función"""
    resultados = {"loss": [], "accuracy": []}
    # ...
    return resultados
```

---

## Parte 6: Debugging de Código Numérico

Cuando trabajes con ML, los bugs no siempre dan errores — a veces el código "funciona" pero produce resultados incorrectos (el modelo no aprende, el loss es NaN, etc.). Aquí van las técnicas clave:

### 5.1 Los 5 Bugs Más Comunes en Código Numérico

```python
import numpy as np

# BUG 1: Shape mismatch silencioso
a = np.array([1, 2, 3])       # Shape: (3,)
b = np.array([[1], [2], [3]]) # Shape: (3, 1)
c = a * b                     # Shape: (3, 3) ← ¡Broadcasting inesperado!
# Esperabas (3,) pero obtuviste (3, 3). SIEMPRE verifica shapes.

# SOLUCIÓN: Imprime shapes obsesivamente al principio
print(f"a.shape={a.shape}, b.shape={b.shape}, c.shape={c.shape}")

# BUG 2: Modificación in-place accidental
original = np.array([1, 2, 3])
referencia = original          # ¡NO es una copia! Es el MISMO objeto
referencia[0] = 999
print(original)  # [999, 2, 3] ← ¡el original cambió!

# SOLUCIÓN: usar .copy()
copia = original.copy()
copia[0] = 0
print(original)  # [999, 2, 3] ← original intacto

# BUG 3: División por cero / Log de cero
probs = np.array([0.0, 0.5, 1.0])
# np.log(probs) → [-inf, -0.693, 0.0] ← ¡-inf!
# SOLUCIÓN: clipping
probs_safe = np.clip(probs, 1e-15, 1 - 1e-15)

# BUG 4: Tipo de dato incorrecto
enteros = np.array([1, 2, 3])          # dtype: int64
resultado = enteros / 4                 # [0.25, 0.5, 0.75] ← OK en Python 3
# Pero en operaciones de PyTorch, mezclar float32 y float64 puede causar errores

# BUG 5: Olvido del axis
datos = np.random.randn(100, 5)
media = np.mean(datos)      # ¡Media de TODO! Un solo número
media = np.mean(datos, axis=0)  # Media por feature: shape (5,) ← Lo que queríamos
```

### 5.2 Técnica de Debugging: "Print-driven Development"

```python
# Cuando algo no funciona en código numérico, imprime:
# 1. Shape de cada tensor/array en cada paso
# 2. Valores mínimo, máximo y media
# 3. Si hay NaN o Inf

def debug_array(name, arr):
    """Helper para imprimir info de debug de un array"""
    print(f"{name}: shape={arr.shape}, dtype={arr.dtype}, "
          f"min={arr.min():.4f}, max={arr.max():.4f}, "
          f"mean={arr.mean():.4f}, "
          f"has_nan={np.isnan(arr).any()}, has_inf={np.isinf(arr).any()}")

# Uso:
x = np.random.randn(32, 10)
debug_array("input", x)
# input: shape=(32, 10), dtype=float64, min=-3.2145, max=2.8901, mean=0.0023, has_nan=False, has_inf=False
```

---

## 🔥 Desafíos del Módulo Previo

### Desafío 1: NumPy Workout (1.5h)

```python
# desafio_previo_1_numpy.py
import numpy as np

# 1. Crea una matriz de 5×5 con los números del 1 al 25
#    Extrae: la diagonal, la segunda fila, la última columna

# 2. Genera 1000 números aleatorios con distribución normal (media=5, std=2)
#    a) Calcula media y desviación estándar (¿se acercan a 5 y 2?)
#    b) ¿Cuántos caen dentro de ±1 std de la media? (debería ser ~68%)
#    c) Grafica un histograma con 30 bins

# 3. Simula un dataset de ML:
#    - 500 muestras, cada una con 3 features
#    - Normaliza cada feature: (x - media) / std  (usa axis=0)
#    - Verifica que después de normalizar, media≈0 y std≈1 por feature

# 4. Implementa estas funciones SIN usar las de NumPy:
def mi_mean(arr):
    """Calcula la media de un array 1D"""
    pass

def mi_std(arr):
    """Calcula la desviación estándar de un array 1D"""
    pass

def mi_argmax(arr):
    """Devuelve el índice del valor máximo"""
    pass

# 5. Multiplicación de matrices:
#    A = [[1, 2], [3, 4]]
#    B = [[5, 6], [7, 8]]
#    a) Calcula A @ B a mano (en papel o con tu función mi_matmul)
#    b) Verifica con NumPy
#    c) ¿A @ B == B @ A? ¿Por qué importa esto en redes neuronales?
```

### Desafío 2: Matplotlib + NumPy Combinados (1.5h)

```python
# desafio_previo_2_visualizacion.py
import numpy as np
import matplotlib.pyplot as plt

# 1. Grafica las 3 funciones de activación (sigmoid, relu, tanh) en un solo subplot
#    con leyenda, grilla, y colores distintos. Rango x: [-6, 6]

# 2. Genera un "dataset" de clasificación 2D:
#    - Clase 0: 200 puntos centrados en (2, 2) con std=1
#    - Clase 1: 200 puntos centrados en (-2, -2) con std=1
#    Grafica con scatter, colores distintos por clase

# 3. "Simula" el entrenamiento de un modelo:
#    - Genera 50 valores de loss que van de 2.5 a 0.05 con algo de ruido
#      (pista: usa np.linspace + np.random.randn * factor_decreciente)
#    - Genera 50 valores de accuracy que van de 0.5 a 0.97
#    - Crea una figura con 2 subplots: loss y accuracy vs epoch
#    - Marca el epoch del mejor accuracy con una línea vertical roja

# 4. Heatmap de una "confusion matrix":
#    Crea una matriz 4×4 que simule una confusion matrix:
#    [[85, 5, 3, 7],
#     [2, 90, 4, 4],
#     [6, 3, 88, 3],
#     [4, 2, 1, 93]]
#    Visualiza como heatmap con etiquetas de clase en los ejes
```

### Desafío 3: OOP y Patrones de ML (1h)

```python
# desafio_previo_3_oop.py
import numpy as np

# DESAFÍO: Construir un mini-framework de "capas" similar a PyTorch

# 1. Crea una clase base Layer con método forward(x) que lanza NotImplementedError

# 2. Crea LinearLayer(Layer) que:
#    - En __init__: recibe in_features, out_features
#    - Inicializa weight y bias con random
#    - forward(x): retorna x @ weight + bias

# 3. Crea ReLULayer(Layer) que:
#    - forward(x): retorna np.maximum(0, x)

# 4. Crea Sequential que:
#    - En __init__: recibe una lista de layers
#    - forward(x): pasa x por cada layer en orden y retorna el resultado final

# 5. Usa tu framework:
model = Sequential([
    LinearLayer(2, 16),
    ReLULayer(),
    LinearLayer(16, 8),
    ReLULayer(),
    LinearLayer(8, 1),
])

x = np.random.randn(5, 2)   # 5 muestras, 2 features
output = model.forward(x)
print(f"Input shape: {x.shape}")
print(f"Output shape: {output.shape}")  # Debería ser (5, 1)

# 6. Añade un método count_parameters() a Sequential
#    que cuente el total de parámetros entrenables (weight + bias de cada LinearLayer)
```

### Desafío Integrador: "Mini Perceptrón" (1.5h)

```python
# desafio_previo_4_integrador.py
# Combina TODO lo aprendido: NumPy + Matplotlib + OOP

import numpy as np
import matplotlib.pyplot as plt

# OBJETIVO: Implementar un Perceptrón (la neurona más simple)
# que clasifique un dataset linealmente separable

class Perceptron:
    def __init__(self, n_features):
        """Inicializa pesos y bias en cero"""
        self.weights = np.zeros(n_features)
        self.bias = 0.0
        self.history = {"accuracy": []}
    
    def predict(self, X):
        """Predicción: 1 si w·x + b > 0, sino 0"""
        # TU IMPLEMENTACIÓN
        pass
    
    def train(self, X, y, epochs=100, lr=0.01):
        """
        Algoritmo del Perceptrón:
        Para cada muestra:
            pred = predict(x)
            error = y_true - pred
            w = w + lr * error * x
            b = b + lr * error
        """
        # TU IMPLEMENTACIÓN
        # Guarda accuracy por epoch en self.history
        pass
    
    def plot_decision_boundary(self, X, y):
        """Grafica los datos y la línea de decisión"""
        # TU IMPLEMENTACIÓN
        # Línea de decisión: w1*x1 + w2*x2 + b = 0
        # Despejando: x2 = -(w1*x1 + b) / w2
        pass

# Crear dataset
np.random.seed(42)
X_pos = np.random.randn(100, 2) + np.array([2, 2])
X_neg = np.random.randn(100, 2) + np.array([-2, -2])
X = np.vstack([X_pos, X_neg])
y = np.array([1]*100 + [0]*100)

# Entrenar
p = Perceptron(n_features=2)
p.train(X, y, epochs=50, lr=0.1)

# Visualizar
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Subplot 1: Frontera de decisión
# (llama a plot_decision_boundary o impleméntalo aquí)

# Subplot 2: Accuracy por epoch
axes[1].plot(p.history["accuracy"], marker='o', markersize=3)
axes[1].set_title("Accuracy por Epoch")
axes[1].set_xlabel("Epoch")
axes[1].set_ylabel("Accuracy")
axes[1].grid(True)

plt.tight_layout()
plt.show()
print(f"Accuracy final: {p.history['accuracy'][-1]:.2%}")
```

**Criterio de éxito del Módulo Previo**:
- ✅ Puedes crear, reshapear y operar arrays de NumPy sin consultar la documentación constantemente
- ✅ Entiendes broadcasting y por qué `(100, 5) + (5,)` funciona
- ✅ Puedes cargar un CSV con pandas, explorarlo, filtrarlo y convertirlo a NumPy array
- ✅ Puedes crear figuras con subplots, scatter plots y heatmaps
- ✅ Entiendes clases, herencia, `super().__init__()` y el patrón `forward()`
- ✅ El desafío integrador (Perceptrón) funciona y genera gráficas correctas

---

### 🏆 Hito del Módulo Previo
> **Desbloqueado**: Fluidez con el ecosistema Python científico. Ya no tendrás fricción con el código en los módulos siguientes — podrás concentrar toda tu energía mental en los conceptos de ML.

---

### 🧩 Desafío Socrático — Módulo Previo

**Pregunta 1 — NumPy:**
> Tienes un array `datos` de shape `(1000, 10)` (1000 muestras, 10 features). Quieres restarle la media de cada feature y dividir por su desviación estándar (normalización Z-score). Escribe el código en UNA sola línea usando broadcasting. ¿Qué shapes tienen `datos.mean(axis=0)` y `datos.std(axis=0)`? ¿Por qué funciona el broadcasting aquí?

**Pregunta 2 — OOP:**
> En PyTorch, cuando haces `model(x)` en realidad NO se llama `model.forward(x)` directamente — se llama `model.__call__(x)`, que internamente llama a `forward()` después de hacer otras cosas (como registrar hooks). ¿Por qué crees que se diseñó así? ¿Qué ventaja tiene usar `__call__` como intermediario en vez de llamar `forward()` directamente?

---

✅ **Cuando completes los 4 desafíos y puedas responder las preguntas socrática, pasa al Módulo 0.**

> **Siguiente**: [Módulo 0 — Fundamentos Matemáticos](plan_estudio_ml_parte1.md)

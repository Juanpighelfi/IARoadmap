# 🔑 Hints — Challenge 2: PCA Manual

## PASO 2: Centrar los datos

### Hint 1 (Dirección)
Necesitás calcular la media de cada feature (columna) y restarla.

### Hint 2 (Pseudo-código)
```
media = calcular_media_por_columna(data)
datos_centrados = datos - media
```

### Hint 3 (Código)
```python
mean = data.mean(axis=0)  # axis=0 → media por columna
data_centered = data - mean  # broadcasting resta la media a cada fila
```

---

## PASO 3: Matriz de Covarianza

### Hint 1 (Dirección)
La covarianza se calcula con datos centrados multiplicados por su transpuesta.

### Hint 2 (Pseudo-código)
```
cov = (1 / (n-1)) * datos_centrados^T · datos_centrados
```

### Hint 3 (Código)
```python
cov_matrix = (1 / (n_samples - 1)) * data_centered.T @ data_centered
```

---

## PASO 4: Eigenvalores y Eigenvectores

### Hint 1 (Dirección)
`np.linalg.eigh()` es para matrices simétricas (la covarianza lo es).

### Hint 2 (Pseudo-código)
```
eigenvalores, eigenvectores = descomposición_eigen(cov_matrix)
indices_ordenados = ordenar_de_mayor_a_menor(eigenvalores)
```

### Hint 3 (Código)
```python
eigenvalores, eigenvectores = np.linalg.eigh(cov_matrix)
idx_sorted = np.argsort(eigenvalores)[::-1]
```

---

## PASO 5: Varianza Explicada

### Hint 1 (Dirección)
Cada eigenvalor / suma total = porcentaje de varianza.

### Hint 2 (Código)
```python
varianza_total = np.sum(eigenvalores)
varianza_explicada = eigenvalores / varianza_total
varianza_acumulada = np.cumsum(varianza_explicada)
```

---

## PASO 6: Proyección

### Hint 1 (Dirección)
Multiplicá los datos centrados por las primeras k columnas de eigenvectores.

### Hint 2 (Código)
```python
W = eigenvectores[:, :n_components]
data_2d = data_centered @ W
```

---

## BONUS: Reconstrucción

### Hint 1 (Código)
```python
data_reconstruido = data_2d @ W.T + mean
```

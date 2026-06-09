# 🔑 Hints — Challenge 3: Transformaciones Lineales

## PARTE 2: Matriz de Rotación

### Hint 1 (Dirección)
Convertí grados a radianes y usá cos/sin para construir la matriz 2x2.

### Hint 2 (Fórmula)
```
R(θ) = [[cos(θ), -sin(θ)],
        [sin(θ),  cos(θ)]]
```

### Hint 3 (Código)
```python
theta = np.radians(angulo_grados)
return np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])
```

---

## PARTE 3: Composición

### Hint 1
En la notación de matrices, la ÚLTIMA operación va a la IZQUIERDA.
"Primero rotar, luego escalar" = S @ R (no R @ S).

### Hint 2 (Código)
```python
AB = S @ R45   # Primero R45, luego S
BA = R45 @ S   # Primero S, luego R45
```

---

## PARTE 4: Forward Pass

### Hint 1
W @ x multiplica cada punto por W. Sumás b después.

### Hint 2 (Código)
```python
z = (W @ datos.T).T + b
a = np.maximum(0, z)  # ReLU
```

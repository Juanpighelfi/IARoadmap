# 🔑 Hints — Challenge 4: Gradientes Manuales

## PASO 1: Forward Pass

### Hint 1 (Dirección)
Seguí la secuencia: z = lineal, a = activación, L = pérdida.

### Hint 2 (Código)
```python
z = W @ x + b
a = sigmoid(z)
L = (a - y_true) ** 2
```

---

## PASO 2: Backward Pass

### Hint 1 (Dirección)
Cada derivada parcial se encadena con la anterior (regla de la cadena).

### Hint 2 (Fórmulas)
```
dL/da = 2(a - y_true)
da/dz = a * (1 - a)
dL/dz = dL/da * da/dz
dL/dW = dL/dz ⊗ x    (outer product)
dL/db = dL/dz
```

### Hint 3 (Código)
```python
dL_da = 2 * (a - y_true)
da_dz = a * (1 - a)
dL_dz = dL_da * da_dz
dL_dW = dL_dz.reshape(-1, 1) @ x.reshape(1, -1)
dL_db = dL_dz
```

---

## PASO 4: Training Loop

### Hint 1
Es lo mismo que los pasos 1-3, pero dentro de un for loop.

### Hint 2 (Estructura)
```python
for epoch in range(1000):
    # Forward
    z = W_train @ x + b_train
    a = sigmoid(z)
    loss = (a - y_true) ** 2
    
    # Backward (mismas fórmulas)
    dL_da = 2 * (a - y_true)
    da_dz = a * (1 - a)
    dL_dz = dL_da * da_dz
    dL_dW = dL_dz.reshape(-1, 1) @ x.reshape(1, -1)
    dL_db = dL_dz
    
    # Update
    W_train -= lr * dL_dW
    b_train -= lr * dL_db
```

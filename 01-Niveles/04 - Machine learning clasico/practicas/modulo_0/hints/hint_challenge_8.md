# 🔑 Hints — Challenge 8: MSE vs Cross-Entropy

## PARTE 1: Loss y gradientes

### Hint 1 (MSE)
```python
mse_loss = (y_hat - y_true) ** 2
mse_grad = 2 * (y_hat - y_true) * y_hat * (1 - y_hat)
```

### Hint 2 (BCE)
```python
bce_loss = -(y_true * np.log(np.clip(y_hat, 1e-15, None)) + 
             (1 - y_true) * np.log(np.clip(1 - y_hat, 1e-15, None)))
bce_grad = y_hat - y_true
```

### Hint 3 (para y_true=0, es lo mismo cambiando y_true)
```python
mse_loss_0 = (y_hat - 0) ** 2
mse_grad_0 = 2 * (y_hat - 0) * y_hat * (1 - y_hat)
```

---

## PARTE 3: Training loop

### Hint 1
```python
z = X.flatten() * w + b
a = 1 / (1 + np.exp(-z))

# BCE
eps = 1e-15
a_clipped = np.clip(a, eps, 1-eps)
loss = -np.mean(y * np.log(a_clipped) + (1-y) * np.log(1-a_clipped))
dz = a - y

# MSE
loss = np.mean((a - y) ** 2)
dz = 2 * (a - y) * a * (1 - a)
```

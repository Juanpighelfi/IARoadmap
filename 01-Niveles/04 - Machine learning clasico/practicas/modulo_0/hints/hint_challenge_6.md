# 🔑 Hints — Challenge 6: Vanishing Gradient

## PARTE 1: Apilar sigmoids

### Hint 1 (forward)
En cada iteración, aplicá sigmoid al valor actual: `z = sigmoid(z)` y agregá a la lista.

### Hint 2 (gradient)
Multiplicá las derivadas locales: para cada activación a, `local_grad = a * (1 - a)`.

### Hint 3 (Código)
```python
# forward
for _ in range(n_layers):
    z = sigmoid(z)
    activations.append(z)

# gradient
for i in range(len(activations) - 1):
    a = activations[i + 1]
    grad *= a * (1 - a)
```

---

## PARTE 2: PyTorch verification

### Hint 1
```python
for _ in range(n):
    z_t = torch.sigmoid(z_t)
```

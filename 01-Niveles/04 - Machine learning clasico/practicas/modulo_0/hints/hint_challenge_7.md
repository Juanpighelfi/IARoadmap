# 🔑 Hints — Challenge 7: Cross-Entropy

## PARTE 1: Binary Cross-Entropy

### Hint 1
BCE = -(y·log(ŷ) + (1-y)·log(1-ŷ)). Necesitás clip para evitar log(0).

### Hint 2 (Código)
```python
y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
loss = -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
return np.mean(loss)
```

---

## PARTE 3: Categorical Cross-Entropy

### Hint 1 (Código)
```python
y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
loss = -np.sum(y_true_onehot * np.log(y_pred), axis=-1)
return np.mean(loss)
```

---

## PARTE 4: Batch

### Hint 1
Aplica BCE elemento a elemento (sin promediar) para ver la loss individual.

### Hint 2 (Código)
```python
losses_individuales = -(batch_y_true * np.log(np.clip(batch_y_pred, 1e-15, None)) + 
                        (1 - batch_y_true) * np.log(np.clip(1 - batch_y_pred, 1e-15, None)))
```

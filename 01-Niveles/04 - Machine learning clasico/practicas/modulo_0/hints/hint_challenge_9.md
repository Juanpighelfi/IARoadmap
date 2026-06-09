# 🔑 Hints — Challenge 9: KL Divergence

## PARTE 1: Cálculo manual

### Hint 1 (Fórmula)
KL(P||Q) = Σ P(i) · log(P(i) / Q(i))

### Hint 2 (Código)
```python
term = P[i] * np.log(P[i] / Q1[i])
```

### Para KL(Q1||P):
```python
term = Q1[i] * np.log(Q1[i] / P[i])
```

---

## PARTE 3: KL Gaussianas (VAEs)

### Hint 1
```python
return -0.5 * np.sum(1 + log_var - mu**2 - np.exp(log_var))
```

---

## PARTE 4: Entropía, CE, KL

### Hint 1
```python
def entropia(p):
    p = p[p > 0]
    return -np.sum(p * np.log(p))

def cross_entropy_fn(p, q, eps=1e-15):
    q = np.clip(q, eps, None)
    return -np.sum(p * np.log(q))

def kl_div(p, q, eps=1e-15):
    q = np.clip(q, eps, None)
    mask = p > 0
    return np.sum(p[mask] * np.log(p[mask] / q[mask]))
```

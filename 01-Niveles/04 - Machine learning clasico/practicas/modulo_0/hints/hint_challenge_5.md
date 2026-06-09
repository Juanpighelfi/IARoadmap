# 🔑 Hints — Challenge 5: Autograd Verify

## PARTE 1: PyTorch Forward + Backward

### Hint 1
Creá tensores con `requires_grad=True` para que PyTorch trackee operaciones.

### Hint 2 (Código)
```python
W_t = torch.tensor([[0.5, -0.3]], requires_grad=True)
b_t = torch.tensor([0.1], requires_grad=True)
z_t = W_t @ x_t + b_t
a_t = torch.sigmoid(z_t)
loss_t = (a_t - y_true_t) ** 2
loss_t.backward()  # Calcula TODOS los gradientes
```

---

## PARTE 2: Función compuesta

### Hint 1
```python
x2 = torch.tensor([3.0], requires_grad=True)
y2 = torch.tensor([2.0], requires_grad=True)
f = x2**2 * y2 + torch.sin(y2)
f.backward()
# Gradientes en x2.grad y y2.grad
```

---

## PARTE 3: Segunda derivada

### Hint 1
`create_graph=True` mantiene el grafo computacional para poder calcular otra derivada.

### Hint 2
```python
grad1 = torch.autograd.grad(f3, x3, create_graph=True)[0]
grad2 = torch.autograd.grad(grad1, x3)[0]
```

---

## CASO 4: Acumulación

### Hint 1
```python
if x_ac2.grad is not None:
    x_ac2.grad.zero_()
```

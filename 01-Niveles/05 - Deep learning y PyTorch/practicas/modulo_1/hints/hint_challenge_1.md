# 🔑 Hints — M1 Challenge 1: Tensores y Autograd

## Desafío 1: Operaciones con tensores

### Hint 1
```python
t3d = torch.randn(2, 3, 4)
r1 = t3d.reshape(6, 4)
r2 = t3d.reshape(2, 12)
m = t3d.mean(dim=dim)
c = a + b  # broadcasting automático
```

## Desafío 2: Autograd

### Hint 1
```python
x = torch.tensor([3.0], requires_grad=True)
y = torch.tensor([2.0], requires_grad=True)
f = x**2 * y + torch.sin(y)
f.backward()
```

### Derivada segunda
```python
grad1 = torch.autograd.grad(f2, x2, create_graph=True)[0]
grad2 = torch.autograd.grad(grad1, x2)[0]
```

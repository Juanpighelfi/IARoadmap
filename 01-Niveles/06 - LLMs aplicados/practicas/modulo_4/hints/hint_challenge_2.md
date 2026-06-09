# 🔑 Hints — M4 Challenge 2: LoRA Manual

## Cálculo de parámetros
```python
lora_params = d * r + r * d  # A: d×r, B: r×d
pct = lora_params / (d * d) * 100
```

## LoRALinear
```python
# Congelar
self.original.weight.requires_grad = False
if self.original.bias is not None:
    self.original.bias.requires_grad = False

# Matrices LoRA
self.A = nn.Parameter(torch.randn(d_in, r) * 0.01)
self.B = nn.Parameter(torch.zeros(r, d_out))

# Forward
def forward(self, x):
    original_out = self.original(x)
    lora_out = (x @ self.A @ self.B) * self.scaling
    return original_out + lora_out

# Merge
def merge(self):
    with torch.no_grad():
        self.original.weight += (self.B.T @ self.A.T) * self.scaling
    return self.original
```

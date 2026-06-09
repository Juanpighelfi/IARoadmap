# 🔑 Hints — M1 Challenge 5: Debugging Training

## Bug 1: Softmax + CrossEntropyLoss
El fix es ELIMINAR `nn.Softmax()` del forward. `CrossEntropyLoss` ya lo incluye.

```python
class FixedModel1(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(20, 64)
        self.fc2 = nn.Linear(64, 2)
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)  # Sin softmax!
```

## Bug 3: Normalización
```python
X_normalized = (X_bad - X_bad.mean(dim=0)) / (X_bad.std(dim=0) + 1e-8)
```

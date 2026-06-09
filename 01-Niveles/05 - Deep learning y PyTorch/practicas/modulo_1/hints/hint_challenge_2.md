# 🔑 Hints — M1 Challenge 2: Custom Modules

## Swish Activation
```python
def forward(self, x):
    return x * torch.sigmoid(x)
```

## ResidualBlock
```python
self.block = nn.Sequential(
    nn.Linear(dim, dim), nn.BatchNorm1d(dim), nn.ReLU(),
    nn.Linear(dim, dim), nn.BatchNorm1d(dim)
)
def forward(self, x):
    return self.relu(self.block(x) + x)  # ← skip connection
```

## MiniResNet
```python
self.project = nn.Linear(input_dim, hidden_dim)
self.blocks = nn.Sequential(*[ResidualBlock(hidden_dim) for _ in range(3)])
self.classifier = nn.Linear(hidden_dim, num_classes)
def forward(self, x):
    x = self.project(x)
    x = self.blocks(x)
    return self.classifier(x)
```

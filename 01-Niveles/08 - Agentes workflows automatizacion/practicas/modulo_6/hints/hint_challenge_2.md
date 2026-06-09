# 🔑 Hints — M6 Challenge 2: Experiment Tracking

## SimpleNet
```python
self.net = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, hidden_dim), nn.BatchNorm1d(hidden_dim), nn.ReLU(), nn.Dropout(dropout),
    nn.Linear(hidden_dim, 10),
)
def forward(self, x): return self.net(x)
```

## Training step
```python
optimizer.zero_grad()
loss = criterion(model(x), y)
loss.backward()
optimizer.step()
```

## Evaluation
```python
out = model(x)
total_loss += criterion(out, y).item() * x.size(0)
correct += (out.argmax(1) == y).sum().item()
```

## MLflow logging
```python
mlflow.set_experiment("FashionMNIST_DNN")
with mlflow.start_run(run_name=f"run_{i+1}"):
    config, acc, loss, model = train_and_log(**params)
    mlflow.log_params(config)
    mlflow.log_metric("test_accuracy", acc)
    mlflow.log_metric("test_loss", loss)
```

# 🔑 Hints — M1 Challenge 3: Training Loop Profesional

## EarlyStopping
```python
def __init__(self, patience=5, min_delta=0.001):
    self.patience = patience
    self.min_delta = min_delta
    self.best_loss = float('inf')
    self.counter = 0
    self.should_stop = False

def __call__(self, val_loss):
    if val_loss < self.best_loss - self.min_delta:
        self.best_loss = val_loss
        self.counter = 0
    else:
        self.counter += 1
        if self.counter >= self.patience:
            self.should_stop = True
    return self.should_stop
```

## Training step
```python
optimizer.zero_grad()
x_flat = batch_x.view(batch_x.size(0), -1)
output = model(x_flat)
loss = criterion(output, batch_y)
loss.backward()
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
optimizer.step()
```

## Validation step
```python
x_flat = batch_x.view(batch_x.size(0), -1)
output = model(x_flat)
loss = criterion(output, batch_y)
val_loss += loss.item() * batch_x.size(0)
val_correct += (output.argmax(1) == batch_y).sum().item()
```

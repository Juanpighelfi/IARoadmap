# 🔑 Hints — M1 Challenge 6: Regularización Comparativa

## create_model
```python
layers = [nn.Flatten(), nn.Linear(784, 256)]
if use_batchnorm:
    layers.append(nn.BatchNorm1d(256))
layers.append(nn.ReLU())
if use_dropout:
    layers.append(nn.Dropout(dropout_rate))
layers.append(nn.Linear(256, 10))
return nn.Sequential(*layers)
```

## Train step
```python
optimizer.zero_grad()
out = model(x)
loss = criterion(out, y_batch)
loss.backward()
optimizer.step()
correct_train += (out.argmax(1) == y_batch).sum().item()
total_train += len(y_batch)
```

## Eval step
```python
out = model(x)
correct_test += (out.argmax(1) == y_batch).sum().item()
total_test += len(y_batch)
```

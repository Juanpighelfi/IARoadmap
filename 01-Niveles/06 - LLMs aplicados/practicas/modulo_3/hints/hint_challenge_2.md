# 🔑 Hints — M3 Challenge 2: Positional Encoding

## Implementación
```python
pe = torch.zeros(max_len, d_model)
pos = torch.arange(0, max_len).unsqueeze(1).float()
div_term = torch.exp(torch.arange(0, d_model, 2).float() * -(np.log(10000.0) / d_model))
pe[:, 0::2] = torch.sin(pos * div_term)
pe[:, 1::2] = torch.cos(pos * div_term)
```

## Permutation Equivariance
```python
scores_1 = F.softmax(tokens_1 @ W_q @ (tokens_1 @ W_k).T / np.sqrt(8), dim=-1)
scores_2 = F.softmax(tokens_2 @ W_q @ (tokens_2 @ W_k).T / np.sqrt(8), dim=-1)
```

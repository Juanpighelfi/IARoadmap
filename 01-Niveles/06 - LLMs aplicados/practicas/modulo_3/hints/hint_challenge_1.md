# 🔑 Hints — M3 Challenge 1: Self-Attention

## Q, K, V
```python
Q = embeddings @ W_q
K = embeddings @ W_k
V = embeddings @ W_v
```

## Attention Scores
```python
scores_scaled = (Q @ K.T) / np.sqrt(d_k)
weights_scaled = F.softmax(scores_scaled, dim=-1)
```

## Output
```python
output = weights_scaled @ V
```

## Causal Mask
```python
mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1).bool()
scores_masked = scores_scaled.clone()
scores_masked.masked_fill_(mask, float('-inf'))
weights_causal = F.softmax(scores_masked, dim=-1)
```

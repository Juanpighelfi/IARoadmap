# 🔑 Hints — M3 Challenge 3: Multi-Head Attention

## Proyecciones
```python
self.W_q = nn.Linear(d_model, d_model)
self.W_k = nn.Linear(d_model, d_model)
self.W_v = nn.Linear(d_model, d_model)
self.W_o = nn.Linear(d_model, d_model)
```

## Split en cabezas
```python
Q = Q.view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)
```

## Scaled Dot-Product
```python
scores = torch.matmul(Q, K.transpose(-2, -1)) / np.sqrt(self.d_k)
context = torch.matmul(attn_weights, V)
```

## Concatenar
```python
context = context.transpose(1, 2).contiguous().view(batch_size, -1, self.d_model)
output = self.W_o(context)
```

## TransformerEncoderLayer
```python
self.self_attn = MyMultiHeadAttention(d_model, n_heads, dropout)
self.norm1 = nn.LayerNorm(d_model)
self.norm2 = nn.LayerNorm(d_model)
self.ffn = nn.Sequential(
    nn.Linear(d_model, d_ff), nn.GELU(), nn.Dropout(dropout),
    nn.Linear(d_ff, d_model), nn.Dropout(dropout))

def forward(self, x):
    attn_out, _ = self.self_attn(x, x, x)
    x = self.norm1(x + attn_out)
    x = self.norm2(x + self.ffn(x))
    return x
```

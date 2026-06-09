# 🔑 Hints — M4 Challenge 1: LLM Anatomy

## Estimación de parámetros
```python
estimated = V * d + L * (4 * d * d + 3 * d * ffn + 4 * d) + d
```
Los 4·d² vienen de Q, K, V, O projections. Los 3·d·ffn del FFN (gate, up, down).

## Tokenización
Es solo `tokenizer.encode(texto)` y `tokenizer.decode([token_id])`.

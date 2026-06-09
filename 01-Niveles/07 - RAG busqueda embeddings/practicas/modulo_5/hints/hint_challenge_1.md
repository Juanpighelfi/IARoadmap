# 🔑 Hints — M5 Challenge 1: Vector Search

## Similitud coseno
```python
def cosine_similarity_matrix(embs):
    norms = np.linalg.norm(embs, axis=1, keepdims=True)
    normalized = embs / norms
    return normalized @ normalized.T
```

## Búsqueda (por cada documento)
```python
sim = np.dot(q_emb, emb) / (np.linalg.norm(q_emb) * np.linalg.norm(emb))
```

## Chunking
```python
end = min(start + chunk_size, len(words))
chunks.append(" ".join(words[start:end]))
start += chunk_size - overlap
```

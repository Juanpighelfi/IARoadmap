# 🔑 Hints — M5 Challenge 2: RAG Pipeline

## SimpleVectorStore.add_documents
```python
def add_documents(self, docs):
    self.documents = docs
    if self.encoder:
        self.embeddings = self.encoder.encode(docs)
    else:
        np.random.seed(42)
        self.embeddings = np.random.randn(len(docs), 384)
```

## SimpleVectorStore.search
```python
def search(self, query, top_k=3):
    if self.encoder:
        q_emb = self.encoder.encode([query])[0]
    else:
        q_emb = np.random.randn(384)
    
    scores = []
    for i, emb in enumerate(self.embeddings):
        sim = np.dot(q_emb, emb) / (np.linalg.norm(q_emb) * np.linalg.norm(emb) + 1e-10)
        scores.append((sim, i))
    
    scores.sort(reverse=True)
    return [(self.documents[idx], score) for score, idx in scores[:top_k]]
```

## format_rag_prompt
```python
context = "\n".join([f"- {doc}" for doc, _ in context_docs])
prompt = f"[SYSTEM]\n{system_prompt}\n\n[CONTEXTO]\n{context}\n\n[PREGUNTA]\n{query}\n\n[RESPUESTA]"
```

# 🔑 Hints — M6 Challenge 1: FastAPI ML

## Schemas Pydantic
```python
class PredictionRequest(BaseModel):
    pixels: List[float] = Field(..., min_length=784, max_length=784)

class PredictionResponse(BaseModel):
    prediction: str
    class_id: int
    confidence: float
    probabilities: dict
    latency_ms: float
```

## Endpoint /predict
```python
start = time.time()
tensor = torch.tensor(request.pixels).view(1, 784).float()
with torch.no_grad():
    logits = model(tensor)
    probs = torch.softmax(logits, dim=1)[0]
conf, pred = torch.max(probs, 0)
latency = (time.time() - start) * 1000
```

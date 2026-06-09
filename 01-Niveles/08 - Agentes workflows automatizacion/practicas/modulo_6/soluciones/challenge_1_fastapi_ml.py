"""
=============================================================================
M6-CHALLENGE 1: FastAPI para ML
=============================================================================
Tu primera API de ML: servir un modelo con endpoints profesionales.
DURACION: ~1.5h | DIFICULTAD: 3/5
=============================================================================
"""
print("=" * 60)
print("M6-CHALLENGE 1: FastAPI para ML")
print("=" * 60)

# === API CODE ===
API_CODE = '''
"""
API de ML con FastAPI.
Ejecutar: uvicorn challenge_1_fastapi_ml:app --reload
Probar: http://localhost:8000/docs
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import torch
import torch.nn as nn
import numpy as np
import time
import logging
from typing import List
from datetime import datetime

# Logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(
    title="ML Model API",
    description="API de clasificacion FashionMNIST",
    version="1.0.0"
)

# --- Modelo simple (en produccion, cargarias un checkpoint) ---
class SimpleClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(784, 256), nn.ReLU(), nn.Dropout(0.3),
            nn.Linear(256, 128), nn.ReLU(), nn.Dropout(0.3),
            nn.Linear(128, 10),
        )
    def forward(self, x):
        return self.net(x)

model = SimpleClassifier()
model.eval()
CLASSES = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat',
           'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# --- Schemas ---
class PredictionRequest(BaseModel):
    pixels: List[float] = Field(..., min_length=784, max_length=784,
                                 description="784 pixel values (28x28 flattened)")

class PredictionResponse(BaseModel):
    prediction: str
    class_id: int
    confidence: float
    probabilities: dict
    latency_ms: float

# --- Metricas in-memory ---
metrics = {"total_requests": 0, "total_latency_ms": 0, "errors": 0}

# --- Endpoints ---
@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "model": "SimpleClassifier",
        "device": "cpu",
        "parameters": sum(p.numel() for p in model.parameters()),
        "classes": len(CLASSES),
        "total_predictions": metrics["total_requests"],
    }

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    start = time.time()
    try:
        tensor = torch.tensor(request.pixels).view(1, 784).float()
        
        with torch.no_grad():
            logits = model(tensor)
            probs = torch.softmax(logits, dim=1)[0]
        
        conf, pred = torch.max(probs, 0)
        latency = (time.time() - start) * 1000
        
        metrics["total_requests"] += 1
        metrics["total_latency_ms"] += latency
        
        response = PredictionResponse(
            prediction=CLASSES[pred.item()],
            class_id=pred.item(),
            confidence=round(conf.item(), 4),
            probabilities={CLASSES[i]: round(p.item(), 4) for i, p in enumerate(probs)},
            latency_ms=round(latency, 2),
        )
        
        logger.info(f"Predicted: {response.prediction} ({response.confidence:.2%}) in {latency:.1f}ms")
        return response
    
    except Exception as e:
        metrics["errors"] += 1
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/metrics")
async def get_metrics():
    avg_latency = (metrics["total_latency_ms"] / metrics["total_requests"]
                   if metrics["total_requests"] > 0 else 0)
    return {
        **metrics,
        "avg_latency_ms": round(avg_latency, 2),
    }
'''

print(API_CODE)

# --- Dockerfile ---
print(f"\n{'='*60}")
print("--- Dockerfile ---")
print("=" * 60)

DOCKERFILE = '''
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "challenge_1_fastapi_ml:app", "--host", "0.0.0.0", "--port", "8000"]
'''
print(DOCKERFILE)

# --- Test script ---
print(f"\n{'='*60}")
print("--- Script de prueba (sin levantar el server) ---")
print("=" * 60)

import torch
import torch.nn as nn
import numpy as np
import time

class SimpleClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(784, 256), nn.ReLU(),
            nn.Linear(256, 128), nn.ReLU(),
            nn.Linear(128, 10),
        )
    def forward(self, x):
        return self.net(x)

model = SimpleClassifier()
model.eval()
CLASSES = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat',
           'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Simular prediccion
pixels = np.random.randn(784).tolist()
tensor = torch.tensor(pixels).view(1, 784).float()

start = time.time()
with torch.no_grad():
    logits = model(tensor)
    probs = torch.softmax(logits, dim=1)[0]
latency = (time.time() - start) * 1000

conf, pred = torch.max(probs, 0)
print(f"  Prediction: {CLASSES[pred.item()]}")
print(f"  Confidence: {conf.item():.2%}")
print(f"  Latency:    {latency:.2f}ms")
print(f"  Top 3:")
top3 = torch.topk(probs, 3)
for i, (p, idx) in enumerate(zip(top3.values, top3.indices)):
    print(f"    {i+1}. {CLASSES[idx.item()]}: {p.item():.2%}")

print("""
  PARA EJECUTAR LA API:
  1. pip install fastapi uvicorn
  2. Copiar el codigo API_CODE a un archivo .py
  3. uvicorn challenge_1_fastapi_ml:app --reload
  4. Abrir http://localhost:8000/docs
  
  PARA DOCKERIZAR:
  1. Guardar el Dockerfile
  2. docker build -t ml-api .
  3. docker run -p 8000:8000 ml-api
""")

print("\nM6-Challenge 1 completado.")

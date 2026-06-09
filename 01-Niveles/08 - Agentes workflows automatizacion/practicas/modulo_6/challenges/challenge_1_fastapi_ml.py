"""
=============================================================================
M6-CHALLENGE 1: FastAPI para ML
=============================================================================
Tu primera API de ML: servir un modelo con endpoints profesionales.
DURACIÓN: ~1.5h | DIFICULTAD: ⭐⭐⭐

HINTS: Si te trabás, consultá modulo_6/hints/hint_challenge_1.md
=============================================================================
"""
print("=" * 60)
print("M6-CHALLENGE 1: FastAPI para ML")
print("=" * 60)

"""
TODO: Implementa una API de ML con FastAPI.

Estructura:
1. SimpleClassifier (nn.Module) — modelo ya definido
2. PredictionRequest (Pydantic) — schema de entrada
3. PredictionResponse (Pydantic) — schema de salida  
4. Endpoints: /health, /predict, /metrics

Completa el código de la API abajo y luego ejecuta:
  uvicorn challenge_1_fastapi_ml:app --reload
"""

API_CODE = '''
"""
TODO: Completa esta API de ML.
Ejecutar: uvicorn challenge_1_fastapi_ml:app --reload
Probar: http://localhost:8000/docs
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import torch
import torch.nn as nn
import numpy as np
import time
from typing import List

app = FastAPI(
    title="ML Model API",
    description="API de clasificación FashionMNIST",
    version="1.0.0"
)

# --- Modelo ---
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

# --- TODO: Define los schemas de Pydantic ---
class PredictionRequest(BaseModel):
    """TODO: Define pixels como List[float] con min_length=784, max_length=784"""
    pass  # Tu código aquí

class PredictionResponse(BaseModel):
    """TODO: Define prediction, class_id, confidence, probabilities, latency_ms"""
    pass  # Tu código aquí

# --- TODO: Implementa los endpoints ---

@app.get("/health")
async def health():
    """TODO: Retorna status, modelo, device, parámetros, clases"""
    pass  # Tu código aquí

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """
    TODO: Implementa predicción:
    1. Convierte pixels a tensor
    2. Forward pass con torch.no_grad()
    3. Aplica softmax
    4. Retorna PredictionResponse
    """
    pass  # Tu código aquí

@app.get("/metrics")
async def get_metrics():
    """TODO: Retorna métricas de uso (total_requests, avg_latency)"""
    pass  # Tu código aquí
'''

print(API_CODE)

# --- Test script (sin levantar el server) ---
print(f"\n{'='*60}")
print("--- Test de predicción (sin server) ---")
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

"""
TODO: Simula una predicción:
1. Crea un input de 784 pixels aleatorios
2. Haz forward pass
3. Aplica softmax
4. Obtén la clase predicha
"""
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

print("\nM6-Challenge 1 completado.")

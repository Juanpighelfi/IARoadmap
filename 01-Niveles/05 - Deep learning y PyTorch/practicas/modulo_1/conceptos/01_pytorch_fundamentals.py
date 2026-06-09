"""
=============================================================================
📐 PYTORCH FUNDAMENTALS — Guía Conceptual Interactiva
=============================================================================
Tensores, autograd, nn.Module y el training loop profesional.
Ejecutar ANTES de los challenges de este módulo.
DURACIÓN: ~40 minutos
=============================================================================
"""
import torch
import torch.nn as nn
import numpy as np

print("=" * 60)
print("1️⃣  TENSORES — La estructura de datos de Deep Learning")
print("=" * 60)

# Crear tensores de varias formas
a = torch.zeros(2, 3)
b = torch.ones(3, 4)
c = torch.randn(2, 3)          # Normal(0,1)
d = torch.arange(0, 10, 2)     # [0, 2, 4, 6, 8]
e = torch.linspace(0, 1, 5)    # [0, 0.25, 0.5, 0.75, 1.0]

print(f"  zeros(2,3):    shape={a.shape}, dtype={a.dtype}")
print(f"  randn(2,3):    shape={c.shape}")
print(f"  arange(0,10,2): {d}")
print(f"  linspace(0,1,5): {e}")

# Conversión NumPy <-> Tensor (COMPARTEN MEMORIA)
np_arr = np.array([1.0, 2.0, 3.0])
t_from_np = torch.from_numpy(np_arr)
np_arr[0] = 99
print(f"\n  NumPy→Tensor comparten memoria: {t_from_np}")

# Reshaping
x = torch.randn(2, 3, 4)
print(f"\n  Original: {x.shape}")
print(f"  view(6,4):   {x.view(6, 4).shape}")
print(f"  view(2,12):  {x.view(2, 12).shape}")
print(f"  permute(2,0,1): {x.permute(2, 0, 1).shape}")

# Broadcasting
a_bc = torch.randn(3, 1)
b_bc = torch.randn(1, 4)
print(f"\n  Broadcasting: (3,1) + (1,4) → {(a_bc + b_bc).shape}")

# Device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"\n  Device disponible: {device}")

print(f"\n{'='*60}")
print("2️⃣  AUTOGRAD — Diferenciación automática")
print("=" * 60)

x = torch.tensor([2.0], requires_grad=True)
y = x**3 + 2*x   # y = x³ + 2x
y.backward()       # dy/dx = 3x² + 2
print(f"  f(x) = x³ + 2x")
print(f"  f(2) = {y.item()}")
print(f"  f'(2) = 3·4 + 2 = 14 → autograd: {x.grad.item()}")

# torch.no_grad() — para inferencia (ahorra memoria)
with torch.no_grad():
    z = x * 2
    print(f"\n  Con no_grad: z.requires_grad = {z.requires_grad}")

print(f"\n{'='*60}")
print("3️⃣  nn.Module — Pensar en Bloques")
print("=" * 60)

class MiRed(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.bn1 = nn.BatchNorm1d(hidden_dim)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.3)
        self.fc2 = nn.Linear(hidden_dim, output_dim)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        return x

model = MiRed(784, 256, 10)
total_params = sum(p.numel() for p in model.parameters())
trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"  Modelo: {model.__class__.__name__}")
print(f"  Parámetros totales: {total_params:,}")
print(f"  Parámetros entrenables: {trainable:,}")

# Listar parámetros
for name, param in model.named_parameters():
    print(f"    {name:20s}  shape={list(param.shape)}")

print(f"\n{'='*60}")
print("4️⃣  TRAINING LOOP — La estructura profesional")
print("=" * 60)

print("""
  El loop profesional:
  
  for epoch in range(epochs):
      model.train()                      # Modo entrenamiento
      for batch_x, batch_y in dataloader:
          optimizer.zero_grad()           # 1. Reset gradientes
          y_pred = model(batch_x)         # 2. Forward pass
          loss = criterion(y_pred, batch_y)  # 3. Calcular loss
          loss.backward()                 # 4. Backward pass
          torch.nn.utils.clip_grad_norm_( # 5. Gradient clipping
              model.parameters(), max_norm=1.0)
          optimizer.step()                # 6. Actualizar pesos
          scheduler.step()                # 7. Actualizar lr
      
      model.eval()                       # Modo evaluación
      with torch.no_grad():              # Sin gradientes
          val_loss = evaluate(model)
      
      # Checkpointing, early stopping, logging...
""")

print(f"\n{'='*60}")
print("5️⃣  OPTIMIZADORES")
print("=" * 60)

print("""
  ┌──────────────┬────────────────────────────────┬─────────────────┐
  │ Optimizer    │ Idea clave                      │ Cuándo usarlo   │
  ├──────────────┼────────────────────────────────┼─────────────────┤
  │ SGD          │ Gradiente puro                  │ Control total   │
  │ SGD+Momentum │ Acumula velocidad               │ SGD muy lento   │
  │ Adam         │ Momentum + lr adaptativo        │ Default seguro  │
  │ AdamW        │ Adam + weight decay desacoplado │ ESTÁNDAR ACTUAL │
  └──────────────┴────────────────────────────────┴─────────────────┘
  
  ⚠️ USA SIEMPRE AdamW por defecto.
""")

print("✅ Guía conceptual completada. → Ir a challenges/")

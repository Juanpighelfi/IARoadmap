"""
=============================================================================
🏆 CHALLENGE 3 (M1): Training Loop Profesional
=============================================================================
Implementa CADA técnica profesional: scheduler, gradient clipping,
checkpointing, early stopping, TensorBoard logging.
DURACIÓN: ~2h | DIFICULTAD: ⭐⭐⭐⭐

HINTS: Si te trabás, consultá modulo_1/hints/hint_challenge_3.md
=============================================================================
"""
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torch.optim.lr_scheduler import CosineAnnealingLR
import os, json, time

print("=" * 60)
print("🏆 M1-CHALLENGE 3: Training Loop Profesional")
print("=" * 60)

# --- TODO: Implementa EarlyStopping ---
class EarlyStopping:
    """
    TODO: Implementa early stopping.
    Para el entrenamiento si val_loss no mejora en `patience` epochs.
    
    Atributos: patience, min_delta, best_loss, counter, should_stop
    __call__(val_loss) → retorna True si debe parar
    """
    def __init__(self, patience=5, min_delta=0.001):
        pass  # Tu código aquí
    
    def __call__(self, val_loss):
        pass  # Tu código aquí

# --- TODO: Implementa el modelo ---
class ProfessionalDNN(nn.Module):
    """
    TODO: Red con capas: Linear → BN → ReLU → Dropout, repetidas.
    input_dim=784, hidden_dims=[512, 256, 128], num_classes=10
    """
    def __init__(self, input_dim=784, hidden_dims=[512, 256, 128],
                 num_classes=10, dropout=0.3):
        super().__init__()
        # TODO: Construye la red secuencial
        pass  # Tu código aquí
    
    def forward(self, x):
        pass  # Tu código aquí

# --- Config ---
CONFIG = {
    "batch_size": 128,
    "epochs": 15,
    "lr": 1e-3,
    "weight_decay": 1e-4,
    "hidden_dims": [512, 256, 128],
    "dropout": 0.3,
    "device": "cuda" if torch.cuda.is_available() else "cpu",
}
device = CONFIG["device"]

# --- Data ---
transform_train = transforms.Compose([
    transforms.RandomRotation(10),
    transforms.ToTensor(),
    transforms.Normalize((0.2860,), (0.3530,)),
])
transform_test = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.2860,), (0.3530,)),
])

print(f"\n  Descargando FashionMNIST...")
train_set = datasets.FashionMNIST('./data', train=True, download=True, transform=transform_train)
test_set = datasets.FashionMNIST('./data', train=False, download=True, transform=transform_test)

train_size = int(0.8 * len(train_set))
val_size = len(train_set) - train_size
train_set, val_set = torch.utils.data.random_split(train_set, [train_size, val_size])

train_loader = DataLoader(train_set, batch_size=CONFIG["batch_size"], shuffle=True)
val_loader = DataLoader(val_set, batch_size=CONFIG["batch_size"])
test_loader = DataLoader(test_set, batch_size=CONFIG["batch_size"])

# --- TODO: Training Loop Profesional ---
model = ProfessionalDNN().to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=CONFIG["lr"], weight_decay=CONFIG["weight_decay"])
criterion = nn.CrossEntropyLoss()
scheduler = CosineAnnealingLR(optimizer, T_max=CONFIG["epochs"])
early_stop = EarlyStopping(patience=5)

os.makedirs("checkpoints", exist_ok=True)
best_val_loss = float('inf')
history = {"train_loss": [], "val_loss": [], "train_acc": [], "val_acc": [], "lr": []}

print(f"  Device: {device}")
print(f"  Params: {sum(p.numel() for p in model.parameters()):,}")
print(f"\n  Entrenando {CONFIG['epochs']} epochs...")

"""
TODO: Implementa el training loop completo:
1. Para cada epoch:
   a) TRAIN: forward → loss → backward → clip_grad_norm_ → step
   b) VALIDATE: forward → loss (sin gradientes)
   c) scheduler.step()
   d) Guardar checkpoint si es el mejor val_loss
   e) Early stopping check
"""

for epoch in range(CONFIG["epochs"]):
    t0 = time.time()
    
    # --- TODO: TRAIN ---
    model.train()
    train_loss, train_correct, train_total = 0, 0, 0
    for batch_x, batch_y in train_loader:
        batch_x, batch_y = batch_x.to(device), batch_y.to(device)
        
        # TODO: zero_grad → forward → loss → backward → clip → step
        pass  # Tu código aquí
    
    # --- TODO: VALIDATE ---
    model.eval()
    val_loss, val_correct, val_total = 0, 0, 0
    with torch.no_grad():
        for batch_x, batch_y in val_loader:
            batch_x, batch_y = batch_x.to(device), batch_y.to(device)
            # TODO: forward → loss → acumular métricas
            pass  # Tu código aquí
    
    scheduler.step()
    
    # TODO: Calcular métricas, logging, checkpointing, early stopping
    elapsed = time.time() - t0
    # print(f"  Epoch {epoch+1:2d}/{CONFIG['epochs']} | ...")

print("\n✅ M1-Challenge 3 completado.")

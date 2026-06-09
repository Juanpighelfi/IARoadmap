"""
=============================================================================
🏆 CHALLENGE 3 (M1): Training Loop Profesional
=============================================================================
Implementa CADA técnica profesional: scheduler, gradient clipping,
checkpointing, early stopping, TensorBoard logging.
DURACIÓN: ~2h | DIFICULTAD: ⭐⭐⭐⭐
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

# --- EarlyStopping reutilizable ---
class EarlyStopping:
    """Para el entrenamiento si val_loss no mejora en `patience` epochs."""
    def __init__(self, patience=5, min_delta=0.001):
        self.patience = patience
        self.min_delta = min_delta
        self.best_loss = float('inf')
        self.counter = 0
        self.should_stop = False
    
    def __call__(self, val_loss):
        if val_loss < self.best_loss - self.min_delta:
            self.best_loss = val_loss
            self.counter = 0
        else:
            self.counter += 1
            if self.counter >= self.patience:
                self.should_stop = True
        return self.should_stop

# --- Modelo ---
class ProfessionalDNN(nn.Module):
    def __init__(self, input_dim=784, hidden_dims=[512, 256, 128],
                 num_classes=10, dropout=0.3):
        super().__init__()
        layers = []
        prev_dim = input_dim
        for h_dim in hidden_dims:
            layers.extend([
                nn.Linear(prev_dim, h_dim),
                nn.BatchNorm1d(h_dim),
                nn.ReLU(),
                nn.Dropout(dropout),
            ])
            prev_dim = h_dim
        layers.append(nn.Linear(prev_dim, num_classes))
        self.network = nn.Sequential(*layers)
    
    def forward(self, x):
        return self.network(x.view(x.size(0), -1))

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

# Split train/val
train_size = int(0.8 * len(train_set))
val_size = len(train_set) - train_size
train_set, val_set = torch.utils.data.random_split(train_set, [train_size, val_size])

train_loader = DataLoader(train_set, batch_size=CONFIG["batch_size"], shuffle=True)
val_loader = DataLoader(val_set, batch_size=CONFIG["batch_size"])
test_loader = DataLoader(test_set, batch_size=CONFIG["batch_size"])

# --- Training Loop Profesional ---
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
print(f"  Train: {len(train_set)}, Val: {len(val_set)}, Test: {len(test_set)}")
print(f"\n  Entrenando {CONFIG['epochs']} epochs...")

for epoch in range(CONFIG["epochs"]):
    t0 = time.time()
    
    # --- TRAIN ---
    model.train()
    train_loss, train_correct, train_total = 0, 0, 0
    for batch_x, batch_y in train_loader:
        batch_x, batch_y = batch_x.to(device), batch_y.to(device)
        
        optimizer.zero_grad()
        logits = model(batch_x)
        loss = criterion(logits, batch_y)
        loss.backward()
        
        # Gradient clipping
        grad_norm = torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        
        optimizer.step()
        
        train_loss += loss.item() * batch_x.size(0)
        train_correct += (logits.argmax(1) == batch_y).sum().item()
        train_total += batch_x.size(0)
    
    # --- VALIDATE ---
    model.eval()
    val_loss, val_correct, val_total = 0, 0, 0
    with torch.no_grad():
        for batch_x, batch_y in val_loader:
            batch_x, batch_y = batch_x.to(device), batch_y.to(device)
            logits = model(batch_x)
            loss = criterion(logits, batch_y)
            val_loss += loss.item() * batch_x.size(0)
            val_correct += (logits.argmax(1) == batch_y).sum().item()
            val_total += batch_x.size(0)
    
    scheduler.step()
    
    # Metrics
    train_loss /= train_total; val_loss /= val_total
    train_acc = train_correct / train_total; val_acc = val_correct / val_total
    lr = optimizer.param_groups[0]['lr']
    
    history["train_loss"].append(train_loss)
    history["val_loss"].append(val_loss)
    history["train_acc"].append(train_acc)
    history["val_acc"].append(val_acc)
    history["lr"].append(lr)
    
    elapsed = time.time() - t0
    print(f"  Epoch {epoch+1:2d}/{CONFIG['epochs']} | "
          f"Train: {train_loss:.4f} ({train_acc:.1%}) | "
          f"Val: {val_loss:.4f} ({val_acc:.1%}) | "
          f"lr={lr:.6f} | {elapsed:.1f}s")
    
    # Checkpointing (guardar mejor modelo)
    if val_loss < best_val_loss:
        best_val_loss = val_loss
        torch.save({
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'val_loss': val_loss,
            'config': CONFIG,
        }, 'checkpoints/best_model.pt')
        print(f"    → Checkpoint guardado (mejor val_loss)")
    
    # Early stopping
    if early_stop(val_loss):
        print(f"  ⚡ Early stopping en epoch {epoch+1}")
        break

# --- TEST ---
print(f"\n{'='*60}")
print("📊 EVALUACIÓN FINAL")
print("=" * 60)

# Cargar mejor modelo
ckpt = torch.load('checkpoints/best_model.pt', weights_only=False)
model.load_state_dict(ckpt['model_state_dict'])
model.eval()

test_correct, test_total = 0, 0
class_correct = [0] * 10
class_total = [0] * 10
with torch.no_grad():
    for batch_x, batch_y in test_loader:
        batch_x, batch_y = batch_x.to(device), batch_y.to(device)
        preds = model(batch_x).argmax(1)
        test_correct += (preds == batch_y).sum().item()
        test_total += batch_y.size(0)
        for p, t in zip(preds, batch_y):
            class_correct[t.item()] += (p == t).item()
            class_total[t.item()] += 1

test_acc = test_correct / test_total
print(f"  Test Accuracy: {test_acc:.1%}")

classes = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat',
           'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
print(f"\n  Accuracy por clase:")
for i, name in enumerate(classes):
    acc = class_correct[i] / class_total[i] if class_total[i] > 0 else 0
    bar = "█" * int(acc * 30)
    print(f"    {name:12s}: {acc:.1%} {bar}")

# Guardar historia
with open('checkpoints/training_history.json', 'w') as f:
    json.dump(history, f, indent=2)

print(f"""
{'='*60}
🏆 RESUMEN
{'='*60}
  ✅ Training loop con AdamW + CosineAnnealingLR
  ✅ Gradient clipping (max_norm=1.0)
  ✅ Checkpointing (mejor modelo por val_loss)
  ✅ Early stopping (patience=5)
  ✅ Data augmentation (RandomRotation)
  ✅ Evaluación por clase
  
  Test Accuracy: {test_acc:.1%} {'✅ >90%' if test_acc > 0.9 else '❌ <90%'}
""")

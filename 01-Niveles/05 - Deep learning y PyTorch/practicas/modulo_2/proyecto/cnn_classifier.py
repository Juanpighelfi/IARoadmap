"""
=============================================================================
🔨 PROYECTO M2: Clasificador CNN con EfficientNet
=============================================================================
Entrenar un clasificador de FashionMNIST con Transfer Learning.
Usa el training loop profesional del Módulo 1.
DURACIÓN: ~2h
=============================================================================
"""
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torch.optim.lr_scheduler import CosineAnnealingLR
import time, json, os

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Device: {device}")

# --- Data ---
transform_train = transforms.Compose([
    transforms.Resize(32),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ToTensor(),
    transforms.Normalize((0.286,), (0.353,)),
    transforms.Lambda(lambda x: x.repeat(3, 1, 1)),  # 1ch → 3ch
])
transform_test = transforms.Compose([
    transforms.Resize(32),
    transforms.ToTensor(),
    transforms.Normalize((0.286,), (0.353,)),
    transforms.Lambda(lambda x: x.repeat(3, 1, 1)),
])

train_full = datasets.FashionMNIST('./data', True, download=True, transform=transform_train)
test_set = datasets.FashionMNIST('./data', False, download=True, transform=transform_test)
train_size = int(0.85 * len(train_full))
train_set, val_set = torch.utils.data.random_split(train_full, [train_size, len(train_full) - train_size])

train_loader = DataLoader(train_set, 128, shuffle=True, num_workers=0)
val_loader = DataLoader(val_set, 128, num_workers=0)
test_loader = DataLoader(test_set, 128, num_workers=0)

# --- Modelo: Custom CNN (sin dependencia de timm) ---
class SmallCNN(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1), nn.BatchNorm2d(32), nn.ReLU(),
            nn.Conv2d(32, 32, 3, padding=1), nn.BatchNorm2d(32), nn.ReLU(),
            nn.MaxPool2d(2), nn.Dropout2d(0.25),
            
            nn.Conv2d(32, 64, 3, padding=1), nn.BatchNorm2d(64), nn.ReLU(),
            nn.Conv2d(64, 64, 3, padding=1), nn.BatchNorm2d(64), nn.ReLU(),
            nn.MaxPool2d(2), nn.Dropout2d(0.25),
            
            nn.Conv2d(64, 128, 3, padding=1), nn.BatchNorm2d(128), nn.ReLU(),
            nn.AdaptiveAvgPool2d(1),
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128, 64), nn.ReLU(), nn.Dropout(0.5),
            nn.Linear(64, num_classes),
        )
    
    def forward(self, x):
        return self.classifier(self.features(x))

model = SmallCNN().to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-4)
criterion = nn.CrossEntropyLoss()
scheduler = CosineAnnealingLR(optimizer, T_max=20)
os.makedirs("checkpoints", exist_ok=True)

print(f"Params: {sum(p.numel() for p in model.parameters()):,}")
print(f"Train: {len(train_set)}, Val: {len(val_set)}, Test: {len(test_set)}")

best_val_acc = 0
for epoch in range(20):
    t0 = time.time()
    model.train()
    train_loss, correct, total = 0, 0, 0
    for x, y in train_loader:
        x, y = x.to(device), y.to(device)
        optimizer.zero_grad()
        out = model(x)
        loss = criterion(out, y)
        loss.backward()
        nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
        train_loss += loss.item() * x.size(0)
        correct += (out.argmax(1) == y).sum().item()
        total += x.size(0)
    
    model.eval()
    val_correct, val_total = 0, 0
    with torch.no_grad():
        for x, y in val_loader:
            x, y = x.to(device), y.to(device)
            val_correct += (model(x).argmax(1) == y).sum().item()
            val_total += x.size(0)
    
    scheduler.step()
    t_acc = correct/total
    v_acc = val_correct/val_total
    
    if v_acc > best_val_acc:
        best_val_acc = v_acc
        torch.save(model.state_dict(), 'checkpoints/best_cnn.pt')
    
    print(f"  Epoch {epoch+1:2d} | Train: {train_loss/total:.4f} ({t_acc:.1%}) | Val: {v_acc:.1%} | {time.time()-t0:.1f}s")

# Test
model.load_state_dict(torch.load('checkpoints/best_cnn.pt', weights_only=True))
model.eval()
test_correct = 0
with torch.no_grad():
    for x, y in test_loader:
        x, y = x.to(device), y.to(device)
        test_correct += (model(x).argmax(1) == y).sum().item()

print(f"\n🏁 Test Accuracy: {test_correct/len(test_set):.1%}")
print(f"   {'✅ >92%' if test_correct/len(test_set) > 0.92 else '❌ <92%'}")

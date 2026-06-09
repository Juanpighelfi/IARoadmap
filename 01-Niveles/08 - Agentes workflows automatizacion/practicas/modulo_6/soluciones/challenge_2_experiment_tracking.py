"""
=============================================================================
M6-CHALLENGE 2: Experiment Tracking con MLflow
=============================================================================
Logear hiperparametros, metricas, y modelos. Comparar runs.
DURACION: ~1h | DIFICULTAD: 2/5
=============================================================================
"""
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import time, os

print("=" * 60)
print("M6-CHALLENGE 2: Experiment Tracking")
print("=" * 60)

try:
    import mlflow
    HAS_MLFLOW = True
    print(f"  MLflow version: {mlflow.__version__}")
except ImportError:
    HAS_MLFLOW = False
    print("  pip install mlflow")
    print("  Continuando con tracking manual...\n")


# --- Simple classifier ---
class SimpleNet(nn.Module):
    def __init__(self, hidden_dim=128, dropout=0.3):
        super().__init__()
        self.net = nn.Sequential(
            nn.Flatten(),
            nn.Linear(784, hidden_dim), nn.BatchNorm1d(hidden_dim), nn.ReLU(), nn.Dropout(dropout),
            nn.Linear(hidden_dim, 10),
        )
    def forward(self, x): return self.net(x)


def train_and_log(hidden_dim, lr, dropout, epochs=5):
    """Entrena un modelo y logea los resultados."""
    
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.286,), (0.353,))])
    train_ds = datasets.FashionMNIST('./data', True, download=True, transform=transform)
    test_ds = datasets.FashionMNIST('./data', False, download=True, transform=transform)
    # Subset for speed
    train_ds = torch.utils.data.Subset(train_ds, range(5000))
    test_ds = torch.utils.data.Subset(test_ds, range(1000))
    train_loader = DataLoader(train_ds, 128, shuffle=True)
    test_loader = DataLoader(test_ds, 128)
    
    model = SimpleNet(hidden_dim, dropout)
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()
    
    config = {"hidden_dim": hidden_dim, "lr": lr, "dropout": dropout, "epochs": epochs}
    
    # Train
    for epoch in range(epochs):
        model.train()
        for x, y in train_loader:
            optimizer.zero_grad()
            loss = criterion(model(x), y)
            loss.backward()
            optimizer.step()
    
    # Evaluate
    model.eval()
    correct = 0
    total_loss = 0
    with torch.no_grad():
        for x, y in test_loader:
            out = model(x)
            total_loss += criterion(out, y).item() * x.size(0)
            correct += (out.argmax(1) == y).sum().item()
    
    test_acc = correct / len(test_ds)
    test_loss = total_loss / len(test_ds)
    
    return config, test_acc, test_loss, model


# --- Run experiments ---
experiments = [
    {"hidden_dim": 64,  "lr": 1e-3, "dropout": 0.2},
    {"hidden_dim": 128, "lr": 1e-3, "dropout": 0.3},
    {"hidden_dim": 256, "lr": 5e-4, "dropout": 0.4},
]

results = []
for i, params in enumerate(experiments):
    print(f"\n  Run {i+1}/{len(experiments)}: {params}")
    t0 = time.time()
    
    if HAS_MLFLOW:
        mlflow.set_experiment("FashionMNIST_DNN")
        with mlflow.start_run(run_name=f"run_{i+1}"):
            config, acc, loss, model = train_and_log(**params)
            mlflow.log_params(config)
            mlflow.log_metric("test_accuracy", acc)
            mlflow.log_metric("test_loss", loss)
            # mlflow.pytorch.log_model(model, "model")  # Uncomment to save model
            print(f"    Logged to MLflow: acc={acc:.1%}, loss={loss:.4f}")
    else:
        config, acc, loss, model = train_and_log(**params)
        print(f"    Results: acc={acc:.1%}, loss={loss:.4f}")
    
    elapsed = time.time() - t0
    results.append({**config, "acc": acc, "loss": loss, "time": elapsed})

# --- Comparison ---
print(f"\n{'='*60}")
print("COMPARACION DE EXPERIMENTOS")
print("=" * 60)
print(f"  {'Run':>4s} | {'Hidden':>7s} | {'LR':>8s} | {'Dropout':>8s} | {'Acc':>7s} | {'Loss':>7s} | {'Time':>5s}")
print(f"  {'-'*4} | {'-'*7} | {'-'*8} | {'-'*8} | {'-'*7} | {'-'*7} | {'-'*5}")
for i, r in enumerate(results):
    best = " <-- MEJOR" if r['acc'] == max(x['acc'] for x in results) else ""
    print(f"  {i+1:4d} | {r['hidden_dim']:7d} | {r['lr']:8.5f} | {r['dropout']:8.2f} | {r['acc']:6.1%} | {r['loss']:7.4f} | {r['time']:4.1f}s{best}")

if HAS_MLFLOW:
    print(f"\n  Para ver el dashboard: mlflow ui")
    print(f"  Luego abrir: http://localhost:5000")

print("\nM6-Challenge 2 completado.")

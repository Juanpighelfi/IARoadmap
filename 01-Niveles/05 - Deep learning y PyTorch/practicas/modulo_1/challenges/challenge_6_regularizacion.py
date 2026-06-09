"""
=============================================================================
🏆 M1-CHALLENGE 6: Regularización Comparativa
=============================================================================
Demuestra experimentalmente el efecto de CADA técnica de regularización.

DURACIÓN: ~1h | DIFICULTAD: ⭐⭐⭐

HINTS: Si te trabás, consultá modulo_1/hints/hint_challenge_6.md
=============================================================================
"""
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Subset
from torchvision import datasets, transforms
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 60)
print("🏆 M1-CHALLENGE 6: Regularización Comparativa")
print("=" * 60)

# --- Dataset PEQUEÑO para forzar overfitting ---
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.286,), (0.353,))])
full_train = datasets.FashionMNIST('./data', True, download=True, transform=transform)
test_set = datasets.FashionMNIST('./data', False, download=True, transform=transform)

# Solo 500 muestras para overfitting fácil
np.random.seed(42)
small_indices = np.random.choice(len(full_train), 500, replace=False)
small_train = Subset(full_train, small_indices)

train_loader = DataLoader(small_train, batch_size=64, shuffle=True)
test_loader = DataLoader(test_set, batch_size=256)


# --- TODO: Define modelos con diferentes niveles de regularización ---

"""
Experimentar en este orden:
1. BASELINE: Sin regularización (solo Linear + ReLU)
2. + Dropout
3. + Weight Decay (L2)
4. + BatchNorm
5. + Data Augmentation
6. FULL: Todo combinado
"""

def create_model(use_dropout=False, use_batchnorm=False, dropout_rate=0.3):
    """
    TODO: Crea un modelo con las opciones de regularización indicadas.
    Arquitectura base: Linear(784→256) → [BN?] → ReLU → [Dropout?] → Linear(256→10)
    """
    layers = [nn.Flatten()]
    
    # TODO: Agrega Linear(784, 256)
    # TODO: Si use_batchnorm, agrega BatchNorm1d(256)
    # TODO: Agrega ReLU
    # TODO: Si use_dropout, agrega Dropout(dropout_rate)
    # TODO: Agrega Linear(256, 10)
    
    pass  # Tu código aquí
    return nn.Sequential(*layers)


def train_and_evaluate(model, train_loader, test_loader, optimizer, epochs=100):
    """Entrena y retorna historias de train/test accuracy."""
    criterion = nn.CrossEntropyLoss()
    train_accs = []
    test_accs = []
    
    for epoch in range(epochs):
        # TODO: Train
        model.train()
        correct_train = 0
        total_train = 0
        for x, y_batch in train_loader:
            # TODO: forward → loss → backward → step
            pass  # Tu código aquí
        
        # TODO: Evaluate
        model.eval()
        correct_test = 0
        total_test = 0
        with torch.no_grad():
            for x, y_batch in test_loader:
                pass  # Tu código aquí
        
        train_accs.append(correct_train / total_train if total_train > 0 else 0)
        test_accs.append(correct_test / total_test if total_test > 0 else 0)
    
    return train_accs, test_accs


# --- TODO: Entrena cada configuración y compara ---
configs = {
    "Baseline (sin regularización)": {"use_dropout": False, "use_batchnorm": False, "wd": 0},
    "+ Dropout(0.5)": {"use_dropout": True, "use_batchnorm": False, "wd": 0},
    "+ Weight Decay (L2)": {"use_dropout": False, "use_batchnorm": False, "wd": 1e-3},
    "+ BatchNorm": {"use_dropout": False, "use_batchnorm": True, "wd": 0},
    "FULL (todo)": {"use_dropout": True, "use_batchnorm": True, "wd": 1e-4},
}

results = {}
for name, cfg in configs.items():
    print(f"\n  Entrenando: {name}")
    model = create_model(use_dropout=cfg["use_dropout"], use_batchnorm=cfg["use_batchnorm"])
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=cfg["wd"])
    train_accs, test_accs = train_and_evaluate(model, train_loader, test_loader, optimizer, epochs=80)
    results[name] = {"train": train_accs, "test": test_accs}
    gap = train_accs[-1] - test_accs[-1]
    print(f"    Train: {train_accs[-1]:.1%}, Test: {test_accs[-1]:.1%}, Gap: {gap:.1%}")


# --- Visualizar ---
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
colors = ['#F44336', '#FF9800', '#2196F3', '#4CAF50', '#9C27B0']

for idx, (name, r) in enumerate(results.items()):
    axes[0].plot(r["train"], color=colors[idx], linewidth=2, label=name)
    axes[1].plot(r["test"], color=colors[idx], linewidth=2, label=name)

axes[0].set_title('Train Accuracy', fontweight='bold'); axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Accuracy'); axes[0].legend(fontsize=8); axes[0].set_ylim(0, 1.05)

axes[1].set_title('Test Accuracy', fontweight='bold'); axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Accuracy'); axes[1].legend(fontsize=8); axes[1].set_ylim(0, 1.05)

plt.suptitle('Efecto de la Regularización (500 muestras de training)', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('challenges/m1_ch6_regularization.png', dpi=100, bbox_inches='tight')
plt.close()


# --- Tabla resumen ---
print(f"\n{'=' * 60}")
print("TABLA RESUMEN")
print("=" * 60)
print(f"  {'Configuración':40s} | {'Train':>6s} | {'Test':>6s} | {'Gap':>5s} | {'Overfit?':>8s}")
print(f"  {'-'*40} | {'-'*6} | {'-'*6} | {'-'*5} | {'-'*8}")
for name, r in results.items():
    train_final = r["train"][-1]
    test_final = r["test"][-1]
    gap = train_final - test_final
    overfit = "SÍ ❌" if gap > 0.15 else "POCO ⚠️" if gap > 0.05 else "NO ✅"
    print(f"  {name:40s} | {train_final:5.1%} | {test_final:5.1%} | {gap:4.1%} | {overfit}")


print(f"""
{'=' * 60}
🧠 REFLEXIÓN
{'=' * 60}

1. ¿Cuál configuración tiene MENOR gap entre train y test?

2. ¿Dropout y weight decay se superponen o son complementarios?

3. ¿BatchNorm es regularización o no?

4. ¿Data augmentation es siempre gratis?

✅ M1-Challenge 6 completado.
""")

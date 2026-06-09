"""
=============================================================================
🏆 M1-CHALLENGE 4: Evaluación de Modelos — Métricas que Importan
=============================================================================
Las métricas correctas son la diferencia entre "mi modelo anda bien" y
"mi modelo resuelve el problema del negocio".

DURACIÓN: ~1.5h | DIFICULTAD: ⭐⭐⭐

CONCEPTO: Accuracy es INSUFICIENTE. Un modelo con 99% accuracy que predice
"no fraude" para todo es inútil si 1% de los datos son fraude.

HINTS: Si te trabás, consultá modulo_1/hints/hint_challenge_4.md
=============================================================================
"""
import torch
import torch.nn as nn
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

print("=" * 60)
print("🏆 M1-CHALLENGE 4: Métricas de Evaluación")
print("=" * 60)

# --- SETUP: Modelo entrenado + predicciones ---
class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Flatten(),
            nn.Linear(784, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.3),
            nn.Linear(256, 128), nn.BatchNorm1d(128), nn.ReLU(), nn.Dropout(0.3),
            nn.Linear(128, 10),
        )
    def forward(self, x): return self.net(x)

# Datos
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.286,), (0.353,))])
test_ds = datasets.FashionMNIST('./data', train=False, download=True, transform=transform)
test_loader = DataLoader(test_ds, batch_size=256)

CLASSES = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat',
           'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Generar predicciones (modelo sin entrenar → habrá errores interesantes)
model = SimpleNet()
model.eval()

all_preds = []
all_labels = []
all_probs = []

with torch.no_grad():
    for x, y in test_loader:
        logits = model(x)
        probs = torch.softmax(logits, dim=1)
        preds = logits.argmax(dim=1)
        all_preds.extend(preds.numpy())
        all_labels.extend(y.numpy())
        all_probs.extend(probs.numpy())

all_preds = np.array(all_preds)
all_labels = np.array(all_labels)
all_probs = np.array(all_probs)

print(f"  {len(all_preds)} predicciones generadas")
print(f"  Accuracy global: {np.mean(all_preds == all_labels)*100:.1f}%")


# =============================================================================
# PARTE 1: Confusion Matrix
# =============================================================================
"""
TODO: Implementa una confusion matrix desde cero (sin sklearn).

La confusion matrix M tiene:
  M[i, j] = cantidad de muestras de clase i predichas como clase j
  
  Diagonal (M[i,i]) = predicciones correctas
  Fuera de diagonal = errores

Esto te muestra CUÁLES clases confunde el modelo.
"""

print(f"\n{'=' * 60}")
print("PARTE 1: Confusion Matrix")
print("=" * 60)

def confusion_matrix_manual(y_true, y_pred, n_classes):
    """
    TODO: Implementa confusion matrix.
    1. Crea una matriz de zeros (n_classes, n_classes)
    2. Para cada par (true, pred), incrementa cm[true, pred]
    """
    cm = np.zeros((n_classes, n_classes), dtype=int)
    # TODO: Tu código aquí
    return cm

cm = confusion_matrix_manual(all_labels, all_preds, 10)

# Visualizar
fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(cm, cmap='Blues')
ax.set_xticks(range(10)); ax.set_xticklabels(CLASSES, rotation=45, ha='right', fontsize=9)
ax.set_yticks(range(10)); ax.set_yticklabels(CLASSES, fontsize=9)
ax.set_xlabel('Predicción', fontsize=12); ax.set_ylabel('Real', fontsize=12)
ax.set_title('Confusion Matrix — FashionMNIST', fontweight='bold', fontsize=14)

for i in range(10):
    for j in range(10):
        color = 'white' if cm[i, j] > cm.max() * 0.5 else 'black'
        ax.text(j, i, str(cm[i, j]), ha='center', va='center', fontsize=8, color=color)

plt.colorbar(im, ax=ax, shrink=0.8)
plt.tight_layout()
plt.savefig('challenges/m1_ch4_confusion.png', dpi=100, bbox_inches='tight')
plt.close()
print("  Confusion matrix guardada.")


# =============================================================================
# PARTE 2: Precision, Recall, F1 — Por clase
# =============================================================================
"""
TODO: Calcula precision, recall, F1 para CADA clase.

Definiciones (para cada clase c):
  TP = verdaderos positivos (predicción=c Y real=c)
  FP = falsos positivos (predicción=c PERO real≠c)  → "falsa alarma"
  FN = falsos negativos (predicción≠c PERO real=c)  → "se me escapó"

  Precision = TP / (TP + FP)  → "de los que dije c, ¿cuántos realmente eran c?"
  Recall    = TP / (TP + FN)  → "de los que realmente eran c, ¿cuántos encontré?"
  F1        = 2 * (P * R) / (P + R)  → media armónica (penaliza desbalances)
"""

print(f"\n{'=' * 60}")
print("PARTE 2: Precision, Recall, F1 por Clase")
print("=" * 60)

def per_class_metrics(cm):
    """
    TODO: Calcula precision, recall, F1 para cada clase.
    
    TP[i] = cm[i, i]                    (diagonal)
    FP[i] = sum(cm[:, i]) - cm[i, i]   (columna i menos diagonal)
    FN[i] = sum(cm[i, :]) - cm[i, i]   (fila i menos diagonal)
    """
    n_classes = cm.shape[0]
    precision = np.zeros(n_classes)
    recall = np.zeros(n_classes)
    f1 = np.zeros(n_classes)
    
    for i in range(n_classes):
        tp = ...  # Tu código aquí
        fp = ...  # Tu código aquí
        fn = ...  # Tu código aquí
        
        precision[i] = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall[i] = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1[i] = 2 * precision[i] * recall[i] / (precision[i] + recall[i]) if (precision[i] + recall[i]) > 0 else 0
    
    return precision, recall, f1

precision, recall, f1 = per_class_metrics(cm)

print(f"\n  {'Clase':15s} | {'Precision':>10s} | {'Recall':>8s} | {'F1':>6s} | {'Support':>8s}")
print(f"  {'-'*15} | {'-'*10} | {'-'*8} | {'-'*6} | {'-'*8}")
for i in range(10):
    support = sum(all_labels == i)
    print(f"  {CLASSES[i]:15s} | {precision[i]:10.3f} | {recall[i]:8.3f} | {f1[i]:6.3f} | {support:8d}")

macro_f1 = np.mean(f1)
weighted_f1 = np.average(f1, weights=[sum(all_labels == i) for i in range(10)])
print(f"\n  Macro F1:    {macro_f1:.3f}")
print(f"  Weighted F1: {weighted_f1:.3f}")

# Visualizar
fig, ax = plt.subplots(figsize=(12, 5))
x_pos = np.arange(10)
width = 0.25
ax.bar(x_pos - width, precision, width, label='Precision', color='#2196F3', alpha=0.8)
ax.bar(x_pos, recall, width, label='Recall', color='#FF5722', alpha=0.8)
ax.bar(x_pos + width, f1, width, label='F1', color='#4CAF50', alpha=0.8)
ax.set_xticks(x_pos); ax.set_xticklabels(CLASSES, rotation=45, ha='right')
ax.set_ylabel('Score'); ax.set_title('Métricas por Clase', fontweight='bold')
ax.legend(); ax.set_ylim(0, 1)
plt.tight_layout()
plt.savefig('challenges/m1_ch4_metrics.png', dpi=100, bbox_inches='tight')
plt.close()


# =============================================================================
# PARTE 3: Curva ROC y AUC (One-vs-Rest)
# =============================================================================
"""
TODO: Calcula la curva ROC para una clase específica (One-vs-Rest).

La curva ROC grafica TPR vs FPR para diferentes umbrales:
  TPR (True Positive Rate) = TP / (TP + FN) = Recall
  FPR (False Positive Rate) = FP / (FP + TN)

AUC = Área bajo la curva (1.0 = perfecto, 0.5 = aleatorio)
"""

print(f"\n{'=' * 60}")
print("PARTE 3: Curva ROC (One-vs-Rest)")
print("=" * 60)

def roc_curve_manual(y_true_binary, scores, n_thresholds=200):
    """
    TODO: Calcula la curva ROC.
    1. Para cada umbral t (de 0 a 1):
       - pred_positive = scores >= t
       - TP = sum(pred_positive & y_true_binary)
       - FP = sum(pred_positive & ~y_true_binary)
       - TPR = TP / total_positives
       - FPR = FP / total_negatives
    """
    thresholds = np.linspace(1, 0, n_thresholds)
    tprs = []
    fprs = []
    
    total_pos = np.sum(y_true_binary)
    total_neg = len(y_true_binary) - total_pos
    
    for t in thresholds:
        # TODO: Tu código aquí
        pass
    
    return np.array(fprs), np.array(tprs), thresholds

def auc_manual(fprs, tprs):
    """TODO: Calcula AUC con la regla del trapecio (np.trapz)."""
    pass  # Tu código aquí

# Calcular ROC para 3 clases de ejemplo
fig, ax = plt.subplots(figsize=(8, 8))
colors = ['#2196F3', '#FF5722', '#4CAF50']

for idx, class_id in enumerate([0, 6, 8]):  # T-shirt, Shirt, Bag
    y_binary = (all_labels == class_id).astype(int)
    scores = all_probs[:, class_id]
    
    fprs, tprs, _ = roc_curve_manual(y_binary, scores)
    auc_val = auc_manual(fprs, tprs)
    
    ax.plot(fprs, tprs, linewidth=2, color=colors[idx],
            label=f'{CLASSES[class_id]} (AUC={auc_val:.3f})')

ax.plot([0, 1], [0, 1], 'k--', linewidth=1, alpha=0.5, label='Random (AUC=0.5)')
ax.set_xlabel('False Positive Rate', fontsize=12)
ax.set_ylabel('True Positive Rate', fontsize=12)
ax.set_title('Curva ROC (One-vs-Rest)', fontweight='bold', fontsize=14)
ax.legend(fontsize=11)
ax.set_aspect('equal')
plt.tight_layout()
plt.savefig('challenges/m1_ch4_roc.png', dpi=100, bbox_inches='tight')
plt.close()


# =============================================================================
# PARTE 4: Calibración de Probabilidades
# =============================================================================
"""
¿Tu modelo dice "80% de confianza"? ¿Realmente acierta el 80% de las veces
que dice 80%?

TODO: Crea un diagrama de calibración (reliability diagram).
1. Agrupa las predicciones por bins de confianza (0-0.1, 0.1-0.2, ...)
2. Para cada bin, calcula la accuracy real
3. Compara: predicción de confianza vs accuracy observada
"""

print(f"\n{'=' * 60}")
print("PARTE 4: Calibración de Probabilidades")
print("=" * 60)

def calibration_curve(y_true, y_pred_probs, n_bins=10):
    """TODO: Calcula la curva de calibración."""
    bin_edges = np.linspace(0, 1, n_bins + 1)
    bin_accs = []
    bin_confs = []
    bin_counts = []
    
    max_probs = np.max(y_pred_probs, axis=1)
    preds = np.argmax(y_pred_probs, axis=1)
    correct = (preds == y_true).astype(float)
    
    for i in range(n_bins):
        # TODO: Para cada bin, encuentra las muestras en ese rango de confianza
        # y calcula la accuracy real
        mask = (max_probs >= bin_edges[i]) & (max_probs < bin_edges[i+1])
        if mask.sum() > 0:
            bin_accs.append(correct[mask].mean())
            bin_confs.append(max_probs[mask].mean())
            bin_counts.append(mask.sum())
    
    return np.array(bin_confs), np.array(bin_accs), np.array(bin_counts)

confs, accs, counts = calibration_curve(all_labels, all_probs)

# Expected Calibration Error (ECE)
# TODO: ECE = Σ (|accuracy_bin - confidence_bin| * n_bin / N)
ece = ...  # Tu código aquí

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].bar(confs, accs, width=0.08, alpha=0.7, color='#2196F3', edgecolor='white', label='Real')
axes[0].plot([0, 1], [0, 1], 'r--', linewidth=2, label='Perfecta calibración')
axes[0].set_xlabel('Confianza predicha'); axes[0].set_ylabel('Accuracy observada')
axes[0].set_title(f'Diagrama de Calibración (ECE={ece:.3f})', fontweight='bold')
axes[0].legend()

axes[1].bar(confs, counts, width=0.08, alpha=0.7, color='#4CAF50', edgecolor='white')
axes[1].set_xlabel('Confianza predicha'); axes[1].set_ylabel('Cantidad de muestras')
axes[1].set_title('Distribución de Confianza', fontweight='bold')

plt.tight_layout()
plt.savefig('challenges/m1_ch4_calibration.png', dpi=100, bbox_inches='tight')
plt.close()


# =============================================================================
# REFLEXIÓN
# =============================================================================
print(f"""
{'=' * 60}
🧠 REFLEXIÓN
{'=' * 60}

1. ¿Cuándo es más importante precision vs recall?

2. ¿Accuracy es suficiente con clases desbalanceadas?

3. ¿Macro F1 vs Weighted F1 — cuándo usar cada uno?

4. ¿Qué pasa si el modelo tiene buen AUC pero mala calibración?

✅ M1-Challenge 4 completado.
""")

"""
=============================================================================
🏆 M1-CHALLENGE 5: Debugging de Training — "¿Por qué no converge?"
=============================================================================
Diagnosticar y arreglar 5 redes rotas con bugs REALES.

DURACIÓN: ~1.5h | DIFICULTAD: ⭐⭐⭐⭐

CONCEPTO: El 80% del tiempo de un ML Engineer es debugging.
          Este challenge simula problemas reales que vas a encontrar.

HINTS: Si te trabás, consultá modulo_1/hints/hint_challenge_5.md
=============================================================================
"""
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
import numpy as np

print("=" * 60)
print("🏆 M1-CHALLENGE 5: Debugging de Training")
print("=" * 60)

# Dataset simple para todos los bugs
np.random.seed(42)
X = torch.randn(1000, 20)
y = (X[:, 0] + X[:, 1] > 0).long()  # Clasificación binaria simple
dataset = TensorDataset(X, y)
loader = DataLoader(dataset, batch_size=64, shuffle=True)

def train_and_report(model, loader, criterion, optimizer, epochs=50, label=""):
    """Entrena y reporta."""
    model.train()
    for e in range(epochs):
        total_loss = 0
        correct = 0
        total = 0
        for xb, yb in loader:
            optimizer.zero_grad()
            out = model(xb)
            loss = criterion(out, yb)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
            correct += (out.argmax(1) == yb).sum().item()
            total += len(yb)
        if e % 10 == 0 or e == epochs - 1:
            print(f"  [{label}] Epoch {e:3d}: loss={total_loss/len(loader):.4f}, acc={correct/total:.1%}")
    return correct / total


# =============================================================================
# BUG 1: Softmax + CrossEntropyLoss (el clásico)
# =============================================================================
"""
TODO: Encuentra y arregla el bug.
PISTA: CrossEntropyLoss ya aplica softmax internamente (LogSoftmax + NLLLoss).
       Si aplicas Softmax en el forward, ¡la aplicas DOBLE!
"""

print(f"\n{'=' * 60}")
print("BUG 1: 'Mi modelo no aprende nada'")
print("=" * 60)

class BuggyModel1(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(20, 64)
        self.fc2 = nn.Linear(64, 2)
        self.softmax = nn.Softmax(dim=1)  # ← ¿Esto está bien?
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.softmax(self.fc2(x))  # ← ¿Y esto?
        return x

# TODO: Entrena el modelo buggy, observa que no converge, luego arréglalo
print("\n  ❌ Versión con bug:")
model_buggy = BuggyModel1()
train_and_report(model_buggy, loader, nn.CrossEntropyLoss(), 
                 torch.optim.Adam(model_buggy.parameters(), lr=1e-3), epochs=30, label="BUGGY")

# TODO: Crea FixedModel1 sin el bug
# class FixedModel1(nn.Module):
#     ...

print("\n  ✅ Versión corregida:")
# TODO: Entrena la versión corregida y verifica que converge


# =============================================================================
# BUG 2: Learning rate absurdo
# =============================================================================
"""
TODO: Experimenta con lr=10, lr=0.0000001, y lr=0.001
¿Cuál converge? ¿Cuál explota? ¿Cuál se queda estancado?
"""

print(f"\n{'=' * 60}")
print("BUG 2: 'La loss se vuelve NaN' o 'No baja'")
print("=" * 60)

class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(20, 64), nn.ReLU(),
            nn.Linear(64, 2),
        )
    def forward(self, x): return self.net(x)

for lr in [10.0, 0.0000001, 0.001]:
    model = SimpleModel()
    acc = train_and_report(model, loader, nn.CrossEntropyLoss(),
                          torch.optim.SGD(model.parameters(), lr=lr), 
                          epochs=30, label=f"lr={lr}")
    print(f"    → Final acc: {acc:.1%}\n")


# =============================================================================
# BUG 3: Sin normalización de datos
# =============================================================================
"""
TODO: Demuestra que datos sin normalizar causan problemas.
1. Crea datos con escala muy diferente (feature 0: ~1000, feature 1: ~0.001)
2. Entrena SIN normalizar → lento/inestable
3. Entrena CON normalizar → converge rápido
"""

print(f"\n{'=' * 60}")
print("BUG 3: 'Mi modelo converge muy lento'")
print("=" * 60)

# Datos con escala muy diferente
X_bad = X.clone()
X_bad[:, 0] *= 1000   # Feature 0 en miles
X_bad[:, 1] *= 0.001  # Feature 1 casi zero
ds_bad = TensorDataset(X_bad, y)
loader_bad = DataLoader(ds_bad, batch_size=64, shuffle=True)

print("\n  ❌ Sin normalización:")
m = SimpleModel()
train_and_report(m, loader_bad, nn.CrossEntropyLoss(),
                 torch.optim.Adam(m.parameters(), lr=1e-3), epochs=30, label="SIN NORM")

# TODO: Normaliza los datos y entrena de nuevo
# X_normalized = (X_bad - X_bad.mean(dim=0)) / (X_bad.std(dim=0) + 1e-8)
print("\n  ✅ Con normalización:")
# TODO: Tu código aquí


# =============================================================================
# BUG 4: Olvidarse de model.eval() y torch.no_grad()
# =============================================================================
"""
TODO: Demuestra que:
- Dropout activo en eval da resultados inconsistentes
- Sin no_grad(), la memoria se acumula
"""

print(f"\n{'=' * 60}")
print("BUG 4: 'Las predicciones cambian cada vez que las corro'")
print("=" * 60)

class ModelWithDropout(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(20, 64), nn.ReLU(), nn.Dropout(0.5),
            nn.Linear(64, 2),
        )
    def forward(self, x): return self.net(x)

model_d = ModelWithDropout()
test_x = torch.randn(1, 20)

# TODO: Sin model.eval() → predicciones varían
print("  Sin model.eval() (dropout ACTIVO):")
for i in range(5):
    out = model_d(test_x)
    print(f"    Run {i}: {out.detach().numpy().round(4)}")

# TODO: Con model.eval() → predicciones consistentes
model_d.eval()
print("\n  Con model.eval() (dropout DESACTIVADO):")
for i in range(5):
    with torch.no_grad():
        out = model_d(test_x)
    print(f"    Run {i}: {out.numpy().round(4)}")


# =============================================================================
# BUG 5: Gradient accumulation (se olvidan de zero_grad)
# =============================================================================
"""
TODO: Demuestra qué pasa cuando NO se llama optimizer.zero_grad().
"""

print(f"\n{'=' * 60}")
print("BUG 5: 'Mi modelo aprende raro, gradientes crecen sin parar'")
print("=" * 60)

# TODO: Entrena sin zero_grad y muestra que los gradientes acumulan
model_g = SimpleModel()
opt = torch.optim.SGD(model_g.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()

print("\n  Sin zero_grad:")
for i in range(5):
    xb, yb = next(iter(loader))
    # ⚠️ NO zero_grad!
    out = model_g(xb)
    loss = criterion(out, yb)
    loss.backward()
    grad_norm = model_g.net[0].weight.grad.norm().item()
    opt.step()
    print(f"    Step {i}: grad_norm = {grad_norm:.4f} ← ¡CRECE!")

print("\n  Con zero_grad:")
for i in range(5):
    xb, yb = next(iter(loader))
    opt.zero_grad()  # ✅
    out = model_g(xb)
    loss = criterion(out, yb)
    loss.backward()
    grad_norm = model_g.net[0].weight.grad.norm().item()
    opt.step()
    print(f"    Step {i}: grad_norm = {grad_norm:.4f} ← estable")


# =============================================================================
# REFLEXIÓN
# =============================================================================
print(f"""
{'=' * 60}
🧠 REFLEXIÓN
{'=' * 60}

CHECKLIST DE DEBUGGING (usalo SIEMPRE):

  □ ¿Los datos están normalizados?
  □ ¿El learning rate es razonable? (probar 1e-4 a 1e-2)
  □ ¿Estoy usando CrossEntropyLoss SIN softmax en el forward?
  □ ¿Llamo optimizer.zero_grad() ANTES de loss.backward()?
  □ ¿Llamo model.eval() para evaluación?
  □ ¿Uso torch.no_grad() para inferencia?
  □ ¿Las dimensiones de input/output son correctas?
  □ ¿Puedo overfittear un batch pequeño? (sanity check)

✅ M1-Challenge 5 completado.
""")

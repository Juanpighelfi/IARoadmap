"""
=============================================================================
🏆 M2 CHALLENGES: CNNs y Computer Vision
=============================================================================
Challenge 1: Convoluciones manuales + cálculo de dimensiones
Challenge 2: Transfer Learning con timm
Challenge 3: Data Augmentation como regularización
DURACIÓN: ~4.5h total | DIFICULTAD: ⭐⭐⭐
=============================================================================
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from torchvision import datasets, transforms

print("=" * 60)
print("🏆 M2-CHALLENGE 1: Convoluciones desde la Intuición")
print("=" * 60)

# Cargar una imagen de FashionMNIST
dataset = datasets.FashionMNIST('./data', train=True, download=True, transform=transforms.ToTensor())
image = dataset[0][0]  # Shape: (1, 28, 28)
print(f"  Imagen shape: {image.shape}")

# Definir kernels manualmente
kernels = {
    "Bordes Verticales": torch.tensor([[-1., 0., 1.],
                                        [-1., 0., 1.],
                                        [-1., 0., 1.]]),
    "Bordes Horizontales": torch.tensor([[-1., -1., -1.],
                                          [ 0.,  0.,  0.],
                                          [ 1.,  1.,  1.]]),
    "Sobel X": torch.tensor([[-1., 0., 1.],
                              [-2., 0., 2.],
                              [-1., 0., 1.]]),
    "Blur": torch.ones(3, 3) / 9.0,
}

fig, axes = plt.subplots(1, len(kernels) + 1, figsize=(3 * (len(kernels) + 1), 3))
axes[0].imshow(image.squeeze(), cmap='gray')
axes[0].set_title('Original'); axes[0].axis('off')

for idx, (name, kernel) in enumerate(kernels.items()):
    k = kernel.unsqueeze(0).unsqueeze(0)  # (1,1,3,3)
    result = F.conv2d(image.unsqueeze(0), k)
    axes[idx + 1].imshow(result.squeeze().detach(), cmap='gray')
    axes[idx + 1].set_title(name, fontsize=9); axes[idx + 1].axis('off')

plt.tight_layout()
plt.savefig('challenges/m2_ch1_kernels.png', dpi=100, bbox_inches='tight')
plt.close()
print("  Filtros aplicados. Guardado gráfico.")

# --- Cálculo de dimensiones ---
print(f"\n--- Cálculo de dimensiones de salida ---")
print(f"  Fórmula: out = (in + 2·padding - kernel_size) / stride + 1\n")

# Input: 64×64 con 3 canales (RGB)
specs = [
    ("Conv2d(3,32, k=5, s=2, p=2)", 64, 5, 2, 2, 32),
    ("MaxPool2d(2)",                 32, 2, 2, 0, 32),
    ("Conv2d(32,64, k=3, s=1, p=1)", 16, 3, 1, 1, 64),
    ("MaxPool2d(2)",                  16, 2, 2, 0, 64),
]

size = 64
for name, expected_in, k, s, p, c_out in specs:
    size = (size + 2*p - k) // s + 1
    print(f"  {name:40s} → {size}×{size}×{c_out}")

# Verificar con PyTorch
print(f"\n  Verificación PyTorch:")
x = torch.randn(1, 3, 64, 64)
x = nn.Conv2d(3, 32, 5, stride=2, padding=2)(x); print(f"  Conv1: {x.shape}")
x = nn.MaxPool2d(2)(x); print(f"  Pool1: {x.shape}")
x = nn.Conv2d(32, 64, 3, stride=1, padding=1)(x); print(f"  Conv2: {x.shape}")
x = nn.MaxPool2d(2)(x); print(f"  Pool2: {x.shape}")

print(f"\n{'='*60}")
print("🏆 M2-CHALLENGE 2: Transfer Learning")
print("=" * 60)

# Explorar modelos preentrenados con timm
try:
    import timm
    available = timm.list_models("*efficientnet_b0*")
    print(f"\n  Modelos EfficientNet disponibles: {len(available)}")
    
    model = timm.create_model('efficientnet_b0', pretrained=False, num_classes=10)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"  EfficientNet-B0 params: {total_params:,}")
    print(f"  Tamaño en memoria: ~{total_params * 4 / 1024 / 1024:.1f} MB (float32)")
    
    # Feature extraction: congelar backbone
    for param in model.parameters():
        param.requires_grad = False
    # Descongelar clasificador
    for param in model.classifier.parameters():
        param.requires_grad = True
    
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    frozen = total_params - trainable
    print(f"  Feature extraction: {trainable:,} entrenables, {frozen:,} congelados")
    print(f"  Ratio: {trainable/total_params*100:.2f}% entrenables")
except ImportError:
    print("  ⚠️ timm no instalado. pip install timm")

print(f"\n{'='*60}")
print("🏆 M2-CHALLENGE 3: Data Augmentation")
print("=" * 60)

# Visualizar augmentaciones
img_pil = datasets.FashionMNIST('./data', train=True, download=True)[0][0]

augmentations = transforms.Compose([
    transforms.RandomRotation(20),
    transforms.RandomAffine(degrees=0, translate=(0.1, 0.1)),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.ToTensor(),
])

fig, axes = plt.subplots(2, 4, figsize=(12, 6))
for i in range(8):
    ax = axes[i // 4, i % 4]
    augmented = augmentations(img_pil)
    ax.imshow(augmented.squeeze(), cmap='gray')
    ax.set_title(f'Aug {i+1}'); ax.axis('off')

plt.suptitle('Data Augmentation × 8', fontweight='bold')
plt.tight_layout()
plt.savefig('challenges/m2_ch3_augmentation.png', dpi=100, bbox_inches='tight')
plt.close()
print("  8 versiones augmentadas generadas. Guardado gráfico.")

print(f"""
{'='*60}
🧠 REFLEXIÓN
{'='*60}
  1. Las primeras capas detectan bordes → son UNIVERSALES
  2. Transfer learning: congela backbone + entrena clasificador
  3. Fine-tuning: descongela últimas N capas con lr pequeño
  4. Data augmentation = regularización implícita (más "datos" sin más datos)

✅ M2 Challenges completados.
""")

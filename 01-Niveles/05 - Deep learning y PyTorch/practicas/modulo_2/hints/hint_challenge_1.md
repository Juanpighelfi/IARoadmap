# 🔑 Hints — M2 Challenge 1: Convolutions

## Kernels
```python
"Bordes Verticales": torch.tensor([[-1., 0., 1.], [-1., 0., 1.], [-1., 0., 1.]]),
"Bordes Horizontales": torch.tensor([[-1., -1., -1.], [0., 0., 0.], [1., 1., 1.]]),
"Sobel X": torch.tensor([[-1., 0., 1.], [-2., 0., 2.], [-1., 0., 1.]]),
"Blur": torch.ones(3, 3) / 9.0,
```

## Cálculo de dimensiones
```python
size = (size + 2*p - k) // s + 1
```

## Transfer Learning
```python
for param in model.parameters():
    param.requires_grad = False
for param in model.classifier.parameters():
    param.requires_grad = True
```

## Data Augmentation
```python
augmentations = transforms.Compose([
    transforms.RandomRotation(20),
    transforms.RandomAffine(degrees=0, translate=(0.1, 0.1)),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.ToTensor(),
])
```

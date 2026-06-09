# 🧮 Módulo 0: Fundamentos Matemáticos Profundos

> **Hito de Carrera**: Leer papers sin "miedo" a la matemática.  
> **Prerrequisito**: [Módulo Previo (Python para ML)](../modulo_previo/) + MLCC completado

---

## 📋 Contenido

Este módulo cubre las 3 herramientas matemáticas esenciales para ML:

| Semana | Tema | Guía Conceptual | Challenges |
|--------|------|-----------------|------------|
| 1 | Álgebra Lineal | `conceptos/01_algebra_lineal_para_ml.py` | Challenges 1-3 |
| 2 | Cálculo y Gradientes | `conceptos/02_calculo_y_gradientes.py` | Challenges 4-6 |
| 3 | Probabilidad y Loss | `conceptos/03_probabilidad_y_loss.py` | Challenges 7-9 |
| Final | Proyecto Integrador | — | `proyecto/backprop_from_scratch.py` |

## 🚀 Cómo Usar

### Flujo recomendado por semana:

1. **Ver los videos** de 3Blue1Brown (ver plan de estudio)
2. **Ejecutar la guía conceptual** del tema:
   ```bash
   python conceptos/01_algebra_lineal_para_ml.py
   ```
3. **Completar los challenges** uno por uno:
   ```bash
   python challenges/challenge_1_matmul.py
   python challenges/challenge_2_pca_manual.py
   python challenges/challenge_3_transformaciones.py
   ```
4. **Crear flashcards** con lo aprendido

### Requisitos

```bash
pip install numpy matplotlib scipy scikit-learn
pip install torch  # Para challenges 5 y 6
```

## 📁 Estructura

```
modulo_0/
├── conceptos/                              ← Guías teórico-prácticas ejecutables
│   ├── 01_algebra_lineal_para_ml.py
│   ├── 02_calculo_y_gradientes.py
│   └── 03_probabilidad_y_loss.py
│
├── challenges/                             ← 9 desafíos code-along
│   ├── challenge_1_matmul.py               ← Matmul desde cero (3 enfoques)
│   ├── challenge_2_pca_manual.py           ← PCA con eigenvectores
│   ├── challenge_3_transformaciones.py     ← Visualización de transformaciones
│   ├── challenge_4_gradientes_manuales.py  ← Forward/backward a mano
│   ├── challenge_5_autograd_verify.py      ← Verificar con PyTorch autograd
│   ├── challenge_6_vanishing_gradient.py   ← Demostrar vanishing gradient
│   ├── challenge_7_cross_entropy.py        ← Implementar cross-entropy
│   ├── challenge_8_mse_vs_ce.py            ← MSE vs CE comparación
│   └── challenge_9_kl_divergence.py        ← KL divergence manual
│
├── proyecto/
│   └── backprop_from_scratch.py            ← Red neuronal completa con NumPy
│
├── linear_algebra_challenge1.py            ← Tu implementación original
├── test_all_challenges.py                  ← Script de verificación
└── README.md                              ← Este archivo
```

## 🏆 Criterios de Éxito

Al completar este módulo deberías poder:

- [ ] Explicar qué hace geométricamente W·x para cualquier matriz W
- [ ] Calcular gradientes a mano para una red simple
- [ ] Explicar por qué 20 sigmoids causan vanishing gradient
- [ ] Implementar cross-entropy y explicar por qué es mejor que MSE
- [ ] Implementar backpropagation desde cero y explicar cada línea
- [ ] Leer secciones matemáticas de papers sin bloqueo

> **Siguiente módulo**: [Módulo 1 — Redes Neuronales Profundas con PyTorch](../study_docs/plan_estudio_ml_parte2.md)

# 📚 Plan de Lectura de Papers — 1 Paper por Día (lunes a viernes)

> **Metodología**: Lee el Abstract + Intro + Figuras. Profundiza en la sección que más te interese. No intentes entender TODO — el objetivo es exposición progresiva.

---

## 🔴 Semana 1-2: Papers Fundacionales (OBLIGATORIOS)

Estos papers DEFINIERON el campo. Aunque son antiguos, la intuición sigue vigente.

| Día | Paper | Año | Concepto clave | Enlace |
|-----|-------|-----|----------------|--------|
| L1 | **Backpropagation** — Rumelhart et al. | 1986 | Regla de la cadena para entrenar redes | [PDF](https://www.nature.com/articles/323533a0) |
| M1 | **LeNet-5** — LeCun et al. | 1998 | Primera CNN práctica (dígitos) | [PDF](http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf) |
| X1 | **Dropout** — Srivastava et al. | 2014 | Regularización por apagado aleatorio | [arXiv](https://arxiv.org/abs/1207.0580) |
| J1 | **Adam Optimizer** — Kingma & Ba | 2015 | Momentum + learning rate adaptativo | [arXiv](https://arxiv.org/abs/1412.6980) |
| V1 | **Batch Normalization** — Ioffe & Szegedy | 2015 | Normalizar activaciones entre capas | [arXiv](https://arxiv.org/abs/1502.03167) |
| L2 | **ResNet** — He et al. | 2015 | Skip connections → redes de 152 capas | [arXiv](https://arxiv.org/abs/1512.03385) |
| M2 | **Attention Is All You Need** — Vaswani et al. | 2017 | EL paper más importante de la década | [arXiv](https://arxiv.org/abs/1706.03762) |
| X2 | **BERT** — Devlin et al. | 2019 | Encoder bidireccional preentrenado | [arXiv](https://arxiv.org/abs/1810.04805) |
| J2 | **GPT-2** — Radford et al. | 2019 | Language modeling unidireccional | [Paper](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) |
| V2 | **LoRA** — Hu et al. | 2021 | Fine-tuning eficiente con bajo rango | [arXiv](https://arxiv.org/abs/2106.09685) |

### Guía de lectura (para cada paper):
1. **Abstract** (2 min) — ¿Qué problema resuelve? ¿Cuál es la contribución?
2. **Figuras y tablas** (5 min) — Son el resumen visual del paper
3. **Intro + Related Work** (10 min) — Contexto y motivación
4. **Método** (15-30 min) — La carne del paper. Acá está la innovación
5. **Resultados** (5 min) — ¿Funciona? ¿Cuánto mejora?

---

## 🟡 Semana 3-4: Papers Modernos (2023-2026)

| Día | Paper | Año | Concepto clave | Enlace |
|-----|-------|-----|----------------|--------|
| L3 | **LLaMA 3 / LLaMA 2** — Meta AI | 23/24 | Evolución de LLMs open-source | [arXiv](https://arxiv.org/abs/2307.09288) |
| M3 | **Flash Attention 2 & 3** — Dao et al. | 23/24 | Attention O(N) ultra-rápida a nivel hardware | [arXiv](https://arxiv.org/abs/2307.08691) |
| X3 | **QLoRA** — Dettmers et al. | 2023 | LoRA + quantización 4-bit | [arXiv](https://arxiv.org/abs/2305.14314) |
| J3 | **Mamba / State Space Models** — Gu et al. | 2023 | Alternativa a Transformers en secuencias largas | [arXiv](https://arxiv.org/abs/2312.00752) |
| V3 | **DPO (Direct Preference Opt.)** — Rafailov | 2023 | Alignment sin reward model (reemplaza RLHF) | [arXiv](https://arxiv.org/abs/2305.18290) |
| L4 | **Mixtral 8x7B (MoE)** — Jiang et al. | 2024 | Scaling real con Mixture of Experts open-weight | [arXiv](https://arxiv.org/abs/2401.04088) |
| M4 | **Scaling Laws** — Kaplan et al. | 2020 | Relaciones power-law en LLMs | [arXiv](https://arxiv.org/abs/2001.08361) |
| X4 | **Speculative Decoding** — Leviathan et al.| 2023 | Inferencia ultra-rápida prediciendo tokens | [arXiv](https://arxiv.org/abs/2211.17192) |
| J4 | **Constitutional AI** — Bai et al. | 2022 | RLHF automatizado, supervisado por IA (Claude) | [arXiv](https://arxiv.org/abs/2212.08073) |
| V4 | **Vision Transformers (ViT)** — Dosovitskiy | 2021 | Transformers aplastando CNNs en imágenes | [arXiv](https://arxiv.org/abs/2010.11929) |

---

## 🟢 Semana 5+: Papers por Especialización

### Si te interesa NLP/LLMs:
| Paper | Concepto | Enlace |
|-------|----------|--------|
| **DeepSeek-V2 / V3** (2024/2025) | Innovaciones en MoE y attention (MLA) multi-head super eficiente | [arXiv](https://arxiv.org/abs/2405.04434) |
| **Ring Attention** — Liu et al. (2024) | Contexto de escala infinita procesado en bloque | [arXiv](https://arxiv.org/abs/2310.01889) |
| RoPE — Su et al. | Rotary positional embeddings (Estándar hoy) | [arXiv](https://arxiv.org/abs/2104.09864) |
| GQA — Ainslie et al. | Grouped Query Attention (Standard en LLaMA 3) | [arXiv](https://arxiv.org/abs/2305.13245) |
| Tree of Thoughts — Yao et al. | Razonamiento deliberado avanzado con LLMs | [arXiv](https://arxiv.org/abs/2305.10601) |

### Si te interesa Computer Vision:
| Paper | Concepto | Enlace |
|-------|----------|--------|
| **Sora / Video Gen** — OpenAI (2024) | Difusión de video basada en parches spatio-temporales | [Report](https://openai.com/sora) |
| YOLO v9/v10 — Wang et al. (2024) | Detección de objetos con PGI y sin NMS (super eficiente) | [arXiv](https://arxiv.org/abs/2402.13616) |
| U-Net — Ronneberger et al. | Segmentación semántica y background de Difusión | [arXiv](https://arxiv.org/abs/1505.04597) |
| CLIP — Radford et al. | Conectar imágenes y texto (base de DALL-E) | [arXiv](https://arxiv.org/abs/2103.00020) |
| SAM 2 — Meta (2024) | Segmentación de cualquier objeto, incluyendo video | [arXiv](https://arxiv.org/abs/2408.00714) |

### Si te interesa GenAI / Agentes:
| Paper | Concepto | Enlace |
|-------|----------|--------|
| **ReAct** — Yao et al. (2023) | Razonamiento y Acción entrelazados (la base de LangChain) | [arXiv](https://arxiv.org/abs/2210.03629) |
| **Agentic workflows** — Ng (2024) | Patrones de diseño para sistemas AI multi-agente | [Blog](https://www.deeplearning.ai/the-batch/issue-241/) |
| **AutoGen** — Wu et al. (2023/24) | Entorno multi-agente programable colaborativo | [arXiv](https://arxiv.org/abs/2308.08155) |

### Si te interesa ML Systems / Infraestructura:
| Paper | Concepto | Enlace |
|-------|----------|--------|
| PyTorch — Paszke et al. | Diseño general de frameworks dinámicos | [arXiv](https://arxiv.org/abs/1912.01703) |
| **vLLM / PagedAttention** (2023) | Manejo de memoria KV-cache para LLM serving | [arXiv](https://arxiv.org/abs/2309.06180) |
| ZeRO — Rajbhandari et al. | Optimización extrema de memoria (DeepSpeed) | [arXiv](https://arxiv.org/abs/1910.02054) |
| Megatron-LM — Shoeybi et al. | Multi-GPU / Multi-Node Model y Tensor parallelism | [arXiv](https://arxiv.org/abs/1909.08053) |

---

## 📝 Template para Notas por Paper

```markdown
# [Nombre del Paper] — [Autor Principal] et al. ([Año])

## TL;DR (1 oración)

## Problema que resuelve

## Idea clave (en mis palabras)

## Método (simplificado)

## Resultados principales

## Conexión con lo que estoy aprendiendo

## Preguntas abiertas
```

> **Meta**: Al terminar las 4 semanas, habrás leído ~20 papers. Es más de lo que muchos PhDs leen en su primer semestre. La clave es constancia, no profundidad perfecta.

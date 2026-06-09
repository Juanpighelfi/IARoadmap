# 📖 Glosario Técnico de ML — Referencia Rápida

> Organizado por módulo. Usa `Ctrl+F` para buscar un término rápidamente.
> Cada definición incluye: significado técnico, intuición, y dónde se usa.

---

## Módulo Previo — Python para ML

| Término | Definición Técnica | Intuición | Dónde aparece |
|---------|-------------------|-----------|--------------|
| **Array (NumPy)** | Estructura de datos n-dimensional homogénea (`ndarray`). Almacena datos contiguos en memoria para operaciones vectorizadas rápidas en C. | La "unidad de dato" de todo ML. Es como una lista, pero tipada, multidimensional y 100x más rápida. | Todo el curso |
| **DataFrame (Pandas)** | Tabla 2D con columnas de tipos potencialmente diferentes, índices, y operaciones de consulta tipo SQL. | Una "hoja de cálculo inteligente" para explorar, filtrar y preprocesar datos antes de entrenar. | Exploración de datos, análisis de resultados |
| **Shape** | Tupla que describe las dimensiones de un array/tensor. Ej: `(32, 3, 224, 224)` = batch de 32 imágenes RGB de 224×224. | La "forma" del dato. Si no coinciden los shapes, nada funciona. Imprime shapes obsesivamente al depurar. | Todo el curso |
| **Broadcasting** | Regla de NumPy/PyTorch para operar arrays de shapes diferentes: se "estira" la dimensión de tamaño 1 para que coincidan. | Permite sumar un vector (5,) a una matriz (100, 5) sin escribir un loop — NumPy lo expande automáticamente. | Normalización, operaciones matriciales |
| **Vectorización** | Reemplazar loops de Python por operaciones de NumPy que ejecutan el loop en C optimizado. | `arr * 2` en vez de `for x in arr: x * 2`. Mismo resultado, 100x más rápido. | Todo código numérico |
| **Series (Pandas)** | Columna individual de un DataFrame. Array 1D con índice. | Es como un array de NumPy pero con etiquetas (índice) y operaciones extra para datos tabulares. | Exploración de datos |
| **EDA (Exploratory Data Analysis)** | Proceso de examinar un dataset antes de modelar: distribuciones, correlaciones, valores faltantes, outliers. | "Conocer tus datos antes de entrenar". Lo primero que hace un profesional con cualquier dataset nuevo. | Antes de cada proyecto |

---

## Módulo 0 — Fundamentos Matemáticos

| Término | Definición Técnica | Intuición | Dónde aparece |
|---------|-------------------|-----------|--------------|
| **Gradiente (∇)** | Vector de derivadas parciales de una función respecto a cada variable. `∇f = [∂f/∂x₁, ∂f/∂x₂, ...]` | Es una flecha que apunta en la dirección de mayor subida de la función. Para minimizar, vamos en dirección opuesta. | Backpropagation, optimización |
| **Backpropagation** | Algoritmo para calcular gradientes eficientemente en una red neuronal, aplicando la regla de la cadena desde la salida hacia la entrada. | "Propagar el error hacia atrás": cada capa recibe cuánto contribuyó al error total y ajusta sus pesos. | Entrenamiento de toda red neuronal |
| **Regla de la cadena** | Si `y = f(g(x))`, entonces `dy/dx = f'(g(x)) · g'(x)`. Para funciones compuestas, multiplica las derivadas. | Si cambio `x`, el efecto en `y` depende de cuánto cambió `g(x)` Y cuánto cambió `y` por ese cambio en `g`. | Backpropagation |
| **Función de pérdida (Loss)** | Función que mide cuán lejos está la predicción del valor real. Ej: MSE, Cross-Entropy. | Es la "nota" que le ponemos al modelo — queremos minimizarla. | Entrenamiento |
| **Cross-Entropy** | `L = -Σ y_i · log(ŷ_i)`. Mide la diferencia entre dos distribuciones de probabilidad. | Penaliza mucho cuando el modelo está "muy seguro" y se equivoca. Si predice 0.99 para la clase incorrecta, el loss es altísimo. | Clasificación |
| **Divergencia KL** | `KL(P||Q) = Σ P(x) · log(P(x)/Q(x))`. Mide cuánta información se pierde al aproximar la distribución P con Q. | "¿Cuán diferente es Q de P?" No es simétrico: `KL(P||Q) ≠ KL(Q||P)`. | VAEs, modelos generativos |
| **Jacobiano** | Matriz de todas las derivadas parciales de primer orden de una función vectorial. | Es la "generalización" del gradiente cuando la función tiene múltiples entradas Y múltiples salidas. | Backprop en capas, normalizing flows |
| **Espacio de representación** | Espacio vectorial donde viven las representaciones internas de los datos en cada capa de la red. | Cada capa "transforma" los datos a un nuevo espacio donde son más fáciles de separar/clasificar. | Toda red neuronal |
| **He Initialization** | Inicializar pesos con `W ~ N(0, √(2/n_in))` donde `n_in` es el número de neuronas de entrada. | Sin buena inicialización, las señales se amplifican o desvanecen capa a capa. He está diseñado para ReLU. | Inicialización de redes |
| **Vanishing Gradient** | Los gradientes se vuelven exponencialmente pequeños al propagarse por muchas capas, impidiendo el aprendizaje de capas tempranas. | Como el "juego del teléfono": el mensaje (gradiente) se pierde a medida que pasa por más personas (capas). | Redes profundas, RNNs |
| **Exploding Gradient** | Lo opuesto: los gradientes crecen exponencialmente, causando actualizaciones inestables o `NaN`. | Solución: Gradient clipping (poner un tope al tamaño del gradiente). | Redes profundas, RNNs |

---

## Módulo 1 — Redes Neuronales Profundas

| Término | Definición Técnica | Intuición | Dónde aparece |
|---------|-------------------|-----------|--------------|
| **Tensor** | Generalización de matrices a N dimensiones. Escalar (0D), vector (1D), matriz (2D), tensor (3D+). | En PyTorch, todo dato es un tensor. Una imagen es un tensor 3D: [canales, alto, ancho]. Un batch de imágenes es 4D: [batch, canales, alto, ancho]. | Todo PyTorch |
| **Autograd** | Sistema de diferenciación automática de PyTorch. Registra operaciones en un grafo y calcula gradientes con `.backward()`. | No necesitas derivar a mano: PyTorch "graba" lo que hiciste con los tensores y calcula los gradientes automáticamente. | PyTorch |
| **Batch Normalization** | Normaliza las activaciones de cada mini-batch: `BN(x) = γ · (x - μ_B) / √(σ²_B + ε) + β`. Parámetros γ y β son aprendibles. | Estabiliza el entrenamiento al evitar que las activaciones se descontrolen. Permite learning rates más altos. | Casi toda red moderna |
| **Dropout** | Durante entrenamiento, "apaga" neuronas aleatoriamente con probabilidad `p`. En inferencia, las deja todas activas (escalando por `1-p`). | Obliga a la red a no depender de ninguna neurona individual → regularización → menos overfitting. | Regularización |
| **Learning Rate Scheduler** | Estrategia para cambiar el learning rate durante el entrenamiento. Ej: CosineAnnealing reduce lr siguiendo medio coseno. | Empezar rápido (lr alto) y luego ir más lento (lr bajo) conforme nos acercamos al mínimo. | Optimización avanzada |
| **Gradient Clipping** | Limitar la norma del gradiente a un máximo: `if ||g|| > threshold: g = g · threshold / ||g||`. | "Ponerle freno" a gradientes que explotarían. Esencial en RNNs y Transformers. | Entrenamiento estable |
| **Weight Decay** | Penalización L2 aplicada directamente a los pesos: `W = W - lr · (grad + λ·W)`. | Empuja los pesos hacia 0, evitando que crezcan demasiado. Regularización implícita. | AdamW, SGD |
| **Early Stopping** | Detener el entrenamiento cuando la métrica de validación deja de mejorar por N epochs (patience). | Prevenir overfitting: si ya no mejora en validación, seguir entrenando solo empeora la generalización. | Regularización |
| **Checkpoint** | Guardar el estado del modelo (pesos + optimizer + epoch) en disco para poder resumir o recuperar el mejor modelo. | Un "save game" de tu entrenamiento. | Entrenamiento robusto |

---

## Módulo 2 — Computer Vision (CNNs)

| Término | Definición Técnica | Intuición | Dónde aparece |
|---------|-------------------|-----------|--------------|
| **Convolución** | Operación `(f * g)(x,y) = ΣΣ f(i,j) · g(x-i, y-j)`. Un kernel/filtro se desliza sobre la imagen aplicando producto punto en cada posición. | Una "lupa" que busca un patrón específico (borde, textura) en cada posición de la imagen. Le da a la red "visión local". | CNNs |
| **Feature Map** | La salida de aplicar un filtro convolucional a una imagen. Cada filtro produce un feature map distinto. | Un "mapa de calor" que muestra DÓNDE se detectó el patrón que busca ese filtro. | CNNs |
| **Pooling (Max/Avg)** | Reducir la resolución espacial tomando el máximo (o promedio) en ventanas. Ej: MaxPool 2×2 reduce dimensión a la mitad. | Hacer la representación más compacta y robusta a pequeños desplazamientos de la imagen. | CNNs |
| **Stride** | Cuántos píxeles avanza el filtro en cada paso. Stride=2 reduce la dimensión a la mitad. | "Paso largo" = menos detalle pero más rápido y con mayor campo receptivo. | Convolución |
| **Padding** | Añadir píxeles (generalmente ceros) al borde de la imagen para controlar las dimensiones de salida. `padding='same'` mantiene dimensiones. | Sin padding, cada convolución "achica" la imagen. Con padding, la controlamos. | Convolución |
| **Receptive Field** | La región de la imagen de entrada que influye en un píxel/neurona de una capa profunda. Crece con cada capa. | "Cuánto ve" una neurona profunda. Las capas finales "ven" toda la imagen porque combinan información de muchas capas anteriores. | Diseño de CNNs |
| **Transfer Learning** | Usar un modelo preentrenado en un dataset grande (ImageNet) y adaptarlo a una tarea específica con pocos datos. | En vez de aprender desde cero, "transferir" el conocimiento visual general (bordes, texturas, formas) que ya aprendió el modelo. | 90% de CV en producción |
| **Fine-tuning** | Descongelar parte del modelo preentrenado y re-entrenar con datos nuevos, generalmente con lr muy bajo. | "Ajuste fino": no cambiamos todo, solo adaptamos las últimas capas a nuestra tarea. | Transfer Learning |
| **Data Augmentation** | Aplicar transformaciones aleatorias a las imágenes de entrenamiento (rotación, flip, color jitter, crop) para artificialmente aumentar la diversidad del dataset. | "Enseñarle al modelo que un gato rotado sigue siendo un gato." Regularización implícita muy potente. | Todo CV |
| **GradCAM** | Gradient-weighted Class Activation Mapping. Usa los gradientes de la última capa convolucional para generar un mapa de calor de las regiones más importantes para la predicción. | "¿Dónde está mirando la red para tomar su decisión?" Herramienta de interpretabilidad y debugging. | Interpretabilidad |
| **Skip/Residual Connection** | Conexión directa que "salta" una o más capas: `output = F(x) + x`. Introducida por ResNet. | Permite que el gradiente fluya directamente a capas tempranas sin degradarse. Hace viable entrenar redes de 100+ capas. | ResNet y derivados |
| **Domain Shift** | Diferencia entre la distribución de datos de entrenamiento y la de producción/test. | El modelo vio fotos de estudio, pero en producción recibe fotos con sombras y fondos complejos. Su rendimiento cae. | Despliegue de modelos |

---

## Módulo 3 — Secuencias y Transformers

| Término | Definición Técnica | Intuición | Dónde aparece |
|---------|-------------------|-----------|--------------|
| **Self-Attention** | Mecanismo donde cada posición de la secuencia calcula scores de relevancia con TODAS las demás posiciones. `Attn(Q,K,V) = softmax(QK^T/√d_k)V` | Cada palabra "mira" a todas las demás y decide a cuáles prestar atención. Captura dependencias sin importar la distancia. | Transformers |
| **Query, Key, Value (Q,K,V)** | Tres proyecciones lineales distintas del mismo input. Q="qué busco", K="qué ofrezco", V="qué información tengo". | Como una búsqueda: Q es tu pregunta, K es la etiqueta de cada documento, V es el contenido del documento. El score Q·K dice cuán relevante es cada documento para tu pregunta. | Self-Attention |
| **Multi-Head Attention** | Ejecutar N cabezas de atención en paralelo, cada una con sus propias proyecciones Q,K,V, y concatenar los resultados. | Cada cabeza puede aprender a atender a diferentes tipos de relaciones (sujeto-verbo, pronombre-antecedente, etc.) | Transformers |
| **Positional Encoding** | Señal añadida a los embeddings para codificar la posición de cada token en la secuencia (sinusoidal o aprendida). | Sin esto, el Transformer no sabe si "el gato comió el ratón" o "el ratón comió el gato" — trata todo como un conjunto, no como secuencia. | Transformers |
| **Masked Attention** | Atención donde se enmascaran (=−∞) las posiciones futuras para que el decoder no pueda "hacer trampa" mirando tokens que aún no ha generado. | En una tarea de generación, el modelo debe predecir el siguiente token usando SOLO los anteriores. La máscara fuerza esto. | Decoder del Transformer |
| **Layer Normalization** | Similar a BatchNorm pero normaliza a lo largo de la dimensión de features (no del batch). `LN(x) = γ · (x - μ) / √(σ² + ε) + β` | Preferido en Transformers porque funciona con cualquier tamaño de batch y en secuencias de longitud variable. | Transformers |
| **Feed-Forward Network (FFN)** | Red de dos capas lineales con activación: `FFN(x) = W₂ · ReLU(W₁x + b₁) + b₂`. Aplicada a cada posición independientemente. | Después de la "comunicación" (atención), cada token procesa su información de forma independiente en el FFN. | Cada capa del Transformer |
| **Embedding** | Representación vectorial densa de un token (palabra, subpalabra, carácter). Mapa de un espacio discreto a uno continuo. | Convertir la palabra "gato" en un vector [0.2, -0.5, 0.8, ...] que captura su significado en un espacio matemático donde "gato" está cerca de "felino". | NLP, entrada del Transformer |
| **Tokenización** | Proceso de dividir texto en unidades (tokens): palabras, subpalabras (BPE, WordPiece), o caracteres. | "Machine Learning" → ["Machine", "Learn", "##ing"] (WordPiece) o ["Mach", "ine", " Learn", "ing"] (BPE). Subword es el estándar actual. | Preprocesamiento NLP |
| **BLEU Score** | Métrica de traducción automática que mide la superposición de n-gramas entre la traducción y la referencia. | "¿Cuántas frases de N palabras consecutivas de mi traducción aparecen en la referencia?" No es perfecta pero es estándar. | Evaluación de traducción |
| **Autoregresivo** | Generar la salida token por token, usando los tokens previamente generados como input. `P(y_t | y_1, ..., y_{t-1})` | El modelo genera una palabra, la añade al contexto, y la usa para generar la siguiente. Como escribir una frase palabra por palabra. | GPT, decoders |

---

## Módulo 4 — LLMs y Fine-tuning

| Término | Definición Técnica | Intuición | Dónde aparece |
|---------|-------------------|-----------|--------------|
| **LLM (Large Language Model)** | Modelo de lenguaje basado en Transformer con billones de parámetros, entrenado en enormes corpus de texto. | Una red tan grande que "aprende" patrones del lenguaje, razonamiento y conocimiento del mundo por la escala pura de datos y parámetros. | GPT, LLaMA, Gemini |
| **LoRA (Low-Rank Adaptation)** | Técnica de fine-tuning que congela el modelo original y entrena solo matrices de bajo rango ΔW = A·B donde A∈ℝ^{d×r}, B∈ℝ^{r×d}, r << d. | En vez de modificar los 7B de parámetros, solo entrenas ~0.4% de parámetros adicionales. Resultado similar, costo 100x menor. | Fine-tuning eficiente |
| **Cuantización** | Reducir la precisión numérica de los pesos (ej: de float32 a int4). `7B params × 4 bytes = 28GB → 7B × 0.5 bytes = 3.5GB` | Comprimir el modelo para que quepa en GPUs pequeñas. Pierde algo de calidad pero a menudo es insignificante. | Despliegue de LLMs |
| **Scaling Laws** | Leyes empíricas: el rendimiento del modelo es una ley de potencia del tamaño del modelo, tamaño del dataset y compute. `L ∝ N^{-α}` | "Más grande = mejor" de forma PREDECIBLE. Esto llevó a la carrera de construir modelos cada vez más gigantes. | Investigación en LLMs |
| **RLHF** | Reinforcement Learning from Human Feedback. Fine-tuning con un modelo de recompensa entrenado con preferencias humanas. | Entrenar al LLM para que genere respuestas que los humanos prefieren: más útiles, honestas y no dañinas. Es lo que hace a ChatGPT diferente de GPT-3. | Alignment de LLMs |
| **Temperature** | Parámetro que escala los logits antes del softmax: `softmax(z_i / T)`. T→0: determinístico. T→∞: uniforme. | Controla la "creatividad": temperatura baja = respuestas predecibles y seguras. Temperatura alta = más variadas pero potencialmente incoherentes. | Generación de texto |
| **Top-k / Top-p Sampling** | Estrategias de muestreo: Top-k limita a los k tokens más probables. Top-p (nucleus) limita al menor conjunto que sume probabilidad p. | Filtrar tokens de baja probabilidad para evitar respuestas incoherentes, sin ser completamente determinístico (greedy). | Generación de texto |
| **Context Window** | Número máximo de tokens que el modelo puede procesar de una vez. Ej: GPT-4 = 128K tokens. | La "memoria de trabajo" del modelo. Si tu texto excede la ventana, el modelo literalmente no ve las partes que no caben. | Arquitectura de LLMs |
| **Tokenizer** | Componente que convierte texto en secuencias de IDs numéricos y viceversa. BPE (Byte Pair Encoding) es el estándar. | El "diccionario" del modelo. Cada modelo tiene su tokenizer específico. "Hello" → [15496]. Afecta directamente la eficiencia y capacidad del modelo. | Preprocesamiento |

---

## Módulo 5 — IA Generativa Avanzada

| Término | Definición Técnica | Intuición | Dónde aparece |
|---------|-------------------|-----------|--------------|
| **Modelo de Difusión** | Modelo generativo que aprende a revertir un proceso de adición gradual de ruido gaussiano. Forward: `x_t = √(α_t)x_{t-1} + √(1-α_t)ε`. Reverse: red neuronal predice ε. | Tomas una foto, le añades ruido hasta que sea solo estática. Luego entrenas una red para aprender a "limpiar" esa estática paso a paso → genera imágenes nuevas partiendo de ruido puro. | Stable Diffusion, DALL-E |
| **U-Net** | Arquitectura encoder-decoder con skip connections entre capas del mismo nivel. Forma de U. | "Comprimir y expandir" con atajos. El encoder ve features de alto nivel, el decoder reconstruye el detalle. Las skip connections preservan información de detalle fino. | Difusión, segmentación |
| **CLIP** | Contrastive Language-Image Pre-training. Modelo que aprende a alinear texto e imágenes en un espacio de embedding compartido. | Entiende que "un gato naranja durmiendo" corresponde a cierta imagen. Esto permite condicionar la generación con texto. | Text-to-Image |
| **RAG (Retrieval-Augmented Generation)** | Pipeline: Query → Embedding → Búsqueda vectorial → Top-K docs → Prompt con contexto → LLM → Respuesta fundamentada. | En vez de confiar solo en la "memoria" del LLM, le damos documentos relevantes como referencia antes de generar la respuesta. Reduce alucinaciones. | Chatbots empresariales |
| **Vector Database** | Base de datos optimizada para almacenar y buscar vectores de alta dimensionalidad usando similitud (coseno, euclidiana). Ej: ChromaDB, Pinecone, FAISS. | El "Google" de los embeddings: le das un vector-query y te devuelve los vectores más similares en milisegundos, incluso entre millones. | RAG |
| **Chunking** | Dividir documentos largos en fragmentos de tamaño controlado para indexarlos en la vector DB. Chunk size y overlap son críticos. | Un PDF de 100 páginas no cabe en un solo embedding. Lo cortamos en pedazos de ~500-1000 tokens con algo de solapamiento para no perder contexto. | RAG |
| **Agente de IA** | LLM equipado con herramientas (búsqueda web, calculadora, APIs, código) que puede decidir autónomamente cuáles usar para resolver una tarea. | Un LLM que no solo responde, sino que puede ACTUAR: buscar en Google, ejecutar código, llamar APIs, y razonar sobre los resultados. | LangChain, CrewAI |
| **Alucinación** | Cuando el LLM genera información que suena correcta pero es inventada o falsa. | El modelo "rellena" huecos de conocimiento con texto plausible pero incorrecto. Es el riesgo #1 de los LLMs en producción. | Todo LLM |

---

## Módulo 6 — MLOps y Producción

| Término | Definición Técnica | Intuición | Dónde aparece |
|---------|-------------------|-----------|--------------|
| **Data Drift** | Cambio en la distribución de los datos de entrada con respecto a los datos de entrenamiento. | El mundo cambia: los usuarios empiezan a subir fotos de nuevas plantas, con nuevos celulares, en distintas condiciones. Tu modelo no fue entrenado para eso. | Monitoreo en producción |
| **Model Drift** | Degradación del rendimiento del modelo en producción debido a cambios en datos o en la relación datos-target. | El modelo "envejece": lo que aprendió ayer ya no aplica tan bien hoy. | Monitoreo en producción |
| **Feature Store** | Repositorio centralizado que almacena, versiona y sirve features preprocesadas para entrenamiento e inferencia. | Evita recalcular las mismas features en múltiples modelos/pipelines. Garantiza consistencia entre training y serving. | MLOps avanzado |
| **A/B Testing (en ML)** | Servir dos versiones del modelo simultáneamente a diferentes usuarios y comparar métricas de negocio. | "¿El modelo nuevo es realmente mejor en producción, o solo en el test set?" Validación con usuarios reales. | Despliegue |
| **CI/CD para ML** | Continuous Integration / Continuous Deployment adaptado a ML: incluye tests de calidad de datos, tests de rendimiento de modelo, y despliegue automatizado. | No solo testeas que el código compila, sino que el modelo cumple un mínimo de accuracy y que los datos de entrada son válidos. | MLOps |
| **TorchScript** | Formato de serialización de PyTorch que permite ejecutar modelos sin Python. `torch.jit.trace()` o `torch.jit.script()`. | Exportar tu modelo para producción: más rápido, sin dependencia de Python, desplegable en C++, móvil, o edge. | Despliegue |
| **Containerización (Docker)** | Empaquetar la aplicación + sus dependencias + el modelo en un contenedor reproducible. | "Funciona en mi máquina" → "Funciona en CUALQUIER máquina que tenga Docker." Reproducibilidad total. | Despliegue |
| **MLflow** | Plataforma de gestión del ciclo de vida de ML: tracking de experimentos, empaquetado de modelos, registro y despliegue. | Tu "diario de laboratorio digital": cada experimento queda registrado con métricas, hiperparámetros, artefactos y código. | Gestión de experimentos |
| **DVC (Data Version Control)** | Git para datos y modelos. Versiona archivos grandes sin meterlos en Git. | Los datos cambian tanto como el código. DVC te permite hacer "git log" de tus datasets y modelos. | Versionado de datos |

---

> [!TIP]
> **Cómo usar este glosario**: No lo leas de principio a fin. Consúltalo cuando encuentres un término desconocido en el material de estudio. Marca con ⭐ los términos que te costaron más y revísalos en tus flashcards de Anki.

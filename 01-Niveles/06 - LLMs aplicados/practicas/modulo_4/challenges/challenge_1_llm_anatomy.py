"""
=============================================================================
M4-CHALLENGE 1: Anatomía de un LLM
=============================================================================
Explorar TinyLlama: arquitectura, tokenización, generación.
DURACIÓN: ~1.5h | DIFICULTAD: ⭐⭐⭐

HINTS: Si te trabás, consultá modulo_4/hints/hint_challenge_1.md
=============================================================================
"""
import torch
print("=" * 60)
print("M4-CHALLENGE 1: Anatomía de un LLM")
print("=" * 60)

try:
    from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
except ImportError:
    print("  pip install transformers accelerate")
    exit()

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# --- TODO: Inspecciona la configuración del modelo ---
print(f"\n--- Arquitectura de {model_name} ---")

"""
TODO: Usa AutoConfig.from_pretrained() para inspeccionar la arquitectura.
Imprime: num_hidden_layers, hidden_size, num_attention_heads, 
         num_key_value_heads (GQA), intermediate_size, vocab_size
"""
config = AutoConfig.from_pretrained(model_name)
# TODO: Imprime cada campo de la config
print(f"  Capas (num_hidden_layers): {config.num_hidden_layers}")
print(f"  d_model (hidden_size):     {config.hidden_size}")
print(f"  Attention heads:           {config.num_attention_heads}")
print(f"  KV heads (GQA):            {getattr(config, 'num_key_value_heads', 'N/A')}")
print(f"  FFN dim (intermediate):    {config.intermediate_size}")
print(f"  Vocab size:                {config.vocab_size}")
print(f"  Max position:              {config.max_position_embeddings}")

# TODO: Estima el número de parámetros SIN descargar el modelo
"""
Fórmula aproximada:
  params ≈ V·d + L·(4·d² + 3·d·ffn + 4·d) + d
Donde V=vocab, d=hidden_size, L=num_layers, ffn=intermediate_size
"""
d = config.hidden_size
L = config.num_hidden_layers
V = config.vocab_size
ffn = config.intermediate_size
estimated = ...  # Tu cálculo aquí
print(f"\n  Parámetros estimados: ~{estimated/1e6:.0f}M")

# --- TODO: Tokenización ---
print(f"\n{'='*60}")
print("--- Tokenización ---")
print("=" * 60)

tokenizer = AutoTokenizer.from_pretrained(model_name)

textos = {
    "Español": "El aprendizaje automático es fascinante para resolver problemas complejos.",
    "English": "Machine learning is fascinating for solving complex problems.",
    "Código":  "def train(model, data): return model.fit(data)",
    "Números": "El precio es $12,345.67 USD",
}

"""
TODO: Para cada texto, tokeniza y muestra:
  1. Cantidad de tokens
  2. Los tokens decodificados
Observa: español usa MÁS tokens que inglés (tokenizer entrenado en inglés)
"""
for idioma, texto in textos.items():
    tokens = tokenizer.encode(texto)
    decoded = [tokenizer.decode([t]) for t in tokens]
    print(f"\n  [{idioma}] ({len(tokens)} tokens)")
    print(f"    Texto:  '{texto}'")
    print(f"    Tokens: {decoded[:15]}{'...' if len(decoded) > 15 else ''}")

# --- Generación ---
print(f"\n{'='*60}")
print("--- Generación: Efecto de la Temperatura ---")
print("=" * 60)

print("""
  Temperature controla la "creatividad":
  - T=0.1: Muy determinista (siempre el token más probable)
  - T=1.0: Muestreo estándar
  - T=2.0: Muy creativo (más variedad, más errores)
  
  Para generar, descomentar las siguientes líneas (requiere ~2GB RAM):
""")

# === TODO: DESCOMENTAR PARA GENERAR ===
# model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float32)
# model.eval()
# prompt = "La inteligencia artificial es"
# inputs = tokenizer(prompt, return_tensors="pt")
# 
# for temp in [0.1, 0.7, 1.5]:
#     with torch.no_grad():
#         out = model.generate(**inputs, max_new_tokens=50, temperature=temp,
#                              do_sample=True, top_p=0.9)
#     print(f"\n  T={temp}: {tokenizer.decode(out[0], skip_special_tokens=True)}")

print("\nM4-Challenge 1 completado.")

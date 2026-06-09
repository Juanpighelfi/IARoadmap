"""
=============================================================================
M4-CHALLENGE 1: Anatomia de un LLM
=============================================================================
Explorar TinyLlama: arquitectura, tokenizacion, generacion.
DURACION: ~1.5h | DIFICULTAD: 3/5
=============================================================================
"""
import torch
print("=" * 60)
print("M4-CHALLENGE 1: Anatomia de un LLM")
print("=" * 60)

try:
    from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
except ImportError:
    print("  pip install transformers accelerate")
    exit()

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# --- Config inspection ---
print(f"\n--- Arquitectura de {model_name} ---")
config = AutoConfig.from_pretrained(model_name)
print(f"  Capas (num_hidden_layers): {config.num_hidden_layers}")
print(f"  d_model (hidden_size):     {config.hidden_size}")
print(f"  Attention heads:           {config.num_attention_heads}")
print(f"  KV heads (GQA):            {getattr(config, 'num_key_value_heads', 'N/A')}")
print(f"  FFN dim (intermediate):    {config.intermediate_size}")
print(f"  Vocab size:                {config.vocab_size}")
print(f"  Max position:              {config.max_position_embeddings}")

# Calcular parametros sin descargar el modelo
d = config.hidden_size
L = config.num_hidden_layers
V = config.vocab_size
ffn = config.intermediate_size
estimated = V * d + L * (4 * d * d + 3 * d * ffn + 4 * d) + d
print(f"\n  Parametros estimados: ~{estimated/1e6:.0f}M")

# --- Tokenizacion ---
print(f"\n{'='*60}")
print("--- Tokenizacion ---")
print("=" * 60)

tokenizer = AutoTokenizer.from_pretrained(model_name)

textos = {
    "Espanol": "El aprendizaje automatico es fascinante para resolver problemas complejos.",
    "English": "Machine learning is fascinating for solving complex problems.",
    "Codigo":  "def train(model, data): return model.fit(data)",
    "Numeros": "El precio es $12,345.67 USD",
}

for idioma, texto in textos.items():
    tokens = tokenizer.encode(texto)
    decoded = [tokenizer.decode([t]) for t in tokens]
    print(f"\n  [{idioma}] ({len(tokens)} tokens)")
    print(f"    Texto:  '{texto}'")
    print(f"    Tokens: {decoded[:15]}{'...' if len(decoded) > 15 else ''}")

print("""
  OBSERVA:
  - Espanol usa MAS tokens que ingles (tokenizer entrenado en ingles)
  - Codigo se tokeniza bien (los LLMs ven MUCHO codigo)
  - Numeros: cada digito puede ser un token separado
""")

# --- Generacion con diferentes temperaturas ---
print(f"\n{'='*60}")
print("--- Generacion: Efecto de la Temperatura ---")
print("=" * 60)

print("""
  Temperature controla la "creatividad":
  - T=0.1: Muy determinista (siempre el token mas probable)
  - T=1.0: Muestreo estandar
  - T=2.0: Muy creativo (mas variedad, mas errores)
  
  top_k: Solo considerar los K tokens mas probables
  top_p (nucleus): Considerar tokens que sumen probabilidad p
  
  Para generar, descomentar las siguientes lineas (requiere ~2GB RAM):
""")

# === DESCOMENTAR PARA GENERAR ===
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

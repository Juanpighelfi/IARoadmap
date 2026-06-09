"""
Smoke test: ejecuta todos los challenges y guías para verificar que no hay errores.
Ejecutar desde modulo_0/: python test_all_challenges.py
"""
import sys
import os
import builtins
import traceback

# === NON-INTERACTIVE SETUP ===
os.environ['MPLBACKEND'] = 'Agg'
builtins.input = lambda *a: None

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
_orig_show = plt.show
plt.show = lambda *a, **kw: plt.close('all')

# Ensure we run from modulo_0 directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print(f"Working directory: {os.getcwd()}")

# Ensure output subdirs exist for savefig calls
for subdir in ['conceptos', 'challenges', 'proyecto']:
    os.makedirs(subdir, exist_ok=True)

results = []

def run_file(filepath):
    """Execute a Python file and report success/failure."""
    name = os.path.relpath(filepath)
    print(f"\n{'='*60}")
    print(f"  TESTING: {name}")
    print(f"{'='*60}")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        # Run from modulo_0 directory (don't change dirs)
        exec(compile(code, filepath, 'exec'), {
            '__name__': '__run_test__',  # Not __main__ to skip if __name__ blocks
            '__file__': filepath,
        })
        plt.close('all')
        results.append((name, "✅ PASS"))
        print(f"\n  ✅ {name}: PASSED")
    except Exception as e:
        plt.close('all')
        results.append((name, f"❌ FAIL: {type(e).__name__}: {str(e)[:80]}"))
        print(f"\n  ❌ {name}: FAILED — {type(e).__name__}: {e}")
        traceback.print_exc(limit=3)

# === Run all files ===
files = [
    # Conceptos (guías)
    "conceptos/01_algebra_lineal_para_ml.py",
    "conceptos/02_calculo_y_gradientes.py",
    "conceptos/03_probabilidad_y_loss.py",
    # Challenges semana 1
    "challenges/challenge_1_matmul.py",
    "challenges/challenge_2_pca_manual.py",
    "challenges/challenge_3_transformaciones.py",
    # Challenges semana 2
    "challenges/challenge_4_gradientes_manuales.py",
    "challenges/challenge_5_autograd_verify.py",
    "challenges/challenge_6_vanishing_gradient.py",
    # Challenges semana 3
    "challenges/challenge_7_cross_entropy.py",
    "challenges/challenge_8_mse_vs_ce.py",
    "challenges/challenge_9_kl_divergence.py",
    # Proyecto (uses __main__ guard, needs special handling)
]

for f in files:
    run_file(f)

# Special case: proyecto has if __name__ == "__main__" guard
print(f"\n{'='*60}")
print(f"  TESTING: proyecto/backprop_from_scratch.py")
print(f"{'='*60}")
try:
    with open("proyecto/backprop_from_scratch.py", 'r', encoding='utf-8') as f:
        code = f.read()
    exec(compile(code, "proyecto/backprop_from_scratch.py", 'exec'), {
        '__name__': '__main__',
        '__file__': "proyecto/backprop_from_scratch.py",
    })
    plt.close('all')
    results.append(("proyecto/backprop_from_scratch.py", "✅ PASS"))
    print(f"\n  ✅ backprop_from_scratch.py: PASSED")
except Exception as e:
    plt.close('all')
    results.append(("proyecto/backprop_from_scratch.py", f"❌ FAIL: {type(e).__name__}: {str(e)[:80]}"))
    print(f"\n  ❌ backprop_from_scratch.py: FAILED — {type(e).__name__}: {e}")
    traceback.print_exc(limit=3)

# === SUMMARY ===
print(f"\n\n{'='*60}")
print(f"  📊 RESUMEN DE TESTS")
print(f"{'='*60}")
passed = sum(1 for _, s in results if "PASS" in s)
for name, status in results:
    print(f"  {status}")

print(f"\n  {passed}/{len(results)} archivos ejecutados correctamente")
if passed == len(results):
    print(f"  🎉 ¡TODO FUNCIONA!")
else:
    print(f"  ⚠️  Hay {len(results) - passed} archivo(s) con errores — revisar arriba")

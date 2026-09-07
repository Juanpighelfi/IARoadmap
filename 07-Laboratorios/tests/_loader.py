import importlib.util
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(lab, default):
    path = Path(os.environ.get(f"LAB{lab:02d}_PATH", ROOT / default / "solucion.py"))
    spec = importlib.util.spec_from_file_location(f"lab{lab:02d}_candidate", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"No se pudo cargar {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

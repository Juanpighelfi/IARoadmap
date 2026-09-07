"""Particiones que conservan la independencia entre piezas fotografiadas."""
import random
from datetime import date


def group_split(rows, test_ratio=.2, seed=0):
    """Divide referencias a filas, manteniendo cada pieza íntegra en un lado."""
    if not 0 < test_ratio < 1:
        raise ValueError("test_ratio debe estar entre 0 y 1")
    groups = sorted({row["pieza_id"] for row in rows})
    if len(groups) < 2:
        raise ValueError("se necesitan al menos dos piezas")
    random.Random(seed).shuffle(groups)
    test_count = max(1, min(len(groups)-1, round(len(groups) * test_ratio)))
    test_groups = set(groups[:test_count])
    train = [row for row in rows if row["pieza_id"] not in test_groups]
    test = [row for row in rows if row["pieza_id"] in test_groups]
    return train, test


def time_split(rows, cutoff):
    """Divide por fecha ISO: train anterior al corte; test desde el corte."""
    cutoff_date = date.fromisoformat(cutoff)
    train = [row for row in rows if date.fromisoformat(row["fecha"]) < cutoff_date]
    test = [row for row in rows if date.fromisoformat(row["fecha"]) >= cutoff_date]
    return train, test


def detect_group_leakage(train, test):
    """Indica si algún pieza_id aparece en ambos conjuntos."""
    train_groups = {row["pieza_id"] for row in train}
    test_groups = {row["pieza_id"] for row in test}
    return bool(train_groups & test_groups)

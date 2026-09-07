def group_split(rows, test_ratio=.2, seed=0):
    """Devuelve (train, test), sin dividir fotos de una misma pieza."""
    raise NotImplementedError


def time_split(rows, cutoff):
    """Divide por fecha ISO: anteriores al corte y desde el corte inclusive."""
    raise NotImplementedError


def detect_group_leakage(train, test):
    """Devuelve True si hay un pieza_id presente en ambos conjuntos."""
    raise NotImplementedError

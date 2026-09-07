def mse(xs, ys, weight, bias):
    """Calcula el error cuadrático medio de weight*x + bias."""
    raise NotImplementedError


def gradients(xs, ys, weight, bias):
    """Devuelve (derivada respecto de weight, derivada respecto de bias)."""
    raise NotImplementedError


def fit(xs, ys, lr=.05, steps=200, w=0.0, b=0.0):
    """Devuelve (w, b, historial), incluida la pérdida inicial y cada paso."""
    raise NotImplementedError

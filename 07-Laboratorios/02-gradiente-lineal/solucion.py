"""Regresión lineal univariada implementada solo con Python estándar."""


def _validate_samples(xs, ys):
    if not xs or len(xs) != len(ys):
        raise ValueError("xs e ys deben tener igual longitud no vacía")


def mse(xs, ys, weight, bias):
    """Devuelve el error cuadrático medio de y_estimado = weight*x + bias."""
    _validate_samples(xs, ys)
    squared_errors = ((weight * x + bias - y) ** 2 for x, y in zip(xs, ys))
    return sum(squared_errors) / len(xs)


def gradients(xs, ys, weight, bias):
    """Devuelve las derivadas (dMSE/dweight, dMSE/dbias)."""
    _validate_samples(xs, ys)
    residuals = [weight * x + bias - y for x, y in zip(xs, ys)]
    count = len(xs)
    weight_gradient = 2 / count * sum(error * x for error, x in zip(residuals, xs))
    bias_gradient = 2 / count * sum(residuals)
    return weight_gradient, bias_gradient


def fit(xs, ys, lr=.05, steps=200, w=0.0, b=0.0):
    """Ejecuta ``steps`` actualizaciones y devuelve (w, b, pérdidas reales)."""
    _validate_samples(xs, ys)
    if lr <= 0 or steps < 0 or not isinstance(steps, int):
        raise ValueError("lr debe ser positivo y steps un entero no negativo")

    history = [mse(xs, ys, w, b)]
    for _ in range(steps):
        weight_gradient, bias_gradient = gradients(xs, ys, w, b)
        w -= lr * weight_gradient
        b -= lr * bias_gradient
        history.append(mse(xs, ys, w, b))
    return w, b, history

def value_iteration(mdp, gamma=.9, tol=1e-9, max_iterations=10000):
    """Devuelve (valores, política) o RuntimeError si no converge.

    ``terminals`` es un conjunto de estados con V=0. Cada resultado es
    (probabilidad, estado_siguiente, recompensa), incluida la recompensa al
    entrar en un terminal.
    """
    raise NotImplementedError


def example_mdp():
    """Devuelve el MDP pequeño especificado en la consigna."""
    raise NotImplementedError

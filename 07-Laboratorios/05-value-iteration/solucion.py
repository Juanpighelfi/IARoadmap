"""Iteración de valores para un MDP tabular finito."""
import math


def _validate_mdp(mdp):
    states = set(mdp["states"])
    terminals = set(mdp["terminals"])
    actions = mdp["actions"]
    if not states or not terminals <= states:
        raise ValueError("states debe incluir todos los terminales")
    if terminals & set(actions):
        raise ValueError("los estados terminales no deben tener acciones")
    nonterminals = states - terminals
    if set(actions) != nonterminals:
        raise ValueError("cada estado no terminal debe tener acciones")

    for state, state_actions in actions.items():
        if not state_actions:
            raise ValueError(f"{state} no tiene acciones")
        for action, outcomes in state_actions.items():
            if not outcomes:
                raise ValueError(f"{state}/{action} no tiene transiciones")
            probability_sum = 0.0
            for probability, next_state, reward in outcomes:
                if (not math.isfinite(probability) or probability < 0
                        or next_state not in states or not math.isfinite(reward)):
                    raise ValueError("transición inválida")
                probability_sum += probability
            if not math.isclose(probability_sum, 1.0, rel_tol=0.0, abs_tol=1e-12):
                raise ValueError("las probabilidades de una acción deben sumar 1")


def value_iteration(mdp, gamma=.9, tol=1e-9, max_iterations=10000):
    """Devuelve (valores, política) al converger dentro del presupuesto.

    Los terminales tienen valor cero. La recompensa por llegar a ellos forma
    parte de la transición entrante: p * (recompensa + gamma * V(siguiente)).
    """
    if not math.isfinite(gamma) or not 0 <= gamma < 1:
        raise ValueError("gamma debe ser finito y estar en [0, 1)")
    if not math.isfinite(tol) or tol <= 0:
        raise ValueError("tol debe ser finito y positivo")
    if isinstance(max_iterations, bool) or not isinstance(max_iterations, int) or max_iterations <= 0:
        raise ValueError("max_iterations debe ser un entero positivo")
    _validate_mdp(mdp)

    terminals = set(mdp["terminals"])
    values = {state: 0.0 for state in mdp["states"]}
    converged = False
    for _ in range(max_iterations):
        updated = dict(values)
        largest_change = 0.0
        for state, actions in mdp["actions"].items():
            action_values = []
            for outcomes in actions.values():
                action_values.append(sum(
                    probability * (reward + gamma * values[next_state])
                    for probability, next_state, reward in outcomes
                ))
            updated[state] = max(action_values)
            largest_change = max(largest_change, abs(updated[state] - values[state]))
        values = updated
        if largest_change < tol:
            converged = True
            break
    if not converged:
        raise RuntimeError("value iteration no convergió dentro de max_iterations")

    policy = {}
    for state, actions in mdp["actions"].items():
        policy[state] = max(
            actions,
            key=lambda action: sum(
                probability * (reward + gamma * values[next_state])
                for probability, next_state, reward in actions[action]
            ),
        )
    assert all(values[state] == 0.0 for state in terminals)
    return values, policy


def example_mdp():
    """Crea un MDP con éxito/fallo terminal y una decisión de retorno."""
    return {
        "states": ("inicio", "riesgo", "meta", "fallo"),
        "terminals": {"meta", "fallo"},
        "actions": {
            "inicio": {
                "avanzar": [(1.0, "riesgo", -1.0)],
                "esperar": [(1.0, "inicio", -2.0)],
            },
            "riesgo": {
                "intentar": [(0.8, "meta", 10.0), (0.2, "fallo", -5.0)],
                "volver": [(1.0, "inicio", -1.0)],
            },
        },
    }

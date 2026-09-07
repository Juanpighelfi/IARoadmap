import math
import unittest
from tests._loader import load
m = load(5, "05-value-iteration")

class MDPTests(unittest.TestCase):
    def test_standard_terminal_convention_and_policy(self):
        mdp = m.example_mdp()
        values, policy = m.value_iteration(mdp, gamma=.9, tol=1e-10)
        self.assertEqual(values["meta"], 0.0)
        self.assertEqual(values["fallo"], 0.0)
        self.assertNotIn("meta", policy)
        self.assertEqual(policy["inicio"], "avanzar")

    def test_stochastic_manual_variant(self):
        mdp = {"states": ("s", "t"), "terminals": {"t"},
               "actions": {"s": {"try": [(.5, "t", 4), (.5, "s", -1)]}}}
        values, policy = m.value_iteration(mdp, gamma=.5, tol=1e-12)
        self.assertAlmostEqual(values["s"], 2.0, places=8)
        self.assertEqual(policy["s"], "try")

    def test_invalid_models_and_parameters(self):
        invalid = [
            {"states": ("s", "t"), "terminals": {"t"}, "actions": {"s": {"a": [(.7, "t", 0)]}}},
            {"states": ("s", "t"), "terminals": {"t"}, "actions": {}},
            {"states": ("s", "t"), "terminals": {"t"}, "actions": {"s": {}}},
        ]
        for mdp in invalid:
            with self.assertRaises(ValueError): m.value_iteration(mdp)
        for kwargs in ({"gamma": math.nan}, {"tol": math.inf}, {"max_iterations": 0}, {"max_iterations": 1.5}):
            with self.assertRaises(ValueError): m.value_iteration(m.example_mdp(), **kwargs)

    def test_probability_sum_uses_strict_absolute_tolerance(self):
        accepted = {"states": ("s", "t"), "terminals": {"t"},
                    "actions": {"s": {"a": [(0.5, "t", 0.0), (0.5000000000005, "t", 0.0)]}}}
        values, policy = m.value_iteration(accepted)
        self.assertEqual(values["t"], 0.0)
        self.assertEqual(policy["s"], "a")

        rejected = {"states": ("s", "t"), "terminals": {"t"},
                    "actions": {"s": {"a": [(0.5, "t", 0.0), (0.500000000002, "t", 0.0)]}}}
        with self.assertRaises(ValueError):
            m.value_iteration(rejected)

    def test_reports_non_convergence(self):
        mdp = {"states": ("s", "t"), "terminals": {"t"},
               "actions": {"s": {"loop": [(1.0, "s", 1.0)]}}}
        with self.assertRaises(RuntimeError):
            m.value_iteration(mdp, gamma=.99, tol=1e-15, max_iterations=2)

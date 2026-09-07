import unittest
from collections import Counter
from tests._loader import load
m = load(4, "04-particion-sin-fuga")

class SplitTests(unittest.TestCase):
    def setUp(self):
        specs = [("A", "2026-01-01")]*5 + [("B", "2026-01-03")] + [("C", "2026-02-01")]*3 + [("D", "2026-03-01")]
        self.rows = [{"foto_id": f"f{i}", "pieza_id": p, "fecha": d} for i, (p, d) in enumerate(specs)]

    def test_group_split_preserves_rows_groups_and_requested_group_count(self):
        for ratio in (.25, .5, .74):
            train, test = m.group_split(self.rows, ratio, seed=7)
            self.assertEqual(Counter(map(id, train + test)), Counter(map(id, self.rows)))
            train_groups = {r["pieza_id"] for r in train}
            test_groups = {r["pieza_id"] for r in test}
            self.assertFalse(train_groups & test_groups)
            expected = max(1, min(3, round(4 * ratio)))
            self.assertEqual(len(test_groups), expected)

    def test_deterministic_and_time_split(self):
        self.assertEqual(m.group_split(self.rows, .34, 5), m.group_split(self.rows, .34, 5))
        train, test = m.time_split(self.rows, "2026-02-01")
        self.assertEqual(Counter(map(id, train + test)), Counter(map(id, self.rows)))
        self.assertTrue(all(r["fecha"] < "2026-02-01" for r in train))
        self.assertTrue(all(r["fecha"] >= "2026-02-01" for r in test))

    def test_leakage_detector_has_positive_and_negative_cases(self):
        train, test = self.rows[:5], self.rows[5:]
        self.assertFalse(m.detect_group_leakage(train, test))
        self.assertTrue(m.detect_group_leakage(train, test + [self.rows[0]]))

    def test_bad_inputs(self):
        with self.assertRaises(ValueError): m.group_split(self.rows, 1.0)
        with self.assertRaises(ValueError): m.group_split([self.rows[0]], .5)

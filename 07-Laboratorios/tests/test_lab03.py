import unittest
from tests._loader import load
m = load(3, "03-busqueda-cuadricula")

class SearchTests(unittest.TestCase):
    def assert_valid_path(self, path, rows, cols, blocked, start, goal, optimal_steps):
        self.assertIsNotNone(path)
        self.assertEqual(path[0], start)
        self.assertEqual(path[-1], goal)
        self.assertEqual(len(path) - 1, optimal_steps)
        self.assertTrue(all(point not in blocked for point in path))
        self.assertTrue(all(0 <= row < rows and 0 <= col < cols for row, col in path))
        for current, following in zip(path, path[1:]):
            self.assertEqual(abs(current[0]-following[0]) + abs(current[1]-following[1]), 1)

    def test_both_algorithms_return_optimal_valid_paths(self):
        cases = [
            (4, 4, {(1, 0), (1, 1), (1, 2)}, (0, 0), (3, 0), 9),
            (5, 6, {(0, 2), (1, 2), (2, 2), (3, 4)}, (0, 0), (4, 5), 9),
        ]
        for algorithm in (m.bfs, m.astar):
            for rows, cols, blocked, start, goal, steps in cases:
                with self.subTest(algorithm=algorithm.__name__, goal=goal):
                    self.assert_valid_path(algorithm(rows, cols, blocked, start, goal), rows, cols, blocked, start, goal, steps)

    def test_both_report_unreachable_and_handle_identity(self):
        for algorithm in (m.bfs, m.astar):
            self.assertIsNone(algorithm(2, 2, {(0, 1), (1, 0)}, (0, 0), (1, 1)))
            self.assertEqual(algorithm(1, 1, set(), (0, 0), (0, 0)), [(0, 0)])

    def test_invalid_endpoint(self):
        for algorithm in (m.bfs, m.astar):
            with self.assertRaises(ValueError):
                algorithm(2, 2, set(), (-1, 0), (1, 1))

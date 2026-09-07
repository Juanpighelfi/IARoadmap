import unittest
from tests._loader import load
m = load(2, "02-gradiente-lineal")
class GradientTests(unittest.TestCase):
    def test_gradient_known(self): self.assertEqual(m.gradients([1,2],[3,5],0,0),(-13.0,-8.0))
    def test_history_is_real_and_matches_initial_and_final_losses(self):
        xs=[-2,-1,0,1,2]; ys=[-3,-1,1,3,5]
        initial=m.mse(xs,ys,0,0); w,b,history=m.fit(xs,ys,lr=.1,steps=100)
        self.assertEqual(len(history),101)
        self.assertAlmostEqual(history[0],initial)
        self.assertAlmostEqual(history[-1],m.mse(xs,ys,w,b))
        self.assertTrue(all(after <= before for before, after in zip(history, history[1:])))
        self.assertLess(history[-1], initial/1000)
    def test_errors(self):
        with self.assertRaises(ValueError): m.gradients([],[],0,0)
        with self.assertRaises(ValueError): m.fit([1],[1,2])

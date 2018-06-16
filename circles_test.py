import unittest
from math import pi
from circles import calc_cricle_area

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        #test when values >=0
        self.assertAlmostEqual(calc_cricle_area(1.), pi)
        self.assertAlmostEqual(calc_cricle_area(0.),0.)
        self.assertAlmostEqual(calc_cricle_area(2.2), pi * 2.2 ** 2)
    def test_values(self):
        #test handling of not allowed input values
        self.assertRaises(ValueError, calc_cricle_area, -2)
    def test_type(self):
        self.assertRaises(TypeError,calc_cricle_area, 2+2j)
        self.assertRaises(TypeError, calc_cricle_area, True)
        self.assertRaises(TypeError, calc_cricle_area, 'string')
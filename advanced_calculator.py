import unittest
import math
from advanced_calculator import *

class TestAdvancedCalculator(unittest.TestCase):

    def test_add(self): self.assertEqual(add(2,3), 5)
    def test_subtract(self): self.assertEqual(subtract(5,3), 2)
    def test_multiply(self): self.assertEqual(multiply(2,3), 6)
    def test_divide(self):
        self.assertEqual(divide(6,3), 2)
        self.assertEqual(divide(6,0), "Error! Division by zero.")

    def test_power(self): self.assertEqual(power(2,3), 8)
    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(-1), "Error! Negative input.")
    def test_sine(self): self.assertAlmostEqual(sine(30), 0.5)
    def test_cosine(self): self.assertAlmostEqual(cosine(60), 0.5)
    def test_tangent(self): self.assertAlmostEqual(tangent(45), 1, places=5)
    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(100), 2)
        self.assertEqual(logarithm(-10), "Error! Non-positive input.")
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(-3), "Error! Negative input.")
    def test_exponential(self): self.assertAlmostEqual(exponential(1), math.e)
    
    def test_memory_functions(self):
        global memory
        memory = None
        self.assertEqual(recall_memory(), "Memory empty")
        memory = 42
        self.assertEqual(recall_memory(), 42)  # This now correctly uses global memory
        self.assertEqual(clear_memory(), "Memory cleared")
        self.assertIsNone(memory)

if __name__ == "__main__":
    unittest.main()

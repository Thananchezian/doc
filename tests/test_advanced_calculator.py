import unittest
import math
from advanced_calculator import (
    add, subtract, multiply, divide, power, square_root,
    factorial, logarithm, exponential,
    sine, cosine, tangent,
    store_memory, recall_memory, clear_memory
)

class TestAdvancedCalculator(unittest.TestCase):

    # Arithmetic tests
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-1)

    # Factorial
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    # Logarithm
    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(100), 2)
        with self.assertRaises(ValueError):
            logarithm(0)

    # Exponential
    def test_exponential(self):
        self.assertAlmostEqual(exponential(1), math.e)

    # Trigonometry
    def test_sine(self):
        self.assertAlmostEqual(sine(30), 0.5)

    def test_cosine(self):
        self.assertAlmostEqual(cosine(60), 0.5)

    def test_tangent(self):
        self.assertAlmostEqual(tangent(45), 1, places=5)
        with self.assertRaises(ValueError):
            tangent(90)  # Undefined

    # Memory
    def test_memory_functions(self):
        clear_memory()
        self.assertEqual(recall_memory(), "Memory empty")
        store_memory(42)
        self.assertEqual(recall_memory(), 42)
        clear_memory()
        self.assertEqual(recall_memory(), "Memory empty")

if __name__ == "__main__":
    unittest.main()

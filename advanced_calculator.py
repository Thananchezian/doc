import pytest
import math
from advanced_calculator import (
    add, subtract, multiply, divide, power, square_root,
    sine, cosine, tangent, logarithm, factorial, exponential,
    calculate, memory
)

# === Basic operations ===
def test_add(): assert add(2, 3) == 5
def test_subtract(): assert subtract(5, 3) == 2
def test_multiply(): assert multiply(2, 3) == 6
def test_divide(): 
    assert divide(6, 3) == 2
    assert divide(5, 0) == "Error! Division by zero."

# === Advanced operations ===
def test_power(): assert power(2, 3) == 8
def test_square_root(): 
    assert square_root(9) == 3
    assert square_root(-1) == "Error! Negative input."
def test_sine(): assert sine(90) == pytest.approx(1.0)
def test_cosine(): assert cosine(0) == pytest.approx(1.0)
def test_tangent(): assert tangent(45) == pytest.approx(1.0)
def test_logarithm(): 
    assert logarithm(100, 10) == 2
    assert logarithm(-5) == "Error! Non-positive input."
def test_factorial():
    assert factorial(5) == 120
    assert factorial(-1) == "Error! Negative input."
def test_exponential(): assert exponential(1) == pytest.approx(math.e)

# === Calculator function and memory tests ===
def test_calculate_basic_operations():
    assert calculate('1', 2, 3) == 5
    assert calculate('2', 5, 3) == 2
    assert calculate('3', 2, 3) == 6
    assert calculate('4', 6, 3) == 2
    assert calculate('4', 5, 0) == "Error! Division by zero."
    assert calculate('5', 2, 3) == 8

def test_calculate_advanced_operations():
    assert calculate('6', 9) == 3
    assert calculate('6', -1) == "Error! Negative input."
    assert calculate('7', angle=90) == pytest.approx(1.0)
    assert calculate('8', angle=0) == pytest.approx(1.0)
    assert calculate('9', angle=45) == pytest.approx(1.0)
    assert calculate('10', 100, base=10) == 2
    assert calculate('10', -5) == "Error! Non-positive input."
    assert calculate('11', 5) == 120
    assert calculate('11', -1) == "Error! Negative input."
    assert calculate('12', 1) == pytest.approx(math.e)

def test_calculate_memory_operations():
    # Memory store via any operation
    calculate('1', 10, 5)
    assert calculate('13') == 15
    # Memory clear
    assert calculate('14') == "Memory cleared."
    assert calculate('13') == 'Empty'

def test_invalid_choice():
    assert calculate('99') == "Invalid input"

import math

# Memory variable
memory = None

# Basic arithmetic
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

# Factorial
def factorial(n):
    if n < 0:
        raise ValueError("Cannot take factorial of negative number")
    return math.factorial(n)

# Logarithm (base 10)
def logarithm(n):
    if n <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    return math.log10(n)

# Exponential
def exponential(n):
    return math.exp(n)

# Trigonometry (angles in degrees)
def sine(angle):
    return round(math.sin(math.radians(angle)), 10)

def cosine(angle):
    return round(math.cos(math.radians(angle)), 10)

def tangent(angle):
    rad = math.radians(angle)
    if math.isclose(math.cos(rad), 0, abs_tol=1e-10):
        raise ValueError("Tangent undefined for this angle")
    return round(math.tan(rad), 10)

# Memory functions
def store_memory(value):
    global memory
    memory = value

def recall_memory():
    return memory if memory is not None else "Memory empty"

def clear_memory():
    global memory
    memory = None

import math

# Memory variable
memory = None

# Basic operations
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return "Error! Division by zero." if b == 0 else a / b
def power(a, b): return a ** b
def square_root(a): return "Error! Negative input." if a < 0 else math.sqrt(a)

# Trigonometry
def sine(deg): return math.sin(math.radians(deg))
def cosine(deg): return math.cos(math.radians(deg))
def tangent(deg): return math.tan(math.radians(deg))

# Logarithm and exponential
def logarithm(a): return "Error! Non-positive input." if a <= 0 else math.log10(a)
def exponential(a): return math.exp(a)

# Factorial
def factorial(n): return "Error! Negative input." if n < 0 else math.factorial(n)

# Memory functions
def store_memory(value):
    global memory
    memory = value
    return "Value stored"

def recall_memory():
    return memory if memory is not None else "Memory empty"

def clear_memory():
    global memory
    memory = None
    return "Memory cleared"

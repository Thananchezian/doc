import math

# Basic operations
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y

# Advanced operations
def power(x, y): return math.pow(x, y)
def square_root(x): return "Error! Negative input." if x < 0 else math.sqrt(x)
def sine(x): return math.sin(math.radians(x))
def cosine(x): return math.cos(math.radians(x))
def tangent(x): return math.tan(math.radians(x))
def logarithm(x, base=10): return "Error! Non-positive input." if x <= 0 else math.log(x, base)
def factorial(x): return "Error! Negative input." if x < 0 else math.factorial(int(x))
def exponential(x): return math.exp(x)

# Memory feature
memory = None
def recall_memory(): 
    global memory
    return memory if memory is not None else "Memory empty"
def clear_memory(): 
    global memory
    memory = None
    return "Memory cleared"

# Optional: CLI interface
def main():
    global memory
    while True:
        print("\n=== Advanced Calculator ===")
        print("1. Add  2. Subtract  3. Multiply  4. Divide")
        print("5. Power  6. Square Root  7. Sine  8. Cosine  9. Tangent")
        print("10. Logarithm  11. Factorial  12. Exponential")
        print("13. Recall Memory  14. Clear Memory  0. Exit")
        choice = input("Enter choice: ")

        if choice == '0':
            print("Exiting calculator. Goodbye!")
            break
        elif choice in ['1','2','3','4','5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1': memory = add(num1, num2)
            elif choice == '2': memory = subtract(num1, num2)
            elif choice == '3': memory = multiply(num1, num2)
            elif choice == '4': memory = divide(num1, num2)
            elif choice == '5': memory = power(num1, num2)
            print(f"Result: {memory}")
        elif choice == '6':
            num = float(input("Enter number: "))
            memory = square_root(num)
            print(f"Result: {memory}")
        elif choice == '7':
            angle = float(input("Enter angle in degrees: "))
            memory = sine(angle)
            print(f"Result: {memory}")
        elif choice == '8':
            angle = float(input("Enter angle in degrees: "))
            memory = cosine(angle)
            print(f"Result: {memory}")
        elif choice == '9':
            angle = float(input("Enter angle in degrees: "))
            memory = tangent(angle)
            print(f"Result: {memory}")
        elif choice == '10':
            num = float(input("Enter number: "))
            base = float(input("Enter base (default 10): ") or 10)
            memory = logarithm(num, base)
            print(f"Result: {memory}")
        elif choice == '11':
            num = int(input("Enter integer: "))
            memory = factorial(num)
            print(f"Result: {memory}")
        elif choice == '12':
            num = float(input("Enter number: "))
            memory = exponential(num)
            print(f"Result: {memory}")
        elif choice == '13':
            print(f"Memory: {recall_memory()}")
        elif choice == '14':
            print(clear_memory())
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()

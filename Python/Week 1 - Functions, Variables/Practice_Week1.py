"""
Week 1 Practice File - Functions and Variables
==============================================
This file contains practical exercises covering fundamental Python concepts:
- Basic output and variables
- Function definition and usage
- Conditional statements and comparisons
- Different approaches to solving the same problem
"""

# ========================================
# SECTION 1: Basic Output and Variables
# ========================================

# Simple "Hello World" program - the traditional first program
print('Hello World!')

# Working with variables and different print formatting methods
name = 'Parth'
print('Hello, ', name)                    # Method 1: Comma separation (adds space automatically)
print('Hello, ', name, sep='|')          # Method 2: Custom separator between values
print(f'Hello, {name}')                  # Method 3: f-string formatting (most modern approach)

# ========================================
# SECTION 2: Calculator with Functions
# ========================================

def main():
    """
    Main function for the calculator program.
    Demonstrates user input, function calls, and conditional logic.
    """
    # Get user input for the calculation
    a = float(input('Enter First Number: '))
    b = float(input('Enter Second Number: '))
    c = input('Enter Operation (+,-,*,/): ')

    # Perform the calculation based on the selected operation
    # Each operation is handled by a separate function for modularity
    if c == '+':
        result = addition(a, b)
    elif c == '-':
        result = subtraction(a, b)
    elif c == '*':
        result = multiplication(a, b)
    elif c == '/':
        result = division(a, b)
    else:
        print('Invalid Operation or input')
        return  # Exit early if invalid operation

    # Display the result with 3 decimal places for precision
    print(f'The result of operation {c} on {a} and {b} is {result:.3f}')


# Mathematical operation functions - each handles one specific operation
def addition(n1, n2):
    """Add two numbers and return the result."""
    return n1 + n2

def subtraction(n1, n2):
    """Subtract the second number from the first and return the result."""
    return n1 - n2

def multiplication(n1, n2):
    """Multiply two numbers and return the result."""
    return n1 * n2

def division(n1, n2):
    """Divide the first number by the second and return the result."""
    return n1 / n2

# Execute the calculator program
main()

# ========================================
# SECTION 3: Number Comparison Programs
# ========================================
# This section demonstrates three different approaches to compare two numbers

# APPROACH 1: Traditional if-elif-else structure
def main():
    """
    Compare two numbers using traditional conditional statements.
    This is the most readable and beginner-friendly approach.
    """
    x = int(input('What is x: '))
    y = int(input('What is y: '))

    # Use clear conditional logic to compare the numbers
    if x < y:
        print(f'{x} < {y}')
    elif x > y:
        print(f'{x} > {y}')
    else:
        print(f'{x} = {y}')

main()

# APPROACH 2: Ternary operator (conditional expression)
def main():
    """
    Compare two numbers using nested ternary operators.
    This is more concise but can be harder to read for beginners.
    """
    x = int(input('What is x: '))
    y = int(input('What is y: '))

    # Nested ternary operators: condition_if_true if condition else condition_if_false
    print(f'{x} {'<' if x < y else '>' if x > y else '='} {y}')

main()

# APPROACH 3: Match statement (Python 3.10+)
def main():
    """
    Compare two numbers using match-case with guard conditions.
    This demonstrates pattern matching with conditional guards.
    """
    x = int(input('What is x: '))
    y = int(input('What is y: '))

    # Match statement with guard conditions (if clauses)
    match x:
        case x if x < y:
            print(f'{x} < {y}')
        case x if x > y:
            print(f'{x} > {y}')
        case x if x == y:
            print(f'{x} = {y}')

main()

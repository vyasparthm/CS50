"""
Introduction to Python Functions
================================

This program demonstrates fundamental concepts about Python functions:
1. Function definition and calling
2. The importance of function definition order
3. Function parameters and arguments
4. Default parameter values
5. Function redefinition behavior

Key Learning Points:
- Functions must be defined before they are called (unless using main() pattern)
- Functions can accept parameters to make them more flexible
- Default parameters provide fallback values when arguments aren't provided
- Functions can be redefined, with the latest definition taking precedence

For a better approach to function organization, see functionsDefined.py
"""

# ========================================
# SECTION 1: Basic Function Usage
# ========================================

# Get user input for personalized greeting
name = input("Hi I am Python, what is your name: ")

# Demonstration of function call order importance
# print(f"Hello, {name}")  # Uncomment to see direct output without function

# Hello(name)  # Try uncommenting this line to see why function definition order matters
               # This will cause a NameError because Hello() is not yet defined

# ========================================
# SECTION 2: Function Definition and Calling
# ========================================

def Hello(to):
    """
    A simple greeting function that takes one parameter.

    Args:
        to (str): The name of the person to greet
    """
    print(f"Hello, {to}")

# Call the function with the user's name
Hello(name)

# ========================================
# SECTION 3: Functions with Default Parameters
# ========================================

def Hello(to="World"):
    """
    An improved greeting function with a default parameter.

    Args:
        to (str, optional): The name to greet. Defaults to "World".

    Note: This redefinition overwrites the previous Hello() function.
    """
    print(f"Hello, {to}")

# Call the function without arguments - uses default value
Hello()
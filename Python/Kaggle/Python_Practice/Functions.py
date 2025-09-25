"""
Python Functions Practice - Kaggle Course
==========================================

This file demonstrates key concepts about Python functions:
1. Using the help() function to get documentation
2. Function definition with default parameters
3. Proper docstring placement and formatting
4. Conditional function calls based on user input
5. Input validation and handling empty strings
"""

# ========================================
# SECTION 1: Getting Help on Functions
# ========================================

# Use the built-in help() function to view documentation for any function
# This displays the function's signature, parameters, and description
help(print)

# ========================================
# SECTION 2: Function Definition and Documentation
# ========================================

# Get user input for personalized greeting
name = input('What is your name?')

def hello(to="World"):
    """
    A greeting function that prints a personalized hello message.

    This function demonstrates:
    - Default parameter values
    - Proper docstring formatting
    - Simple output generation

    Args:
        to (str, optional): The name of the person to greet.
                           Defaults to "World" if no argument is provided.

    Returns:
        None: This function prints output but doesn't return a value.

    Example:
        hello("Alice")  # Prints: Hello, Alice
        hello()         # Prints: Hello, World
    """
    print("Hello,", to)

# ========================================
# SECTION 3: Conditional Function Execution
# ========================================

# Check if the user provided a non-empty name (after removing whitespace)
# This demonstrates input validation and conditional logic
if name.strip():  # strip() removes leading/trailing whitespace
    hello(name)   # Call function with user's name if provided
else:
    hello()       # Call function with default parameter if name is empty

# ========================================
# SECTION 4: Viewing Custom Function Documentation
# ========================================

# Uncomment the line below to see the docstring of our custom function
# This will display the documentation we wrote for the hello() function
# help(hello)
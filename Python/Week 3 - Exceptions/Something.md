**Note for 3 Exceptions.txt**

Exceptions in Python refer to problems in your code, where "exceptional" means something has gone wrong that requires handling. Errors can broadly be categorized into syntax errors (must be fixed before execution) and runtime errors (occur while code is running).

Here are three examples of exceptions:

### 1. SyntaxError

A **SyntaxError** is a problem with the code structure or typography that you have typed. These errors must be fixed in the code itself before Python can run the program at all.

```python
# SyntaxError: Occurs due to a structural error, like forgetting a required character.
# The interpreter cannot run the code until this mistake is fixed.
# Example shown is an unterminated string literal (missing closing quote).

print("Hello, world 
```

### 2. ValueError

A **ValueError** is a type of runtime error. It occurs when a function receives an argument that is of the correct type but an inappropriate value. This is often encountered when attempting to convert user input (which is always a string) into an integer (`int`) when the input is non-numeric.

```python
# Handling a ValueError using try and except.

def get_int():
    # Loop indefinitely until valid input is received
    while True:
        try:
            # Attempt to convert user input to an integer (int).
            # This is the line that can raise a ValueError if input is not a number (e.g., "cat").
            x = int(input("What's x? "))
            
        except ValueError:
            # If a ValueError occurs, we catch it and inform the user or handle it.
            # Using 'pass' here silently ignores the error and keeps the loop running, re-prompting the user.
            pass 
        
        else:
            # The 'else' clause executes only if the code in 'try' succeeds without raising an exception.
            # Since the operation was successful, we break out of the infinite loop.
            break 
            
    return x
```

### 3. NameError

A **NameError** typically refers to an error where a variable name is used but has not been defined. This frequently happens in programs utilizing exception handling if an exception occurs during a variable assignment operation. The assignment is interrupted, preventing the variable from ever being initialized.

```python
# NameError: Occurs when trying to access a variable name that is not defined.
# This can happen if an assignment (like x = int(input(...))) fails due to an earlier exception.

try:
    # If the user types a non-integer, ValueError occurs, 
    # and the assignment of 'x' is prevented.
    y = int(input("Enter a number: "))
    
except ValueError:
    print("Invalid input received.")
    
# If the try block failed, 'y' was never defined, and the code below will fail 
# with a NameError because it attempts to use the undefined variable 'y'.
# If using a try-except structure, the logic should be structured 
# using the 'else' keyword or return values to avoid this.

# Example of NameError resulting from failed assignment:
# print(y) 
```
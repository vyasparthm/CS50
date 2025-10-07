These study notes summarize the concepts and syntax related to exceptions, drawing solely on the provided sources.

---

# Study Notes: 3 Exceptions

Exceptions refer to **problems in your code**. When something is exceptional, it means **something has gone wrong** that should ideally be solved. Programmers should write code defensively, anticipating unexpected user input.

## I. Types of Errors

| Error Type | Description | Cause/Example | Notes |
| :--- | :--- | :--- | :--- |
| **Syntax Error** | A problem with the code typed by the programmer (e.g., typographical mistake). | Forgetting to close a quote (`"hello, world` missing the final `"`).. | **Must be fixed manually**; cannot be resolved by subsequent code or error handling. |
| **Runtime Error (Exception)** | Errors that occur **while the code is running**. These usually stem from unexpected values or operations. | Handled using `try` and `except`. |
| **Value Error** | Occurs when an input value is inappropriate for the operation being attempted. | Passing a non-numeric string (e.g., `"cat"`) to the `int()` function, which expects base 10 (decimal system) numbers. |
| **Name Error** | Occurs when code references a variable that has **not been defined**. | If a Value Error occurs during assignment (`x = int(input(...))`), the exception interrupts the process, and the variable (`x`) is never successfully defined, leading to a Name Error later when the code attempts to use it. |

Why the variable X is not printing: Assignment Interruption When an exception (like a Value Error) occurs during the assignment process (x = int(input(prompt))), the error interrupts the copying of the value from the right side of the assignment operator (=) to the left side. Because the error happens before assignment, the variable (x) is effectively never defined. If subsequent code attempts to use this undefined variable, a Name Error results.

## II. Handling Exceptions (The `try-except-else` Block)

The fundamental syntax for defensive programming involves three optional components to manage control flow when failures occur:

| Keyword | Purpose | Syntax | Execution Flow |
| :--- | :--- | :--- | :--- |
| **`try`** | Specifies the minimal block of code that might raise an exception. | `try:` <br> `    # Indented code to attempt` | Always attempted first. |
| **`except`** | Specifies the specific type of exception to handle and the code to run if that exception occurs. | `except ValueError:` <br> `    # Indented error handling code` | Only executes if the specific error is raised in the `try` block. Generally better practice than catching all errors. |
| **`else`** | Specifies code that **only executes if the `try` block succeeds** (i.e., no exception occurred). | `else:` <br> `    # Indented success code` | Crucial for avoiding Name Errors: ensures subsequent logic that relies on a variable defined in `try` only runs if the definition was successful. |
| **`pass`** | Used inside an `except` block to **silently ignore** the error. It catches the exception but takes no further action, allowing the loop to continue. | `except ValueError:` <br> `    pass` |

## III. Combining Exceptions with Loops and Functions

A common programming paradigm in Python is to use an infinite loop (`while True`) combined with `try/except` to continuously prompt the user until they provide valid input.

### Syntax for Continuous Reprompting

```python
while True: # Deliberately induces an infinite loop
    try:
        # 1. Attempt the operation (e.g., getting and converting input)
        x = int(input("What's x? ")) 
    except ValueError:
        # 2. If failure, handle the exception (e.g., give feedback)
        print("x is not an integer") 
    else:
        # 3. If success, exit the loop
        break 

# Code execution continues here once loop is broken
print(f"x is {x}")
```

### Functions and Return Values

When creating a reusable function (an abstraction) to handle input, the preferred method to exit the loop upon success is using `return`, which is "sort of stronger than break".

| Keyword | Context | Effect |
| :--- | :--- | :--- |
| **`break`** | Inside a loop (e.g., `while True`). | Breaks execution out of the most recently started loop. |
| **`return`** | Inside a custom function. | Breaks execution out of the loop *and* hands back a specified value to the caller. |

**Refined Function Definition (Example `get_int`):**

A custom function can be defined to handle input defensively and return the value, often taking a `prompt` argument to make it reusable:

```python
def get_int(prompt): # Function takes a 'prompt' parameter
    while True:
        try:
            # Returns the integer result immediately upon success
            return int(input(prompt)) 
        except ValueError:
            # Handles failure by continuing the loop (e.g., silent reprompt)
            pass 
            
# Caller uses the function:
def main():
    x = get_int("What's x? ") # Passes the required prompt as an argument
    # ...
```

***Note on Code Style:*** While using conditional checks (e.g., `is numeric`) is a valid strategy, the sources suggest the "Pythonic" way is often to use **exceptions (try/except)** to handle errors rather than preemptively checking conditions.
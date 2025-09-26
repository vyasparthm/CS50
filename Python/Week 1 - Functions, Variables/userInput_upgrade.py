"""
Improved version of userInput.py demonstrating efficient string processing.

This program shows how to chain multiple string methods together to:
1. Clean user input (remove whitespace)
2. Format names properly (title case)
3. Extract individual parts of the name
4. Minimize code while maximizing functionality

This is a more concise and efficient approach compared to the step-by-step
method shown in userInput.py.
"""

# Get user input and immediately apply string cleaning and formatting
# Chaining methods: strip() removes whitespace, title() capitalizes each word
name = input("Hello, I am Python, what is your name?").strip().title()

# Display the formatted name using f-string formatting
print(f"1. Hello, {name}, How are you doing today?")

# Extract individual parts of the name using string splitting
# split(" ") divides the string at spaces and returns a list of words
# We use tuple unpacking to assign the first and last names to separate variables
first, last = name.split(" ")

# Print only the first name for a more personal greeting
print(f"Hello, {first}")




"""
Simple program demonstrating user input and various string manipulation techniques.
This program shows different ways to format output and manipulate user input strings.
"""

# Get user input and store it in a variable for later use
# The input() function prompts the user and returns their response as a string
name = input("Hello, I'm Python, what's your name?")

# Demonstrate different ways to print user's input stored in variable 'name'
# All the methods below accomplish the same goal but use different string formatting approaches

print("1. Hello, "+ name)  # Method 1: String concatenation using the + operator

print("2. Hello, ", name, ". How are you today?")  # Method 2: Using comma to print multiple values

print(f"3. Hello, {name}")  # Method 3: f-string formatting (most modern and preferred)

# String cleaning: Remove any leading/trailing whitespaces from user input
# This handles cases where users accidentally add spaces before or after their name
name = name.strip()  # strip() removes whitespace from both ends of the string
print(f"4. Hello, {name}")

# String case manipulation: Capitalize only the first character of the string
# capitalize() makes the first character uppercase and the rest lowercase
name = name.capitalize()
print(f"5. Hello, {name}")

# Title case: Capitalize the first letter of each word (useful for names)
# title() capitalizes the first letter of each word in the string
name = name.title()
print(f"6. Hello, {name}")

# Convert entire string to uppercase
# upper() transforms all characters to their uppercase equivalents
name = name.upper()
print(f"7. Hello, Upper case, {name}")

# Convert entire string to lowercase
# lower() transforms all characters to their lowercase equivalents
name = name.lower()
print(f"8. Hello, Lower case, {name}")

# Demonstration of different ways to include quotation marks within strings
print("9. Hello, ""Bud"  "")          # Method 1: Double quotes within double quotes (concatenation)

print("10. Hello,\"Bud\"  ")          # Method 2: Escape quotes using backslash

print("11. Hello, 'bud' ")            # Method 3: Single quotes within double quotes

# Best practice: Chain multiple string methods together for efficient processing
# This combines strip() to remove whitespace and title() to capitalize properly
name = name.strip().title()

print(f"12. Hello, {name}")  # Final formatted output with clean, properly capitalized name



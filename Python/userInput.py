# Simple program to get the user input their name
#Input fuction basically takes a user's input, lets put it in a variable so we can print it later
name = input("Hello, I'm Python, what's your name?")

#print user's input stored in varibvale name
# All theww below does the same thing but there is a difference in the way of doing things
print("1. Hello, "+ name) # You can use + to concat strings

print ( "2. Hello, ", name, ". How are you today?") # or use a comma to print multiple values

print(f"3. Hello, {name}")

#lets remove any whitespaces if a user has unintentionally put any white spaces..

name = name.strip() #strip gets rid of white spaces from strings
print(f"4. Hello, {name}")

# How about Captilazing first character?

name = name.capitalize()
print(f"5. Hello, {name}")

#When you wasnt first and last name capitalized
name = name.title()
print(f"6. Hello, {name}")

# How to use quatation marks within the string???
print("1. Hello, ""Bud"  "")

print("2. Hello,\"Bud\"  ")

print("3. Hello, 'bud' ")




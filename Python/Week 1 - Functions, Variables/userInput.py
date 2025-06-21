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

#Convert Everything to Upper Case
name = name.upper()
print(f"7. Hello, Upper case,{name}")

#Convert Everything to Lower Case
name = name.lower()
print(f"8. Hello, Lower case,{name}")

# How to use quatation marks within the string???
print("9. Hello, ""Bud"  "")

print("10. Hello,\"Bud\"  ")

print("11. Hello, 'bud' ")


# How about doing everything together? Make user name in title case and strip off extra spaces?

name = name.strip().title()

print(f"11. Hello, {name}")



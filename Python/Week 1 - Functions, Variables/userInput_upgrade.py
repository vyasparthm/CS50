""" In userInput.py we saw that we needed to write multiple lines just to print a user's name.
    in this code, we can see that we can do all of the good stuff to avoid user's inintentional mistakes and minimize  the lines of code

"""

# Ask for input
name = input("Hello, I am Python, what is your name?").strip().title()

#Print it
print(f"1. Hello, {name}, How are you doing today?")


#Split user's name and print first name

first,last = name.split(" ")

print(f"Hello, {first}")




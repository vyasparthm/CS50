"""
This code will show us the functions and what we can do with them. Lets define a simple function and go from there
If the function is is not defined before its used, it will throw an error!!, try uncommenting line 10 and see how it goes

There is a better and standard way so that you don't have to keep defining functions before you get to use them, look into functionsDefined.py
"""

#Let's make a function to Print Hello from what we did earlier.

name = input("Hi I am Python, what is your name: ")
# print(f"Hello, {name}") #Uncomment to see the effect of function

# Hello(name) #Try uncommenting this to see why order of defination of function matters

#Define a function called Hello with input parameter, to here will replace the input parameter


def Hello(to):
    print(f"Hello, {to}")

Hello(name)    

# How anout a default value?


def Hello(to ="World"):
    print(f"Hello, {to}")

Hello()    
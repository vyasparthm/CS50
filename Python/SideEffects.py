"""
Here we will see a side effect in action. 
What is a Side Effect?
    A side effect in a function refers to any change or interaction that a function makes beyond its return value. 
    It's an action that affects the state outside the function's scope or has an observable effect beyond the function's output.
Let's say I have a global variable (counter) and I am trying to modify it in a function down the line but that global variable is also being reffered somewhere below,
now that value is changed.

Comment/
"""

counter = 0

def increment_counter():
    global counter # Comment this line and you will notice python giving an error : UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value
    
    counter =  counter + 1
    return counter

print(increment_counter())

print(counter) # I called the function before this print, so now it prints the updated value
"""
This code file will explain for loops.
"""

# # Lets start with the meowing cat

# for i in [0,1,2]:
#     print('Meow',end= ' ')

## One more way for count for for loops

# help(range)

# for i in range(3):
#     print('Meow', end= ' ')

## Pythonic way of doing things:
## if you do not plan to use the variable i again later in the code, you can just use "_" in loop.


# for _ in range(3):
#     print('Meow', end= ' ')

## Strings can also multiply while printing    
# print('Meow\n' * 3)

## Now lets get input from user and meow that many times

# n = int(input('How many meows did you want?: '))
# for _ in range(n):
#     print ('Meow', end=' ')
# print(f'\n Printed Meow: {n} times')


## How about combining the loops? 
## This will be helpful to keep the program on util a valid input value is received.
# while True:
#     n = int(input('How many meows did you want again?: '))
#     if n > 0:
#         break
# for _ in range(n):
#     print('Meow')

# #  Lets put things in a function
def main():
    n = int(input('How may meows did you want?: '))
    meow(n)
    print(f'\nPrinted Meow: {n} times')

def meow(x):
    for _ in range(x):
        print('Meow', end=' ')

main()


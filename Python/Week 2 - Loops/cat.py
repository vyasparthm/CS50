"""
This code file will show how we can use  while loop in python.
"""

# i = 0

# while i <3:
#     print('Meow', end=' ')
#     i += 1
# print('\n','Finish')
# # OR the below if you prefere to count towards 0
# i = 3
# while i!=0:
#     print('Meow', end=' ')
#     i -= 1
# print ('\n','Finish')    

## Or how about taking a user input
while True:
    n = int(input('How many meows did you want again?: '))
    if n > 0:
        print('Meow', end=' ')

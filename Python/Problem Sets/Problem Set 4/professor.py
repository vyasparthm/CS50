'''
In a file called professor.py, implement a program that:

Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with n digits. No need to support operations other than addition (+).
Note: The order in which you generate x and y matters. Your program should generate random numbers in x, y pairs to simulate generating one math question at a time (e.g., x0 with y0, x1 with y1, and so on).

Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user's score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a single randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
'''

import random

def main():
    level = get_level()
    score = 0
    for problem in range(0,10):
     x = get_integer(level)
     y = get_integer(level)
     print(f'{x} + {y} = ')
     
     for attempt in range(0,3):
         
         try:
            answer = int(input(''))
            if x + y == answer:
                score += 1
                break
            else:
                print('EEE')
                print(f'{x} + {y} = ',sep= '')
                if attempt == 2:
                    print(f'Correct Answer = {x + y}')
         except ValueError:
            print('Only Numbers are allowed!')
            print(f'{x} + {y} = ',sep= '')
    
    
    print(f'Score: {score}')
     
         

def get_level():
    while True:
        try: 
            x = int(input('Enter Level: '))
            if x not in range(1,4):
                print('Valid choices are: 1 or 2 or 3\nTry Again!')
                continue
            else:         
                return x
        except ValueError:
            print('EEE')
        

     

def get_integer(n):
     return random.randint(10**(n-1),10** n-1)





if __name__ == '__main__':
    main()
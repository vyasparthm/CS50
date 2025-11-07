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
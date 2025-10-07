'''
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. 
For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py,
 implement a program that:->
   1. prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is a positive integer, and then outputs,
      as a percentage rounded to the nearest integer, how much fuel is in the tank.
        If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
        And if 99% or more remains, output F instead to indicate that the tank is essentially full.

    2. If, though, X or Y is not an integer, X is greater than Y, or Y is 0,
      instead prompt the user again. (It is not necessary for Y to be 4.) 
Be sure to catch any exceptions like ValueError or ZeroDivisionError.
'''
def main():
    while True:
        user_input = input('Enter fraction:')
        
        try:
            result = get_fraction(user_input)
            if result == None:
                continue
            else:
                print(result)
                break

        except ValueError:
            print ('Cannot Enter non numerical values!!')  
            continue
        except ZeroDivisionError:
            print('Cannot Divide by Zero')
            continue
        


        


def get_fraction(n):
    numbers = n.split('/')
   
    if len(numbers) != 2:
        return None
    elif numbers[0].isdigit() == False or numbers[1].isdigit() == False:
        raise ValueError 
    elif int(numbers[1]) == 0:
        raise ZeroDivisionError
    elif int(numbers[0]) > int(numbers[1]):
        return None   
    else :
        fuel_percentage= int(numbers[0]) / int(numbers[1])*100
        if fuel_percentage <= 1:
            return 'E'
        elif fuel_percentage >= 99:
            return 'F'
        else:
            return (f'{round(fuel_percentage)}%')

if __name__ == '__main__':
    main()
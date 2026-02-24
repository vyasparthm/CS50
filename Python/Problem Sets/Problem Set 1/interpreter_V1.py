'''
In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place.
Assume that the user's input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

    x is an integer
    y is +, -, *, or /
    z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.
'''


def expression_result(x:int,y:str,z:int):
    '''Takes 3 values and performs mathematical calculation based on values and expression'''
    if y == '+':
        return x + z
    elif y == '-':
        return x - z
    elif y == '/' and z != 0:
        return x/z
    elif y == '*':
        return x*z
    else:
        return ' Invalid expression!'
    


def main():
    x,y,z = input('Enter expression: ').split()
    a= int(x)
    b = str(y)
    c= int(z)
    print(f"The result: {expression_result(a,b,c)}")

if __name__ == '__main__':
    main()


    
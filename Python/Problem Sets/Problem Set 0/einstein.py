'''
Einstein
Even if you haven’t studied physics (recently or ever!), you might have heard that 𝐸 =𝑚⁢𝑐2, 
wherein 𝐸 represents energy (measured in Joules),
        𝑚 represents mass (measured in kilograms), 
        𝑐 represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. 
 Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the user for:
mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
'''

def main():
    c = 300000000
    m = int(input("Enter Mass m(Integers only): "))
    print ('The Energy, E = ', m * int(pow(c,2)))
    

if __name__ == '__main__':
    main()

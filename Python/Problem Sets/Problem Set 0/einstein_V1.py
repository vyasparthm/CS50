'''
Einstein
Even if you haven't studied physics (recently or ever!), you might have heard that E =mc2, 
wherein E represents energy (measured in Joules),
        𝑚 represents mass (measured in kilograms), 
        c represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. 
 Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the user for:
mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
'''

c = 300000000

def  mass_energy(number:int) -> int:
    """Calculates multiplication of input value and square of speed of light
       Assumption: User will always input an integer. 
    """
    return number * pow(c,2)

def main():
    user_input = int(input("Enter value of mass(Numbers only): "))
    print(f"E = {mass_energy(user_input)}")

if __name__ == "__main__":
    main()
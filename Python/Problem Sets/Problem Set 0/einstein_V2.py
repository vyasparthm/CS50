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
c = 300000000 # Speed of light as a hard coded constant

def main():
    user_input = int(input("Enter the value of mass in kilograms:"))
    print(energy_calculator(user_input))


def energy_calculator(mass:int)->int:
    return f"The Energy E ={mass * pow(c,2)} as per Einstein's formula"




if __name__ =="__main__":
    main()
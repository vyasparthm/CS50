"""
Author: Parth V.
Usage: This is a simple python program to demonstrate a simple calculation in python.

"""


def main():
    mass = int(input("Enter Mass, I'll give you E:"))
    
    print(f"Here is the Energy (E): {energy(mass)}")

def energy(n):
    c = 300000000 
    return n * pow(c,2)

if __name__ == "__main__":
    main()

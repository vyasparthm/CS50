"""
Author: Parth V.
Usage: This is a simple python program to demonstrate how we can convert strings to lower case in python.

"""


def main():
    statement = str(input("Enter your statement: "))
    print(f"Better use your indoor voice and say: {indoorVoice(statement)}")
    

def indoorVoice(text):
    return text.lower()

## Added this line guard to make the script more modular
if __name__ == "__main__":
    main()
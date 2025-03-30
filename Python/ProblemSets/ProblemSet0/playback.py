"""
Author: Parth V.
Usage: This is a simple python program to demonstrate how we can replace values in strings in python.

"""

def main():
    statement = str(input(" Say Something: "))
    print(f"Here is slower playback: {playback_speed(statement)}")


def playback_speed(text):
    return text.replace(" ","...")


if __name__ == "__main__":
    main()
'''
Some people have a habit of lecturing speaking rather quickly, and it'd be nice to slow them down, a la YouTube's 0.75 playback speed, or even by having them pause between words.
In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).
'''

def main():
    user_input = str(input("What do you want to talk about today? "))
    print(playback(user_input))


def playback(string:str)->str:
    return string.strip().replace(" ","...")

if __name__ == "__main__":
    main()
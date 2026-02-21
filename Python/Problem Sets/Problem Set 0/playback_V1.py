'''
Playback Speed
Some people have a habit of lecturing speaking rather quickly, and it'd be nice to slow them down, a la YouTube's 0.75 playback speed,
 or even by having them pause between words.

In a file called playback.py, 
implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).
'''

def playback(text:str) -> str:
    """ This function replaces space with  three dots showing an example how replace works """
    return text.strip().replace(" ","...")

def main():
    user_input = input("Enter string: ")
    print(playback(user_input))

if __name__ == '__main__':
    main()
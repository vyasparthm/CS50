'''
Indoor Voice
WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called IndoorVoice.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. 
Punctuation and whitespace should be outputted unchanged. You're welcome, but not required,
 to prompt the user explicitly, as by passing a str of your own as an argument to input.
'''
def main():
    voice_input = input("What sis you want to say? ")
    print (f"Shhh, use your indoor voice, say like this: {convert_to_lowercase(voice_input)}")


def convert_to_lowercase(text: str) -> str:
    """
    Converts the input string to lower case
    """
    return text.lower()

if __name__ == '__main__':
    main()
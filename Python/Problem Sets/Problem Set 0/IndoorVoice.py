'''
Indoor Voice
WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called IndoorVoice.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. 
Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required,
 to prompt the user explicitly, as by passing a str of your own as an argument to input.
'''

def main():
    userInput = str(input('What did you want to say? '))
    indoor(userInput)

def indoor(strings):
    print('Hey, We''re indoor, use your indoor voice:', strings.lower())

main()    

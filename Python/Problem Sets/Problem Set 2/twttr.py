'''
When texting or tweeting, it's not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr.
In a file called twttr.py,
 implement a program that prompts the user for a str of text and then outputs that same text
   but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
'''

def main():
    vovels = ['a','e','i','o','u']
    user_input = str(input('Enter String to Shorten: ')).lower()
    print(shorten_string(vovels,user_input))

    
def shorten_string(value: list,inpt: str):    
    for i in value:
        inpt = inpt.replace(i,'')
    return inpt        
        
main()        






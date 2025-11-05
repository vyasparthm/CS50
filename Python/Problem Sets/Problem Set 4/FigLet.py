r'''FIGlet, named after Frank, Ian, and Glen's letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:

 _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/
Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

In a file called figlet.py, implement a program that:

    Expects zero or two command-line arguments:
        Zero if the user would like to output text in a random font.
        Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
    Prompts the user for a str of text.
    Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
'''
from pyfiglet import Figlet
import sys
import random


figlet = Figlet()
font_list = figlet.getFonts()
# print(font_list)
if len(sys.argv) not in(1,3):
    sys.exit('Inappropriate number of Arguments')
elif len(sys.argv) == 3:
      if sys.argv[1] not in ('-f','--font') :
            sys.exit('First argument needs to be -f or --font')
      if sys.argv[2] not in font_list:
            sys.exit('Font Not found!!')
      figlet.setFont(font= sys.argv[2])
      
      
else:
    figlet.setFont(font=random.choice(font_list))
    
user_input = str(input('Enter String: '))
print(figlet.renderText(user_input))


        
    



# C:\Users\Parth\CS50\CS50\Python\Problem Sets\Problem Set 4

# f = Figlet()
# print(f.renderText('text to render'))
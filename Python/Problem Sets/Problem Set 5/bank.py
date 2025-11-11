'''
In a file called bank.py, implement a program that prompts the user for a greeting.
 If the greeting starts with “hello”, output $0. 
 If the greeting starts with an “h” (but not “hello”), output $20.
   Otherwise, output $100. 
   ** Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
'''
def main():
     userinput = str(input('Greeting: ').lower().strip())
     print(verifyGreeting(userinput))

def verifyGreeting(value):
     value = str(value).lower().strip()  
     if value[0] == 'h' and 'hello' not in value:
          return ('$20 for you')
     elif 'hello' in value:
          return ('$0 for you')
     else:
          return ('$100 for you')



if __name__ == '__main__':
     main()
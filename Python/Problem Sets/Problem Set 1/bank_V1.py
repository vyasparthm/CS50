'''
In a file called bank.py, implement a program that prompts the user for a greeting.
 If the greeting starts with “hello”, output $0. 
 If the greeting starts with an “h” (but not “hello”), output $20.
   Otherwise, output $100. 
   ** Ignore any leading whitespace in the user's greeting, and treat the user's greeting case-insensitively.
'''

def check_greeting(greeting:str) -> str:
    """Determine payout based on the specific greeting prefix."""
    cleaned_greeting = greeting.strip().lower()
    
    if cleaned_greeting.startswith('hello'):
        return 0
    elif cleaned_greeting.startswith('h'):
        return 20
    else:
        return 100



def main():
    user_input = input('Welcome to the Bank of Avengers, how may I help? ')
    amount = check_greeting(user_input)
    print(f"${amount}")

if __name__ == '__main__':
    main()    
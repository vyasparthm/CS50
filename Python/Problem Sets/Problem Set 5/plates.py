'''
In Massachusetts, home to Harvard University, it's possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

1. “All vanity plates must start with at least two letters.”
2. “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
3. “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0'.”
4. “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not.
 Assume that any letters in the user's input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
   Assume that s will be a str. You're welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
'''

def main():
    plate = input('Enter proposed plate: ').upper()
    if is_valid(plate):
        print('Valid')
    else:
        print('Not Valid')



def check_len(user_input):
    if  2 <= len(user_input) <=6 :
        # print('Matches length criteria')
        return True
    else:
        # print('Enter plate with at least 2 characters or 6 characters max ')
        return False

def starts_with(user_input):
    if user_input[0:2].isalpha():
        # print('Passed 1 ,Starts with 2 letters')
        return True
    else:
        # print('First two lettrs needs to be characters not numbers')    
        return False

def numbers_middle(user_input):
    ## Now the below one passes for the most cases, it doesn't pass for soemthing like "A23A3"
    # if len(user_input) >0 and user_input[len(user_input) - 1].isalpha():
    #     print ('numbers not allowed in middle')
    #     return False
    # else:
    #     print('Passed Number in the middle')
    #     return True
    
    ## Lets check where the first digit start
    ## Debug Only
    # print(f"numbers_middle called with: '{user_input}'")
    # print(f"Type: {type(user_input)}, Length: {len(user_input)}")

    first_digit_pos = None
    for i, char in enumerate(user_input):
        # print(f"Checking char at {i}: '{char}', isdigit: {char.isdigit()}")
        if char.isdigit():
            first_digit_pos = i
            break
    ## if no numbers then True
    if first_digit_pos == None:
        return True
    
    if user_input[first_digit_pos] == '0':
        return False
    
    # Add this print to debug
    # print(f"Checking from position {first_digit_pos}: {user_input[first_digit_pos:]}")
    
    # # Check if all characters after first number are Digits
    for char in user_input[first_digit_pos:]:
        if not char.isdigit():
            # print(f"Found non-digit: {char}")  # Add this too
            return False
    return True

def non_alpha_numeric(user_input):
    return user_input.isalnum()
def is_valid(user_input):
    # print(f"is_valid called with: '{user_input}'")
    # print(f"check_len: {check_len(user_input)}")
    # print(f"starts_with: {starts_with(user_input)}")
    # print(f"numbers_middle: {numbers_middle(user_input)}")
    # print(f"non_alpha_numeric: {non_alpha_numeric(user_input)}")
    return( check_len(user_input) and  starts_with(user_input)  and   numbers_middle(user_input)  and    non_alpha_numeric(user_input))
        


    


if __name__ == '__main__':
    main()

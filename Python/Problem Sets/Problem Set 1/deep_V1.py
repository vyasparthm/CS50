'''
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life,
 the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two.
 Otherwise output No.
'''


def check_answer(text:str) ->str:
    '''Checks if the Value entered by user matches 42, case insensitive'''
    if text.lower() in ('42','forty-two', 'forty two'):
        return "Yes"
    else:
        return 'No'




def main():
    user_input = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    print(check_answer(user_input))



if __name__ == '__main__':
    main()
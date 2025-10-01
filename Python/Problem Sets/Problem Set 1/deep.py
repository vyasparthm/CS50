'''
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life,
 the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two.
 Otherwise output No.
'''

def main():
    userinput = str(input('What is the Answer to the great Question of Life, the Universe and Everything?  '))
    checkAns(userinput)


def checkAns(value):
    '''
    This will check our answer and if the Answer is in the below fgorms of 42 then print yes!!
    '''
    if value  in ('42','Forty-two','forty two','fortytwo'):
        print('Yes!!')
    else:
        print('NO.')




if __name__ == '__main__':
    main()
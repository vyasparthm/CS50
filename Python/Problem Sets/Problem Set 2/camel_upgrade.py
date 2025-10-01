'''
A little bit of upgraded version, just so that you can ignore consecutive Uppercase letters, Example: HELLOMyNameIsParth will print: HELLO_My_Name_Is_Parth

'''
def main():
    camelcase = input('Enter CamelCase Input: ')
    camel(camelcase)

def camel(camelcase):
    #Track if there is an empty string
    if not camelcase:
        print('Empty String!')
    
    #print first character As-Is
    print(camelcase[0], end='')

    # First we will ignore the first character because we already printed that
    for i in range(1,len(camelcase)):
        current = camelcase[i]   # for tracking keep current character in memory for comparison
        previous = camelcase[i-1] # for tracking keep previous character in memory for comparison
        
        # if currenct character is upper and next is lower then add underscore before current
        if current.isupper() and previous.islower():
            print('_',current,end='',sep='')
        
        # this is where we handle the case of multiple upper characters together
        elif current.isupper() and previous.isupper() and i+1 < len(camelcase) and camelcase[i+1].islower():
            print('_',current, end ='', sep='')
        
        #no uppercase anywhere? that gotta be a straight up print
        else:
            print(current,end='',sep='')


if __name__ == '__main__':
    main()           
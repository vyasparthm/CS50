name = input("Enter name: ")


## This will automatically close the file, one less thing to remember and less lines of code
with open('names.txt','a') as file:
    file.write(f'{name}\n')

## Not so pythonic though
# file.close()




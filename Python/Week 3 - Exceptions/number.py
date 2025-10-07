
while True:
    try:
        x = int(input('Enter number: '))
        
    except ValueError:
        print('X is not an integer, Please enter integer.')
    else:
        break

print(f'X is: {x}')
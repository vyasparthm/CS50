import emoji as e

def main():
   while True:
    user_input = str(input("Enter text for Emoji: "))
    result = e.emojize(user_input, language= 'alias')
   
    if result != user_input:
        print(result)
        break
    else:
        print('Emoji not found, Try again!')
        
    

main()




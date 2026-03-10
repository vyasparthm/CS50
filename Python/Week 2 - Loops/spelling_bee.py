words = {"Pair": 4,"hair":4,"chair":5}

def main():
    print("Welcome to Spelling bee!")
    print("Your letters are: A I P C R H G")
    score = 0
 

    while len(words)>0:
        print(f"{len(words)} words left")
        guess = input("Guess a word: ")
        
        if guess in words.keys():
            points = words.pop(guess)
            score += points
            print(f"Good, you scored {score} in total.")
            # print(f"Good, you scored {words[guess]} Points")
            
            
            
        else:
            print("Try Again")

if __name__ == '__main__':
    main()
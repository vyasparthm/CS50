def main():
    vowel = ["a","e","i","o","u"]
    user_input = input("Enter a tweet: ")
    final_tweet =""

    final_tweet = user_input.translate(str.maketrans("","","aeiouAEIOU"))
      
    print(final_tweet)




if __name__ == "__main__":
    main()
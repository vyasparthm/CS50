def main():
    ## 1. Print Everything manually
    # print(write_letter("Mario", "Princess Peach"))
    # print(write_letter("Luigi", "Princess Peach"))
    # print(write_letter("Daisy", "Princess Peach"))
    # print(write_letter("Yoshi", "Princess Peach"))
    

    ## 2. Loop and List
    receivers = ["Mario","lugi","Daisy","Yoshi"]
    sending_party = "Princess Peach"
    for receiver in receivers:
        print(write_letter(receiver,sending_party))



def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {receiver},
    
       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+ 
    """


main()

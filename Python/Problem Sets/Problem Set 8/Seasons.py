from datetime import date
import inflect 


class BirthdayToMinutes:
    def __init__(self,bday_str):
        self.bday = self.verify_Birthday(bday_str)

        
    def verify_Birthday(self,bday_str):
     try:
         formatted_bday = date.fromisoformat(bday_str)
         return formatted_bday
     except ValueError:
         return "Wrong birthday or format, try again"
    
    def calculate_time(self):
        days_elapsed = date.today() - self.bday
        return days_elapsed.days * 24 * 60



def main():
    dob = input("What is your birthday?(YYYY-MM-DD) ")
    dob_verification = BirthdayToMinutes(dob)
    minutes = dob_verification.calculate_time()
    p = inflect.engine()
    minutes_words = p.number_to_words(minutes, andword="").capitalize()
    print (f"Its been: {minutes_words} minutes")


    
    
    


if __name__ == "__main__":
    main()

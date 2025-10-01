'''
Suppose that you’re in a country where it’s customary to eat 
    breakfast between 7:00 and 8:00, 
    lunch between 12:00 and 13:00, and 
    dinner between 18:00 and 19:00. 
Wouldn’t it be nice if you had a program that could tell you what to eat when?

In meal.py, implement a program that prompts the user for a time and outputs whether it's breakfast time, lunch time, or dinner time.
 If it's not time for a meal, don't output anything at all. Assume that the user's input will be formatted in 24-hour time as #:## or ##:##. 
 And assume that each meal's time range is inclusive. For instance, whether it's 7:00, 7:01, 7:59, or 8:00, or anytime in between, it's time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time,
 a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
'''

def main():
    timeinput = input('Enter Time in 24 hour format(HH:MM): ')
    convert(timeinput)

def convert(value):
    if '07:00' <= value <= '08:00':
        print('Good morning!!! Breakfast Time!')
    elif '12:00' <= value <= '13:00':
        print('Afternoon! It is lunch Time')
    elif '18:00' <= value <= '19:00':
        print('Good Evening! Ready for Dinner?')
    else:
        print('Are you sure this is the right time to eat?')
if __name__ == '__main__':
    main()
'''
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order,
 which is arguably bad design. Dates in that format can't be easily sorted because the date's year comes last instead of first.
 Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). 
 Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601,
 an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, 
 no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date,
 anno Domini, in month-day-year order,
   formatted like 9/8/1636 or September 8, 1636,
   wherein the month in the latter might be any of the values in the list below:

Then output that same date in YYYY-MM-DD format.
 If the user's input is not a valid date in either format, 
 prompt the user again. 
 Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
'''
from datetime import datetime as dt

def main():
    
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    months_dict = {}
    for i in range(len(months)):
        months_dict[months[i]] = f'{i+1:02}'



    date_by_user = input('Enter Date: ').title()
    ## strptime is too libral, it will accept anything as input and if user inserts: July 93, 2020 it will fail
    # while True:
    #     try:
    #         if '/' in user_input:
    #             date_obj = dt.strptime(user_input, '%m/%d/%Y').date()
    #         elif ',' in user_input:
    #             date_obj = dt.strptime(user_input, '%B %d, %Y').date()
    #         else:
    #             raise ValueError('Invalid Format')
    #         print(date_obj)
    #         break
    #     except:
    #         print('Invalid input')
    print(print_date(date_by_user,months_dict))

    
def print_date(user_input,dict_months):
    while True:
        if '/' in user_input:
             month = user_input.split('/')[0]
             if month in dict_months.get(month):
                day =  user_input.split('/')[1]
                if int(day) in range(1,31):
                    year =  user_input.split('/')[2]
                    return f'{year}-{month}-{day:02}'
                break
        elif ',' in user_input:
            
            if not dict_months.get(user_input.split()[0]):
                print('Incorrect Month, Try Again!!')
                continue
            elif  dict_months.get(user_input.split()[0]):        
                day = user_input.split()[1].replace(',','')
                month =  dict_months.get(user_input.split()[0])
                day = int(day)
                if day in range(1,31):
                    year = user_input.split()[2]
                    return f'{year}-{month}-{day:02}'
                break
                
            else:
                continue
                


if __name__ == '__main__':
    main()
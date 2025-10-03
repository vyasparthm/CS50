'''
In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit,
   per the FDA's poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry).
   Ignore any input that isn't a fruit.
'''

def main():
    fruit_Cal=[
                {'Fruit': 'Apple', 'Calories': 130},
                {'Fruit': 'Avocado California', 'Calories': 50},
                {'Fruit': 'Banana', 'Calories': 110},
                {'Fruit': 'Cantaloupe', 'Calories': 50},
                {'Fruit': 'Grape Fruit', 'Calories': 60},
                {'Fruit': 'Grapes', 'Calories': 90},
                {'Fruit': 'Honeydew Melon', 'Calories': 50},
                {'Fruit': 'Kiwi Fruit', 'Calories': 90},
                {'Fruit': 'Lemon', 'Calories': 15},
                {'Fruit': 'Lime', 'Calories': 20},
                {'Fruit': 'Nectarine', 'Calories': 60},
                {'Fruit': 'Orange', 'Calories': 80},
                {'Fruit': 'Peach', 'Calories': 60},
                {'Fruit': 'Pear', 'Calories': 100},
                {'Fruit': 'Pineapple', 'Calories': 50},
                {'Fruit': 'Plums', 'Calories': 70},
                {'Fruit': 'Strawberries', 'Calories': 50},
                {'Fruit': 'Sweet Cherries', 'Calories': 100},
                {'Fruit': 'Tangerine', 'Calories': 50},
                {'Fruit': 'Watermelon', 'Calories': 80},
                ]
    question = str(input('Enter the Name of Fruit: '))
    
    for i in fruit_Cal:
        if i['Fruit'].lower() == question.lower():
            print(f'Calories for {i['Fruit']} :  {i['Calories']}')
            break
    else:
        print(f'Fruit: {question} not found')            
if __name__ == '__main__':
    main()        
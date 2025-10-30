'''
Suppose that you're in the habit of making a list of items you need from the grocery store.

In a file called grocery.py,
 implement a program that prompts the user for items, one per line, until the user inputs control-d.
   Then output the user's grocery list in all uppercase, 
   sorted alphabetically by item, 
   prefixing each line with the number of times the user inputted that item.
   No need to pluralize the items.
   Treat the user's input case-insensitively.

NOTE: Use ctrl + z to break out of inserting the list and print the list   
'''
from collections import Counter

def main():
    

    items = {}
    grocery_count = Counter()

    try:
        while True:
            grocery_item = input('Enter Item: ').lower()
            grocery_count[grocery_item] +=1
    except EOFError:
        pass
    for item in sorted(grocery_count.keys()):
        print(f'{grocery_count[item]} {item.upper()}')

   


            








if __name__ == '__main__':
    main()    
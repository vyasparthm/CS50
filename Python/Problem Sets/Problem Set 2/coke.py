'''
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py,
 implement a program that prompts the user to insert a coin, one at a time, 
 each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
 Assume that the user will only input integers, and ignore any integer that isn't an accepted denomination.
'''

def main():
    total_cost = 50
    current_sum = 0
    # amount_due = total_cost
    # print(amount_due)

    while current_sum != total_cost:
        amount_due = total_cost- current_sum
        print(f'Amount Due: {amount_due}')
        insert_coin = int(input('Insert coin: '))
        current_sum +=  insert_coin
        # print(f'current_sum: {current_sum}')
    print('Received 50 cents, Dispatching ice cold Coke!')


main()            
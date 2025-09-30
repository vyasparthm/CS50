'''
Tip Calculator

In the United States, it’s customary to leave a tip for your server after dining in a restaurant,
 typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!
'''
def main():
    dollars = dollars_to_float(input("What is the total Dollar Amount?: "))
    percent = percent_to_float(input('How much tip would you like to leave?: '))
    tip = percent * dollars
    print(f'Leave the tip = {tip:2f} \n Totalling the amount = $ {float(tip) + float(dollars):2f}')


def dollars_to_float(n):
    return float(n.replace('$',''))

def percent_to_float(x):
    return float(x.replace('%',''))/100



if __name__ == '__main__':
    main()
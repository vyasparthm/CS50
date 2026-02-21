'''
Tip Calculator

In the United States, it's customary to leave a tip for your server after dining in a restaurant,
 typically an amount equal to 15% or more of your meal's cost. Not to worry, though, we've written a tip calculator for you, below!
'''

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = (dollars * percent) /100
    print(f"Leave tip ${tip:.2f}.\nTotal amount: ${dollars +percent}",)


def dollars_to_float(d):
    """ converts entered dollar amount into float"""
    return float(d)


def percent_to_float(p):
    """ converts entered percentage amount into float"""
    return float(p)


if __name__ == "__main__":
    main()
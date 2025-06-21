"""
This code file will have details about all it items you can do with numbers with floating point values in python

you can use float() instead of int()
The value of float() can be rounded to the nearest decimal point, per python documentation round(number[,ndigits]).
if you specify the number for ndigits --> That is the leel of precision you get

"""


x = float(input("Add first value:"))
y = float(input("Add second value:"))

z = x+y
# print(x+y)
# print("rounded value: ",round(x+y))

#Formatting the numbers

# print(f"{x+y :,}") # this will add a comma and make the number more readable

# Formatting the rounding
print(round(x+y,3))

#another way using format string, up to n digits after decimal point
print(f"{z:.3f}")
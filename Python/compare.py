x = int(input("What is X:"))
y = int(input("What is Y:"))


# 1. Uncomment this Section to see each if condition is evaluated even if lets say only first or second needed to be executed.
# if x < y:
#     print (f"X: {x} is less than Y: {y}")
# print("<")

# if x > y:
#     print(f"X: {x} is greater than Y: {y}")
# print(">")

# if x == y:
#     print(f"X: {x} is equal to Y: {y}")
# print("=")    

# 2. Now lets make sure we only execute the code till its needed rather than executing everything to save some resources and time.
# Python does it with elif condition

if x < y:
    print (f"X: {x} is less than Y: {y}")
    print("<")


elif x > y:
    print(f"X: {x} is greater than Y: {y}")
    print(">")

elif x == y:
    print(f"X: {x} is equal to Y: {y}")
    print("=")  
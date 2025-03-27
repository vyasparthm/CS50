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

# if x < y:
#     print (f"X: {x} is less than Y: {y}")
#     print("<")


# elif x > y:
#     print(f"X: {x} is greater than Y: {y}")
#     print(">")

# # if both conditions above are false than its sure that x must be the same as y, you can also use it as default and just use "else" instead of "elif" below. 
# # This will reduce one more iteration from the condition evaluation

# # elif x == y:
# #     print(f"X: {x} is equal to Y: {y}")
# #     print("=")  
# else:
#     print(f"X: {x} is equal to Y: {y}")
#     print("=")  


#3. The use of "or" in comparison, notice how it reduced the lines of code I had to write.

# if x < y or x > y:
#     print(f"X: {x} is not equal to Y: {y}")
# else:
#     print(f"X: {x} is  equal to Y: {y}")


# 4. How about using other comparison operators and make the execution flow more simpler, lets only evaluate 2 conditions.

if x != y:
    print(f"X: {x} is not equal to Y: {y}")
else:
    print(f"X: {x} is  equal to Y: {y}")    



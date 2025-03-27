'''
Lets use +, -, *, /, % as well and see how things pan out.
'''

# 1. Normal pattern
# x = int(input("What is X:"))


# #  1. Check if the number is even

# if x % 2 == 0: 
#     print("X is even")
# else:
#     print ("X is odd")  


# 2. Lets get back into the habit of defining main() function

x = int(input("What is x? "))
def main():
    
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n): 
    if n % 2 == 0: 
        return True
    else:
        return False
    
main()
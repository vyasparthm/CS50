"""
To showcase about how we can generate patterns like:
1. ###
2.  #
    #
    #
3.  ###
    ###
    ###
"""
# # Pattern 1:
# for _ in range(3):
#     print('#', end='')


# # Pattern 2:
# def main():
#     print_column(4)

# def print_column(height):
#     for _ in range(height):
#         print('#')

# main()

# # Pattern 3: 

# # # First way

# def main():
#     print_squre(3)

# def print_squre(size):
#     for i in range(size):
#         for j in range(size):
#             print('#', end='')
#         print() #\n adds an additional line after the above print has laready added a new line.

# main()

# # Second  way:
# def main():
#     print_squre(4)

# def print_squre(size):
#     for _ in range(size):
#         print('#' * size)

# main()

# # Third Way:
def main():
    print_squre(int(input('What size of squre?:')))

def print_squre(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print('#' * width)

main()
import sys

# print('Hello, My name is:', sys.argv[0])
# print('Hello, My name is:', sys.argv[1])
# print('Hello, My name is:', sys.argv)

# try:
#     print('Hello, My name is:', sys.argv[1])
# except IndexError :
#     print('Too Few Arguments, Try again with your name')


# if len(sys.argv)<2:
#     print('Too few Arguments, Try again with your name')
# elif len(sys.argv) >2:
#     print('Too many arguments')
# else:
#     print('Hello, My name is:', sys.argv[1])


if len(sys.argv)<2:
    sys.exit('Too few Arguments, Try again with your name')


for i in (sys.argv[1:]):
    
    print('Hello, My name is:', i)    
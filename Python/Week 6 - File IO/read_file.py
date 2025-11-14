## Read all lines at once then print, not so much memory eficient while dealingwith alrge files

# with open('names.txt','r') as file:
#     lines = file.readlines()
    
#     for line in lines:
#         print(f'Hello, {line.rstrip()}')

# # How about reading line by line

with open('names.txt','r') as file:        
    for line in file:
        print(f'Hello, {line.rstrip()}')
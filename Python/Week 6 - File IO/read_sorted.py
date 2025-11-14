
## This is good nut we're doing too many things
# names = []
# with open('names.txt','r') as file:        
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f'Hello, {name}')

## If you don't intend to make any other transformations and just print the sorted
with open('names.txt','r') as file:        
    for line in sorted(file, reverse= True): ## Add Reverse = True for sorting decending
        print(f'Hello, {line.rstrip()}')
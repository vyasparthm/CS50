# # Lets start a list
avengers = ['Cap','Iron-Man','Hulk','Scarlet Witch','Black Widow']

# # Print out all

# print(avengers)

# # Lets use a loop to print all of them on a new line

# for avenger in range(len(avengers)):
#     print(avengers[avenger],end='\n')
 
# #  Lets print a little better to show which element is being printed as well


for avenger in range(len(avengers)):
    print(avenger+1,'.',avengers[avenger],sep= '',end='\n')
    # # +1 here just increase a counter to show we start with 1 instead of 0, this is just an illusion to show the user
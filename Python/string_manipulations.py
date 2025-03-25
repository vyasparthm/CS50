"""
This code file will show some basic manipulations we can d using python strings, comment/uncomment the sections and run this file.
"""


##1. We will see some basic manipulation like new line, tab and some formatting in this Section

# print( "This is Basic String:","Hello World")
# print( "This is Basic String:","Hello World", sep="") # With Seperator defined, notice the missing space
# print("This is string with new line:", "Hello\nWorld") #\n is used for new line like many other programming languages
# print("This is string with tab:", "Hello\tWorld") #\t is used for tab


## 2. Lets see some Methods we can use on strings.

# my_string ="Hello World, I am Python"
# print(len(my_string)) #to print length
# print(my_string.upper()) # For upper case
# print(my_string.lower()) # For lower case
# print(my_string.title()) # For title case
# print(my_string.split()) #to split string at space


##3. Lets see some examples with indexing

# new_string = "Hello World!!!"
# print(new_string)

# print(new_string[0]) #prints nth index of the string
# print(new_string[:3]) #prints up to nth index
# print(new_string[0:5]) #prints characters in range, [start:end]

# print(new_string[::-1]) # this will reverse the string
# print(new_string[::1]) #print as is
# print(new_string[::2]) #print every second character


## 4. Manipulations and formatting
# new_String = "I'm going to be an example of Formatting"

# print(new_String)

# new_String = new_String + "and string manipulation." #concat with another string
# print(new_String)


# print (new_String *3) # multiplies and prints it 3 times

# print("I am thinking of learning", "about",new_String,"today")
# print(f"I am going to be learning about: {new_String}")

## 4.1 Formatting with placeholders
player = 'Zlatan'
goals = 35

print("I am going to insert %s's name in goal list with %s goals this season"%(player,goals))



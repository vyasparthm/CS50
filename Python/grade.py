'''
Lets cqalculate user's grades.
'''

score = int(input("What is score:"))


# 1. General flow of calculating grades

# if score >= 90 and score <= 100:
#     print("Congrats on getting Grade: A")
# elif score > 80 and score < 90:
#     print("Congrats on Grade: B")

# elif score > 70 and score < 80:
#     print("Your Grade: C")

# elif score > 60 and score < 70:
#     print("Your Grade: D")

# else:
#     print("I'am afraid, Your Grade: F. See the professor.")


# 2. How about chaining these together?

# if 90 <= score <= 100:
#     print("Congrats on getting Grade: A")
# elif  80 <= score < 90:
#     print("Congrats on Grade: B")

# elif  70 <= score < 80:
#     print("Your Grade: C")

# elif  60 <= score < 70:
#     print("Your Grade: D")

# else:
#     print("I'am afraid, Your Grade: F. See the professor.")


# 3. For more readability, lets ask the program series of questions and stop the execution once the condition is satisfied? 
# This will reduce the number of iterations while generating outcome, reducing execution time.

if score >= 90:
    print("Congrats on getting Grade: A")
elif  score >= 80:
    print("Congrats on Grade: B")

elif   score >= 70:
    print("Your Grade: C")

elif  score >= 60:
    print("Your Grade: D")

else:
    print("I'am afraid, Your Grade: F. See the professor.")

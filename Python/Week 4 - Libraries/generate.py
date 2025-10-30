# import random # Uncomment to import the whole module

from random import choice  # This is the best practice however so it doiesn't load entire module. Helpful wwhen your code grows
from random import randint # Return random integer in range [a, b], including both end points.
from random import shuffle # Shuffle list x in place, and return None.


# print(rand.choice(['Heads','Tails']))

# print(choice(['Heads','Tails']))

# print (randint(1,10))
a = [2,4,6,8,10]
print(shuffle(a))
for item in a:
    print(item)
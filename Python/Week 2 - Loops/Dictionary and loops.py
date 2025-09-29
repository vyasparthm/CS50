
# avengers = {
#     1:"Iron-man",
#     2:"Hulk",
#     3:"HawkEye"
#     }

# for avenger in avengers:
#     print(avenger,avengers[avenger], sep=':')

## How about multiple values for a given key?
students = [{"name": "Tony", "Origin": "NYC", "Strength": "Suit"},
			{"name": "Hulk", "Origin": "Rio", "Strength": "Science"},
			{"name": "Hawkeye", "Origin": "Waverly", "Strength": "Arrows"},
			{"name": "Phillip Coulson", "Origin": "Manitowoc", "Strength": None}, #No disrespect Phil
							]
							
for student in students:
    print(student["name"], student["Origin"], student["Strength"], sep=", ")
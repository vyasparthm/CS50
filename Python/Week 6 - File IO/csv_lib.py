import csv


heros = []
with open('names_lib.csv','r') as file:
    reader = csv.reader(file)
    ## Do it row by row 
    # for row in reader:
        # heros.append({"hero": row[0], "home": row[1]})
    for hero, home,area in reader:
        heros.append({"hero": hero, "home": home, "area": area})
       

for hero in sorted(heros,key= lambda hero: hero["hero"]):
    print(f'{hero["hero"]} belongs to {hero["home"]},{hero["area"]}')
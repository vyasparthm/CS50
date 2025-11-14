heros = []
with open('names.csv','r') as file:
    for line in file:
        row,universe = line.rstrip().split(',')
        hero = {'name': row, 'universe': universe}
        heros.append(hero)
       

def get_name(hero):
    return hero["name"]

def get_universe(hero):
    return hero["universe"]

#Change to either name/universe to change sort order
# for hero in sorted(heros, key= get_universe):
    ## Uncomment for Traditional way
    # print(f'{hero["name"]} belongs to {hero["universe"]}')
## Here comes the Lambda function

for hero in sorted(heros,key= lambda hero: hero["name"]):
    print(f'{hero["name"]} belongs to {hero["universe"]}')

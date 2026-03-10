def main():
    item = {"Voyager 1":0.01,"Atlantis":0.00}
    # Access and Search
    # print("1. Search for value: ",item.get("Name")) #Get value by searching for a key
    # print("2. List all keys: ",item.keys()) # Get All the keys listed
    # print("3. List all Values",item.values()) # Get all the values
    # print("4. List everything inside: ",item.items())

    # Adding and udpating
    # item_updated = {"Name":"Atlantis"}
    # # item.update(item_updated) #to Update but it only takes a dictionary as input
    # # item.update({"Name":"Atlantis"})
    # print (item)

    # for name in item.keys():
    #     print(f"Key: {name} and Value:{item[name]}")
    for name in item.values():
        print(f"Value: {name} ")

if __name__ == '__main__':
    main()
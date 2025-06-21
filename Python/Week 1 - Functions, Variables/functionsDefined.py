def main():
    name = input("Hi I am Python, What is your name? ")
    Hello(name)



def Hello(to ="World"):
    print(f"Hello, {to}")

main()


# Uncomment below to check the scope, name is only defined in the function main
print(main.__name__) 
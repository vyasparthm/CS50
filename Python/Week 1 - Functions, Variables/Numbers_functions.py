def main():
    x = int(input("Enter the value to be squared: "))
    print(f"The Square of your input {x} = ", square(x))

def square(n):
    return pow(n,2)

main()

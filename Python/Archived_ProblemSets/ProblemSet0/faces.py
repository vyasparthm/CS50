"""
Author: Parth V.
Usage: This is a simple python program to demonstrate how we can convert emoticon like text into emoji in python.

"""

def main():
    emoticon = str(input("Enter Value: "))
    print (f"Here is the  output: {convert(emoticon)}")


def convert(value):
    result = value

    if ":)" in result:
       result = result.replace(":)","🙂")
    if ":(" in result:
       result = result.replace(":(","🙁")

    else:
        result
    return result


if __name__ == "__main__":
    main()

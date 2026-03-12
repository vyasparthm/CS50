def main():
    user_input = input("Enter Camel Case: ")
    print(camel(user_input))
    


def camel(inp:str)->str:
    """ Converts the user input from CamelCase to snake_Case"""
    snake_case = []

    for index,char in enumerate(inp):
        if char.isupper():
            if snake_case:
                snake_case.append("_")
            snake_case.append(char.lower())
        else:
            snake_case.append(char)
    return "".join(snake_case)


if __name__ == "__main__":
    main()
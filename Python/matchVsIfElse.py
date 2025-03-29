'''
Now if else is cool, but what is better? turns out python has something called "match" this can perform much better comparisons and faster.

We'll do a traditional if else and then an example of match.
'''

def main():
    x = int(input("Enter Status Code: "))
    print(showStatus(x))

## Traditional if-else
# def showStatus(n):
#     if n == 200:
#         return "OK"
#     elif n == 404:
#         return "Not Found"
#     elif 400 <= n < 500:
#         return f"Client Error: {n}"
#     elif 500 <= n <600:
#         return f"Server Error: {n}"
#     else:
#         return f"Unknown Status Code: {n}"
    
def showStatus(n):
    match n:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _ as n if 400 <= n < 500:  #case _ handles a wild card case same as just ELSE but you can also put conditions here
            return f"Client Error: {n}"
        case _ as n if 500 <= n < 600:
            return f"Server Error: {n}"
        case _: 
            return f"Unknown Code: {n}"


main()




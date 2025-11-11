'''
In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. You should replace YourApiKey with the actual API key you obtained from your CoinCap account dashboard, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions
'''

import requests as r
import json as j
import sys

if len(sys.argv) !=2:
    print("Usage: python solution.py <number_of_bitcoins>")
    sys.exit()


apiKey = '' # Put your key here
baseurl = 'https://rest.coincap.io/v3/assets/bitcoin'


headers ={
    "Authorization": f"Bearer {apiKey}",
    "Content-Type": "application/json"
}

try:
    response = r.get(baseurl,headers= headers)
    
    data = response.json()
    # print(data)

    btc_price = float(data['data']['priceUsd'])
    print(f'Price for 1 btc: {btc_price}')
    print(f'price for your ask:{sys.argv[1]} = {int(sys.argv[1]) * btc_price}')
    
    inner_data = data['data']
    print('--'*40)
    print('** More Details Below **')
    print('--'*40)
    for key,value in inner_data.items():
        print(f'\t**{key} = {value} **')
except r.RequestException:
    print('Error!! Unable to fetch data.')





# try:
#    for index,(key,value) in enumerate(response.items(), start=1):
        
#         print(f'{index},{key}: {value}')
        
# except  r.RequestException:
#     print('Error')

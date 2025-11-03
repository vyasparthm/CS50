import requests
import sys
import json


if len(sys.argv) !=2:
    sys.exit()

response = requests.get('https://itunes.apple.com/search?entity=song&limit=10&term=' + sys.argv[1])
# print(json.dumps(response.json(), indent=2))

output = response.json()
# for result in output['results']:
#     print(result['trackName'])

for i,result in enumerate(output['results'], start=1):
    print(f'{i}.{result['trackName']}')


import requests
import json


# remove the minus sign
apiKey = 'f59b1cdb743ce0ab9b21a94ac246b02f06ee2d85'
url = 'https://api.github.com/pjmeehan/dataRepresentation/week02/carviewer2'
filename ="repo.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
print (response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)

import requests

#url = "https://www.gmit.ie"

#response = requests.get(url)

#print(response.status_code)
#print(response.text)

url = 'http://127.0.0.1:5000/car'
data = {'reg':'123', 'make' : 'blah', 'model':'blah', 'price':12345}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
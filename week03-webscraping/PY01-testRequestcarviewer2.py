import requests
from bs4 import BeautifulSoup

with open("../dataRepresentation/week02/carviewer2.html") as fp:
	soup = BeautifulSoup(fp, 'html.parser')
	
print(soup1.prettify())
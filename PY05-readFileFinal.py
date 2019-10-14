from bs4 import BeautifulSoup
import csv

with open("../dataRepresentation/Lab2.html") as fp:
	soup = BeautifulSoup(fp, 'html.parser')

#print(soup.tr)

employee_file = open('employee_file.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


rows = soup.findAll("tr")
for row in rows:

	
	cols = row.findAll("td")
	dataList = []
	for col in cols:
		dataList.append(col.text)
	employee_writer.writerow(dataList)
dataList.remove('Update')
dataList.remove('Delete')	
print(dataList)	



employee_file.close()
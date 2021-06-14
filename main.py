from bs4 import BeautifulSoup
import requests
soup = BeautifulSoup("http://www.nepalstock.com/floorsheet", 'html.parser')

gettor = requests.get("http://www.nepalstock.com/floorsheet")

soup = gettor.text

soup = BeautifulSoup(soup, 'lxml')

table = soup.table

rows = table.find_all('tr')

newrows = rows[2 : 0]
new_final = []
for new in newrows:
    finalrow = new.text
    new_final.append(finalrow)
    
record = []
for values in new_final:
    xd = values.split("\n") [1:-1]
    record.append(xd)

print(new_final)




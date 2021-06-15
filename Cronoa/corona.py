from bs4 import BeautifulSoup
import requests
import csv





html_text = requests.get("https://www.worldometers.info/coronavirus/").text
soup = BeautifulSoup(html_text, 'lxml')
tableBody = soup.table
tableRows = tableBody.find_all('tr')

firstData =[]
firstData.append(tableRows[0].text.split("\n") [1 : -1])

tableRows = tableRows[8 :]
convert = []

for i in tableRows:
    converted =  i.text
    convert.append(converted)

splitted = []
for i in convert:
    ram = i.split("\n") [1: -1] 
    splitted.append(ram)

with open("jeevan.csv", "a") as f:
    x = csv.writer(f)
    x.writerow(firstData[0])
    for items in splitted:
        
        x.writerow(items)


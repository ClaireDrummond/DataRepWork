import requests 
from bs4 import BeautifulSoup 

with open("../Wk2/LabWeek2.html") as fp:     
	soup = BeautifulSoup(fp,'html.parser') 

# print(soup.tr)

rows = soup.findAll("tr") 
for row in rows:      
#	print("------")      
#	print(row)
	
	cols = row.findAll("td")      
#	for col in cols:          
#		print(col.text) 
	
	dataList = []     
	for col in cols:         
		dataList.append(col.text)     
	print (dataList)
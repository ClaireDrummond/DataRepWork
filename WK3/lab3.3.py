from bs4 import BeautifulSoup

with open("../Wk2/LabWeek2.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

print (soup.prettify())
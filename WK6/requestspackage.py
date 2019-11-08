import requests


#url = 'https://www.gmit.ie'
#response = requests.get(url)
#print (response.status_code)
#print (response.headers) # for full header

url = 'http://127.0.0.1:5000/cars' # send to cars
# data is a dict object: will get converted into json by the requests package
data = {'reg':'123','make':'blah','model':'blah','price':1234}

response = requests.post(url, json=data)
print(response.status_code) 
print(response.json())
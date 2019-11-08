import json

data =  {
    'name':'joe',
    'age':21,
    "student": True
    }
#print(data)

# Convert to JSON:
file = open("simple.json",'w')
#json.dump(data,file, indent=4) # indent adds more whitespace
                                
jsonString = json.dumps(data)   
                               
print(jsonString)
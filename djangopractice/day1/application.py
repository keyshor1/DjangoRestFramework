import requests
import json 

URL = 'http://127.0.0.1:8000/api/createstudent/'

data = {
    'name': 'anshu',
    'rollno': '13',
    'description': 'She is the queen'
}

# convert python dictionary or datatype to json
json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)

# retrive data using r object from api 
data = r.json()
print(data)
import requests
import json


URL='http://127.0.0.1:8000/api/studentcrud/'


def get_student(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)

    data = r.json()
    print(data)

# get_student()

def create_student():
    data = {
        'name': 'kishor',
        'rollno': '200',
        'description': 'GOAT'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)

    data = r.json()
    print(data)

# create_student()

def update_student():
    data = {
        'id': '11',
        'name': 'credid',
        'rollno': '200',
        'description': 'he is the demoncoc'
    }
    
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)

    data = r.json()
    print(data)

# update_student()

def delete_data(id):
    data = {'id': id}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)

    data = r.json()
    print(data)

# delete_data()

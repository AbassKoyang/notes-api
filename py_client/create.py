import requests
from getpass import getpass


auth_endpoint = "http://localhost:8000/auth/"
username = input("What is your username? \n")
password = getpass("What is your password? \n")
title = input("Enter note title \n")
content = input("Enter cotent \n")

auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json());

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }

    endpoint = "http://localhost:8000/notes/"

    data = {
        'title': title,
        'content': content
    }
    response = requests.post(endpoint, headers=headers, json=data);
    print(response.json())
    # print(response.text)
    # print(response.status_code)
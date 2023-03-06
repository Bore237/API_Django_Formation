import requests  
from getpass import getpass 

endpoint = 'http://127.0.0.1:8000/product/auth'
username = input("Entrer votre nom username:\n")
password = getpass("Entrer votre password:\n")
auth_response = requests.post(endpoint, json={'username':username, 'password':password})
print(type(auth_response.json()))

if auth_response.status_code == 200 :
    endpoint = "http://127.0.0.1:8000/product/createlist/"
    headers = {   
               'Authorization': 'Bearer 0e8b46c0e430e9fbeefe5368e9b1bcdcd863b41a'
               } 
    response = requests.get(endpoint)
    print(response.json()) 
    print (response.status_code)
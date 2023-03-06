import requests

#endpoint = "http://httpbin.org/anything"
endpoint = "http://127.0.0.1:8081/api/"
response = requests.get(endpoint, params={'abc':123}, json={'query': 'Hello'})
#print(response.text)
print(response.json())
print(response.status_code)

#HTTP REQUEST --> HTML
#REST API HTTP ---> JSON JAVE SRIPTS OBJECT NOTATION

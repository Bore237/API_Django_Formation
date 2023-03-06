import requests

#endpoint = "http://httpbin.org/anything"
endpoint = "http://127.0.0.1:8081/product/put/"
#response = requests.get(endpoint)
#print(response.text)
response = requests.post(endpoint, json={'name':'Corossol', 'content':'just pratique', 'price':20})
print(response.json())
print(response.status_code)
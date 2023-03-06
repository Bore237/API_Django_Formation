import requests  

endpoint = "http://127.0.0.1:8000/product/9/update/" 
response = requests.put(endpoint, 
                        json={'name': 'Orange', 
                              'content': 'Best fruit',
                              'price':300})
print(response.json()) 
print (response.status_code)
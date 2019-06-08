import requests

response = requests.post('http://192.168.1.113:8080', data = "This is test data 1 2 3 4 5 6")

print(response.text)

import requests

URL= "http://api.open-notify.org/astros.json"

#GET requests

resp = requests.get(URL)

print(resp)
print(type(resp))
print(type(resp.json()))
print(resp.json())

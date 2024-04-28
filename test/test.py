import requests

MAX_REQUEST=1000

data = {}

for i in range(1000):
    res = requests.get("http://127.0.0.1:8000/")
    id = res.json()["id"]
    if data.get(id):
        data[id] = data[id] + 1
    else:
        data[id] = 1

print(data)
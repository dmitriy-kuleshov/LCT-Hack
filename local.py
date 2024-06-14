import requests

headers = {
    'Content-Type': 'application/json'
}

# Отправка POST-запросов с использованием параметра json
res = requests.post("http://localhost:3001/api/datasets/3", json={"name": "baklan", "expenses": 666}, headers=headers)
#res = requests.post("http://localhost:3001/api/datasets/4", json={"name": "666", "expenses": 999}, headers=headers)

# Печать ответов от сервера
print(res.json())
# print(res2.json())

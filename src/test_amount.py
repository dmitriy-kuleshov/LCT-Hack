import requests

url = "http://localhost:5000/api/amount"
payload = {
    "products": ["Электрочайник BOSCH TWK3A013"]
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(f"Status Code: {response.status_code}")
print(f"Response Content: {response.content}")

try:
    print(response.json())
except requests.exceptions.JSONDecodeError as e:
    print("Error decoding JSON:", e)

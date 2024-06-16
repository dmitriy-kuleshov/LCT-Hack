import requests

url = "http://127.0.0.1:5000/api/amount"
payload = {
    "products": ["Электрочайник BOSCH TWK3A013"]
}

response = requests.post(url, json=payload)

print(f"Status Code: {response.status_code}")
print(f"Response Content: {response.content}")

try:
    print(response.json())
except requests.exceptions.JSONDecodeError as e:
    print("Error decoding JSON:", e)

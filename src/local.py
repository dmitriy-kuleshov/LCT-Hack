import requests

url = "http://127.0.0.1:5000/get_product"
params = {
    "table": "ostatki_21_2022",
    "product_name": "Электрочайник BOSCH TWK3A013"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.json())

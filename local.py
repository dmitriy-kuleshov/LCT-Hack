import requests

url = "http://127.0.0.1:5000/get_product"
params = {
    "table": "oboroty_21_2022",
    "product_name": "Камера видеонаблюдения R Vi-IPC32MS-IR V.2 (2.8 мм)"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.json())

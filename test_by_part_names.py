import requests
import json

base_url = "http://localhost:5000"  # Укажите базовый URL вашего Flask приложения


def test_search_products(search_query):
    url = f"http://localhost:5000/products"
    try:
        response = requests.get(url, params={'q': search_query})
        if response.status_code == 200:
            data = response.json()
            print(f"Search Products Test Passed. Found products with '{search_query}':")
            print(json.dumps(data, indent=2))
        else:
            print(f"Search Products Test Failed. Status Code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Search Products Test Failed. Exception: {str(e)}")


# Запуск теста для поиска товаров по части имени
if __name__ == "__main__":
    search_query = "Клей"  # Здесь указываете часть имени товара для поиска
    test_search_products(search_query)

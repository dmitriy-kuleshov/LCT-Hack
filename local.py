import requests

headers = {
    'Content-Type': 'application/json'
}

# Название для поиска
name_to_search = "Карманный термоанемометр стик-класса TESTO 405"

try:
    # Отправка GET-запроса для извлечения данных по названию
    response = requests.get(f"http://localhost:3001/api/datasets_by_name?name={name_to_search}", headers=headers)
    response.raise_for_status()  # Проверка на успешный статус ответа
    print(response.json())
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")  # HTTP ошибка
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")  # Ошибка соединения
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")  # Ошибка таймаута
except requests.exceptions.RequestException as req_err:
    print(f"An error occurred: {req_err}")  # Другие ошибки
except ValueError as json_err:
    print(f"JSON decode error: {json_err}")  # Ошибка декодирования JSON

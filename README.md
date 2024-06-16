# API для управления продуктами

Этот API предоставляет интерфейс для взаимодействия с базой данных PostgreSQL, позволяя выполнять CRUD операции (создание, чтение, обновление, удаление) над таблицами, содержащими информацию о продуктах. Таблицы включают данные по оборотам и остаткам различных счетов за 2022 год.

## Конфигурация базы данных

Информация о подключении к базе данных хранится в файле `config.py` в следующем формате:

```python
DATABASE = {
    'host': 'localhost',
    'port': '5432',
    'dbname': 'hack_db',
    'user': 'postgres',
    'password': 'sanji'
}
```

Endpoint: /get_product
Методы
- GET

- POST

- PUT

- DELETE

Параметры
Все методы принимают следующие параметры:

table (обязательно): имя таблицы для операции. Допустимые значения:
- oboroty_21_2022
- oboroty_101_2022
- oboroty_105_2022
- ostatki_21_2022
- ostatki_101_2022
- ostatki_105_2022
- product_name (обязательно): наименование продукта.




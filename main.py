import csv
import psycopg2
from config import host, user, password, db_name
from flask import Flask
from flask_restful import Api, Resource, reqparse


connection = None

try:
    print(f"Попытка подключения к базе данных с параметрами: host={host}, user={user}, db_name={db_name}")
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        print(f"SELECT version: {cursor.fetchone()}")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE users(
    #         id serial PRIMARY KEY,
    #         first_name varchar(50) NOT NULL,
    #         nick_name varchar(50) NOT NULL);"""
    #     )
    #     # connection.commit()
    #     print("[INFO] Table created successfully")

    # вставка определенных данных в БД
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO users (first_name, nick_name) VALUES
    #         ('Dima', 'mugiwara');"""
    #     )
    #     print("[INFO] Data was successfully inserted")

    # извлечение данных из таблицы в БД
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT nick_name FROM users WHERE first_name = 'Dima'"""
        )
        print(cursor.fetchone())

    # удаление таблицы (это просто для понимания как это делается)
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE users;"""
    #     )
    # print("[INFO] Table was deleted")

except psycopg2.OperationalError as oe:
    print("[INFO] Ошибка подключения к PostgreSQL:", oe)
except Exception as e:
    print("[INFO] Другая ошибка при работе с PostgreSQL:", e)
finally:
    if connection:
        connection.close()
        print("[INFO] Подключение к PostgreSQL закрыто")
'''
app = Flask(__name__)
api = Api()

datasets = {
    1: {"name": "105/2", "expenses": 10},
    2: {"name": "101/7", "expenses": 15}
}



def load_datasets():
    datasets = {}
    try:
        with open('xxx.csv', mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data_id = int(row['id'])
                datasets[data_id] = {"name": row['name'], "expenses": int(row['expenses'])}
    except FileNotFoundError:
        print("Файл не найден. Используется пустой набор данных.")
    return datasets


datasets = load_datasets()

parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("expenses", type=int)


class Main(Resource):
    def get(self, data_id):
        if data_id == 0:
            return datasets
        else:
            return datasets[data_id]

    def delete(self, data_id):
        del datasets[data_id]
        return datasets

    # передача несуществующего data_id (создание новой записи)
    def post(self, data_id):
        datasets[data_id] = parser.parse_args()
        return datasets

    # обновление существующей записи через data_id
    def put(self, data_id):
        datasets[data_id] = parser.parse_args()
        return datasets


api.add_resource(Main, "/api/datasets/<int:data_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3001, host="localhost")  # для удаленного сервера значение False

'''
# доработать взаимодействие с БД
import csv
import psycopg2
from config import host, user, password, db_name
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

'''connection = None

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

    # создание БД
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


def get_db_connection():
    return psycopg2.connect(database=db_name, user=user, password=password, host=host)


# парсер для обработки входящих данных
parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("expenses", type=int)


# def load_datasets():
#     datasets = {}
#     try:
#         with open('xxx.csv', mode='r', encoding='utf-8') as file:
#             csv_reader = csv.DictReader(file)
#             for row in csv_reader:
#                 data_id = int(row['id'])
#                 datasets[data_id] = {"name": row['name'], "expenses": int(row['expenses'])}
#     except FileNotFoundError:
#         print("Файл не найден. Используется пустой набор данных.")
#     return datasets
#
#
# datasets = load_datasets()

class Main(Resource):
    def get(self, data_id):
        conn = get_db_connection()
        cur = conn.cursor()
        if data_id == 0:
            cur.execute("SELECT * FROM datasets;")
            rows = cur.fetchall()
            result = {}
            for row in rows:
                result[row[0]] = {"name": row[1], "expenses": row[2]}
            conn.close()
            return result
        else:
            cur.execute("SELECT * FROM datasets WHERE id = %s;", (data_id,))
            row = cur.fetchone()
            conn.close()
            if row:
                return {row[0]: {"name": row[1], "expenses": row[2]}}
            else:
                return {"message": "Dataset not found"}, 404

    def delete(self, data_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM datasets WHERE id = %s;", (data_id,))
        conn.commit()
        conn.close()
        return {"message": "Dataset deleted"}

    # передача несуществующего data_id (создание новой записи)
    def post(self, data_id):
        args = parser.parse_args()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO datasets (id, name, expenses) VALUES (%s, %s, %s);",
                    (data_id, args["name"], args["expenses"]))
        conn.commit()
        conn.close()
        return {"message": "Dataset created"}, 201

    # обновление существующей записи через data_id
    def put(self, data_id):
        args = parser.parse_args()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE datasets SET name = %s, expenses = %s WHERE id = %s;",
                    (args["name"], args["expenses"], data_id))
        conn.commit()
        conn.close()
        return {"message": "Dataset updated"}


class GetByName(Resource):
    def get(self):
        name = request.args.get('name')
        if not name:
            return {"message": "Name parameter is required"}, 400

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM datasets WHERE name = %s;", (name,))
        rows = cur.fetchall()
        conn.close()

        if rows:
            result = {}
            for row in rows:
                result[row[0]] = {"name": row[1], "expenses": row[2]}
            return jsonify(result)
        else:
            return {"message": "Dataset not found"}, 404


class Amount:
    def post():
        # {
        #     products: string[], //список имен продуктов 
        #     date: string //список отчетная дата дд.мм.гггг
        # }

        #парсинг аргументов

        # answer = getAmount(products, amount)
        # return answer

        return {
            #то что нашел в бд
            "data": [{
                "name": 'Test1', 
                "amount": '1',
            },
            {
                "name": 'Test2',
                "amount": '2',
            }], 
            #то что не нашел
            "not_found": ['Test3']
        }
    
class Forecast:
    def post():
        # {
        #     products: string[], //список имен продуктов 
        # }

        #парсинг аргументов


        return {
            #то что нашел в бд
            "data": [{
                "name": 'Test1', 
                "date": 'дд.мм.ггг',
            },
            {
                "name": 'Test2',
                "date": 'дд.мм.ггг',
            }], 
            #то что не нашел
            "not_found": ['Test3']
        }
    
class Purchase:
    def get():


        return {
            #то что по формату из тз
        }
    

    


api.add_resource(Main, "/api/datasets/<int:data_id>")
api.add_resource(GetByName, "/api/datasets_by_name")
api.add_resource(Amount, "api/amount")
api.add_resource(Forecast, "api/forecast")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3001, host="localhost")  # для удаленного сервера значение False

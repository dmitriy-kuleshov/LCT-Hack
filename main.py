import psycopg2
from flask import Flask, request, jsonify
from config import DATABASE
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


# Функция для получения соединения с базой данных
def get_db_connection():
    conn = psycopg2.connect(
        host=DATABASE['host'],
        port=DATABASE['port'],
        dbname=DATABASE['dbname'],
        user=DATABASE['user'],
        password=DATABASE['password']
    )
    return conn

# для неточного поиска
@app.route('/products', methods=['GET'])
def search_products():
    search_query = request.args.get('q', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        valid_tables = ['ostatki_21_2022', 'ostatki_101_2022', 'ostatki_105_2022']

        # Используем первую из доступных таблиц для поиска
        for table in valid_tables:
            query = f'SELECT "Основные средства", "Количество" FROM {table} WHERE LOWER("Основные средства") LIKE %s'
            cursor.execute(query, ('%' + search_query.lower() + '%',))
            results = cursor.fetchall()

            if results:
                # Если нашли результаты в таблице, преобразуем их в JSON и возвращаем
                serialized_results = [{'name': row[0], 'amount': row[1]} for row in results]
                return jsonify(serialized_results)

        # Если ничего не найдено, возвращаем пустой список
        return jsonify([])

    finally:
        cursor.close()
        conn.close()


# функция для получения количества продуктов и списка ненайденных продуктов
def get_amounts(products):
    conn = get_db_connection()
    cursor = conn.cursor()

    amounts = {}
    not_found = []

    valid_tables = ['ostatki_21_2022', 'ostatki_101_2022', 'ostatki_105_2022']

    try:
        for product in products:
            found = False
            for table in valid_tables:
                query = f'SELECT "Основные средства", "Количество" FROM {table} WHERE "Основные средства" = %s'
                cursor.execute(query, (product,))
                result = cursor.fetchone()
                if result:
                    amounts[result[0]] = result[1]
                    found = True
                    break
            if not found:
                not_found.append(product)

        return amounts, not_found

    finally:
        cursor.close()
        conn.close()


# ресурс для API, обрабатывающий запросы на получение количества продуктов
class Amount(Resource):
    def post(self):
        data = request.get_json()
        if not data or 'products' not in data:
            return jsonify({'error': 'Products are required'}), 400

        products = data['products']

        amounts, not_found = get_amounts(products)

        found_products = [{"name": name, "amount": amount} for name, amount in amounts.items()]

        return jsonify({
            "data": found_products,
            "not_found": not_found
        })


# добавление ресурса API
api.add_resource(Amount, "/api/amount")


# путь для работы с продуктами
@app.route('/get_product', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_product():
    if request.method == 'GET':
        table = request.args.get('table')
        product_name = request.args.get('product_name')
    else:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        table = data.get('table')
        product_name = data.get('product_name')

    if not table or not product_name:
        return jsonify({'error': 'Table and product_name are required'}), 400

    valid_tables = [
        'oboroty_21_2022', 'oboroty_101_2022', 'oboroty_105_2022',
        'ostatki_21_2022', 'ostatki_101_2022', 'ostatki_105_2022'
    ]

    if table not in valid_tables:
        return jsonify({'error': 'Invalid table name'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        if request.method == 'GET':
            query = f'SELECT * FROM {table} WHERE "Основные средства" = %s'
            cursor.execute(query, (product_name,))
            result = cursor.fetchall()

            if not result:
                return jsonify({'error': 'Product not found'}), 404

            column_names = [desc[0] for desc in cursor.description]
            products = [{col: val for col, val in zip(column_names, row) if val is not None} for row in result]

            return jsonify(products)

        elif request.method == 'POST':
            columns = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))
            query = f'INSERT INTO {table} ({columns}) VALUES ({values})'
            cursor.execute(query, tuple(data.values()))
            conn.commit()

            return jsonify({'message': 'Product added successfully'}), 201

        elif request.method == 'PUT':
            update_data = ', '.join([f'"{key}" = %s' for key in data if key != 'product_name'])
            query = f'UPDATE {table} SET {update_data} WHERE "Основные средства" = %s'
            cursor.execute(query, tuple(data[key] for key in data if key != 'product_name') + (product_name,))
            conn.commit()

            return jsonify({'message': 'Product updated successfully'})

        elif request.method == 'DELETE':
            query = f'DELETE FROM {table} WHERE "Основные средства" = %s'
            cursor.execute(query, (product_name,))
            conn.commit()

            return jsonify({'message': 'Product deleted successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)

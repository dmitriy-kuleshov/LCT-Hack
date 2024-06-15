import psycopg2
from config import DATABASE
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host=DATABASE['host'],
        port=DATABASE['port'],
        dbname=DATABASE['dbname'],
        user=DATABASE['user'],
        password=DATABASE['password']
    )
    return conn


@app.route('/get_product', methods=['GET'])
def get_product():
    table = request.args.get('table')
    product_name = request.args.get('product_name')

    if not table or not product_name:
        return jsonify({'error': 'Table and product_name are required'}), 400

    valid_tables = [
        'oboroty_21_2022', 'oboroty_101_2022', 'oboroty_105_2022' , 'ostatki_21_2022', 'ostatki_101_2022', 'ostatki_105_2022'
    ]

    if table not in valid_tables:
        return jsonify({'error': 'Invalid table name'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Предполагается, что столбец, который вы ищете, называется "Основные средства"
        query = f"SELECT * FROM {table} WHERE \"Основные средства\" = %s"
        cursor.execute(query, (product_name,))
        result = cursor.fetchall()

        if not result:
            cursor.close()
            conn.close()
            return jsonify({'error': 'Product not found'}), 404

        # Получаем названия столбцов
        column_names = [desc[0] for desc in cursor.description]
        # Преобразуем результат в список словарей
        products = [dict(zip(column_names, row)) for row in result]

        cursor.close()
        conn.close()

        return jsonify(products)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

import psycopg2
from config import DATABASE

conn = None


def get_db_connection():
    conn = psycopg2.connect(
        database=DATABASE['dbname'],
        user=DATABASE['user'],
        password=DATABASE['password'],
        host=DATABASE['host'],
        port=DATABASE['port']
    )
    return conn


def get_table_columns(conn, table_name):
    with conn.cursor() as cur:
        cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}';")
        columns = cur.fetchall()
    return [column[0] for column in columns]


def main():
    try:
        conn = get_db_connection()
        tables = ['oboroty_21_2022', 'oboroty_101_2022', 'oboroty_105_2022', 'ostatki_21_2022', 'ostatki_101_2022',
                  'ostatki_105_2022']
        for table in tables:
            columns = get_table_columns(conn, table)
            print(f"Table {table} has columns: {columns}")
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    main()

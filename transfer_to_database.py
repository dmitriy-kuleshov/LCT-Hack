import psycopg2
import pandas as pd
from config import DATABASE

# Список файлов CSV и соответствующих таблиц с указанием кодировок
csv_files = [
    ('Оборотная ведомость сч. 21 за 2022г. .csv', 'oboroty_21_2022', 'utf-32'),
    ('Оборотная ведомость сч. 101 за 2022г. .csv', 'oboroty_101_2022', 'utf-32'),
    ('Оборотная ведомость сч. 105 за 2022г. .csv', 'oboroty_105_2022', 'utf-32'),
    ('Ведомость остатков сч. 21 за 2022г. .csv', 'ostatki_21_2022', 'utf-8-sig'),
    ('Ведомость остатков сч. 101 за 2022г. .csv', 'ostatki_101_2022', 'utf-8-sig'),
    ('Ведомость остатков сч. 105 за 2022г. .csv', 'ostatki_105_2022', 'utf-8-sig')
]


# Функция для определения типа данных PostgreSQL на основе типа данных pandas
def get_pg_type(dtype):
    if dtype == 'object':
        return 'TEXT'
    elif dtype == 'int64':
        return 'NUMERIC'  # для целых чисел
    elif dtype == 'float64':
        return 'NUMERIC'  # для вещественных чисел
    else:
        return 'TEXT'  # По умолчанию используем текстовый тип


conn = None
cur = None

try:
    print("Подключение к базе данных...")
    conn = psycopg2.connect(
        database=DATABASE['dbname'],
        user=DATABASE['user'],
        password=DATABASE['password'],
        host=DATABASE['host'],
        port=DATABASE['port']
    )
    cur = conn.cursor()

    for csv_file, table_name, encoding in csv_files:
        try:
            print(f"Чтение файла {csv_file} с кодировкой {encoding}...")
            # Чтение CSV файла с помощью pandas для определения структуры данных
            df = pd.read_csv(csv_file, nrows=1, encoding=encoding)

            # Получение имен столбцов и их типов данных, преобразование типов данных для PostgreSQL
            column_names = df.columns.tolist()
            column_types = [get_pg_type(str(df[col].dtype)) for col in df.columns]

            # Формирование строки для создания таблицы
            create_table_query = f"CREATE TABLE {table_name} ("

            for i, (col_name, col_type) in enumerate(zip(column_names, column_types)):
                create_table_query += f'"{col_name}" {col_type}'  # Обрамляем название столбца в двойные кавычки
                if i < len(column_names) - 1:
                    create_table_query += ", "

            create_table_query += ");"

            print(f"Создание таблицы {table_name}...")
            # Создание таблицы в PostgreSQL
            cur.execute(create_table_query)
            conn.commit()

            print(f"Загрузка данных в таблицу {table_name}...")
            # Загрузка данных из CSV в PostgreSQL с использованием \COPY
            copy_query = f"COPY {table_name} FROM STDIN WITH (FORMAT CSV, HEADER true, DELIMITER ',');"
            with open(csv_file, 'r', encoding=encoding) as f:
                cur.copy_expert(sql=copy_query, file=f)
                conn.commit()

            print(f"Таблица {table_name} создана и данные успешно загружены из CSV в PostgreSQL!")
        except Exception as e:
            print(f"Ошибка при обработке файла {csv_file}: {e}")

except psycopg2.Error as e:
    print("Ошибка при подключении к PostgreSQL:", e.pgcode, e.pgerror, e.diag.message_primary)

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()

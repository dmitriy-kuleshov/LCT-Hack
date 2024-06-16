import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Функция для чтения CSV файла с различными кодировками
def read_csv_with_encodings(file_path, encodings):
    for encoding in encodings:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            return df
        except Exception as e:
            print(f"Ошибка чтения {file_path} с кодировкой {encoding}: {e}")
    return None

# Функция для поиска товара в файлах и вывода информации
def search_product_in_files(product_name, csv_files):
    product_data = []
    columns_of_interest = [
        'Остаточная стоимость', 'Сальдо на конец периода, дебет',
        'Остаток на 31 марта 2022 г. дебет', 'Остаток на 30 июня 2022 г. дебет',
        'Остаток на 30 сентября 2022 г. дебет', 'Остаток на 31 декабря 2022 г. дебет',
        'Количество(конец периода)', 'Суммарный остаток на 31 декабря 2022 г. дебет', 
        'Количество'
    ]

    for file_name, encodings in csv_files:
        print(f"Чтение: {file_name}")
        df = read_csv_with_encodings(file_name, encodings)
        
        if df is not None:
            if 'Основные средства' in df.columns:
                product_info = df[df['Основные средства'].str.contains(product_name, na=False)]
            elif 'Наименование нефинансового актива' in df.columns:
                product_info = df[df['Наименование нефинансового актива'].str.contains(product_name, na=False)]
            elif 'МОЛ' in df.columns:
                product_info = df[df['МОЛ'].str.contains(product_name, na=False)]
            else:
                print(f"Товар не найден в файле {file_name}")
                continue
            
            if not product_info.empty:
                print(product_info)
                # Сохраняем данные по остаткам товара
                if 'Дата' in df.columns:
                    for _, row in product_info.iterrows():
                        date = pd.to_datetime(row['Дата'])
                        value = None
                        for column in columns_of_interest:
                            if column in row and not pd.isna(row[column]):
                                value = row[column]
                                break
                        if value is not None:
                            product_data.append((date, value))
                        else:
                            print(f"Нет данных по остаткам для строки: {row}")
            else:
                print(f"Товар '{product_name}' не найден в файле {file_name}")
        else:
            print(f"Ошибка чтения {file_name}")

    print(f"Собранные данные по товару: {product_data}")
    return product_data

# Функция для рассчета потребления за каждый квартал
def calculate_consumption(product_data):
    quarterly_consumption = []
    
    # Сортируем данные по дате
    product_data.sort(key=lambda x: x[0])
    
    # Рассчитываем потребление за каждый квартал
    for i in range(len(product_data) - 1):
        start_date, start_value = product_data[i]
        end_date, end_value = product_data[i + 1]
        
        # Рассчитываем потребление как разницу между конечным и начальным остатками
        consumption = start_value - end_value
        quarterly_consumption.append((start_date, consumption))
    
    return quarterly_consumption

# Функция для прогнозирования времени до окончания товара
def forecast_end_date(product_data):
    # Посчитаем среднее время для потребления одной единицы товара
    consumption_rates = []
    for i in range(len(product_data) - 1):
        start_date, start_value = product_data[i]
        end_date, end_value = product_data[i + 1]
        
        # Рассчитываем потребление за период
        consumption = start_value - end_value
        if consumption > 0:
            rate = (end_date - start_date) / consumption
            consumption_rates.append(rate.days)
    
    # Среднее время потребления одной единицы товара
    average_consumption_rate = np.mean(consumption_rates)
    
    if np.isnan(average_consumption_rate) or average_consumption_rate <= 0:
        print("Недостаточно данных для прогноза или неверные данные.")
        return None
    
    # Прогнозируем время до окончания товара
    last_date, last_value = product_data[-1]
    future_date = last_date + pd.DateOffset(days=int(last_value * average_consumption_rate))
    
    return future_date

# Функция для построения графика остатков
def plot_product_data(product_data):
    if not product_data:
        print("Нет данных для построения графика.")
        return

    product_data.sort(key=lambda x: x[0])  # Сортируем по дате
    dates, values = zip(*product_data)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker='o')
    plt.xlabel('Дата')
    plt.ylabel('Остаток')
    plt.title('График остатков товара')
    plt.grid(True)
    plt.show()

# Основной блок кода для выполнения программы
if __name__ == "__main__":
    product_name = input(f"Введите имя товара: ")
    csv_files = [
        ('Оборотная ведомость сч. 21 за 2022г. .csv', ['utf-32', 'utf-8-sig', 'utf-16', 'latin1']),
        ('Оборотная ведомость сч. 101 за 2022г. .csv', ['utf-32', 'utf-8-sig', 'utf-16', 'latin1']),
        ('Оборотная ведомость сч. 105 за 2022г. .csv', ['utf-32', 'utf-8-sig', 'utf-16', 'latin1']),
        ('Ведомость остатков сч. 21 за 2022г. .csv', ['utf-8-sig', 'utf-32', 'utf-16', 'latin1']),
        ('Ведомость остатков сч. 101 за 2022г. .csv', ['utf-8-sig', 'utf-32', 'utf-16', 'latin1']),
        ('Ведомость остатков сч. 105 за 2022г. .csv', ['utf-8-sig', 'utf-32', 'utf-16', 'latin1'])
    ]
    
    # Поиск товара в файлах и сбор данных
    product_data = search_product_in_files(product_name, csv_files)

    if product_data:
        plot_product_data(product_data)
        
        # Рассчет потребления за кварталы
        quarterly_consumption = calculate_consumption(product_data)
        
        if quarterly_consumption:
            # Вывод потребления за каждый квартал
            print("Потребление за каждый квартал:")
            for date, consumption in quarterly_consumption:
                print(f"{date.date()}: {consumption}")
            
            # Прогнозирование времени до окончания товара
            end_date = forecast_end_date(product_data)
            
            if end_date:
                print(f"Товар '{product_name}' закончится к {end_date.date()}.")
            else:
                print("Не удалось спрогнозировать дату окончания товара.")
        else:
            print("Недостаточно данных для расчета потребления.")
    else:
        print("Нет данных для построения графика и прогнозирования.")
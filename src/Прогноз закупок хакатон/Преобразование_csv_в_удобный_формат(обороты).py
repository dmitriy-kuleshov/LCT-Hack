import csv
import os
import pandas as pd
import re

#функция обработки данных для исследования
def obrabotka(data, schN, qua):
    
    #добавление столбца классификатора
    data['Классификатор'] = None

    #регулярное выражение для поиска классификаторов
    classifier_pattern = re.compile(fr'^({schN}\.\d+)')

    #текущий классификатор
    current_classifier = None
    
    #удаление ненужных столбцов
    if 'Unnamed: 0' in data.columns:
        data.drop(columns=['Unnamed: 0'], inplace=True)
        
    if 'Unnamed: 0.1' in data.columns:
        data.drop(columns=['Unnamed: 0.1'], inplace=True)
            
    #замена пустых строк на NaN
    data.replace('', pd.NA, inplace=True)

    #добавление столбцов с кварталом и номером счёта
    data['Квартал'] = qua
    data['Номер счёта'] = schN
    
    if schN == 105:
        #проход по строкам DataFrame
        for index, row in data.iterrows():
            unnamed_value = str(row['Инвентарный / номенклатурный номер']).strip()
            match = classifier_pattern.search(unnamed_value)
            if match:
                #оставляем только код, убирая текстовое описание
                current_classifier = match.group(1)
            elif pd.notna(row['Код справочника']) and pd.notna(row['Наименование нефинансового актива']):
                data.at[index, 'Классификатор'] = current_classifier

        #удаление строк, в которых 'Основные средства' является NaN
        data = data.dropna(subset=['Код справочника', 'Наименование нефинансового актива']).copy()
        #удаление ненужных столбцов
        if 'Инвентарный / номенклатурный номер' in data.columns:
            data.drop(columns=['Инвентарный / номенклатурный номер'], inplace=True)
            
        data.rename(columns = {'Наименование нефинансового актива':'Основные средства'}, inplace = True)

        # Список столбцов в нужном порядке
        columns_titles = [
        'Основное средство', 'Код справочника', 'Единица измерения',
        'Остаток на 1 января 2022 г. дебет', 'Сумма на 1 января 2022 г. дебет',
        'Оборот за 1 квартал 2022 г. дебет', 'Суммарный оборот за 1кв. дебет',
        'Оборот за 1 квартал 2022 г. кредит', 'Суммарный оборот за 1кв. кредит',
        'Остаток на 31 марта 2022 г. дебет ', 'Суммарный остаток на 31 марта 2022 г. дебет ',
        'Классификатор', 'Квартал', 'Номер счёта', 'Остаток на 1 апреля 2022 г. Дебет',
        'Сумма на 1 апреля 2022 г. дебет', 'Оборот за 2 квартал 2022 г. дебет',
        'Суммарный оборот за 2кв. дебет', 'Оборот за 2 квартал 2022 г. кредит',
        'Суммарный оборот за 2кв. кредит', 'Остаток на 30 июня 2022 г. дебет ',
        'Суммарный остаток на 30 июня 2022 г. дебет ', 'Остаток на 1 июля 2022 г. дебет',
        'Сумма на 1 июля 2022 г. дебет', 'Оборот за 3 квартал 2022 г. дебет',
        'Суммарный оборот за 3кв. дебет', 'Оборот за 3 квартал 2022 г. кредит',
        'Суммарный оборот за 3кв. кредит', 'Остаток на 30 сентября 2022 г. дебет ',
        'Суммарный остаток на 30 сентября 2022 г. дебет ', 'Остаток на 1 октября 2022 г. дебет',
        'Сумма на 1 октября 2022 г. дебет', 'Оборот за 4 квартал 2022 г. дебет',
        'Суммарный оборот за 4кв. дебет', 'Оборот за 4 квартал 2022 г. кредит',
        'Суммарный оборот за 4кв. кредит', 'Остаток на 31 декабря 2022 г. дебет ',
        'Суммарный остаток на 31 декабря 2022 г. дебет'
        ]

        # Переупорядочиваем столбцы
        data = data.reindex(columns=columns_titles)
        
    
    elif schN == 101 or schN == 21:

        #проход по строкам DataFrame
        for index, row in data.iterrows():
            unnamed_value = str(row['Основные средства']).strip()
            match = classifier_pattern.search(unnamed_value)
            if match:
                #оставляем только код, убирая текстовое описание
                current_classifier = match.group(1)
            elif pd.notna(row['Основные средства']) and pd.notna(row['Количество(начало периода)']) and pd.notna(row['Количество(конец периода)']):
                data.at[index, 'Классификатор'] = current_classifier

        #удаление строк, в которых 'Основные средства' является NaN
        data = data.dropna(subset=['Основные средства', 'Сальдо на начало периода, дебет',
                               'Продукт, в интересах которого осуществляется закупка, код']).copy()
    
    #удаление пустых строк
    data = data.dropna(how='all')
        
    #переиндексация, начиная с 1
    data.reset_index(drop=True, inplace=True)
    
    
    return data



#чтение CSV (ведомость остатков сч.21)

#обработка данных на основе оборотных ведомостей 2022 год

data_21_1 = pd.read_csv("21_1_2022.csv", encoding="utf-32")
data_21_2 = pd.read_csv("21_2_2022.csv", encoding="utf-32")
data_21_3 = pd.read_csv("21_3_2022.csv", encoding="utf-32")
data_21_4 = pd.read_csv("21_4_2022.csv", encoding="utf-32")

#обработка данных             сч.No  Q
data_21_1 = obrabotka(data_21_1, 21, 1)
data_21_2 = obrabotka(data_21_2, 21, 2)
data_21_3 = obrabotka(data_21_3, 21, 3)
data_21_4 = obrabotka(data_21_4, 21, 4)



#чтение CSV (ведомость остатков сч.101)

#обработка данных на основе оборотных ведомостей 2022 год

data_101_1 = pd.read_csv("101_1_2022.csv", encoding="utf-32")
data_101_2 = pd.read_csv("101_2_2022.csv", encoding="utf-32")
data_101_3 = pd.read_csv("101_3_2022.csv", encoding="utf-32")
data_101_4 = pd.read_csv("101_4_2022.csv", encoding="utf-32")

#обработка данных                сч.No  Q
data_101_1 = obrabotka(data_101_1, 101, 1)
data_101_2 = obrabotka(data_101_2, 101, 2)
data_101_3 = obrabotka(data_101_3, 101, 3)
data_101_4 = obrabotka(data_101_4, 101, 4)



#чтение CSV (ведомость остатков сч.105)

#обработка данных на основе оборотных ведомостей 2022 год

data_105_1 = pd.read_csv("105_1_2022.csv", encoding="utf-32")
data_105_2 = pd.read_csv("105_2_2022.csv", encoding="utf-32")
data_105_3 = pd.read_csv("105_3_2022.csv", encoding="utf-32")
data_105_4 = pd.read_csv("105_4_2022.csv", encoding="utf-32")

#обработка данных                сч.No  Q
data_105_1 = obrabotka(data_105_1, 105, 1)
data_105_2 = obrabotka(data_105_2, 105, 2)
data_105_3 = obrabotka(data_105_3, 105, 3)
data_105_4 = obrabotka(data_105_4, 105, 4)



#ведомость остатков по счёту 21
data21_q14 = pd.concat([data_21_1, data_21_2, 
                 data_21_3, data_21_4])

data21_q14.to_csv('Оборотная ведомость сч. 21 за 2022г. .csv', index=False, encoding="utf-32")


#ведомость остатков по счёту 101
data101_q14 = pd.concat([data_101_1, data_101_2, 
                 data_101_3, data_101_4])

data101_q14.to_csv('Оборотная ведомость сч. 101 за 2022г. .csv', index=False, encoding="utf-32")


#ведомость остатков по счёту 105
data105_q14 = pd.concat([data_105_1, data_105_2, 
                 data_105_3, data_105_4])

data105_q14.to_csv('Оборотная ведомость сч. 105 за 2022г. .csv', index=False, encoding="utf-32")

#общая оборотная ведомость по всем счетам
dataedinya = pd.concat([data21_q14, data101_q14, data105_q14])
dataedinya.to_csv('Оборотная ведомость по сч. 21, 101, 105 за 2022г. .csv', index=False, encoding="utf-32")
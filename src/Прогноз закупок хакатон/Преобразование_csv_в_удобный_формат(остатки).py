import csv
import os
import pandas as pd
import re



#функция обработки данных для исследования
def obrabotka(data, schN, date):
    
    #добавление столбцов с датой и номером счёта
    data['Номер счёта'] = schN
    data['Дата'] = date    

    if schN == 105:
        #преобразование в числовой формат
        data.loc[:, 'Цена'] = pd.to_numeric(data['Цена'], errors='coerce')
        data.loc[:, 'Количество'] = pd.to_numeric(data['Количество'], errors='coerce')
        data.loc[:, 'Сумма'] = pd.to_numeric(data['Сумма'], errors='coerce')
    
        #удаление ненужных столбцов
        data.drop(columns=['Unnamed: 0'], inplace=True)
        
        #переименование столбца с номером строки
        data.rename(columns={'Unnamed: 0': 'ID'}, inplace=True)        

        #добавление столбца классификатора
        data['Классификатор'] = None

        #регулярное выражение для поиска классификаторов в формате 105.№
        classifier_pattern = re.compile(r'^\d{3}\.\d+$')

        #текущий классификатор
        current_classifier = None

        #проход по строкам DataFrame
        for index, row in data.iterrows():
            mol_value = str(row['МОЛ']).strip()
            if classifier_pattern.match(mol_value):
                current_classifier = mol_value
            elif pd.notna(row['Цена']) and pd.notna(row['Количество']) and pd.notna(row['Сумма']):
                data.at[index, 'Классификатор'] = current_classifier

        #удаление строк, которые не содержат данные о товарах
        data = data.dropna(subset=['Цена', 'Количество', 'Сумма'], how='all').reset_index(drop=True)
        data = data.dropna(subset=['Цена']).copy() #удалить NaN-значные строки
        data.rename(columns = {'МОЛ':'Основные средства'}, inplace = True)
    
    elif schN == 101:
        
        # Преобразование в числовой формат
        columns_to_numeric = [
            'Инвентарный номер', 'Амортизационная группа', 'Срок полезного использования',
            'Мес. норма износа, %', 'Износ, %', 'Балансовая стоимость', 'Количество',
            'Сумма амортизации', 'Остаточная стоимость'
        ]
        
        for col in columns_to_numeric:
            data[col] = pd.to_numeric(data[col], errors='coerce')
                   
        # Добавление столбца классификатора
        data['Классификатор'] = None

        # Регулярное выражение для поиска классификаторов в формате 101.№
        classifier_pattern = re.compile(r'^(101\.\d+)')

        # Текущий классификатор
        current_classifier = None

        # Проход по строкам DataFrame
        for index, row in data.iterrows():
            osn_sredstvo_value = str(row['Unnamed: 0']).strip()
            match = classifier_pattern.search(osn_sredstvo_value)
            if match:
                # Оставляем только код, убирая текстовое описание
                current_classifier = match.group(1)
            elif pd.notna(row['Инвентарный номер']) and pd.notna(row['Балансовая стоимость']) and pd.notna(row['Количество']):
                data.at[index, 'Классификатор'] = current_classifier

        # Удаление ненужных столбцов
        if 'Unnamed: 0' in data.columns:
            data.drop(columns=['Unnamed: 0'], inplace=True)
        
        if 'Unnamed: 0.1' in data.columns:
            data.drop(columns=['Unnamed: 0.1'], inplace=True)

        # Удаление строк, которые не содержат данные о товарах
        data = data.dropna(subset=[
            'Основное средство', 'Инвентарный номер', 'ОКОФ', 'Амортизационная группа',
            'Способ начисления амортизации', 'Дата принятия к учету', 'Состояние',
            'Срок полезного использования', 'Мес. норма износа, %', 'Износ, %',
            'Балансовая стоимость', 'Количество', 'Сумма амортизации', 'Остаточная стоимость'
        ], how='all').reset_index(drop=True)
        
        # Удаление строк, в которых 'Инвентарный номер' является NaN
        data = data.dropna(subset=['Инвентарный номер']).copy()      
        
        data.rename(columns = {'Основное средство':'Основные средства'}, inplace = True)
        
    elif schN == 21:
        # Преобразование в числовой формат
        columns_to_numeric = [
            'Инвентарный номер', 'Амортизационная группа', 'Срок полезного использования',
            'Мес. норма износа, %', 'Износ, %', 'Балансовая стоимость', 'Количество',
            'Сумма амортизации', 'Остаточная стоимость'
        ]
        
        for col in columns_to_numeric:
            data[col] = pd.to_numeric(data[col], errors='coerce')
                   
        # Добавление столбца классификатора
        data['Классификатор'] = None

        # Регулярное выражение для поиска классификаторов в формате 21.№
        classifier_pattern = re.compile(r'^(21\.\d+)')

        # Текущий классификатор
        current_classifier = None

        # Проход по строкам DataFrame
        for index, row in data.iterrows():
            osn_sredstvo_value = str(row['Unnamed: 0']).strip()
            match = classifier_pattern.search(osn_sredstvo_value)
            if match:
                # Оставляем только код, убирая текстовое описание
                current_classifier = match.group(1)
            elif pd.notna(row['Дата принятия к учету']) and pd.notna(row['Балансовая стоимость']) and pd.notna(row['Количество']):
                data.at[index, 'Классификатор'] = current_classifier

        # Удаление ненужных столбцов
        if 'Unnamed: 0' in data.columns:
            data.drop(columns=['Unnamed: 0'], inplace=True)
        
        if 'Unnamed: 0.1' in data.columns:
            data.drop(columns=['Unnamed: 0.1'], inplace=True)

        # Удаление строк, которые не содержат данные о товарах
        data = data.dropna(subset=[
            'Основное средство', 'Инвентарный номер', 'ОКОФ', 'Амортизационная группа',
            'Способ начисления амортизации', 'Дата принятия к учету', 'Состояние',
            'Срок полезного использования', 'Мес. норма износа, %', 'Износ, %',
            'Балансовая стоимость', 'Количество', 'Сумма амортизации', 'Остаточная стоимость'
        ], how='all').reset_index(drop=True)
        
        # Удаление строк, в которых 'Дата принятия к учету' является NaN
        data = data.dropna(subset=['Дата принятия к учету']).copy()  
        
        data.rename(columns = {'Основное средство':'Основные средства'}, inplace = True)

    #переиндексация, начиная с 1
    data.reset_index(drop=True, inplace=True)
    
    return data



#чтение CSV (ведомость остатков сч.21)

#обработка данных на основе ведомости остатков 
#на 31.03, 30.06, 30.09, 31.12 2022 года.

data_21_31032022 = pd.read_csv("21_31.03.2022.csv", encoding="utf-8")
data_21_30062022 = pd.read_csv("21_30.06.2022.csv", encoding="utf-8")
data_21_30092022 = pd.read_csv("21_30.09.2022.csv", encoding="utf-8")
data_21_31122022 = pd.read_csv("21_31.12.2022.csv", encoding="utf-8")

#обработка данных                             сч.No    Дата
data_21_31032022 = obrabotka(data_21_31032022, 21, "31.03.2022")
data_21_30062022 = obrabotka(data_21_30062022, 21, "30.06.2022")
data_21_30092022 = obrabotka(data_21_30092022, 21, "30.09.2022")
data_21_31122022 = obrabotka(data_21_31122022, 21, "31.12.2022")

#чтение CSV (ведомость остатков сч.101)

#обработка данных на основе ведомости остатков 
#на 31.03, 30.06, 30.09, 31.12 2022 года.

data_101_31032022 = pd.read_csv("101_31.03.2022.csv", encoding="utf-8")
data_101_30062022 = pd.read_csv("101_30.06.2022.csv", encoding="utf-8")
data_101_30092022 = pd.read_csv("101_30.09.2022.csv", encoding="utf-8")
data_101_31122022 = pd.read_csv("101_31.12.2022.csv", encoding="utf-8")

#обработка данных                               сч.No    Дата
data_101_31032022 = obrabotka(data_101_31032022, 101, "31.03.2022")
data_101_30062022 = obrabotka(data_101_30062022, 101, "30.06.2022")
data_101_30092022 = obrabotka(data_101_30092022, 101, "30.09.2022")
data_101_31122022 = obrabotka(data_101_31122022, 101, "31.12.2022")

#чтение CSV (ведомость остатков сч.105)

#обработка данных на основе ведомости остатков 
#на 31.03, 30.06, 30.09, 31.12 2022 года.

data_105_31032022 = pd.read_csv("105_31.03.2022.csv", encoding="utf-8")
data_105_30062022 = pd.read_csv("105_30.06.2022.csv", encoding="utf-8")
data_105_30092022 = pd.read_csv("105_30.09.2022.csv", encoding="utf-8")
data_105_31122022 = pd.read_csv("105_31.12.2022.csv", encoding="utf-8")

#обработка данных                               сч.No    Дата
data_105_31032022 = obrabotka(data_105_31032022, 105, "31.03.2022")
data_105_30062022 = obrabotka(data_105_30062022, 105, "30.06.2022")
data_105_30092022 = obrabotka(data_105_30092022, 105, "30.09.2022")
data_105_31122022 = obrabotka(data_105_31122022, 105, "31.12.2022")



#ведомость остатков по счёту 21
data21 = pd.concat([data_21_31032022, data_21_30062022, 
                 data_21_30092022, data_21_31122022])

data21.to_csv('Ведомость остатков сч. 21 за 2022г. .csv', index=False, encoding="utf-8-sig")

#ведомость остатков по счёту 101
data101 = pd.concat([data_101_31032022, data_101_30062022, 
                 data_101_30092022, data_101_31122022])

data101.to_csv('Ведомость остатков сч. 101 за 2022г. .csv', index=False, encoding="utf-8-sig")

#ведомость остатков по счёту 105
data105 = pd.concat([data_105_31032022, data_105_30062022, 
                 data_105_30092022, data_105_31122022])

data105.to_csv('Ведомость остатков сч. 105 за 2022г. .csv', index=False, encoding="utf-8-sig")

#общая ведомость остатков по всем счетам
dataedinya = pd.concat([data21, data101, data105])
dataedinya.to_csv('Ведомость остатков по сч. 21, 101, 105 за 2022г. .csv', index=False, encoding="utf-8-sig")
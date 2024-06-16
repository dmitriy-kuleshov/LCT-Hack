import pandas as pd


#преобразование данных в csv - ведомости остатков
data_xlsx = pd.read_excel('Ведомость остатков на 31.03.2022г. (сч. 105).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_31.03.2022.csv', encoding='utf-8-sig')
data_xlsx = pd.read_excel('Ведомость остатков на 31.03.2022г. (сч. 101).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_31.03.2022.csv', encoding='utf-8-sig')
data_xlsx = pd.read_excel('Ведомость остатков на 31.03.2022г. (сч. 21).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_31.03.2022.csv', encoding='utf-8-sig')


data_xlsx = pd.read_excel('Ведомость остатков на 30.06.2022г. (сч. 105).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_30.06.2022.csv', encoding='utf-8-sig')
data_xlsx = pd.read_excel('Ведомость остатков на 30.06.2022г. (сч. 101).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_30.06.2022.csv', encoding='utf-8-sig')
data_xlsx = pd.read_excel('Ведомость остатков на 30.06.2022г. (сч. 21).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_30.06.2022.csv', encoding='utf-8-sig')


data_xlsx = pd.read_excel('Ведомость остатков на 30.09.2022г. (сч. 105).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_30.09.2022.csv', encoding='utf-8-sig')
data_xlsx = pd.read_excel('Ведомость остатков на 30.09.2022г. (сч. 101).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_30.09.2022.csv', encoding='utf-8-sig')
data_xlsx = pd.read_excel('Ведомость остатков на 30.09.2022г. (сч. 21).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_30.09.2022.csv', encoding='utf-8-sig')


data_xlsx = pd.read_excel('Ведомость остатков на 31.12.2022г. (сч. 105).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_31.12.2022.csv', encoding='utf-8-sig')
data_xlsx = pd.read_excel('Ведомость остатков на 31.12.2022г. (сч. 101).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_31.12.2022.csv', encoding='utf-8-sig')
data_xlsx = pd.read_excel('Ведомость остатков на 31.12.2022г. (сч. 21).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_31.12.2022.csv', encoding='utf-8-sig')




#преобразование данных в csv - оборотно-счётные ведомости
data_xlsx = pd.read_excel('Оборотная ведомость по сч. 105 за 1 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_1_2022.csv', encoding='utf-32')
data_xlsx = pd.read_excel('Оборотная ведомость по сч. 105 за 2 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_2_2022.csv', encoding='utf-32')
data_xlsx = pd.read_excel('Оборотная ведомость по сч. 105 за 3 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_3_2022.csv', encoding='utf-32')
data_xlsx = pd.read_excel('Оборотная ведомость по сч. 105 за 4 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_4_2022.csv', encoding='utf-32')


data_xlsx = pd.read_excel('Оборотно-сальдовая ведомость по сч. 101 за 1 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_1_2022.csv', encoding='utf-32')
data_xlsx = pd.read_excel('Оборотно-сальдовая ведомость по сч. 101 за 2 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_2_2022.csv', encoding='utf-32')
data_xlsx = pd.read_excel('Оборотно-сальдовая ведомость по сч. 101 за 3 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_3_2022.csv', encoding='utf-32')
data_xlsx = pd.read_excel('Оборотно-сальдовая ведомость по сч. 101 за 4 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_4_2022.csv', encoding='utf-32')


data_xlsx = pd.read_excel('Оборотно-сальдовая ведомость по сч. 21 за 1 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_1_2022.csv', encoding='utf-32')
data_xlsx = pd.read_excel('Оборотно-сальдовая ведомость по сч. 21 за 2 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_2_2022.csv', encoding='utf-32')
data_xlsx = pd.read_excel('Оборотно-сальдовая ведомость по сч. 21 за 3 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_3_2022.csv', encoding='utf-32')
data_xlsx = pd.read_excel('Оборотно-сальдовая ведомость по сч. 21 за 4 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_4_2022.csv', encoding='utf-32')
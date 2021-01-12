import pandas as pd

football = pd.read_csv('data_sf.csv')
df = football

df.groupby(['Nationality'])[['Club','Name']].nunique()
df.groupby(['Club'])['Name'].count()
df.groupby(['Club'])['Dribbling'].median()
df.groupby(['Club'])['Strength'].max()
df.groupby(['Club'])['Balance'].min()

# Посчитайте среднюю (mean) и медианную (median) зарплату (Wage) футболистов 
# из разных клубов (Club). 
# В скольких клубах средняя и медианная зарплаты совпадают?
#
# Подсказка: чтобы в процессе группировки применить к данным одновременно 
# две агрегирующие функции, необходимо указать их как аргументы метода agg:
# df.groupby(столбец_для_группировки)[столбцы_для_отображения].agg(['функция_1', 'функция_2'])

x = df.groupby(['Club'])['Wage'].agg(['mean','median'])
x.columns
x.columns = ['mean','median']
mm = x[ x['mean'] == x['median'] ]
len(mm)

# Продолжаем работать с клубами, в которых средняя зарплата совпадает с медианной. 
# Каков максимальный размер средней зарплаты в этой группе клубов?

mm['mean'].max()

# Как называется клуб, где игроки получают такую зарплату?
mm[ mm['mean'] == mm['mean'].max() ].index[0]
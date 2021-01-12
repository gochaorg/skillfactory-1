import pandas as pd

football = pd.read_csv('data_sf.csv')
df = football

df.groupby(['Club']).groups
grouped_df = df.groupby(['Club']).sum()
grouped_df.loc['Ajax']
grouped_df.loc['Ajax']['Wage']

grouped_df = df.groupby(['Club'])['Wage'].sum()
display(grouped_df)

# Но помните наш исходный вопрос: "В каком клубе самая высокая зарплата?"
# Для ответа на этот вопрос нам достаточно лишь отсортировать 
# полученные данные по убыванию суммы зарплат с помощью функции sort_values:

grouped_df = df.groupby(['Club'])['Wage'].sum().sort_values(ascending=False)
print(grouped_df.head(5))

###############

# Отметьте позиции (Position), по которым общая сумма зарплат (Wage) игроков 
# превышает 5 млн евро в год.

x = df.groupby(['Position'])['Wage'].sum().sort_values(ascending=False)
[ (a,b) for (a,b) in x.items() if b > 5000000 ]

import pandas as pd

football = pd.read_csv('data_sf.csv')
df = football

df.groupby(['Nationality'])[['Club','Name']].nunique()
df.groupby(['Club'])['Name'].count()
df.groupby(['Club'])['Dribbling'].median()
df.groupby(['Club'])['Strength'].max()
df.groupby(['Club'])['Balance'].min()

# С помощью функции groupby посчитайте сумму зарплат (Wage) футболистов 
# клуба (Club) "Chelsea".

df.groupby(['Club']).sum().loc['Chelsea']['Wage']

# Определите максимальную зарплату футболиста 
# национальности (Nationality) Аргентина ("Argentina") в возрасте 20 лет.

df.groupby(['Nationality','Age']).max().loc['Argentina'].loc[20]['Wage']

# Определите максимальную зарплату футболиста 
# национальности (Nationality) Аргентина ("Argentina") в возрасте 30 лет.

df.groupby(['Nationality','Age']).max().loc['Argentina'].loc[30]['Wage']

# Определите минимальную зарплату футболиста 
# национальности (Nationality) Аргентина ("Argentina") в возрасте 30 лет.

df.groupby(['Nationality','Age']).min().loc['Argentina'].loc[30]['Wage']

# Определите максимальную силу (Strength) и баланс (Balance) 
# среди игроков клуба (Club) "FC Barcelona" из Аргентины ("Argentina"). 
# Ответ введите через точку с запятой без пробела.

df.groupby(['Club','Nationality']).max().loc['FC Barcelona'].loc['Argentina'][['Strength','Balance']]
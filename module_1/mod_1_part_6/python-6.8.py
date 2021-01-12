import pandas as pd

football = pd.read_csv('data_sf.csv')
df = football

# df.groupby(['Nationality'])[['Wage','Age','ShotPower']].mean()
df.groupby(['Nationality'])[['Wage','Age','ShotPower']].mean().sort_values(['Wage'],ascending=False).head(10)
df.loc[df['Nationality'] == 'Dominican Republic'][['Name','Club','Wage','Age','ShotPower']]

# Посчитайте среднюю зарплату (Wage) и цену (Value) игроков разных позиций (Position). 
# Представители какой позиции имеют самую высокую среднюю ценность?

df.groupby(['Position'])[['Wage','Value']].mean().sort_values(['Value'],ascending=False).head(10)
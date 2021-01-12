import pandas as pd

football = pd.read_csv('data_sf.csv')
df = football

pivot = df.loc[df['Club'].isin(['FC Barcelona','Real Madrid','Juventus','Manchester United'])].pivot_table(values=['Wage'],
index=['Nationality'],
columns=['Club'],
aggfunc='sum',
margins=True)
display(pivot)

df2 = df.pivot_table(columns = 'Position', index = 'Club', values = 'Wage', aggfunc = 'max')
df2.loc['Manchester City']['GK'] 
import pandas as pd

football = pd.read_csv('data_sf.csv')
df = football

small_df = df[df.columns[1:8]].head(25)
small_df

s = small_df['Nationality'].value_counts(normalize=True)
display(s)

# Данные об игроках каких позиций (Position) занимают более 10% датасета?
[ [ x[0], x[1] ] 
  for x in dict(football.Position.value_counts(normalize=True)).items() 
  if x[1] > 0.1
]

# Данные об игроках каких позиций (Position) занимают менее 1% датасета?
[ [ x[0], x[1] ] 
  for x in dict(football.Position.value_counts(normalize=True)).items() 
  if x[1] < 0.01
]

#########

s = small_df['Age'].value_counts()
display(s)

s = small_df['Wage'].value_counts()
display(s)

s = small_df['Wage'].value_counts(bins=4)
display(s)

small_df.loc[(small_df['Wage'] > s.index[3].left) & (small_df['Wage'] <= s.index[3].right)]

small_df = df[df.columns[0:7]].head(25)
s = small_df['Wage'].value_counts(bins=4)
s.index
s.index[3]
s.index[3].left
s.index[3].right
small_df['Wage'] > s.index[3].left

##########
football.FKAccuracy.value_counts()

football.FKAccuracy.describe()
football.FKAccuracy.value_counts(bins=5)
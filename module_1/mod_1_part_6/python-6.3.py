import pandas as pd

football = pd.read_csv('data_sf.csv')
df = football

small_df = df[df.columns[1:8]].head(25)
small_df

s = small_df['Nationality'].value_counts()
display(s)

s.index
s.index[0]
len(s.index)
s['Germany']
s.loc[s > 1]

# Сколько футбольных клубов представлено в датасете?
football.Club.unique().size
len(football.Club.unique())

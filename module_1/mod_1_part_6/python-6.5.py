import pandas as pd

football = pd.read_csv('data_sf.csv')
df = football

small_df = df[df.columns[0:7]].head(25)

############################

s = small_df['Nationality'].value_counts()
print(s.index)
print(len(s.index))
len(small_df['Nationality'].unique())
small_df['Nationality'].nunique()

result = len(df['Position'].unique)
df['Position'].nunique() 
len(df['Position'].unique()) 
df['Position'].unique() 
df['Position'].count() 
len(df['Position'].value_counts()) 


############

s = small_df['Nationality'].value_counts()
s_df = s.reset_index()
display(s_df)

s_df.columns = ['Nationality','Players Count']
display(s_df)


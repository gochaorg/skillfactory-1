import pandas as pd

football = pd.read_csv('data_sf.csv')
df = football

small_df = df[df.columns[1:8]].head(25)
small_df

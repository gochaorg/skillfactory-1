import pandas as pd

d = pd.read_csv('data_sf.csv')
d.describe()

d.describe(include = ['object'])
# d.describe(include = ['GK'])
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(d.describe(include='all'))

############
df = pd.DataFrame([[i,i+1.2,i+2, 'hi'] for i in range(10)],
                  columns = ['foo', 'bar', 'baz', 'foobar'])
display(df)
df.mean()
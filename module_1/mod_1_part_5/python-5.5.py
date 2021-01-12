import pandas as pd

football = pd.read_csv('data_sf.csv')
display(football.info())

football.columns.size
football['Club'].describe()

football['Wage'].describe()
dict(football.dtypes)['Wage']

football['Position'].describe()

len([ str(x) for x in dict(football.dtypes).values() if str(x)=='int64' ])
len([ str(x) for x in dict(football.dtypes).values() if str(x)=='object' ])
len([ str(x) for x in dict(football.dtypes).values() if str(x)=='float64' ])

football.columns[football.columns.size-1]

[ x for x in football.columns if x == 'Surname' ]
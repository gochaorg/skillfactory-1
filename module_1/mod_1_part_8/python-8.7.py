import pandas as pd

log = pd.read_csv(
    'log.csv', 
    header=None
    )
log.describe(include='all')

sample = pd.read_csv('sample.csv')
sample.columns = [ 'name', 'city', 'age', 'profession' ]

log.columns = [ 'user_id', 'time', 'bet', 'win' ]

users = pd.read_csv(
    'users.csv', 
    encoding='koi8-r',delimiter='\t',
    names=['user_id','email','geo'],header=None,skiprows=1
    )

sample.info()
sample.name.unique()
sample.city.unique()
sample.age.unique()
sample.profession.unique()

sample.values_count()
sample.city.value_counts().sum()

log.user_id.value_counts()
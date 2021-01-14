import pandas as pd

log = pd.read_csv(
    'log.csv', 
    header=None
    )
log.columns = [ 'user_id', 'time', 'bet', 'win' ]
log.describe(include='all')

sample = pd.read_csv('sample.csv')
sample.columns = [ 'name', 'city', 'age', 'profession' ]

users = pd.read_csv(
    'users.csv', 
    encoding='koi8-r',delimiter='\t',
    names=['user_id','email','geo'],header=None,skiprows=1
    )

#################################

sample = pd.read_csv("sample.csv")
sample3 = sample[ sample.City.str.contains('о', na=False) ]
sample4 = sample[ ~sample.City.str.contains('о', na=False) ]

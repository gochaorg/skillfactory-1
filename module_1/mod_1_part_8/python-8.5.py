import pandas as pd

log = pd.read_csv(
    'log.csv', 
    header=None
    )
log.describe(include='all')

sample = pd.read_csv('sample.csv')
sample.columns = [ 'name', 'city', 'age', 'profession' ]

log.columns = [ 'user_id', 'time', 'bet', 'win' ]
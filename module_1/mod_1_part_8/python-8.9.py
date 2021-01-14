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

# С помощью функции query найдите тех, 
# у кого ставка меньше 2000, а выигрыш больше 0. 
# Сохраните в новый датафрейм log2. 

log = pd.read_csv("log.csv",header=None)
log.columns = ['user_id','time', 'bet','win']
# Напишите ваш код ниже
log2 = log.query('bet < 2000 & win > 0')
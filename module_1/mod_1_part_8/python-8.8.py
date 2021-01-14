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

# sample2 = sample[ sample.age < 30 ]
# bug https://skillfactorydspr.slack.com/archives/C018B0V2SMR/p1608748006351500
sample2 = sample[ sample['Age'] < 30 ]

########################

# Создайте новый датафрейм log_win, 
# в который будут входить только записи, 
# где пользователь выиграл. 
# Посчитайте, сколько таких записей, и сохраните в переменной win_count. 
log = pd.read_csv("log.csv",header=None)
log.columns = ['user_id','time', 'bet','win']
win_count=len(log[ log.win>0 ])


############
# Создайте новый датафрейм sample2, 
# в который будут входить только записи о рабочих младше 30 лет. 
sample = pd.read_csv("sample.csv")
sample2 = sample[ ( sample.Profession == 'Рабочий' ) & (sample.Age < 30) ]
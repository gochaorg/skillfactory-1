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
sample2 = sample.copy()
sample2.Age = sample2.Age.apply( lambda x:x+1 )

#  С помощью apply и lambda-функции замените все буквы в поле City 
# на маленькие и сохраните в sample2. 
# Вам может понадобиться функция s.lower().
# Обратите внимание: когда в столбце есть пропущенные значения, 
# необходимо в явном виде указывать, что это str.
sample = pd.read_csv("sample.csv")
sample2 = sample.copy()
sample2.City = sample2.City.apply( lambda x:str(x).lower() )

#######

def profession_code(s):
    lst = ['Рабочий', 'Менеджер']
    idx = lst.index(s)
    return idx if idx>=0 else 2

def profession_code(s):
    try:
        return ['Рабочий', 'Менеджер'].index(s)
    except:
        return 2


###################################
# Примените функцию profession_code для того, 
# чтобы заменить поле Profession с помощью apply. 
# Сохраните получившийся датафрейм в переменную sample2. 

sample = pd.read_csv("sample.csv")
sample2 = sample.copy()
sample2.Profession = sample2.Profession.apply( profession_code )

########################
# Напишите функцию age_category, которая на вход получает число, а на выход отдаёт: 
#     "молодой" — если возраст меньше 23
#    "средний" — если возраст от 23 до 35
#    "зрелый" — если возраст больше 35

def age_category(age):
    return "молодой" if age < 23 else ("средний" if age < 35 else "зрелый" )

sample = pd.read_csv("sample.csv")
sample['Age_category'] = sample.Age.apply(age_category)

###############################################
# Преобразуем поле user_id в датафрейме log, 
# оставив только идентификатор пользователя. 
# Например, вместо "Запись пользователя № — user_974" 
# должно остаться только "user_974".
#
# На месте записей с ошибками в user_id 
# должна быть пустая строка "". 
# Сделайте это через apply и новую функцию, которую вы создадите. 
# Результат сохраните в log:

log = pd.read_csv('log.csv', header=None)
log.columns = ['user_id','time','bet','win']

def fetchUserId( s ):
    idx = s.find( 'user' )
    return s[idx:] if idx>=0 else ''

log.user_id = log.user_id.apply(fetchUserId)

##################
# 

def remove_prefix(text, prefix):    
    return text[text.startswith(prefix) and len(prefix):] if type(text) is str else text

log = pd.read_csv("log.csv",header=None) 
log.columns = ['user_id','time','bet','win']
log.time = log.time.apply( lambda x:remove_prefix(x,'[') )
t = log.time[0]

#################
def fetchUserId( s ):
    idx = s.find( 'user' )
    return s[idx:] if idx>=0 else ''

def remove_prefix(text, prefix):    
    return text[text.startswith(prefix) and len(prefix):] if type(text) is str else text

log = pd.read_csv("log.csv",header=None) 
log.columns = ['user_id','time','bet','win']
log.time = log.time.apply( lambda x:remove_prefix(x,'[') )
log.user_id = log.user_id.apply(fetchUserId)
log = log[ log.user_id != '' ]
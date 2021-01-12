import pandas as pd

football = pd.read_csv('data_sf.csv')
football.describe()
football.describe(include = ['object'])

# Чему равен средний возраст (Age), футболистов в наборе данных, округлённый до целого?
round(football.Age.mean())

# Каково количество непустых строк в колонке Composure (Хладнокровие) набора данных о футболистах?
football.Composure.count()
football.Composure.size
football.Composure.value_counts().sum()
football.Composure.items().size

# Каково в наборе данных о футболистах стандартное отклонение параметра коротких пасов (ShortPassing), округлённое до второго знака после запятой?
football.ShortPassing.describe()
round(football.ShortPassing.std(),2)

# Какова сумма заработных плат за год (Wage) в наборе данных о футболистах?
football.Wage.sum()

# Какова минимальная стоимость футболиста (Value) в наборе данных о футболистах?
football.Value.min()
import pandas as pd

football = pd.read_csv('data_sf.csv')
football.describe()
football.describe(include = ['object'])

# Чтобы вывести информацию целиком, а не в обрезанном виде, можно написать:
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(football.describe())

# Каково среднее значение возраста футболистов в наборе данных (округлите до целого)?
football['Age'].describe()
round(football['Age'].mean())
round(football['Age'].min())

# Какова максимальная заработная плата за год (Wage) у футболистов?
football['Wage'].max()

# Какова медианная заработная плата за год (Wage) у футболистов?
football['Wage'].median()

football['Penalties'].min()

# Какое значение у первого (25%) квартиля параметра ShortPassing?
football['ShortPassing'].quantile(0.25)

# Какова самая частая национальность (Nationality) футболистов?
print( football['Nationality'].describe() )
print( football['Nationality'].value_counts() )
print( football['Nationality'].value_counts().index[0] )

# Сколько разных клубов в наборе данных о футболистах?
football['Club'].describe()
football['Club'].unique().size

# Сколько раз встречается самая частая позиция 'GK' в наборе данных?
football['Position'].describe()
football['Position'].value_counts().values[0]

# Каков максимальный возраст футболиста?
football['Age'].max()
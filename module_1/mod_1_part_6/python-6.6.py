import pandas as pd

football = pd.read_csv('data_sf.csv')
df = football

# У какого процента испанских футболистов (Nationality = 'Spain') 
# зарплата (Wage) находится в пределах 25% минимума 
# от наблюдаемого уровня зарплат среди испанских игроков? 
# Ответ дайте в виде целого числа (округлите полученный результат) без знака %.

dfSpain = df[ df.Nationality == 'Spain' ]
wageRange = dfSpain.Wage.value_counts(bins=4)
wageRange.values
wageRange.values[0]
wageRange.values.sum()
round(100.0 * wageRange.values[0] / wageRange.values.sum())

# Укажите количество уникальных сборных (Nationality), 
# к которым относятся футболисты, выступающие за клуб (Club) 
# "Manchester United".

df[ df.Club == 'Manchester United' ].Nationality.unique().size

# С помощью функции unique определите 
# двух футболистов из Бразилии (Nationality = 'Brazil'), 
# выступающих за клуб (Club) 'Juventus'. 
# Перечислите их имена (Name, как в датафрейме) 
# через запятую в алфавитном порядке.

df[ (df.Club == 'Juventus') & (df.Nationality == 'Brazil') ].Name.unique()

# Укажите, какой из клубов (Club) 
# насчитывает большее количество футболистов возрастом (Age) старше 35 лет.

df[ df.Age > 35 ].Club.value_counts()

# С помощью функции value_counts с параметром bins 
# разбейте всех футболистов родом из Аргентины (Nationality = 'Argentina') 
# на 4 равные группы по возрасту. 
# Сколько футболистов в возрасте от 34,75 до 41 года в сборной Аргентины?

df[ df.Nationality == 'Argentina' ].Age.value_counts( bins=4 )

# Сколько процентов футболистов из Испании (Nationality = 'Spain') 
# имеют возраст (Age) 21 год? 
# Введите с точностью до 2 знаков после запятой без указания знака % 
# (например, 12.35).

round(
    100.0 *
    df[ (df.Nationality == 'Spain') & (df.Age == 21) ].size /
    df[ df.Nationality == 'Spain' ].size,2
)
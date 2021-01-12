import pandas as pd

football = pd.read_csv('data_sf.csv')
football.describe()
football.describe(include = ['object'])

football[football.Age > 20]

football[(football.Age < football.Age.mean())&
        (football.Club == 'FC Barcelona')].Wage.mean()

# Какова средняя скорость (SprintSpeed) футболистов, зарплата (Wage) которых выше среднего? Ответ округлите до сотых.
round(football[
    football.Wage > football.Wage.mean()
].SprintSpeed.mean(),3)


# Какова средняя скорость (SprintSpeed) футболистов, 
# зарплата (Wage) которых ниже среднего? Ответ округлите до сотых.
round(football[
    football.Wage < football.Wage.mean()
].SprintSpeed.mean(),3)

# Какую позицию (Position) занимает футболист с самой высокой зарплатой (Wage)?
football[ football.Wage == football.Wage.max() ].Position.values[0]

# Сколько пенальти (Penalties) забили 
# бразильские (Nationality, Brazil) футболисты за период, 
# данные о котором представлены в датасете?
football[ football.Nationality == 'Brazil' ].Penalties.sum()

# Укажите средний возраст (Age) игроков, 
# у которых точность удара головой (HeadingAccuracy) > 50. 
# Ответ округлите до сотых.
round( football[ football.HeadingAccuracy > 50 ].Age.mean(), 2 )

# Укажите возраст (Age) самого молодого игрока, 
# у которого хладнокровие (Composure) и реакция (Reactions) превышают 90% 
# от максимального значения, представленного в датасете.
football[ 
    (football.Composure > football.Composure.max() * 0.9) &
    (football.Reactions > football.Reactions.max() * 0.9)
].Age.min()

# Определите, на сколько средняя реакция (Reactions) 
# самых взрослых игроков (т.е. игроков, чей возраст (Age) равен максимальному) 
# больше средней реакции самых молодых игроков. Ответ округлите до сотых.
round( 
    football[ football.Age == football.Age.max() ].Reactions.mean() -
    football[ football.Age == football.Age.min() ].Reactions.mean()
    , 2 )

# Из какой страны (Nationality) происходит больше всего игроков, 
# чья стоимость (Value) превышает среднее значение?
football[ football.Value > football.Value.mean() ].Nationality.value_counts()


# Определите, во сколько раз средняя зарплата (Wage) голкипера (Position, GK) 
# с максимальным значением показателя " Рефлексы" (GKReflexes) 
# выше средней зарплаты голкипера с максимальным значением показателя "Владение мячом" 
# (GKHandling). Ответ округлите до сотых.

round(
football[ 
    ( football.Position == 'GK' ) &
    ( football.GKReflexes == football.GKReflexes.max() )
].Wage.mean()
/
football[ 
    ( football.Position == 'GK' ) &
    ( football.GKHandling == football.GKHandling.max() )
].Wage.mean()
,2
)


# Определите, во сколько раз средняя сила удара (ShotPower) 
# самых агрессивных игроков 
# (игроков с максимальным значением показателя "Агрессивность" (Aggression)) 
# выше средней силы удара игроков с минимальной агрессией. 
# Ответ округлите до сотых.

round(
football[ 
    football.Aggression == football.Aggression.max()
].ShotPower.mean()
/
football[ 
    football.Aggression == football.Aggression.min()
].ShotPower.mean()
,2
)

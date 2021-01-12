import pandas as pd

football = pd.read_csv('data_sf.csv')
df = football

# Применим другую агрегирующую функцию count, чтобы посчитать количество футболистов по клубам и национальностям:
pivot = df.loc[df['Club'].isin(
    ['FC Barcelona','Real Madrid','Juventus','Manchester United']
    )].pivot_table(values=['Name'],
index=['Nationality'],
columns=['Club'],
aggfunc='count',
fill_value=0)
display(pivot)

# А вот таким образом мы можем обращаться к элементам сводной таблицы:
pivot.loc['Argentina']['Name']['Manchester United']

# Создайте сводную таблицу, содержащую сведения о количестве игроков, 
# занимающих разные позиции в каждом клубе. 
# Отсутствующие значения замените нулями.
#
# Каково среднее количество вратарей (GK) в клубе? 
# Ответ округлите до трёх цифр после запятой.

p1 = df.pivot_table( 
    values=['Name'], 
    index=['Position'], 
    columns=['Club'], 
    aggfunc='count',
    fill_value=0
    )

round( p1.loc['GK'].mean(), 3 )

# Используя таблицу, созданную на предыдущем шаге, определите, 
# сколько клубов не содержат данных о центральных полузащитниках. (CM)
# Подсказка: для выполнения этого задания желательно сохранить 
# сводную таблицу в виде отдельного датафрейма и 
# сгруппировать часть данных этого датафрейма с помощью value_counts().

p1.loc['CM'].value_counts().loc[0]
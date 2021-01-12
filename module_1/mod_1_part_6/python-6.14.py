import pandas as pd

football = pd.read_csv('data_sf.csv')
df = football

# С помощью функции loc посчитайте, сколько получают ("Wage") русские футболисты ("Russia"), играющие за ФК "AS Monaco".
df[ (df.Nationality == 'Russia') & (df.Club == 'AS Monaco') ].Wage.mean()

# Создайте сводную таблицу, содержащую сведения 
# о средней скорости футболистов (SprintSpeed), 
# занимающих разные позиции (Position) в разных футбольных клубах (Club).

pivot = df.pivot_table(
    values=['SprintSpeed'],
    aggfunc='mean',
    index=['Position'],
    columns=['Club'],
    fill_value=0,
    margins=True
    )

display(pivot)

# Основываясь на данных таблицы, 
# отметьте три позиции, представители которых в среднем обладают 
# самой высокой скоростью.

p1 = pivot
p1.loc[ ['RB','LM','RM', 'CF', 'RS' ] ].sort_values(('SprintSpeed','All'),ascending=False)
#p1.sort_values(('SprintSpeed','All'),ascending=False)

#p2 = pd.DataFrame( p1.index

p1.loc[ ['ST' ] ].sort_values(('SprintSpeed','All'),ascending=False)

p2 = df.pivot_table(
    values=['SprintSpeed'],
    aggfunc='mean',
    index=['Club'],
    columns=['Position'],
    fill_value=0,
    margins=True
    )

p2.sort_values(
    ('SprintSpeed','ST'),ascending=False
).drop( [
    ('SprintSpeed','CAM'),
    ('SprintSpeed','CB')
    ]
    ,axis=1
    )

[ c for c in p2.columns if c != ('SprintSpeed','ST') ]

p2.sort_values(
    ('SprintSpeed','ST'),ascending=False
).drop(
    [ c for c in p2.columns if c != ('SprintSpeed','ST') ],
    axis=1)
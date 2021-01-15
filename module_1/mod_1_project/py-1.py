import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

# разделяет строку по вертикальной черте, 
# возвращает массив
def split_str_as_list( g ):
    if type(g) is str:
        return g.split('|')
    return []

# Нормализации 1.а - одная ячейка одно значени, в частности жанры перечислены через вертикальную черту
def normalize_nf1( src_df, column, norm_f, newColumn=None, includeColumns=None ):
    """Нормализация DataFrame к 1 форме - случай split('|')
       Если в ячейки есть 2 или более значения, 
         1. то вся строка будет продублирова столько раз, сколько значейний в ячейке
         2. значение ячеек будет заменено на разультат разбияния

       Args:
         src_df - DataFrame
         column : str - Колонка содержащяя множествно значений
         norm_f( value ):List[values] - функция разбиения значения на список значений
         newColumn : str | None - переименование колонки
         includeColumns : None | List[str] - список колонок которые следует оставить

       Returs:
         Новый DataFrame

       Пример

       | a | b   |
       |===|=====|
       | 0 | 1,2 |

       После normalize_nf1( data, 'b', lambda x:x.split(',') )

       | a | b |
       |===|===|
       | 0 | 1 |
       | 0 | 2 |
    """
    if not (type(src_df) is pd.DataFrame):
        raise "!! src_df not pd.DataFrame"
    if not (type(column) is str):
        raise "!! column not str"
    if not callable(norm_f):
        raise "!! norm_f not callable"    

    # Целевая колонка не указана - используем оригинальную
    if newColumn==None:
        newColumn = column
    elif not( type(newColumn) is str):
        raise "!! newColumn must None|str"

    # Строим новый массив данных
    column_store = {}
    for col_name in src_df.columns:
        column_store[col_name] = []
        column_store[col_name if col_name!=column else newColumn] = []

    # по строчное хранение
    row_store = []        
    for index, srow in src_df.iterrows():
        raw_unsplitted_data = srow[column]
        splitted_data = norm_f(raw_unsplitted_data)
        for splitted_value in splitted_data:
            row = {}
            for col_name in src_df.columns:
                row[col_name] = srow[col_name]
                row[col_name if col_name!=column else newColumn] = srow[col_name] if col_name != column else splitted_value
            row_store.append( row )
    
    for row in row_store:
        for k in column_store.keys():
            column_store[k].append(row[k])

    df = pd.DataFrame( column_store, index=range(0,len(row_store)) )

    # Грохаем лишние колонки
    if type(includeColumns) is list:
        cols = []
        keep_cols = []
        for col_name in df.columns:
            cols.append(col_name)
            if col_name == newColumn:
                keep_cols.append(col_name)
            elif col_name in includeColumns:
                keep_cols.append(col_name)
        drop_cols = [ c for c in cols if c not in keep_cols ]
        df = df.drop( drop_cols, axis=1 )

    return df

raw_data = pd.read_csv('movie_bd_v5.csv')
genres = normalize_nf1( raw_data, 'genres', split_str_as_list, 'genre', ['imdb_id'] )
acts = normalize_nf1( raw_data, 'cast', split_str_as_list, 'actor', ['imdb_id'] )
dirs = normalize_nf1( raw_data, 'director', split_str_as_list, 'dir', ['imdb_id'] )
prods = normalize_nf1( raw_data, 'production_companies', split_str_as_list, 'prod', ['imdb_id'] )

# Копируем исходные данные
movies = raw_data.copy()

# Удаляем те, что уже нормализированы
movies = movies.drop( ['genres','cast','director','production_companies'], axis=1 )

# Вычисление даты из строки формата MM/DD/YYYY
def date_str_to_values( s ):
    '''
    Вычисление даты из строки формата MM/DD/YYYY
    Args:
        s : str - строка с датой в формате MM/DD/YYYY
    Returns:
        { 'y': int # год
        , 'm': int # месяц
        , 'd': int # дата
        }
    '''
    nums = list(map( lambda x:int(x), s.split('/') ))
    return { 'y':nums[2], 'm':nums[0], 'd':nums[1] }

# Вычисляем колонки year, month, date
movies['year'] = movies['release_date'].apply( lambda x: date_str_to_values(x)['y'] )
movies['month'] = movies['release_date'].apply( lambda x: date_str_to_values(x)['m'] )
movies['date'] = movies['release_date'].apply( lambda x: date_str_to_values(x)['d'] )

# Удаляем те, что уже нормализированы
movies = movies.drop( ['release_date'], axis=1 )

# Если дата(год) не совпадает с release_year - ругаемся
if( len(movies[ movies.release_year != movies.year ])>0 ):
    raise '!! movies.release_year != movies.year'

# Удаляем те, что уже нормализированы
movies = movies.drop(['release_year'], axis=1)

# Добавляем колонку profit
movies['profit'] = movies['revenue'] - movies['budget']

# Добавляем колонку original_title_len - Длина заголовка в символах
movies['original_title_len'] = movies['original_title'].apply( lambda x: len(x) )

# Подсчет кол-ва слов
# Есть не однозначность под пониманием кол-ва слов
#
# https://skillfactorydspr.slack.com/archives/C017W2EQTRV/p1610720433015800
#
# Описания фильмов какой студии в среднем самые длинные по количеству слов?
# 1. Описание - это колонка overview ?
# 2. В понятие слово входят только буквы или еще спец символы (запятые, точки - например park, это слово из 5 букв включая запятую или 4 буквы исключая запятую) ?
# 3. Слова с разделитем например Twenty-two - считам за два слова или еще пример here's ?
# 4. Слова не содержащие букв например числа - считаем за слова ?
# 5. Или мне просто разделить по пробелу ?
#
# Добрый день!
# 1. Да, это overview
# 2. Разделять только по пробелам, park, - это слово из 5 символов
# 3. Разделитель не считаем за два слово
# 4. считаем за слова
#
# Вариант 1
def words_of( text ):
    words = []
    word = ''
    for c in text:
        if c.isalpha():
            word = word + c
        else:
            if len(word)>0:
                words.append(word)
                word = ''
    return words

# Вариант 2
def simple_words_of( text ):
    return text.split(' ')

movies['overview_words_count'] = movies['overview'].apply( lambda x: len(simple_words_of(x)) )
movies

# 1. У какого фильма из списка самый большой бюджет?
r = movies[ movies.budget == movies.budget.max() ]
r.original_title.iloc[0] + ' (' + r.imdb_id.iloc[0] + ')'

# 2. Какой из фильмов самый длительный (в минутах)?
r = movies[ movies.runtime == movies.runtime.max() ]
r.original_title.iloc[0] + ' (' + r.imdb_id.iloc[0] + ')'

# 3. Какой из фильмов самый короткий (в минутах)?
r = movies[ movies.runtime == movies.runtime.min() ]
r.original_title.iloc[0] + ' (' + r.imdb_id.iloc[0] + ')'

# 4. Какова средняя длительность фильмов?
round(movies.runtime.mean())

# 5. Каково медианное значение длительности фильмов?
round(movies.runtime.median())

# 6. Какой самый прибыльный фильм?
r = movies[ movies.profit == movies.profit.max() ]
r.original_title.iloc[0] + ' (' + r.imdb_id.iloc[0] + ')'

# 7. Какой фильм самый убыточный?
r = movies[ movies.profit == movies.profit.min() ]
r.original_title.iloc[0] + ' (' + r.imdb_id.iloc[0] + ')'

# 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?
len( movies[ movies.profit > 0 ] )

# 9. Какой фильм оказался самым кассовым в 2008 году?
d = movies[ movies.year == 2008 ]
r = d[ d.revenue == d.revenue.max() ]
r.original_title.iloc[0] + ' (' + r.imdb_id.iloc[0] + ')'

# 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?
d = movies[ (movies.year >= 2012) & (movies.year <= 2014) ]
r = d[ d.profit == d.profit.min() ]
r.original_title.iloc[0] + ' (' + r.imdb_id.iloc[0] + ')'

# 11. Какого жанра фильмов больше всего?
genres.describe()
genres.describe().loc['top']['genre']

# 12. Фильмы какого жанра чаще всего становятся прибыльными?
# Обсуждение https://skillfactorydspr.slack.com/archives/C017W2EQTRV/p1610540743055200
# Обсуждение https://skillfactorydspr.slack.com/archives/C017W2EQTRV/p1610710126014500
# Постановка вопроса не правильна в корне
#   при том мысль такая же была - 
#   что популярный (top по частоте упоминания) != прибыльный (profit)
genres.genre.value_counts().index[0]

# 13. У какого режиссера самые большие суммарные кассовые сборы?
j = dirs.merge( movies, on='imdb_id', how='outer' )
j.groupby(['dir'])['revenue'].sum().sort_values(ascending=False).index[0]

# 14. Какой режисер снял больше всего фильмов в стиле Action?
j = genres.merge( movies, on='imdb_id', how='outer' )
j = j.merge( dirs, on='imdb_id', how='outer' )
j = j[ j.genre == 'Action' ]
j.groupby( ['dir'] )['genre'].count().sort_values(ascending=False).index[0]

# 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году?
j = acts.merge( movies, on='imdb_id', how='outer' )
j = j[ j.year == 2012 ]
j.groupby(['actor'])['revenue'].sum().sort_values(ascending=False).index[0]

# 16. Какой актер снялся в большем количестве высокобюджетных фильмов?
j = acts.merge( movies, on='imdb_id', how='outer' )
# в фильмах, где бюджет выше среднего по данной выборке. 
j = j[ j.budget > j.budget.mean() ]
j.groupby('actor').count().sort_values(['imdb_id'],ascending=False).index[0]

# 17. В фильмах какого жанра больше всего снимался Nicolas Cage?
j = acts.merge( genres, on='imdb_id', how='outer' )
j = j[ j.actor=='Nicolas Cage' ].drop(['imdb_id'], axis=1)
j = j.groupby(['genre']).count().sort_values(['actor'],ascending=False)
j.index[0]

# 18. Самый убыточный фильм от Paramount Pictures
j = prods.merge( movies, on='imdb_id', how='left' )
j = j.query( "prod == 'Paramount Pictures' " )
j = j[ j.profit == j.profit.min() ]
r = j
r.original_title.iloc[0] + ' (' + r.imdb_id.iloc[0] + ')'

# 19. Какой год стал самым успешным по суммарным кассовым сборам?
d = movies.groupby(['year']).sum().sort_values(['year'],ascending=False)
d.index[0]

# 20. Какой самый прибыльный год для студии Warner Bros?
# https://skillfactorydspr.slack.com/archives/C017W2EQTRV/p1607752079405900?thread_ts=1607728173.403500&cid=C017W2EQTRV
# Приветствую! Надо учесть все четыре компании с Warner Bros. в названии.
j = prods.merge( movies, on='imdb_id', how='left' )
j = j[ j['prod'].str.contains('Warner Bros') ]
j = j.groupby('year')['profit'].sum().sort_values(ascending=False)
j = j.loc[[2014,2008,2012,2010,2015]].sort_values(ascending=False)
j.index[0]

# 21. В каком месяце за все годы суммарно вышло больше всего фильмов?
movies.groupby(['month']).count().sort_values(['imdb_id'],ascending=False).index[0]

# 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)
movies.groupby(['month']).count().loc[ [8,7,6] ].imdb_id.sum()

# 23. Для какого режиссера зима – самое продуктивное время года?
j = dirs.merge( movies, on='imdb_id', how='left' )
j['winter'] = j['month'].apply( lambda x: x in [1,2,12])
j = j[ j['winter'] ].groupby('dir')['imdb_id'].count().sort_values(ascending=False)
j.index[0]

# 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?
# https://skillfactorydspr.slack.com/archives/C017W2EQTRV/p1610572293067300
# Под вопросом
# "Какая студия даёт самые длинные названия своим фильмам по количеству символов?"
# имеется виду
# "Какая студия даёт самые длинные названия своим фильмам по количеству символов (в среднем по всей выборке)?"
j = prods.merge( movies, on='imdb_id', how='left' )
j = j.groupby(['prod'])['original_title_len'].mean().sort_values(ascending=False)
j.index[0]

# 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?
# overview_words_count
j = prods.merge( movies, on='imdb_id', how='left' )
j = j.groupby(['prod'])['overview_words_count'].mean().sort_values(ascending=False)
j.index[0]

# 26. Какие фильмы входят в 1 процент лучших по рейтингу?
# 1) Inside Out, The Dark Knight, 12 Years a Slave
# 2) BloodRayne, The Adventures of Rocky & Bullwinkle
# 3) Batman Begins, The Lord of the Rings: The Return of the King, Upside Down
# 4) 300, Lucky Number Slevin, Kill Bill: Vol. 1
# 5) Upside Down, Inside Out, Iron Man 
j = movies.sort_values(['vote_average'],ascending=False)
j = j.head( int(len(j)*0.01) )

len( j[ j.original_title.str.contains('BloodRayne') ] )>0

# original_title
cases = { '1': ['Inside Out','The Dark Knight', '12 Years a Slave']
        , '2': ['BloodRayne','The Adventures of Rocky & Bullwinkle'] 
        , '3': ['Batman Begins','The Lord of the Rings: The Return of the King','Upside Down']
        , '4': ['300','Lucky Number Slevin','Kill Bill: Vol. 1']
        , '5': ['Upside Down','Inside Out','Iron Man']
        }
matched_cases = []
for k,titles in cases.items():
    fails = 0
    print("case",k,titles)
    for title in titles:
        inTop = len(j[ j.original_title.str.contains(title) ]) > 0
        #print(inTop)
        if inTop:
            print('  ',title,"in top %1")
        else:
            print('  ',title,"not in top %1")
            fails = fails + 1
    if fails==0:
        matched_cases.append((k,titles))
for mc in matched_cases:
    print( 'matched ',mc)

# 27. Какие актеры чаще всего снимаются в одном фильме вместе?

# Варианты
# 1) Johnny Depp & Helena Bonham Carter
# 2) Ben Stiller & Owen Wilson
# 3) Vin Diesel & Paul Walker 
# 4) Adam Sandler & Kevin James 
# 5) Daniel Radcliffe & Rupert Grint

pairs = [
    { 'count': 0, 'names': ['Johnny Depp', 'Helena Bonham Carter'] },
    { 'count': 0, 'names': ['Ben Stiller', 'Owen Wilson'] },
    { 'count': 0, 'names': ['Vin Diesel', 'Paul Walker'] },
    { 'count': 0, 'names': ['Adam Sandler', 'Kevin James'] },
    { 'count': 0, 'names': ['Daniel Radcliffe', 'Rupert Grint'] },
]

for index, srow in raw_data.iterrows():
    actors = srow.cast.split('|')
    for p in pairs:
        matched = 0
        for name in p['names']:
            if name in actors:
                matched = matched + 1
        if matched==len(p['names']):
            p['count'] = p['count'] + 1

print(pairs)
sorted_pairs = sorted(pairs, key=lambda p:p['count'])
sorted_pairs[ len(sorted_pairs)-1 ]

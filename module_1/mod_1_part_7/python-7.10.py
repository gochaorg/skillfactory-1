import pandas as pd

movies = pd.read_csv('movies.csv')
movies.head()

ratings = pd.read_csv('ratings.csv')
ratings.head()

joined = ratings.merge(movies, on='movieId', how='left')
joined.head() 

ratings1 = pd.read_csv('ratings_example.txt', sep = '\t')
ratings1.head()

movies1 = pd.read_csv('movies_example.txt', sep = '\t')
movies1.head()

ratings1.merge(movies1, on = 'movieId', how = 'outer')
ratings1.merge(movies1, on = 'movieId', how = 'left')
ratings1.merge(movies1, on = 'movieId', how = 'inner')
ratings1.merge(movies1, on = 'movieId', how = 'right')

movies1.drop_duplicates(subset = 'movieId', keep = 'first', inplace = True)
movies1.head()

ratings1.merge(movies1, on = 'movieId', how = 'outer')
ratings1.merge(movies1, on = 'movieId', how = 'left')

items_dict = {
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 100132, 312394], 
    'vendor': ['Samsung', 'LG', 'Apple', 'Apple', 'LG', 'Apple', 'Samsung', 'Samsung', 'LG', 'ZTE'],
    'stock_count': [54, 33, 122, 18, 102, 43, 77, 143, 60, 19]
}

purchase_log = {
    'purchase_id': [101, 101, 101, 112, 121, 145, 145, 145, 145, 221],
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 103845, 100132], 
    'price': [13900, 5330, 38200, 49990, 9890, 33000, 67500, 34500, 89900, 11400]
}

items_df = pd.DataFrame(items_dict)
purchase_df = pd.DataFrame(purchase_log)

# Объедините получившиеся датафреймы по столбцу item_id с типом outer.
# Определите, модель с каким item_id есть в статистике продаж purchase_df, 
# но не учтена на складе 
# (подсказка: подумайте, какой датафрейм должен быть "левым", а какой "правым", чтобы получить необходимые данные). Введите ответ в виде целого числа.

items_df.merge( purchase_df, on="item_id", how="outer")

# Посчитайте объем выручки для каждой модели, которую можно получить, 
# распродав все остатки на складе. 
# Модель с каким item_id имеет максимальное значение выручки после 
# распродажи остатков? Ответ дайте в виде целого числа.
# Примечание: перемножение столбцов датафрейма можно производить разными способами, 
# но самый простой - перемножение "в лоб" вида df['col1'] = df['col2'] * df['col3']. 
# Для присоединения новых данных к датафрейму тоже можно использовать 
# различные методы, включая функцию .append(), 
# которая позволяет присоединять к датафрейму другой датафрейм, серии или словари. 

d = items_df.merge( purchase_df, on="item_id", how="inner")
d['r'] = d['price'] * d['stock_count']
d.sort_values(['r'],ascending=False)
d.r.sum()
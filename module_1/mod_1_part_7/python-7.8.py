import pandas as pd

movies = pd.read_csv('movies.csv')
movies.head()

ratings = pd.read_csv('ratings.csv')
ratings.head()

joined = ratings.merge(movies, on='movieId', how='left')
joined.head() 
import pandas as pd

movies = pd.read_csv('movies.csv')
movies.head()

ratings = pd.read_csv('ratings.csv')
ratings.head()

len(ratings)

ratings.rating.describe()
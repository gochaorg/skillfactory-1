import pandas as pd
import os

# files = os.listdir('data')
# files

# # После чтения папки список файлов оказался следующим:
# files = ['setup.py', 'ratings.txt', 'stock_stats.txt', 'movies.txt', 'run.sh', 'game_of_thrones.mov']

# # Создайте на основе списка files новый список data, в который поместите только файлы, содержащие в названии "txt".
# data = [ f for f in files if 'txt' in f ]

# for root, dirs, files in os.walk('data'):
#     print(root, dirs, files)

#data = pd.DataFrame(columns = ['userId', 'movieId', 'rating', 'timestamp'])

#temp = pd.read_csv( os.path.join('data', filename), names = ['userId', 'movieId', 'rating', 'timestamp'] )

#########################

files = os.listdir('data')
dframes = []
for f in files:
    print( "reading "+f )
    df = pd.read_csv( 
        os.path.join('data',f),
        names = ['userId', 'movieId', 'rating', 'timestamp']
    )
    dframes.append(df)

df = pd.concat(dframes)
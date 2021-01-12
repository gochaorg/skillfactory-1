import pandas as pd
import os

files = os.listdir('data')
files

# После чтения папки список файлов оказался следующим:
files = ['setup.py', 'ratings.txt', 'stock_stats.txt', 'movies.txt', 'run.sh', 'game_of_thrones.mov']

# Создайте на основе списка files новый список data, в который поместите только файлы, содержащие в названии "txt".
data = [ f for f in files if 'txt' in f ]
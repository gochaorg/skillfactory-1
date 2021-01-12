import pandas as pd

data = pd.Series(["Январь", "Февраль", "Март", "Апрель"],
                 index = ['Первый', "Второй", "Третий", "Четвёртый"])
display(data)

data.loc["Первый"]

data.loc[["Первый", "Третий"]]

data.iloc[0]

data.iloc[[0, 2]]

data = pd.Series(list(range(10, 1001)))

print(data.loc[10] + data.loc[23] - data.loc[245] + data.iloc[122])

data = pd.Series(list(range(10, 1001)))
data.size
data.iloc[990]

data = pd.Series(["Кот", "Собака", "Корова", "Лемур"], index = [3,7,12,26]) 
display(data)
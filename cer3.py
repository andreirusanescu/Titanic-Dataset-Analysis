import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('train.csv')
data = data.select_dtypes(include=['number'])
it = 0
for column in data:
    plt.figure(figsize=(8, 6))
    if it == 1:
        plt.hist(data[column], bins=2, color='skyblue', edgecolor='black')
    elif it == 2:
        plt.hist(data[column], bins=3, color='skyblue', edgecolor='black')
    elif it == 0 or it == 3:
        plt.hist(data[column], bins=30, color='skyblue', edgecolor='black')
    elif it == 4 or it == 5 or it == 6:
        plt.hist(data[column], bins=4, color='skyblue', edgecolor='black')
    else:
        plt.hist(data[column], bins=10, color='skyblue', edgecolor='black')
    plt.title(f'Histograma pentru {column}')
    plt.xlabel('Valoare')
    plt.ylabel('Frecventa')
    plt.show()
    it += 1
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('train.csv')
bins = [0, 20, 40, 60, data['Age'].max()]
index = [0, 1, 2, 3]

data['age_index'] = pd.cut(data['Age'], bins = bins, labels=index)
males1 = len(data[(data['Sex'] == "male") & (data['age_index'] == 0) & (data['Survived'] == 1)])
total_males1 = len(data[(data['Sex'] == "male") & (data['age_index'] == 0)])

males2 = len(data[(data['Sex'] == "male") & (data['age_index'] == 1) & (data['Survived'] == 1)])
total_males2 = len(data[(data['Sex'] == "male") & (data['age_index'] == 1)])

males3 = len(data[(data['Sex'] == "male") & (data['age_index'] == 2) & (data['Survived'] == 1)])
total_males3 = len(data[(data['Sex'] == "male") & (data['age_index'] == 2)])

males4 = len(data[(data['Sex'] == "male") & (data['age_index'] == 3) & (data['Survived'] == 1)])
total_males4 = len(data[(data['Sex'] == "male") & (data['age_index'] == 3)])

print(f'Prima categorie: {males1} barbati')
print(f'A doua categorie: {males2} barbati')
print(f'A treia categorie: {males3} barbati')
print(f'A patra categorie: {males4} barbati')

perc1 = round((males1 / total_males1) * 100, 2)
print(perc1)
perc2 = round((males2 / total_males2) * 100, 2)
print(perc2)
perc3 = round((males3 / total_males3) * 100, 2)
print(perc3)
perc4 = round((males4 / total_males4) * 100, 2)
print(perc4)

labels = ['0-20', '21-40', '41-60', '61+']
percs = [perc1, perc2, perc3, perc4]
plt.figure(figsize=(8, 6))
plt.bar(labels, percs, color='skyblue', edgecolor='black')
plt.xlabel('Categorii de varsta')
plt.ylabel('Procent %')
plt.title('Procentul de supravietuire al barbatilor in functie de varsta')
plt.savefig('cer6.png')

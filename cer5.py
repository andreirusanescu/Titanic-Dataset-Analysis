import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('train.csv')
# intervalele de varsta
bins = [0, 20, 40, 60, data['Age'].max()]
# indexul corespunzator fiecarui interval
index = [0, 1, 2, 3]

data['age_index'] = pd.cut(data['Age'], bins = bins, labels = index)

# frecventa valorilor varstelor
age_count = data['age_index'].value_counts().sort_index()

labels = ['0-20', '21-40', '41-60', '61+']
plt.figure(figsize=(8, 6))
plt.bar(labels, age_count, color='skyblue', edgecolor='black')
plt.xlabel('Categorii de varsta')
plt.ylabel('Numarul total de pasageri')
plt.title('Numarul de pasageri / categorie')
plt.savefig('cer5.png')
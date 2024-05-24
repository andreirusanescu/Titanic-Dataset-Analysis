import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('train.csv')
titles = data['Name'].str.split(', ').str[1].str.split('.').str[0].unique()
male_titles = ['Mr', 'Master', 'Don', 'Rev', 'Dr', 'Major', 'Sir', 'Col', 'Capt', 'Jonkheer']
female_titles = ['Mrs', 'Miss', 'Mme', 'Ms', 'Lady', 'Mlle', 'the Countess']
good, bad = 0, 0
for index, row in data.iterrows():
    title = row['Name'].split(', ')[1].split('.')[0]
    sex = row['Sex']
    if (sex == 'male' and title in male_titles) or (sex == 'female' and title in female_titles):
        good += 1
    else:
        bad += 1

print(good, bad)
results = [good, bad]
labels = ['corect', 'incorect']
plt.figure(figsize=(5, 5))
plt.bar(labels, results, color='skyblue', edgecolor='black')
plt.title('Numarul persoanelor identificate corect')
plt.ylabel('Numarul')
plt.show()
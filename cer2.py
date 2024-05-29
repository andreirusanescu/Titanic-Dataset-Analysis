import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('train.csv')

survived_column = data['Survived']
survived = sum(survived_column)
total = len(survived_column)
survival_rate = round((survived / total) * 100, 2)
print(f'Au supravietuit: {survival_rate}%')
print(f'Nu au supravietuit: {100 - survival_rate}%')

passengers_column = data['Pclass']
total = len(passengers_column)

# precizie de 2 zecimale
first_class = round((sum(passengers_column == 1) / total) * 100, 2)
second_class = round((sum(passengers_column == 2) / total) * 100, 2)
third_class = round((sum(passengers_column == 3) / total) * 100, 2)
print(f'Pasageri de clasa I: {first_class}%')
print(f'Pasageri de clasa II: {second_class}%')
print(f'Pasageri de clasa III: {third_class}%')

sex_column = data['Sex']
total = len(sex_column)
males = round((sum(sex_column == "male") / total) * 100, 2)
females = round((sum(sex_column == "female") / total) * 100, 2)
print(f'Barbati: {males}%')
print(f'Femei: {females}%')

graph_data = {
	'Supravietuitori': survival_rate,
	'Nesupravietuitori': 100 - survival_rate,
	'Clasa I': first_class,
	'Clasa II': second_class,
	'Clasa III': third_class,
	'Barbati': males,
	'Femei': females
}

categories = ['Supravietuitori', 'Nesupravietuitori', 'Clasa I', 'Clasa II', 'Clasa III', 'Barbati', 'Femei']
values = [survival_rate, 100 - survival_rate, first_class, second_class, third_class, males, females]

# Initializarea graficului
fig, ax = plt.subplots(figsize=(14, 7))

# Pozitiile pentru fiecare bara, sunt impartite liniar
x_pos = np.arange(len(categories))

# Crearea barelor
bars = ax.bar(x_pos, values, color=['green', 'red', 'cyan', 'orange', 'purple', 'blue', 'pink'])

# Label-urile pentru grafic
ax.set_xticks(x_pos)
ax.set_xticklabels(categories)
ax.set_ylabel('Procent %')
ax.set_title('Distributia supravietuitorilor, claselor si a genurilor')

# Valorile de deasupra barelor, in procente
for bar in bars:
	yval = bar.get_height()
	ax.text(bar.get_x() + bar.get_width() / 3, yval, f'{yval}%', va='bottom')

plt.savefig('cer2.png')
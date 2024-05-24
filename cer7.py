import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('train.csv')

children = data[data['Age'] < 18]
survived_children = data[(data['Age'] < 18) & (data['Survived'] == 1)]
children_rate = round((len(survived_children) / len(children)) * 100, 2)
adults = data[data['Age'] >= 18]
survived_adults = data[(data['Age'] >= 18) & (data['Survived'] == 1)]
adults_rate = round((len(survived_adults) / len(adults)) * 100, 2)
print(f'Procentul de supravietuire al copiilor: {children_rate}')
print(f'Procentul de supravietuire al adultilor: {adults_rate}')

labels = ['Copii', 'Adulti']
rates = [children_rate, adults_rate]
plt.figure(figsize=(8, 6))
plt.bar(labels, rates, color='skyblue', edgecolor='black')
plt.ylabel('Procent %')
plt.title('Procentul de supravietuire al copiilor si al adultilor')
plt.show()

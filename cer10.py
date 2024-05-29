import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('train.csv')

# SibSp - frati si sotii
# Parch - copii si parinti
data['Relatives'] = data['Parch'] + data['SibSp']
data['Alone'] = (data['Relatives'] == 0).astype(int)
plt.hist([data[data['Alone'] == 0]['Survived'],
          data[data['Alone'] == 1]['Survived']],
          color = ['skyblue', 'mediumseagreen'],
          label = ['Nu are rude', 'Are rude'])
plt.xlabel('Supravietuire')
plt.ylabel('Pasageri')
plt.title('Cum influenteaza rudele de pe vas rata de supravietuire a unui pasager ?')
plt.legend()
plt.savefig('cer10.png')
sns.catplot(x = 'Pclass', y = 'Fare', hue = 'Survived', kind = 'strip', data = data.head(100), palette = 'pastel')
plt.title('Relatia dintre tarif, clasa si supravietuirea pasagerilor')
plt.xlabel('Pclass')
plt.ylabel('Fare')
plt.savefig('cer10_2.png')

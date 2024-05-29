import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('train.csv')

# SibSp - siblings & spouses
# Parch - hildren & parents
data['Relatives'] = data['Parch'] + data['SibSp']
data['Alone'] = (data['Relatives'] == 0).astype(int)
plt.hist([data[data['Alone'] == 0]['Survived'],
          data[data['Alone'] == 1]['Survived']],
          color = ['skyblue', 'mediumseagreen'],
          label = ['No relatives'])
plt.xlabel('Survival')
plt.ylabel('Passenger Count')
plt.title('How does having relatives on board affect the survival rate ?')
plt.legend()
plt.savefig('Cer10.png')
sns.catplot(x = 'Pclass', y = 'Fare', hue = 'Survived', kind = 'strip', data = data.head(100), palette = 'pastel')
plt.title('Relationship between fare, class and state of survival')
plt.xlabel('Pclass')
plt.ylabel('Fare')
plt.savefig('Cer10_2.png')

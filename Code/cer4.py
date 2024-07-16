import numpy as np
import pandas as pd

data = pd.read_csv('train.csv')
missing_values = data.isnull().sum()
filtered = missing_values[missing_values != 0]
proportion = filtered / len(data) * 100

print("Coloanele cu valori lipsa si proportia lor:")
for column in filtered.index:
    print(f"{column}: {filtered[column]} valori lispsa, {round(proportion[column], 2)}%")

survivers = data.groupby('Survived')
print()
for column in filtered.index:
    print(column)
    for survived, group in survivers:
        missing_group = group[column].isnull().sum()
        group_length = len(group)
        percentage = missing_group / group_length * 100
        print(f"Survived = {survived}: {missing_group} valori lipsa ({round(percentage, 2)}%)")
    print()

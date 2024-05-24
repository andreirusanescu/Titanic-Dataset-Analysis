import numpy as np
import pandas as pd

data = pd.read_csv('train.csv')
missing_values = data.isnull().sum()
filtered = missing_values[missing_values != 0]

print(data.isna().sum())
print(data)
for column in filtered.index:
    if data[column].dtype == 'float64' or data[column].dtype == 'int64':
        data[column] = data[column].fillna(data[column].mean())
    else:
        data[column] = data[column].fillna(data[column].mode()[0])

print(data.isna().sum())
print(data)
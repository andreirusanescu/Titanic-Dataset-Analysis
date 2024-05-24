import numpy as np
import pandas as pd

data = pd.read_csv('train.csv')
print(f'There are {len(data.columns)} columns')
print(data.dtypes)
print()
num_missing = data.isnull().sum()
print(f'Missing values for each column')
print(num_missing)
print()
print(f'There are {len(data)} lines')
ret = data.duplicated().sum()

if ret:
    print('There are duplicate rows')
else:
    print('There are no duplicate rows')
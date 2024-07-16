import numpy as np
import pandas as pd

data = pd.read_csv('train.csv')
print(f'Sunt {len(data.columns)} coloane')
print()
print('Tipurile de date pentru fiecare coloana')
print(data.dtypes)
print()
missing_values = data.isnull().sum()
print(f'Valorile lipsa pentru fiecare coloana')
print(missing_values)
print()
print(f'In total sunt {len(data)} linii')
ret = data.duplicated().sum()
if ret:
	print(f'Sunt {ret} linii duplicate')
else:
	print('Nu sunt linii duplicate')
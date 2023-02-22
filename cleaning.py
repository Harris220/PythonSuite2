import pandas as pd
import numpy as np
import datetime as dt

data = pd.read_csv('contacts.csv')
data['date'] = pd.to_datetime(data['date'])
print(data.dtypes)

print('-----------------------------')

nb_na = data.isnull().sum()
print(nb_na)

print('-----------------------------')

print(data.loc[data[['title']].duplicated(keep=False),:])
data.drop_duplicates(subset=['title'], inplace=True, ignore_index=True)

print('-----------------------------')

print(data.describe)
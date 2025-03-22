import pandas as pd
import os

os.chdir(r'C:\Users\esarn\OneDrive\Desktop\coding\postgresql\testing\data_sets')
df = pd.read_csv('testdb.user_test.csv')

filter_name = ['Emily']

df1 = df.loc[(df['name_first'].isin(filter_name))]

print(df)
print(df1)

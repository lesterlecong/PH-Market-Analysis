import pandas as pd

df = pd.read_csv('Data/Philippines 20-Year Bond Yield Historical Data.csv')
df.drop(['Open', 'High', 'Low', 'Change %'], axis=1, inplace=True)
print(df.head())

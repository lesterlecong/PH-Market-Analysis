import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

df = pd.read_csv('Data/Philippines 20-Year Bond Yield Historical Data.csv')
df.set_index('Date', inplace=True)
df.drop(['Open', 'High', 'Low', 'Change %'], axis=1, inplace=True)
print(df.head())

df.plot()
plt.legend(loc=4)
plt.show()

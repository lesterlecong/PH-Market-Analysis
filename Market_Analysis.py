import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

def get_ph_20_year_bond_yield():
    df = pd.read_csv('Data/Philippines 20-Year Bond Yield Historical Data.csv')
    df.set_index('Date', inplace=True)
    df.drop(['Open', 'High', 'Low', 'Change %'], axis=1, inplace=True)
    return df


ph_20_yr_bond = get_ph_20_year_bond_yield()

ph_20_yr_bond.plot()
plt.legend(loc=4)
plt.show()

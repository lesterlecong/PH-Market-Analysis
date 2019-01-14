import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

def get_ph_20_year_bond_yield():
    df = pd.read_csv('Data/Philippines 20-Year Bond Yield Historical Data.csv')
    df.set_index('Date', inplace=True)
    df.drop(['Open', 'High', 'Low', 'Change %'], axis=1, inplace=True)
    return df

def get_ph_25_year_bond_yield():
    df = pd.read_csv('Data/Philippines 25-Year Bond Yield Historical Data.csv')
    df.set_index('Date', inplace=True)
    df.drop(['Open', 'High', 'Low', 'Change %'], axis=1, inplace=True)
    return df

def get_ph_10_year_bond_yield():
    df = pd.read_csv('Data/Philippines 10-Year Bond Yield Historical Data.csv')
    df.set_index('Date', inplace=True)
    df.drop(['Open', 'High', 'Low', 'Change %'], axis=1, inplace=True)
    return df

fig = plt.figure()
ax1 = plt.subplot2grid((2,1), (0,0))

ph_10_yr_bond = get_ph_10_year_bond_yield()
ph_20_yr_bond = get_ph_20_year_bond_yield()
ph_25_yr_bond = get_ph_25_year_bond_yield()

ph_10_yr_bond['Price'].plot(ax = ax1, label='10 yr bond yield')
ph_20_yr_bond['Price'].plot(ax = ax1, label='20 yr bond yield')
ph_25_yr_bond['Price'].plot(ax = ax1, label='25 yr bond yield')

ax1.legend(loc=4)
plt.legend(loc=4)
plt.show()

# -*- coding: utf-8 -*-
"""Forex Selling & Buying Strategy Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GfAlgKAfwgqyYX5DmGmRdu5wmkc8wi34
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

from google.colab import files
uploaded = files.upload()

df = pd.read_csv('AAPL.csv')

df.head()

# Viz
plt.figure(figsize=(12,4))
plt.plot(df['Adj Close'], label='AAPL')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.show()

# Simple moving average
sma30  = pd.DataFrame()

sma30['Adj Close Price'] = df['Adj Close'].rolling(window=30).mean()

sma30

sma100 = pd.DataFrame()

sma100['Adj Close Price'] = df['Adj Close'].rolling(window=100).mean()

sma100

# Visualize
# Viz
plt.figure(figsize=(12,4))
plt.plot(df['Adj Close'], label='Apple')
plt.plot(sma30['Adj Close Price'], label='30 Days Avg')
plt.plot(sma100['Adj Close Price'], label='100 Days Avg')

plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.show()

# data to store all data

# What does it do

"""If short-term average crosses long-term average - Buy 
Ex: if sma30 crosses sma100, Buy **bold text** bold text
"""

data = pd.DataFrame()
data['All'] = df['Adj Close']
data['SMA30'] = sma30['Adj Close Price']
data['SMA100'] = sma100['Adj Close Price']

data

def buy_sell(data):
  # when crossing of 30 and 100
  priceBuy = []
  priceSell = []
  flag = 1

  for i in range(len(data)):
    if data['SMA30'][i] > data['SMA100'][i]:
      if flag != 1:
        priceBuy.append(data['All'][i])
        priceSell.append(np.nan)
        flag = 1
      else:
        priceBuy.append(np.nan)
        priceSell.append(np.nan)
    elif data['SMA30'][i] < data['SMA100'][i]:
      if flag != 0:
        priceBuy.append(np.nan)
        priceSell.append(data['All'][i])
        flag = 0
      else:
        priceBuy.append(np.nan)
        priceSell.append(np.nan)
    else:
      priceBuy.append(np.nan)
      priceSell.append(np.nan)
  return (priceBuy, priceSell)

buy_sell = buy_sell(data)

data['Buy_signal'] = buy_sell[0]
data['Sell_signal'] = buy_sell[1]

data

plt.figure(figsize=(12,4))
plt.plot(data['All'], label='All', alpha=0.35)
plt.plot(data['SMA30'], label='30 Days')
plt.plot(data['SMA100'], label='100 Days')
plt.scatter(data.index, data['Buy_signal'],label = 'Buy', marker = '+', color='green')
plt.scatter(data.index, data['Sell_signal'],label = 'Sell', marker = 'v', color='red')
plt.title('Buy Sell Signals')
plt.ylabel('Time')
plt.xlabel('Price')
plt.legend(loc='upper left')
plt.show()


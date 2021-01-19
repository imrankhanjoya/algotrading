import pandas as pa
import yfinance as yf
import numpy as np
import talib as ta
import mplfinance as mpf



symbol_list = ['TATAMOTORS.NS','HLVLTD.BO','ONGC.NS','WIPRO.NS','COALINDIA.NS','INDUSINDBK.NS','TITAN.NS','NESTLEIND.NS','NTPC.NS','CIPLA.NS','BRITANNIA.NS','MARUTI.NS','BAJAJFINSV.NS','TATASTEEL.NS','HEROMOTOCO.NS','KOTAKBANK.NS','LT.NS','TECHM.NS','HDFCLIFE.NS','BAJAJ-AUTO.NS','TCS.NS','ICICIBANK.NS','ULTRACEMCO.NS','BHARTIARTL.NS','GRASIM.NS','RELIANCE.NS','ITC.NS','HINDALCO.NS','GAIL.NS','SHREECEM.NS','M&M.NS']
symbol_list = ['TATAMOTORS.NS']

data = yf.download(tickers='TATAMOTORS.NS',period="1d",interval="5m")
data['price'] = (data['High']+data['Low']+data['Close'])/3
data['VWAP'] =(data['Volume']*data['price']).cumsum()/ data['Volume'].cumsum()
data['SMA5'] = ta.SMA(data['Close'].values, timeperiod=5)
data['CROSSOVER'] = ((data['VWAP'] - data['SMA5'])/data['VWAP'])*100
data['CROSSOVER'] = data['SMA5'] - data['VWAP']
#data.loc[data['CROSSOVER']<0,'CROSSOVER'] = data['CROSSOVER']*-1 
#data.loc[(data['VWAP'] == data['SMA5']),'CROSSOVER'] = True

addplot  = [
    mpf.make_addplot(data['VWAP']),
    mpf.make_addplot(data['SMA5']),
    mpf.make_addplot(data['CROSSOVER']),
]




mpf.plot(data, type='candle', addplot=addplot)
print(data)


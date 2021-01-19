import pandas as pa
import yfinance as yf
import numpy as np
import talib as ta



symbol_list = ['TATAMOTORS.NS','HLVLTD.BO','ONGC.NS','WIPRO.NS','COALINDIA.NS','INDUSINDBK.NS','TITAN.NS','NESTLEIND.NS','NTPC.NS','CIPLA.NS','BRITANNIA.NS','MARUTI.NS','BAJAJFINSV.NS','TATASTEEL.NS','HEROMOTOCO.NS','KOTAKBANK.NS','LT.NS','TECHM.NS','HDFCLIFE.NS','BAJAJ-AUTO.NS','TCS.NS','ICICIBANK.NS','ULTRACEMCO.NS','BHARTIARTL.NS','GRASIM.NS','RELIANCE.NS','ITC.NS','HINDALCO.NS','GAIL.NS','SHREECEM.NS','M&M.NS']
symbol_list = ['TATAMOTORS.NS']

data = yf.download(tickers='TATAMOTORS.NS',period="1d",interval="5m")
data['price'] = (data['High']+data['Low']+data['Close'])/3
data['VWAP'] =(data['Volume']*data['price']).cumsum()/ data['Volume'].cumsum()





print(data)


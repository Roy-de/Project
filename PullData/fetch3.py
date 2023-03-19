#Use this script to fetch data when the server was offline and later restarted
from pandas_datareader import data as pdr
import yfinance as yf
import time
from time import strftime


yf.pdr_override()
def get_data():
    time_end = strftime("%Y-%m-%d",time.localtime())
    #time format should be %Y-%m-%d
    data = pdr.get_data_yahoo("BTC-USD",start ="2023-01-01" ,end = time_end)
    print(data)
    
if __name__ == '__main__':
    get_data()
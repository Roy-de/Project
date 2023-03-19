#This is a script to fetch data from yahoo finance api using yfinance 

import yfinance as yf
import time
import asyncio

#Fetching the data
class data:
    def fetch_data():
        start = time.time()
        data = yf.Ticker("BTC-USD")
        print(data.info(interval="1d"))
        end = time.time()
        print("Runtime: %d seconds" %(end - start))


#Class that gets the data from yfinance 
if __name__ == '__main__':
    def Run():
        while True:
            data.fetch_data()
            time.sleep(1)
            return Run()
    Run()    
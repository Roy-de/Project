import websockets
import asyncio
import json
import time
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

xdata = []
ydata = []

def update_graph():
    ax.plot(xdata, ydata , color='b')
    ax.legend([f"Last price: {ydata[-1]}"])
    
    fig.canvas.draw()
    plt.pause(0.05)

async def main():
    #Url that contains the endpoint to connect to
    url = "wss://stream.binance.com:9443/stream?streams=btcusdt@ticker"
    #Establish connection to the websocket
    async with websockets.connect(url) as client:
        while True:
            data = json.loads(await client.recv())["data"]
            
            eventtime = time.localtime(data['E'] // 1000)
            eventtime = f"{eventtime.tm_hour}:{eventtime.tm_min}:{eventtime.tm_sec}"
            
            print(eventtime,data['v'])
            
            xdata.append(eventtime)
            ydata.append(float(data['v']))
            update_graph()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    

"""Lets try to reconstruct the url to accept user defined inputs
url : "wss://stream.binance.com:{port}/stream?streams={ticker}@{timeframe}   #Main part of the url
port: 9443 #Specify the port to connect to
ticker: 'Example: btcusdt'
timeframe: 'Example: miniTicker'

Final_url = "wss://stream.binance.com:{port}/strems?streams={ticker}@{timeframe}"
"""    
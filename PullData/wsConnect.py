import websocket
import json
import time

#Parse the uri to connect to the exchange websocket

class connection:
    #Connect to binance websocket
    #Add other connections below this one if you find any
    binance_uri = "wss://stream.binance.com:9443/stream?streams=btcusdt@miniTicker"
    #function to convert time to a much more understandable time
    def converttime(data):
        eventtime = time.localtime(data['E']// 1000)
        eventtime = f"{eventtime.tm_hour}:{eventtime.tm_min}:{eventtime.tm_sec}"
        
    def on_message(connection,message):
        #Get data in json format since it is already in json format
        data = json.loads(message)["data"]
        eventtime = time.localtime(data['E'] // 1000)
        eventtime = f"{eventtime.tm_hour}:{eventtime.tm_min}:{eventtime.tm_sec}"
            
        print(eventtime,data['o'],data['h'],data['l'],data['c'])

    try:
        Connection = websocket.WebSocketApp(binance_uri,on_message=on_message)
        print("Date   :Open\t\t:High\t\t:low\t\t:close")
        Connection.run_forever()
    except websocket.WebSocketConnectionClosedException :
        print("Error establishing a connection: {error}")    
    


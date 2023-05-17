import time 
from kafka import KafkaProducer
import wsConnect

#Add additional paths

#This will produce data to kafka topics
producer = KafkaProducer(
    #Bootsrap server for topics
    bootsrap_servers=['localhost:9092'],
)

if __name__ == '__main__':
    print("Started producing messages")
    while True:
        producer.send(wsConnect.connection)
        time.sleep(1)
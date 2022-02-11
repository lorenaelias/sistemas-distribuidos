import paho.mqtt.client as paho
import time

def on_connect(client,userdata,flags,rc):             #create function for callback
    if rc==0:
        print("client is connected")
        global connected
        connected=True
    else:
        print("connection failed")

def on_message(client, userdata, message):
    Messagereceived = True
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

Messagereceived = False
connected=False

broker = "localhost"
port = 12345

client = paho.Client("client1")
client.on_message=on_message

client.connect(broker, port=port)
client.subscribe("/")

client.loop_start()

# while connected != True:
#     time.sleep(0.2)

while Messagereceived!=True:
    time.sleep(0.1)
    
client.loop_stop()
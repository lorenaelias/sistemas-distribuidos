import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("client is connected")
        global connected
        connected = True
    else:
        print("connection failed")

connected = False
broker = "localhost"
port = 12345 

print("creating new instance")

client = mqtt.Client("admin")
client.on_connect=on_connect

print("connecting to broker")
client.connect(broker, port=port)

client.loop_start()

# while connected!=True:
#     time.sleep(0.2)

# for i in range(10):  

print("Publishing message to topic","/") 
client.publish("/", " hello MQtt")

client.loop_stop()
#!/usr/bin/env python 

import os
import time
import sys
from datetime import datetime
import paho.mqtt.client as mqtt
import protobuf_logger_pb2

broker="broker.hivemq.com"
#broker = "18.196.22.171"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    #client.subscribe("enerlyzer_devel/#")
    client.subscribe("enerlyzer/#")

def on_message(client, userdata, msg):
    msg_hex = [elem.encode("hex") for elem in msg.payload]
    #print(msg.topic + " " + str(msg_hex))
    print("length: "+str(len(msg_hex)))
    protobuf_dataset = protobuf_logger_pb2.dataset()
    protobuf_dataset.ParseFromString(msg.payload)
    print(protobuf_dataset)

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

#mqtt_client.connect(broker, 1883, 60)

mqtt_publish_result = mqtt_client.publish("enerlyzer/live/pwr", "test", qos=2)
print(mqtt_publish_result)
if mqtt_publish_result.rc == mqtt.MQTT_ERR_SUCCESS:
    print("published successfully")
    
if mqtt_publish_result.rc == mqtt.MQTT_ERR_NO_CONN:
    print("Not connected")    
    mqtt_client.connect(broker, 1883, 60)
mqtt_client.loop_forever()

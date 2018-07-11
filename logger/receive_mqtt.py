#!/usr/bin/env python 

import os
import time
import sys
from datetime import datetime
import paho.mqtt.client as mqtt

broker="broker.hivemq.com"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("enerlyzer/pwr/supply_voltage/#")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(broker, 1883, 60)

mqtt_client.loop_forever()

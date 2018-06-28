#!/usr/bin/env python 

from influxdb import InfluxDBClient
import os
import json
import time
import sys
from datetime import datetime



import paho.mqtt.client as mqtt


my_env = os.environ.copy()    
client = InfluxDBClient('localhost', 8086, 'influx_user', my_env["INFLUX_USER_PASSWORD"], 'enerlyzer')

LAST_TIME_STAMP_FN = "last_time_stamp.txt"
last_time_stamp = 0.0;
if os.path.isfile(LAST_TIME_STAMP_FN):
    with open(LAST_TIME_STAMP_FN, 'r') as last_time_stamp_file:
        last_time_stamp = float(last_time_stamp_file.readlines()[0].strip())
        
broker="broker.hivemq.com"
mqtt_client= mqtt.Client("client-001") 
mqtt_client.connect(broker)

while 1:
    QUERY="SELECT * FROM powerdata WHERE logger_time > "+str(last_time_stamp)
    last_time_stamp_old = last_time_stamp;
    print(QUERY)
    logger_data = client.query(QUERY)
    for data_set_a in logger_data: 
        #print(data_set)
        for data_set_b in data_set_a: 
            lt=data_set_b['logger_time']
            print(lt)
            if lt == None:
                print(data_set_b)
            else:    
                last_time_stamp = data_set_b['logger_time']
              #  try:
                for key in data_set_b:
                    print("publish: "+"enerlyzer/pwr/"+key+", "+str(data_set_b[key]))
                    mqtt_client.publish("enerlyzer/pwr/"+key, data_set_b[key], qos=1)
                mqtt_client.loop(timeout=1.0)
        

                
               # except:
               #     with open(LAST_TIME_STAMP_FN, 'w') as last_time_stamp_file:
                #        last_time_stamp_file.write(str(last_time_stamp_old))
               #     sys.exit(1)
                last_time_stamp_old = last_time_stamp;
        
        
    with open(LAST_TIME_STAMP_FN, 'w') as last_time_stamp_file:
        last_time_stamp_file.write(str(last_time_stamp))
    time.sleep(0.5)

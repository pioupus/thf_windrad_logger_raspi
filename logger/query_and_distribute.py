#!/usr/bin/env python 

from influxdb import InfluxDBClient
import os
import json
import time
from datetime import datetime


import paho.mqtt.publish as publish



my_env = os.environ.copy()    
client = InfluxDBClient('localhost', 8086, 'influx_user', my_env["INFLUX_USER_PASSWORD"], 'enerlyzer')

LAST_TIME_STAMP_FN = "last_time_stamp.txt"
last_time_stamp = 0.0;
if os.path.isfile(LAST_TIME_STAMP_FN):
    with open(LAST_TIME_STAMP_FN, 'r') as last_time_stamp_file:
        last_time_stamp = float(last_time_stamp_file.readlines()[0].strip())
        
while 1:
    QUERY="SELECT * FROM powerdata WHERE logger_time > "+str(last_time_stamp)
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
                publish.single("enerlyzer/pwr/coin_mv", data_set_b["coin_cell_mv"], hostname="iot.eclipse.org")
            
    with open(LAST_TIME_STAMP_FN, 'w') as last_time_stamp_file:
        last_time_stamp_file.write(str(last_time_stamp))
    time.sleep(0.5)

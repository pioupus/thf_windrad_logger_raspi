#!/usr/bin/env python 

from influxdb import InfluxDBClient
import os
import json
from datetime import datetime


my_env = os.environ.copy()    
client = InfluxDBClient('localhost', 8086, 'influx_user', my_env["INFLUX_USER_PASSWORD"], 'enerlyzer')

while 1:
    logger_data = client.query("SELECT * FROM powerdata")
    print(logger_data)
    time.sleep(0.5)


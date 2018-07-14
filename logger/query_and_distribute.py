#!/usr/bin/env python 

from influxdb import InfluxDBClient
import os
import json
import time
import sys
from datetime import datetime
import protobuf_logger_pb2


import paho.mqtt.client as mqtt


my_env = os.environ.copy()    
client = InfluxDBClient('localhost', 8086, 'influx_user', my_env["INFLUX_USER_PASSWORD"], 'enerlyzer')

LAST_TIME_STAMP_FN = "last_time_stamp.txt"
last_time_stamp = 0.0;
if os.path.isfile(LAST_TIME_STAMP_FN):
    with open(LAST_TIME_STAMP_FN, 'r') as last_time_stamp_file:
        last_time_stamp = float(last_time_stamp_file.readlines()[0].strip())

if last_time_stamp == 0:
    QUERY="SELECT max(logger_time) FROM powerdata"
    max_time_stamp = client.query(QUERY)
    last_time_stamp = list(max_time_stamp.get_points())[0]["max"]
    print("starting with timestamp "+str(last_time_stamp))
    
broker="broker.hivemq.com"
mqtt_client= mqtt.Client("client-001") 
mqtt_client.connect(broker)

sequence_number=0
while 1:
    QUERY="SELECT * FROM powerdata WHERE logger_time > "+str(last_time_stamp)
    last_time_stamp_old = last_time_stamp;
    print(QUERY)
    logger_data = client.query(QUERY)
    print("influx")
    data_sets = list(logger_data.get_points())
    for data_set_b in data_sets:
        #print(data_set_b)
        print(type(data_set_b))

        last_time_stamp = data_set_b['logger_time']
        #  try:
        

        person = protobuf_logger_pb2.dataset()
        person.logger_time =        data_set_b["logger_time"]
        person.current_l1_avg = round(data_set_b["current_l1_avg"]*1000)
        person.current_l2_avg = round(data_set_b["current_l2_avg"]*1000)
        person.current_l3_avg = round(data_set_b["current_l3_avg"]*1000)
        
        person.voltage_l21_avg = round(data_set_b["voltage_l21_avg"]*1000)
        person.voltage_l32_avg = round(data_set_b["voltage_l32_avg"]*1000)
        person.voltage_l13_avg = round(data_set_b["voltage_l13_avg"]*1000)
        
        person.current_l1_eff = round(data_set_b["current_l1_eff"]*1000)
        person.current_l2_eff = round(data_set_b["current_l2_eff"]*1000)
        person.current_l3_eff = round(data_set_b["current_l3_eff"]*1000)

        person.voltage_l21_eff = round(data_set_b["voltage_l21_eff"]*1000)
        person.voltage_l32_eff = round(data_set_b["voltage_l32_eff"]*1000)
        person.voltage_l13_eff = round(data_set_b["voltage_l13_eff"]*1000)
        
        person.current_l1_max = round(data_set_b["current_l1_max"]*1000)
        person.current_l2_max = round(data_set_b["current_l2_max"]*1000)
        person.current_l3_max = round(data_set_b["current_l3_max"]*1000)
        
        person.voltage_l21_max = round(data_set_b["voltage_l21_max"]*1000)
        person.voltage_l32_max = round(data_set_b["voltage_l32_max"]*1000)
        person.voltage_l13_max = round(data_set_b["voltage_l13_max"]*1000)

        person.temperature_l1 = round(data_set_b["temperature_l1"]*1000)
        person.temperature_l2 = round(data_set_b["temperature_l2"]*1000)
        person.temperature_l3 = round(data_set_b["temperature_l3"]*1000)
        
        person.voltage_aux = round(data_set_b["voltage_aux"]*1000)
        person.frequency_Hz = round(data_set_b["frequency_Hz"]*1000)
        person.power = round(data_set_b["power"]*1000)
        
        person.external_current_sensor = data_set_b["external_current_sensor"]
        person.supply_voltage = data_set_b["supply_voltage"]
        person.cpu_temperature = data_set_b["cpu_temperature"]
        person.coin_cell_mv = data_set_b["coin_cell_mv"]
        

        mqtt_client.publish("enerlyzer/pwr/", data_set.SerializeToString(), qos=2)
        mqtt_client.loop(timeout=1.0)


                
               # except:
               #     with open(LAST_TIME_STAMP_FN, 'w') as last_time_stamp_file:
                #        last_time_stamp_file.write(str(last_time_stamp_old))
               #     sys.exit(1)
        last_time_stamp_old = last_time_stamp;
        
        
    with open(LAST_TIME_STAMP_FN, 'w') as last_time_stamp_file:
        last_time_stamp_file.write(str(last_time_stamp))
    time.sleep(0.5)

#!/usr/bin/env python 
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError
import time
from datetime import datetime
import requests
from subprocess import call
  
DB_NAME = 'enerlyzer_logger'
START_UP_TIMEOUT = 5*60

def is_influx_failing():
    try:
        client = InfluxDBClient('localhost', 8086, 'root', 'root', DB_NAME)
        query = 'select value from cpu_load_short;'
        #client.get_list_measurements()
        result = client.query(query)
        return False
    except requests.exceptions.ConnectionError:
        return True
    except InfluxDBClientError as e:
        print(e.message)
        return False

while True:
    if is_influx_failing():
        print('influxdb could not connect')
        call(["systemctl", "restart", "influxdb"])
        timer_value = 0
        successfully_restarted = True
        while is_influx_failing():
            if timer_value % 10 == 0:
                print("still failing: "+str(timer_value))    
            time.sleep(1)
            timer_value = timer_value +1
            if timer_value > START_UP_TIMEOUT:
                successfully_restarted = False
                break;
        if successfully_restarted:
            print("successfully restarted: "+str(timer_value)) 
            call(["systemctl", "restart", "logger.service"])
            
    time.sleep(5)

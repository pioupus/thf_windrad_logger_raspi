#!/usr/bin/env python 
import subprocess
import time
import os
import json
from datetime import datetime

import socket

def string_to_ord(text,length):
    result = []
    for char in text:
        result.append(ord(char))
    for i in range(len(result),length):
        result.append(0)
    return result

class RPCProtocol:
    def __init__(self, comport_path, baud, xml_search_dir):
        my_env = os.environ.copy()
        #my_env["LD_LIBRARY_PATH"] = "/home/pi/JSONtoRPCbridge/bin/release"

        self.rpc_json_bridge_process = subprocess.Popen([my_env["THF_LOGGER_RPC_BIN"], comport_path, str(baud), xml_search_dir], env=my_env, cwd=r'../', stdin=subprocess.PIPE,stdout=subprocess.PIPE, shell = False)
        self._start_tag_positions = []
        self._stop_tag_positions = []




    def _test_json_input(self, test_str):
        result = True
        test_str = test_str[2:-2];                # remove the / of the /{
        
        #print("test_str: "+test_str)
        decoded_answer = {}
        try:
            decoded_answer = json.loads(test_str)
        except ValueError:
            result = False
        
        rpc = {"success": result, "answer":decoded_answer}
        
        return rpc
    

        

    def _append_answer_byte(self, character):
        self._input_buffer += character
        input_not_empty = True
        finished = False
        decoded_answer = {}
        count = 0;
        duration_position_time = 0;
        duration_stop_tag_time = 0;
        duration_start_tag_time = 0;

        while input_not_empty:

            found = False
            
            if self._input_buffer.endswith("/{"):
                self._start_tag_positions.append(len(self._input_buffer)-2);
            

            if self._input_buffer.endswith("}/"):
                self._stop_tag_positions.append(len(self._input_buffer)-2);

            positions_tag_time = time.clock()
            if self._input_buffer.endswith("}/"):
                for start in self._start_tag_positions:

                    for stop in self._stop_tag_positions:
                        if stop < start:
                            continue
                        test_str = self._input_buffer[start : stop  + len('}/')]
                        rpc_result = self._test_json_input(test_str)
                        if rpc_result["success"]:
                            self._input_buffer = self._input_buffer[stop +len("}/"):];
                            finished = True;
                            found = True;
                            decoded_answer = rpc_result["answer"]
                            break;
            
            if found == False:
                input_not_empty = False

        rpc = {"finished": finished, "answer":decoded_answer}
        return rpc
        

    def _send_and_receive_json(self,json_request, await_answer = True):
        start = time.clock()
        self._input_buffer = ''
        self._start_tag_positions = []
        self._stop_tag_positions = []
        
        rpc_request_string = json.dumps(json_request)
        print("rpc_request_string: "+ rpc_request_string)

        #start_stdinwrite = time.clock()
        self.rpc_json_bridge_process.stdout.flush()
        self.rpc_json_bridge_process.stdin.write('/'+rpc_request_string+'/\n')
        self.rpc_json_bridge_process.stdin.flush()
        #print("stdinwrite[ms]: "+str((time.clock() - start_stdinwrite)*1000))

        byte_count = 0
        duration_total = 0.0
        duration_total_read = 0.0
        duration_total_append = 0.0
        while await_answer:
            byte_count = byte_count +1
            
           # start_time = time.clock()
            answer_byte = self.rpc_json_bridge_process.stdout.read(1);
          #  duration_read = (time.clock() - start_time)*1000
            
            #start_time = time.clock()
            rpc_answer = self._append_answer_byte(answer_byte)
           # duration_append = (time.clock() - start_time)*1000
            
            ##duration_total = duration_total + duration_append + duration_read
            #duration_total_append = duration_total_append + duration_append
            #duration_total_read = duration_total_read + duration_read
            
  
            if rpc_answer["finished"]:
               # print("count: "+str(byte_count)+
                #      " total: "+str(duration_total)+
                #      " duration_total_append: "+str(duration_total_append)+
                #      " duration_total_append_avg: "+str(duration_total_append/byte_count)+
                #      " duration_total_read: "+str(duration_total_read)
               #       )
                #print("_send_and_receive_json[ms]: "+str((time.clock() - start)*1000))
                return rpc_answer["answer"]
            #time.sleep(0.05)
            
        
            
    def __del__(self):
        rpc_request = {
                'controll':{
                    'command':'quit',
                    'arguments':{}
                    }
            }
        self._send_and_receive_json(rpc_request, await_answer = False)

        
        
    def call(self,function_name, arguments, timeout_ms = 100):
        rpc_request = {
                'rpc':{
                    'timeout_ms':timeout_ms,
                    'request':{
                            'function':function_name,
                            'arguments':arguments
                        }
                    }
            }
        decoded_answer = self._send_and_receive_json(rpc_request)
        #print("decoded_answer: "+ str(decoded_answer)) 
        return decoded_answer['rpc']['reply']
    

    def get_server_hash(self):
        rpc_request = {
                'controll':{
                    'command':'get_hash',
                    'arguments':{}
                    }
            }
        decoded_answer = self._send_and_receive_json(rpc_request)
        #print(self._decoded_answer) 
        return decoded_answer['controll']['result']['hash']
    
    def get_version(self):
        rpc_request = {
                'controll':{
                    'command':'get_version',
                    'arguments':{}
                    }
            }
        decoded_answer = self._send_and_receive_json(rpc_request)
        
        version_info =   { "git_hash": decoded_answer['controll']['result']['git_hash'],
                   "git_unix_date":decoded_answer['controll']['result']['git_unix_date'],
                   "git_string_date":decoded_answer['controll']['result']['git_string_date']
                }
        
        return version_info
                    
    
my_env = os.environ.copy()
print("using THF_LOGGER_SERIAL "+my_env["THF_LOGGER_SERIAL"])  
print("using THF_LOGGER_BAUD "+my_env["THF_LOGGER_BAUD"])  
print("using THF_LOGGER_RPC_XML "+my_env["THF_LOGGER_RPC_XML"])  

proto = RPCProtocol(my_env["THF_LOGGER_SERIAL"],my_env["THF_LOGGER_BAUD"],my_env["THF_LOGGER_RPC_XML"])

arguments_sys_stat = {}
arguments_sys_stat["unix_date_time"] = int(round(time.time()))

result = proto.call("set_unix_date_time",arguments_sys_stat)


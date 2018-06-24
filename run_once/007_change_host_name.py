#!/usr/bin/env python 

FILENAME_HOSTS = '/etc/hosts'
FILENAME_HOST_NAME = '/etc/hostname'

DESIRED_HOST_NAME = "enerlyzer"

host_lines = []
with open(FILENAME_HOSTS) as f:
    host_lines = f.readlines()

with open(FILENAME_HOSTS, 'w') as f:
    for line in host_lines:
        tabs = line.split()
        ip = ''
        hostname = ''
        if len(tabs) > 0:
            ip = tabs[0].strip()
        if len(tabs) > 1:
            hostname = tabs[1].strip()
        if (ip == "127.0.0.1" or ip == "127.0.1.1") and hostname != "localhost":
            hostname = DESIRED_HOST_NAME
            tabs[1] = hostname;
            line = '\t'.join(tabs)
        f.write(line)
    
with open(FILENAME_HOST_NAME, 'w') as f:
        f.write(DESIRED_HOST_NAME)
    
    

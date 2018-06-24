#!/bin/sh
echo $MY_PASSWORD | sudo -S python 007_change_host_name.py
echo $MY_PASSWORD | sudo -S iconfig eth0 down
echo $MY_PASSWORD | sudo -S iconfig eth0 up

#!/bin/sh

echo $MY_PASSWORD | sudo -S apt update
echo $MY_PASSWORD | sudo -S apt-get -y install libqt5serialport5 libqt5xml5 python-pip resolvconf
echo $MY_PASSWORD | sudo -S pip install paho-mqtt

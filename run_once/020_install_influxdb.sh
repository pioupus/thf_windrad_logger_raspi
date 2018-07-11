#!/bin/sh
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

echo $MY_PASSWORD | sudo -S apt install apt-transport-https
echo $MY_PASSWORD | sudo -S curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
echo $MY_PASSWORD | sudo -S apt update
echo $MY_PASSWORD | sudo -S apt-get -y install influxdb python-influxdb python-protobuf
echo $MY_PASSWORD | sudo -S cp -rf $SCRIPTPATH/../etc/influxdb/influxdb.conf /etc/influxdb/influxdb.conf
#sudo service influxdb start

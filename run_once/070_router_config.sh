#!/bin/sh
echo $MY_PASSWORD | sudo -S apt-get -y install hostapd bridge-utils
sudo systemctl restart dhcpcd
sudo systemctl restart dnsmasq
sudo systemctl enable dnsmasq
sudo chmod 600 /etc/hostapd/hostapd.conf
echo $MY_PASSWORD | sudo -S bash -c 'echo RUN_DAEMON=yes >> /etc/default/hostapd'
echo $MY_PASSWORD | sudo -S bash -c 'echo DAEMON_CONF="/etc/hostapd/hostapd.conf" >> /etc/default/hostapd'
sudo systemctl unmask hostapd
sudo systemctl start hostapd
sudo systemctl enable hostapd
echo $MY_PASSWORD | sudo -S bash -c 'echo net.ipv4.ip_forward=1 >> /etc/sysctl.conf'

sudo iptables -t nat -A  POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -A FORWARD -i ethX -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT

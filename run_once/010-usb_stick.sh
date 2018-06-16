#!/bin/sh

echo $MY_PASSWORD | sudo -S mkdir /media/
echo $MY_PASSWORD | sudo -S mkdir /media/usbstick
echo $MY_PASSWORD | sudo -S chmod 775 /media/usbstick
echo $MY_PASSWORD | sudo -S bash -c 'echo LABEL=logger_usb_stick  /media/usbstick/ ext2   defaults 0 0 >> /etc/fstab'



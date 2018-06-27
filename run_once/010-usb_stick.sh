#!/bin/sh

echo $MY_PASSWORD | sudo -S mkdir /media/
echo $MY_PASSWORD | sudo -S mkdir /media/usbstick
echo $MY_PASSWORD | sudo -S chmod 777 /media/usbstick
echo $MY_PASSWORD | sudo -S bash -c 'echo LABEL=logger_usb_stick  /media/usbstick/        ext2    rw,user,exec,sync,auto,nofail   0       2 >> /etc/fstab'
echo $MY_PASSWORD | sudo -S mount -a


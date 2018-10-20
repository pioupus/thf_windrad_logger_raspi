# How To
- Install raspbian lite on SD-Card
- add the line 'enable_uart=1' to /boot/config.txt
- delete 'console=serial0,115200' from cmdline.txt
- put the file 'ssh' in the /boot/ directory for enabling ssh
- write the lines
```
MY_PASSWORD=xxx
INFLUX_USER_PASSWORD=yyy
```

to ~/logger.env where xxx is your ssh sudo password

- add the line 
```
set -a; source /home/pi/logger.env; set +a
```

to ~/bashrc

- run sudo apt-get update
- install git using sudo apt-get install git
- clone this repository using git clone https://github.com/pioupus/thf_windrad_logger_raspi.git
- cd thf_windrad_logger/update/
- execute ./run_run_once.py

create and copy the ssh key to remote backup server for rsync via ssh:
 --ssh-

- ssh-keygen -f ~/.ssh/server_enerlyzer_receiver
- ssh-copy-id -i ~/.ssh/server_enerlyzer_receiver enerlyzer_receiver@62.113.246.9
- eval `ssh-agent -s`
- ssh-add ~/.ssh/server_enerlyzer_receiver

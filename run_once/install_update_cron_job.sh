 #!/bin/sh
 
croncmd_update="python /home/pi/thf_windrad_logger_raspi/update/do_update.py > /home/pi/update_cron_log.log 2>&1"
cronjob_update="*/15 * * * * $croncmd_update"


croncmd_backup="/bin/bash --login /home/pi/thf_windrad_logger_raspi/logger/backup.sh > /media/usbstick/logger_data/backup.log"
cronjob_backup="*/15 * * * * $croncmd_backup"


( crontab -l | grep -v -F "$croncmd_update" ; echo "$cronjob_update" ) | crontab - 
( crontab -l | grep -v -F "$croncmd_backup" ; echo "$cronjob_backup" ) | crontab - 

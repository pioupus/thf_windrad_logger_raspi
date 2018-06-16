 #!/bin/sh
 
croncmd="/home/pi/thf_windrad_logger_raspi/update/do_update.py > /home/pi/update_cron_log.log 2>&1"

cronjob="0 */15 * * * $croncmd"

( crontab -l | grep -v -F "$croncmd" ; echo "$cronjob" ) | crontab - 

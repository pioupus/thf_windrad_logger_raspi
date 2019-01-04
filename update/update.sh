#!/bin/sh

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

logger_env=/home/pi/logger.env
if [ -e "$logger_env" ]; then
    set -a; source $logger_env; set +a
fi 

python $SCRIPTPATH/do_update.py

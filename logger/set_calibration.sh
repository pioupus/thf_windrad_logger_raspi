 
#!/bin/sh

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

export THF_LOGGER_RPC_BIN_PATH=$SCRIPTPATH"/../bin/JSONtoRPCbridge/"

export THF_LOGGER_SERIAL="/dev/ttyS0"
export THF_LOGGER_BAUD=115200
export THF_LOGGER_RPC_XML=$SCRIPTPATH"/xml/"

export THF_LOGGER_RPC_BIN=${THF_LOGGER_RPC_BIN_PATH}/consoleapp
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${THF_LOGGER_RPC_BIN_PATH}

./set_calibration.py

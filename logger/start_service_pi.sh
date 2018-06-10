#!/bin/sh

THF_LOGGER_RPC_BIN_PATH="/home/pi/JSONtoRPCbridge/bin/release"

export THF_LOGGER_SERIAL="/dev/ttyS0"
export THF_LOGGER_BAUD=115200
export THF_LOGGER_RPC_XML="/home/pi/thf_logger/xml_rpc/"

export THF_LOGGER_RPC_BIN=${THF_LOGGER_RPC_BIN_PATH}/consoleapp
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${THF_LOGGER_RPC_BIN_PATH}

./pyRPCProtocol.py
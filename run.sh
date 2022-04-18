#!/bin/bash
SCRIPT_PATH="`dirname $0`"
CONFIG_FILE="$SCRIPT_PATH/config.sh"
SCRIPT_FILE="$SCRIPT_PATH/main.py"

# Source the config file.
if [[ -f $CONFIG_FILE ]]
then
    source $CONFIG_FILE
else
    echo "A config file must be provided as 'config.sh', consider copying 'config_example.sh'."
    exit
fi

# Activate the virtual environment.
source $VIRTUALENV

# Run the program.
python $SCRIPT_FILE \
    -c $COMPLETED \
    -m $MOVIES \
    -s $SERIES \
    --cache $CACHE \
    --logs $LOGS

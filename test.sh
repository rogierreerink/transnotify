#!/bin/bash

COMPLETED="test/torrents/completed"
CACHE="test/var/cache/transnotify"
LOGS="test/var/log/transnotify"

python main.py \
    -c $COMPLETED \
    --cache $CACHE \
    --logs $LOGS

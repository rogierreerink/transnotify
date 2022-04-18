#!/bin/bash

COMPLETED="test/torrents/completed"
MOVIES="test/media/movies"
SERIES="test/media/series"
CACHE="test/var/cache/transnotify"
LOGS="test/var/log/transnotify"

python main.py \
    -c $COMPLETED \
    -m $MOVIES \
    -s $SERIES \
    --cache $CACHE \
    --logs $LOGS

#!/usr/bin/env bash

NUM=$1
LOG_FILE="result.log"

rm -f "$LOG_FILE"
for ((i=0; i < NUM; i++))
do
    python -m "holdem.holdem" >> "$LOG_FILE"
    echo '-' >> "$LOG_FILE"
done

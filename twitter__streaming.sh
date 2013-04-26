#!/usr/bin/env bash
 
while :
do
  echo Now Streaming...
  date
  python twitter__streaming.py >> filename.dat
  sleep 240
done

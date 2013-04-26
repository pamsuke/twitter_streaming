#!/usr/bin/env bash
 
while :
do
  echo Now Streaming...
  echo date
  python twitter__streaming.py >> filename.dat
  sleep 240
done

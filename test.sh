#!/bin/bash

for n in `seq 3`
do
  echo "--- fast version #${n} ---"
  time ansible -i fast.py all -m ping --list-hosts 
done

for n in `seq 3`
do
  echo "-- slow version #${n} ---"
  time ansible -i slow.py all -m ping --list-hosts 
done

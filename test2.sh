#!/bin/bash

for n in `seq 3`
do
  echo "--- fast version 2 #${n} ---"
  time ansible -i fast2.py all -m ping --list-hosts 
done

#!/bin/bash

for d in {01..25}
do
  if [[ -f $d/p1.py ]]
  then
    $d/p1.py $d/input
  fi

  if [[ -f $d/p2.py ]]
  then
    $d/p2.py $d/input
  fi
done

#!/bin/bash

cat $1 | sed '1d' | sed '4d' | sed -e $'s/{/{\\\n/g' | sed -E 's/treatStage\(pt\(([0-9]*), ([0-9]*)\), ([0-9]*)\) @ ([0-9]*),/treatStage\(pt\(\1, \2\), \3\) @ \4!/g' | sed -e $'s/!/\\\n,\\\n/g' | sed -e $'s/}/\\\n}/g' > tmp 

cat tmp | sed -E 's/reduce in SCENARIO-DIAGNOSIS :/%/g' | sed '2,3d' | sed '3,5d' > $2
cat tmp | sed -E 's/reduce in SCENARIO-DIAGNOSIS :/%/g' | sed '2,3d' | sed '2,3d' | sed '3d' > $3
cp tmp $1

cat $2 | sed '1d' | \
  sed -E 's/atloc\(b\(([0-9]*)\), pt\(([0-9]*), ([0-9]*)\)\) @ ([0-9]*)/\1, \2, \3, \4/g' | \
  sed -E 's/atloc\(ob\(([0-9]*)\), pt\(([0-9]*), ([0-9]*)\)\) @ ([0-9]*)/3, \2, \3, \4/g' | \
  sed -E 's/\(treatStage\(pt\(([0-9]*), ([0-9]*)\), ([0-9]*)\) @ ([0-9]*)\)/2, \1, \2, \4;/g' | \
  sed -E 's/treatStage\(pt\(([0-9]*), ([0-9]*)\), ([0-9]*)\) @ ([0-9]*)/2, \1, \2, \4/g' | \
  sed -E 's/\(([0-9]*), ([0-9]*), ([0-9]*), ([0-9]*)\)/\1, \2, \3, \4;/g' | \
  sed -e $'s/;/\\\n/g' | sed $'1 s/^/0, 0, 1, 0\\\n/' | sed $'1 s/^/1, 0, 4, 0\\\n/' | \
  sed $'1 s/^/bot, x, y, t\\\n/' | sed '/^ *$/d' > $4 

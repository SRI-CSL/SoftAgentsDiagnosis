#!/bin/bash

echo "--------------------------------------" > $4
echo "deviate " $1 $2 "-g " $3 >> $4 
script -q -a $4 deviate $1 $2 -g $3 > /dev/null
echo "--------------------------------------" >> $4
echo "deviate " $1 $2 "-i -g " $3 >> $4 
script -q -a $4 deviate $1 $2 -i -g $3 > /dev/null
echo "--------------------------------------" >> $4
echo "deviate " $1 $2 "-fv -g " $3 >> $4 
script -q -a $4 deviate $1 $2 -fv -g $3 > /dev/null
echo "--------------------------------------" >> $4
echo "deviate " $1 $2 "-m -g " $3 >> $4 
script -q -a $4 deviate $1 $2 -m -g $3 > /dev/null
echo "--------------------------------------" >> $4
echo "deviate " $1 $2 "-u -g " $3 >> $4 
script -q -a $4 deviate $1 $2 -u -g $3 > /dev/null
dos2unix -q $4 

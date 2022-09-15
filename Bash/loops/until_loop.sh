################## THE UNTIL LOOP ###################

until command
do
    statement(s) to be executed until command is true
done


#!/bin/bash

# until var a is NOT less than 10 
# print var a
# add 1 to var a 
a=0
until [ ! $a -lt 10 ]
do
    echo $a 
    a=`expr $a + 1`
done

# runs until contion id true

#0
#1
#2
#3
#4
#5
#6
#7
#8
#9

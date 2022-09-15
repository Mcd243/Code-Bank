################## THE WHILE LOOP #################

while command
do  
    statement(s) to be executed if command is true
done


# while var a is less than 10 
# print var a and add 1 to var a 

#!/bin/bash
a=0
while [ $a -lt 10 ]
do
    echo $a
    a=`expr $a + 1`
done
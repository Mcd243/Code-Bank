############### NESTED LOOPS ####################

#!/bin/bash

# while a is less than 10
    # set b to value in a 
    # while b is greater than or equal to 0 
        # print b to a new line 
        # subtract 1 from b
    # print ?
    # add 1 to a
# stop the loop
a=0
while [ "$a" -lt 10 ]
do
    b="$a"
    while [ "$b" -ge 0 ]
    do
        echo -n "$b "
        b=`expr $b - 1`
    done
    echo 
    a=`expr $a + 1`    
done




##################### BREAK ####################

break    - break the loop

break n  - break the loop when it reaches name

#!/bin/bash

a=0
while [ $a -lt 10 ]
do
    echo $a
    if [ $a -eq 5 ]
    then
        break
    fi
    a=`expr $a + 1`
done

#0
#1
#2
#3
#4
#5


################### CONTINUE ##################

#!/bin/bash

NUMS="1 2 3 4 5 6 7"
for NUM in $NUMS
do
    Q=`expr $NUM % 2`
    if [ $Q -eq 0 ]
    then
        echo "Number is an even number!!"
        continue
    fi
    echo "Found odd number"
done




#!/bin/bash

# st a flag for the while loop to run
FLAG=true
declare -a LIST=()
echo "Add some integers to work out the average of all the integers. Enter x to>
# collect the integers from the user
while $FLAG
        do
        echo "Add an integer: "
        read INT
        if [[ "$INT" =~ "[0-9]+" ]]
                then
                        echo "adding $INT"
                        LIST+=("$INT")
        elif [ $INT == "x" ]
                then
                        FLAG=false
        else 
                echo "Enter an integer or x to exit"
        fi
done
  


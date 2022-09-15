#!/bin/bash

# set the needed variables
COUNT=0
POT=0
FLAG=true
echo "Add some integers to work out the average of all the integers. Enter x to exit "

while $FLAG
        do
        # collect an integer from the user
        echo "Add an integer: "
        read INT
        # check that the user input is an integer
        if [[ "$INT" =~ "[0-9]" ]]
                then
                #add the user input to the pot and increment the counter
                echo "There is $POT in the pot"
                POT=`expr $POT + $INT`
                COUNT=`expr $COUNT + 1`
        # check to see if the user wants to finish
        elif [ $INT == "x" ]
                then
                #calculate the average
                AVE=`expr $POT / $COUNT | bc -l`
                echo "The average of your numbers is : $AVE"
                FLAG=false
        # if the user gives incorrect input instruct them
        else 
                echo "Enter an integer or x to exit"
        fi
done


#!/bin/bash


#########################################################################


# set the needed variables



COUNT=0
POT=0
FLAG=true
echo "Add some integers to work out the average of all the integers. Enter x to exit "
while $FLAG
do
# collect an integer from the user
echo "Add an integer: "
read INT
# check that the user input is an integer
if [[ "$INT" =~ [0-9]+ ]]
# "$INT" =~ [0-9]+ This correct syntax, It should not have "." in [0-9]+
then
#add the user input to the pot and increment the counter
echo "There is $POT in the pot"
POT=`expr $POT + $INT`
COUNT=`expr $COUNT + 1`
# check to see if the user wants to finish
elif [ $INT == "x" ]
then
#calculate the average
# AVE=`expr $POT / $COUNT | bc -l`, Please check this line. bc -l should be with echo.
AVE=`echo $POT / $COUNT | bc -l`
echo "The average of your numbers is : $AVE"
FLAG=false
# if the user gives incorrect input instruct them
else
echo "Enter an integer or x to exit"
fi
done


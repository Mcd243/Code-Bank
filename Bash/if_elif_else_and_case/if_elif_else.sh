
if [ expression 1 ]
then
   Statement(s) to be executed if expression 1 is true
elif [ expression 2 ]
then
   Statement(s) to be executed if expression 2 is true
elif [ expression 3 ]
then
   Statement(s) to be executed if expression 3 is true
else
   Statement(s) to be executed if no expression is true
fi



########## BASIC IF STATEMENT ##############

#!/bin/bash
# get user input and store in myvar
read -p "Enter numeric value: " myvar
if [ $myvar -gt 10 ]
then
echo "Value is greater than 10"
# finish
fi

################ IF ELSE ##################

#!/bin/bash
# get user input and store in myvar
read -p "Enter numeric value: " myvar
if [ $myvar -gt 10 ]
then
echo "Value is greater than 10"
else
echo "Value is not greater than 10"
# finish
fi


################# IF ELIF ##################

#!/bin/bash
# get user input and store in myvar
read -p "Enter numeric value: " myvar
if [ $myvar -gt 10 ]
then
echo "Value is greater than 10"
elif [ $myvar -eq 10 ]
echo "Value is not greater than 10"
# finish
fi
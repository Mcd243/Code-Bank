#!/bin/sh
echo "How much money do you have?"
read MONEY
echo "How many years do you want to store your money?"
read YEARS
echo "What is the interest rate"
read INTEREST_RATE
y=0
# bc -l handles floats
interest_rate_correct=`echo $INTEREST_RATE / 100 | bc -l`
        echo "Correct interest rate is $interest_rate_correct"

while [ $y -le $YEARS ]
do
        #MONEY=`expr $MONEY + $MONEY \* $INTEREST_RATE / 100`
        #echo "In year $y you will have $MONEY (incorrect due to INTEREST_RATE / 100 is always zero (0.12 for example, so .12 is neglagted and it is considered as 0"
       #IR=`expr $INTEREST_RATE / 100`
       
       
        MONEY=`echo $MONEY + $MONEY \* $interest_rate_correct | bc -l`
        echo "Value of in $y is $MONEY"
       
        y=`expr $y + 1`
done
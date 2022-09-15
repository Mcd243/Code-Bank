#!/bin/bash

####################### ROUND ROBIN ###########################

# Variables to point to the files to be appended next
FETCH1=1
FETCH2=$(($FETCH1+1))

# A while loop that completes when the total number of files have been appended to
# final_chapter.txt 
while [[ $COUNTR -gt 0 ]]
do

# Read the contents of 2 files from tmp1 and append to final_chapter.txt if 
if [[ $NUM1 -gt 0 ]]
then
sudo cat ./tmp1/$FETCH1 >> final_chapter.txt
NUM1=$(($NUM1-1))
COUNTR=$(($COUNTR-1))
fi

if [[ $NUM1 -gt 0 ]]
then
sudo cat ./tmp1/$FETCH2 >> final_chapter.txt
NUM1=$(($NUM1-1))
COUNTR=$(($COUNTR-1))
fi

# Read the contents of 2 files from tmp2 and append to final_chapter.txt
if [[ $NUM2 -gt 0 ]]
then
sudo cat ./tmp2/$FETCH1 >> final_chapter.txt
NUM2=$(($NUM2-1))
COUNTR=$(($COUNTR-1))
fi

if [[ $NUM2 -gt 0 ]]
then
sudo cat ./tmp2/$FETCH2 >> final_chapter.txt
NUM2=$(($NUM2-1))
COUNTR=$(($COUNTR-1))
fi

# Read the contents of 2 files from tmp3 and append to final_chapter.txt
if [[ $NUM3 -gt 0 ]]
then
sudo cat ./tmp3/$FETCH1 >> final_chapter.txt
NUM3=$(($NUM3-1))
COUNTR=$(($COUNTR-1))
fi

if [[ $NUM3 -gt 0 ]]
then
sudo cat ./tmp3/$FETCH2 >> final_chapter.txt
NUM3=$(($NUM3-1))
COUNTR=$(($COUNTR-1))
fi

# Update file numbers to fetch for the next iteration.
FETCH1=$(($FETCH1+2))
FETCH2=$(($FETCH1+1))

done
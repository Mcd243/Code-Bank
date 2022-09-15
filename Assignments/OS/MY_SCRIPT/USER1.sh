#!/bin/bash

echo 'Loading the final chapter...'
sleep 1
echo '.'
sleep 1
echo '..'
sleep 1
echo '...'
sleep 1
echo "  _____   _              ___   _                 _      ___   _                    _               ";
echo " |_   _| | |_    ___    | __| (_)  _ _    __ _  | |    / __| | |_    __ _   _ __  | |_   ___   _ _ ";
echo "   | |   | ' \  / -_)   | _|  | | | ' \  / _\` | | |   | (__  | ' \  / _\` | | '_ \ |  _| / -_) | '_|";
echo "   |_|   |_||_| \___|   |_|   |_| |_||_| \__,_| |_|    \___| |_||_| \__,_| | .__/  \__| \___| |_|  ";
echo "                                                                           |_|                     ";
echo ''
cat ./final_chapter.txt
echo ''
echo ''
echo ''
echo 'From here you have a few options.'
sleep 1


FLAG=true

while [[ "$FLAG" == "true" ]]
do
echo ''
echo 'What would you like to do?'
sleep 1
echo ''
echo 'Enter: [1] - to read the chapter.'
echo '       [2] - to search and change text in the chapter.'
echo '       [3] - add some text to the end of the chapter'
echo '       [x] - to teminate the program.'
sleep 1
echo ''
read CHOICE
if [[ $CHOICE -eq 1 ]]
then
cat ./final_chapter.txt
echo ''
echo ''

elif [[ $CHOICE -eq 2 ]]
then
echo 'Ok... You want to find some text in the chapter and then replace it with some new text.'
sleep 1
echo 'First enter the text you would like to find:'
read OLD
echo "Great. You want to replace $OLD." 
sleep 1
echo 'Now enter the text you would like to replace it with'
read NEW
echo "Ok... replacing $OLD with $NEW. "
sed "s|$OLD|$NEW|g" ./final_chapter.txt 
echo ''

elif [[ $CHOICE -eq 3 ]]
then
echo 'Ok... You want to add some text to the end of the chapter'
echo ''
sleep 1
echo 'Add your text now:'
echo ''
read APPEND 
echo $APPEND >> ./final_chapter.txt
echo ''

elif [[ "$CHOICE" = "x" ]]
then
echo 'The pen is mightier than the sword...'
sleep 1
echo " ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .           ▌ ▐·▄▄▄ .▄▄▄  ";
echo "▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀·    ▪     ▪█·█▌▀▄.▀·▀▄ █·";
echo "▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄     ▄█▀▄ ▐█▐█•▐▀▀▪▄▐▀▀▄ ";
echo "▐█▄▪▐█▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌    ▐█▌.▐▌ ███ ▐█▄▄▌▐█•█▌";
echo "·▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀      ▀█▄▀▪. ▀   ▀▀▀ .▀  ▀";
echo 'Good Bye X~D' 
echo ''
FLAG=false


else
echo ''
echo 'Your choice is not recognised.'
echo ''
sleep 1
echo 'Its easy... just enter 1, 2, 3 or x when prompted.'
sleep 2

fi

done

#https://www.brianchildress.co/using-variables-with-sed/

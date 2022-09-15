#!/bin/bash

echo 'Loading the final chapter...'
sleep 1
echo '.'
sleep 1
echo '..'
sleep 1
echo '...'
sleep 1
# Graphics thanks to patrojk.com: http://patorjk.com/software/taag
echo "  _____   _              ___   _                 _      ___   _                    _               ";
echo " |_   _| | |_    ___    | __| (_)  _ _    __ _  | |    / __| | |_    __ _   _ __  | |_   ___   _ _ ";
echo "   | |   | ' \  / -_)   | _|  | | | ' \  / _\` | | |   | (__  | ' \  / _\` | | '_ \ |  _| / -_) | '_|";
echo "   |_|   |_||_| \___|   |_|   |_| |_||_| \__,_| |_|    \___| |_||_| \__,_| | .__/  \__| \___| |_|  ";
echo "                                                                           |_|                     ";
echo ''
# Read out the final chapter.
cat ./final_chapter.txt
echo ''
echo ''
echo ''
echo 'From here you have a few options.'
sleep 1

# Flag to exit the while loop on users request.
FLAG=true

# Take in user input untill the user quits
while [[ "$FLAG" == "true" ]]
do
echo ''
echo 'What would you like to do?'
sleep 1
echo ''
# Print options for the user to choose.
echo 'Enter: [1] - to read the chapter.'
echo '       [2] - to search and change text in the chapter.'
echo '       [3] - add some text to the end of the chapter'
echo '       [x] - to teminate the program.'
sleep 1
echo ''
read CHOICE

# Read the chapter
if [[ $CHOICE -eq 1 ]]
then
cat ./final_chapter.txt
echo ''
echo ''
# Search and replace text
elif [[ $CHOICE -eq 2 ]]
then
echo 'Ok... You want to find some text in the chapter and then replace it with some new text or just delete it.'
sleep 1
echo 'First enter the text you would like to find:'
read OLD
    # Check if user has entered any text. If they have not, prompt them to add some text.
    while [[ $(echo $OLD | wc -c) == 1 ]]
    do
        echo ''
        echo 'You have not entered any text...'
        echo ''
        echo 'Please enter the text you would like to find.'
        read OLD
    done
    
    if [[ $(echo $OLD | wc -c) -gt 1 ]]
    then
    echo "Great. You want to replace $OLD." 
    sleep 1
    fi

echo 'Now enter the text you would like to replace it with...'
echo 'If you would like to delete your chosen text just press enter...'
echo 'or enter "x" to exit.'
echo ''
sleep 1
read NEW
    # Check if user has entered any text. If they have not, prompt them to add some text.
    if [[ $(echo $NEW | wc -c) == 1 ]]
    then
    echo ''
    echo "Deleting $OLD"
    sed "s|$OLD|$NEW|g" ./final_chapter.txt
    sleep 1

    elif [[ "$NEW" == "x" ]]
    then
    exit 

    else 
    [[ $(echo $NEW | wc -c) -gt 1 ]]   
    echo 'Ok... replacing "$OLD" with "$NEW".'
    echo ''
    sleep 1 
    # sed operation link: https://www.brianchildress.co/using-variables-with-sed/
    sed "s|$OLD|$NEW|g" ./final_chapter.txt 
    echo ''
    fi

# Add text to be appended to the end of the text.
elif [[ $CHOICE -eq 3 ]]
then
echo 'Ok... You want to add some text to the end of the chapter'
echo ''
sleep 1
echo 'Add your text now:'
echo ''
read APPEND
    # Check if user has entered any text. If they have not, prompt them to add some text.
    while [[ $(echo $APPEND | wc -c) == 1 ]]
    do
    echo ''
    echo 'You have not entered any text...'
    echo ''
    echo 'Please add your text now:'
    read APPEND
    done 
echo $APPEND >> ./final_chapter.txt
echo ''
# Quit the program
elif [[ "$CHOICE" = "x" ]]
then
echo 'The pen is mightier than the sword...'
sleep 1
# Graphics thanks to patrojk.com: http://patorjk.com/software/taag
echo " ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .           ▌ ▐·▄▄▄ .▄▄▄  ";
echo "▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀·    ▪     ▪█·█▌▀▄.▀·▀▄ █·";
echo "▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄     ▄█▀▄ ▐█▐█•▐▀▀▪▄▐▀▀▄ ";
echo "▐█▄▪▐█▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌    ▐█▌.▐▌ ███ ▐█▄▄▌▐█•█▌";
echo "·▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀      ▀█▄▀▪. ▀   ▀▀▀ .▀  ▀";
echo 'Good Bye X~D' 
echo ''
FLAG=false
# Exception handling for unrecognised user input.
else
echo ''
echo 'Your choice is not recognised.'
echo ''
sleep 1
echo 'Its easy... just enter 1, 2, 3 or x when prompted.'
sleep 2
fi
done



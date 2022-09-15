#!/bin/bash

# A function to check if Docker is installed. If it is not, install it.
docker_check(){
docker -v
if [ $? -ne 128 ] ; then
echo ''
echo "Docker is installed on your machine. Lets create some containers..."
sleep 4
else
echo ''
echo "Docker is not installed on your machine. Let us install it...."
sudo apt-get install apt-transport-https ca certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-get update
sudo apt install docker.io
sudo docker info
fi
}


# A function to ctreate a container
function create_container() {
sudo docker run --name $1 -t -d ubuntu /bin/bash
}


# A function to find the folders and send the files to the respective containe
SEND() {
find ~ -type d -name "$1" -exec sudo docker cp {} $2:/tmp/ \;
sudo docker exec $2 ls -l /tmp/$1
}

# Create a script to sort files in GoD1
echo '#!/bin/bash' > GET_BSORT1
echo 'mkdir renamed1' >> GET_BSORT1
echo 'cd Docker1' >> GET_BSORT1
echo 'for item in `seq 1 $(ls | wc -l)`' >> GET_BSORT1
echo 'do' >> GET_BSORT1
echo 'mv $(find . -type f -exec ls -l {} \; | sort -nr -k5 | tail -n 1 | cut -f11 -d" " | cut -c3-) $item' >> GET_BSORT1
echo 'mv $item /tmp/renamed1' >> GET_BSORT1
echo 'done' >> GET_BSORT1
echo 'cd ..' >> GET_BSORT1
echo 'rm -r Docker1' >> GET_BSORT1

# Create a script to sort files in GoD2
echo '#!/bin/bash' > GET_BSORT2
echo 'mkdir renamed2' >> GET_BSORT2
echo 'cd Docker2' >> GET_BSORT2
echo 'for item in `seq 1 $(ls | wc -l)`' >> GET_BSORT2
echo 'do' >> GET_BSORT2
echo 'mv $(find . -type f -exec ls -l {} \; | sort -nr -k5 | tail -n 1 | cut -f11 -d" " | cut -c3-) $item' >> GET_BSORT2
echo 'mv $item /tmp/renamed2' >> GET_BSORT2
echo 'done' >> GET_BSORT2
echo 'cd ..' >> GET_BSORT2
echo 'rm -r Docker2' >> GET_BSORT2

# Create a script to rename files in GoD3
echo '#!/bin/bash' > GET_B
echo 'mkdir renamed3' >> GET_B
echo 'cd Docker3' >> GET_B
echo 'for item in `seq 1 $(ls | wc -l)`' >> GET_B
echo 'do' >> GET_B
echo 'mv $(ls | head -n 1) $item' >> GET_B
echo 'mv $item /tmp/renamed3' >> GET_B
echo 'done' >> GET_B
echo 'cd ..' >> GET_B
echo 'rm -r Docker3' >> GET_B

###################### Main ############################

# Graphics thanks to patrojk.com: http://patorjk.com/software/taag
echo " ______     ______     __    __     ______        ______     ______         ";
echo "/\  ___\   /\  __ \   /\ \"-./  \   /\  ___\      /\  __ \   /\  ___\        ";
echo "\ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\      \ \ \/\ \  \ \  __\        ";
echo " \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\     \ \_____\  \ \_\          ";
echo "  \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/      \/_____/   \/_/          ";
echo "                                                                            ";
echo " _____     ______     ______     __  __     ______     ______     ______    ";
echo "/\  __-.  /\  __ \   /\  ___\   /\ \/ /    /\  ___\   /\  == \   /\  ___\   ";
echo "\ \ \/\ \ \ \ \/\ \  \ \ \____  \ \  _\"-.  \ \  __\   \ \  __<   \ \___  \  ";
echo " \ \____-  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \/\_____\ ";
echo "  \/____/   \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_/ /_/   \/_____/ ";
echo "                                                                            ";
sleep 1
echo ''
echo 'THE FINAL CHAPTER'
echo ''
sleep 1
rm final_chapter.txt
echo 'Creating final_chapter.txt... '
touch final_chapter.txt

# Check if Docker is installed. If it is not, install it.
echo ''
echo 'Checking for Docker...'
sleep 1
echo ''
docker_check

# create 3 docker containers
echo 'Creating first container...'
sleep 1
create_container GoD1 
echo ''
echo 'Creating second container...'
sleep 1
create_container GoD2
echo ''
echo 'Creating third container...'
sleep 1
create_container GoD3
echo ''

# send text files to the docker containers
echo 'Sending files to the first container...'
sleep 1
SEND Docker1 GoD1 
echo ''
echo 'Sending files to the second container...'
sleep 1
SEND Docker2 GoD2 
echo ''
echo 'Sending files to the third container...'
sleep 1
SEND Docker3 GoD3
echo ''

# send the SORT script to GoD1 and GoD2
echo 'Sending a script to sort files in the first container...'
sleep 1
sudo docker cp GET_BSORT1 GoD1:/tmp
sudo docker exec GoD1 chmod u+x /tmp/GET_BSORT1
echo ''
echo 'Sending a script to sort files in the first container...'
sleep 1
sudo docker cp GET_BSORT2 GoD2:/tmp
sudo docker exec GoD2 chmod u+x /tmp/GET_BSORT2
echo ''
echo 'Sending a script to sort files in the first container...'
sleep 1
sudo docker cp GET_B GoD3:/tmp
sudo docker exec GoD3 chmod u+x /tmp/GET_B
echo ''

# Store the number of files in each container.
# These variables will be used to keep track of the files that are being operated on.
NUM1=$(sudo docker exec GoD1 ls /tmp/Docker1 | wc -l)
NUM2=$(sudo docker exec GoD2 ls /tmp/Docker2 | wc -l)
NUM3=$(sudo docker exec GoD3 ls /tmp/Docker3 | wc -l)

# Calculate the total number of files to be moved and operated on.
# COUNTR will be used keep track of the files that need to be appended to
# final_chapter.txt
COUNTR=$((NUM1+NUM2+NUM3))

echo "Moving $COUNTR files..."
echo ''

# Execute the sort script in GoD1 and GoD2 and import files locally
echo 'Sorting files in the first container...'
sleep 1 
echo ''
sudo docker exec --workdir /tmp GoD1 bash GET_BSORT1
sudo docker exec GoD1 rm /tmp/GET_BSORT1
echo 'Fetching files... '
sleep 1
echo ''
sudo docker cp GoD1:/tmp/renamed1 ./tmp1

echo 'Sorting files in the second container...'
sleep 1 
echo ''
sudo docker exec --workdir /tmp GoD2 bash GET_BSORT2
sudo docker exec GoD2 rm /tmp/GET_BSORT2
echo 'Fetching files... '
sleep 1
echo ''
sudo docker cp GoD2:/tmp/renamed2 ./tmp2

#import files localy GoD3
echo 'Renaming files in the third container...'
sleep 1 
echo ''
sudo docker exec --workdir /tmp GoD3 bash GET_B
sudo docker exec GoD3 rm /tmp/GET_B
echo 'Fetching files... '
sleep 1
echo ''
sudo docker cp GoD3:/tmp/renamed3 ./tmp3

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

################## clean up ###################

# Stop the running containers and remove them.
STOP() {
        sudo docker stop $1
        sudo docker rm $1
}
echo 'Removing first container...'
STOP GoD1
echo 'Removing second container...'
STOP GoD2
echo 'Removing third container...'
STOP GoD3
# Remove temporary directories from the host machine.
echo 'Removing temporary files... '
sudo rm -r ./tmp1
sudo rm -r ./tmp2
sudo rm -r ./tmp3
# Remove the sorting and renaming scripts from the host machine.
rm GET_BSORT1
rm GET_BSORT2
rm GET_B

###############################################

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
echo 'From here you have a few options...'
sleep 1

# Flag to exit the while loop on users request.
FLAG=true

# Create a file to handle modifications to the text.
touch output

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
echo '       [3] - add some text to the end of the chapter.'
echo '       [x] - to terminate the program.'
sleep 1
echo ''
echo 'Enter your choice below:'
read CHOICE
echo ''

# Read the chapter
if [[ $CHOICE -eq 1 ]]
then
cat ./final_chapter.txt
echo ''

# Search and replace or delete text
elif [[ $CHOICE -eq 2 ]]
then
echo 'Ok... You want to find some text in the chapter and then replace it with some new text or just delete it.'
sleep 1
echo ''
echo 'First enter the text you would like to find below:'
echo ''
read OLD
echo ''

# If the user doesnt enter any text ask until they enter some text.
while [[ $(echo $OLD | wc -c) == 1 ]]
do
echo 'You have not entered any text...'
echo ''
echo 'Please enter the text you would like to find.'
read OLD
done

# If the user enters some text store the user input.
if [[ $(echo $OLD | wc -c) -gt 1 ]]
then
echo "Ok, finding all instances of \"$OLD\"."
echo '' 
sleep 1
fi

echo 'Now enter the text you would like to replace it with...'
echo ''
echo 'If you would like to delete your chosen text just press enter...'
echo ''
echo 'or enter "x" to exit.'
echo ''
sleep 1
read NEW

# Check if user has entered any text. If they have not, prompt them to add some text.
if [[ $(echo $NEW | wc -c) == 1 ]]
then
echo "Deleting \"$OLD\""
echo ''
sed "s|$OLD|$NEW|g" ./final_chapter.txt > output
cat output > final_chapter.txt 
sleep 1

# If the user enters x exit. 
elif [[ "$NEW" == "x" ]]
then
echo 'Exiting...'
    
# Replace the old text with the new text.
else 
[[ $(echo $NEW | wc -c) -gt 1 ]]   
echo "Ok... replacing \"$OLD\" with \"$NEW\"."
echo ''
sleep 1 
# sed operation link: https://www.brianchildress.co/using-variables-with-sed/
sed "s|$OLD|$NEW|g" ./final_chapter.txt > output
cat output > final_chapter.txt
echo ''
fi

# Add text to be appended to the end of the text.
elif [[ $CHOICE -eq 3 ]]
then
echo 'Ok... You want to add some text to the end of the chapter...'
echo ''
sleep 1
echo 'Add your text below:'
echo ''
read APPEND

# Check if user has entered any text. If they have not, prompt them to add some text.
while [[ $(echo $APPEND | wc -c) == 1 ]]
do
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

# Exit the loop.
FLAG=false

# Remove this temporary file
rm output

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

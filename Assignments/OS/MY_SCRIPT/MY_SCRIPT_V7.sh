#!/bin/bash

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
echo 'NUMB=$(ls ./Docker1 | wc -l)' >> GET_BSORT1
echo 'echo "$NUMB"' >> GET_BSORT1
echo 'cd Docker1' >> GET_BSORT1
echo 'for i in `seq 1 $NUMB`' >> GET_BSORT1
echo 'do' >> GET_BSORT1
echo 'mv $(find . -type f -exec ls -l {} \; | sort -nr -k5 | tail -n 1 | cut -f11 -d" " | cut -c3-) $i' >> GET_BSORT1
echo 'mv $i /tmp' >> GET_BSORT1
echo 'done' >> GET_BSORT1
echo 'cd ..' >> GET_BSORT1
echo 'rm -r Docker1' >> GET_BSORT1

# Create a script to sort files in GoD2
echo '#!/bin/bash' > GET_BSORT2
echo 'NUMB=$(ls ./Docker2 | wc -l)' >> GET_BSORT2
echo 'echo "$NUMB"' >> GET_BSORT2
echo 'cd Docker2' >> GET_BSORT2
echo 'for i in `seq 1 $NUMB`' >> GET_BSORT2
echo 'do' >> GET_BSORT2
echo 'mv $(find . -type f -exec ls -l {} \; | sort -nr -k5 | tail -n 1 | cut -f11 -d" " | cut -c3-) $i' >> GET_BSORT2
echo 'mv $i /tmp' >> GET_BSORT2
echo 'done' >> GET_BSORT2
echo 'cd ..' >> GET_BSORT2
echo 'rm -r Docker2' >> GET_BSORT2

# Create a script to rename files in GoD3
echo '#!/bin/bash' > GET_B
echo 'NUMB=$(ls ./Docker3 | wc -l)' >> GET_B
echo 'echo "$NUMB"' >> GET_B
echo 'cd Docker3' >> GET_B
echo 'for i in `seq 1 $NUMB`' >> GET_B
echo 'do' >> GET_B
echo 'mv $(ls | head -n 1) $i' >> GET_B
echo 'mv $i /tmp' >> GET_B
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
echo 'Creating final_chapter.txt... '
touch final_chapter.txt


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
echo 'Sorting files in the first container'
sleep 1 
echo ''
sudo docker exec --workdir /tmp GoD1 bash GET_BSORT1
sudo docker exec GoD1 rm /tmp/GET_BSORT1
echo 'Fetching files... '
sleep 1
echo ''
sudo docker cp GoD1:/tmp ./tmp1

echo 'Sorting files in the secod container'
sleep 1 
echo ''
sudo docker exec --workdir /tmp GoD2 bash GET_BSORT2
sudo docker exec GoD2 rm /tmp/GET_BSORT2
echo 'Fetching files... '
sleep 1
echo ''
sudo docker cp GoD2:/tmp ./tmp2

#import files localy GoD3
echo 'Renaming files in the third container'
sleep 1 
echo ''
sudo docker exec --workdir /tmp GoD3 bash GET_B
sudo docker exec GoD3 rm /tmp/GET_B
echo 'Fetching files... '
sleep 1
echo ''
sudo docker cp GoD3:/tmp ./tmp3

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
STOP GoD1
STOP GoD2
STOP GoD3
# Remove temporary directories from the host machine.
sudo rm -r ./tmp1
sudo rm -r ./tmp2
sudo rm -r ./tmp3
# Remove the sorting and renaming scripts from the host machine.
rm GET_BSORT1
rm GET_BSORT2
rm GET_B

###############################################


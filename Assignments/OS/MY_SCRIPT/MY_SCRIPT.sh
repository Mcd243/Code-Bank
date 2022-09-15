#!/bin/bash

# A function to ctreate a container
function create_container() {
sudo docker run --name $1 -t -d ubuntu /bin/bash
}


# A function to find the folders and send the files to the respective containe>
SEND() {
   find ~ -type d -name "$1" -exec sudo docker cp {} $2:/tmp/ \;
   sudo docker exec $2 ls -l /tmp/$1
}

# A funtion to send the sort script to a docker container
SEND_SORT() {
    sudo docker cp SORT $1:/tmp/$2
}


# Create a script for sorting files in a docker container
echo '\#\!/bin/bash' > SORT
echo $'list=$(ls -l | sort -rnk5 | awk \'OFS=\" \" {print$9}\')' >> SORT
echo 'echo $list' >> SORT
chmod u+x SORT

# Create a script to store the names of text files in a list 
echo '\#\!/bin/bash' > LIST
echo $'list=$(ls -l | awk \'OFS=\" \" {print$9}\')' >> LIST
echo 'echo $list' >> LIST
chmod u+x LIST


###################### Main ############################

echo "Welcome to Game of Dockers...\n"
sleep 3
echo "We are going to play a game with some docker containers to cearte a "
echo "new chapter for your book.\n" 
sleep 4
echo "Get ready....."
sleep 3
echo "creating the final chapter text file...\n"
touch final_chapter.txt

sleep 3
# create 3 docker containers
create_container GoD1 
create_container GoD2
create_container GoD3
# send text files to the docker containers
SEND Docker1 GoD1
SEND Docker2 GoD2
SEND Docker3 GoD3
# send the SORT script to GoD1 and GoD2
SEND_SORT GoD1 Docker1
SEND_SORT GoD2 Docker2
# send the LIST script to GoD3
sudo docker cp LIST GoD3:/tmp/Docker3




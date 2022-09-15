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

# A function to find the biggest file in the directory and append it to final_chapter
GET_BIGGEST() {
    if [[ "$(sudo docker exec $1 ls /tmp/$2 | wc -l)" != "0" ]] 
    then
    sudo docker exec $1 cp /tmp/$2/$(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-) /tmp/next 
    sudo docker exec $1 cat /tmp/next >> final_chapter.txt 
    sudo docker exec $1 rm /tmp/next 
    fi
}
###################### Main ############################

echo "Welcome to Game of Dockers..."
sleep 1
echo "We are going to play a game with some docker containers to cearte a "
echo "new chapter for your book." 
sleep 1
echo "Get ready....."
sleep 1
echo "creating the final chapter text file..."
touch final_chapter.txt

sleep 1
# create 3 docker containers
create_container GoD1 
create_container GoD2
create_container GoD3
# send text files to the docker containers
SEND Docker1 GoD1 
SEND Docker2 GoD2 
SEND Docker3 GoD3

# Round Robin appended to final_chapter.txt
GET_BIGGEST GoD1 Docker1
GET_BIGGEST GoD1 Docker1
GET_BIGGEST GoD2 Docker2
GET_BIGGEST GoD2 Docker2
if [[ "$(sudo docker exec GoD3 ls /Docker3 | wc -l)" != "0" ]] 
then
sudo docker exec GoD3 cp /tmp/Docker3/$(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-) /tmp 
sudo docker exec GoD3 cat /tmp/next >> final_chapter.txt 
sudo docker exec GoD3 rm /tmp/next 
fi 






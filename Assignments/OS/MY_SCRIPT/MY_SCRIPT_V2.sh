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
    sudo docker cp SORT$3 $1:/tmp
}

EXEC() {
    sudo docker exec --workdir /tmp GoD$2 bash $1
}

# Create a script for sorting files in container GoD1
echo '#!/bin/bash' > SORT1
echo $'list=$(ls -l /tmp/Docker1 | sort -rnk5 | awk \'OFS=\" \" {print$9}\')' >> SORT1
echo 'echo $list' >> SORT1
echo 'ls -l /tmp/Docker1' >> SORT1
chmod u+x SORT1

# Create a script for sorting files in container GoD1
echo '#!/bin/bash' > SORT2
echo $'list=$(ls -l /tmp/Docker2 | sort -rnk5 | awk \'OFS=\" \" {print$9}\')' >> SORT2
echo 'echo $list' >> SORT2
echo 'ls -l /tmp/Docker2' >> SORT2
chmod u+x SORT2


# Create a script to store the names of text files in a list in container GoD3
echo '#!/bin/bash' > LIST
echo $'list=$(ls -l /tmp/Docker3 | awk \'OFS=\" \" {print$9}\')' >> LIST
echo 'echo $list' >> LIST
echo 'ls -l /tmp/Docker3' >> LIST
chmod u+x LIST


###################### Main ############################

echo "Welcome to Game of Dockers...\\n"
sleep 1
echo "We are going to play a game with some docker containers to cearte a "
echo "new chapter for your book.\\n" 
sleep 1
echo "Get ready....."
sleep 1
echo "creating the final chapter text file...\\n"
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
# send the SORT script to GoD1 and GoD2
SEND_SORT GoD1 Docker1 1
SEND_SORT GoD2 Docker2 2
# send the LIST script to GoD3
sudo docker cp LIST GoD3:/tmp

# Execute the sort script in GoD1 and GoD2
EXEC SORT1 1
EXEC SORT2 2
sudo docker exec --workdir /tmp GoD3 bash LIST





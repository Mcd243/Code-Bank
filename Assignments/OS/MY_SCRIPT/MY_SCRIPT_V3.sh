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

# A function to get text from a container and append it to final_chapter.txt
GET_TXT() {
sudo docker exec --workdir /tmp $1 bash $2
sudo docker exec $1 cat /tmp/next >> final_chapter.txt
sudo docker exec $1 rm /tmp/next
sudo docker exec $1 touch /tmp/next
NUM1=$(( $NUM1 - 1 ))
}

echo '#!/bin/bash' > GET_BSORT1
echo 'NUMB=$(ls ./Docker1 | wc -l)' >> GET_BSORT1
echo 'echo "$NUMB"' >> GET_BSORT1
echo 'if [[ "$NUMB" != "0" ]]' >> GET_BSORT1
echo 'then' >> GET_BSORT1
echo 'cd Docker1' >> GET_BSORT1
echo 'echo "$(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-)"' >> GET_BSORT1
echo 'mv -u $(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-) /tmp/next' >> GET_BSORT1
echo 'fi' >> GET_BSORT1

echo '#!/bin/bash' > GET_BSORT2
echo 'NUMB=$(ls ./Docker2 | wc -l)' >> GET_BSORT2
echo 'echo "$NUMB"' >> GET_BSORT2
echo 'if [[ "$NUMB" != "0" ]]' >> GET_BSORT2
echo 'then' >> GET_BSORT2
echo 'cd Docker2' >> GET_BSORT2
echo 'echo "$(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-)"' >> GET_BSORT2
echo 'mv -u $(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-) /tmp/next' >> GET_BSORT2
echo 'fi' >> GET_BSORT2

echo '#!/bin/bash' > GET_B
echo 'NUMB=$(ls ./Docker3 | wc -l)' >> GET_B
echo 'echo "$NUMB"' >> GET_B
echo 'if [[ "$NUMB" != "0" ]]' >> GET_B
echo 'then' >> GET_B
echo 'cd Docker3' >> GET_B
echo 'echo "$(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-)"' >> GET_B
echo 'mv -u $(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-) /tmp/next' >> GET_B
echo 'fi' >> GET_B

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
# send the SORT script to GoD1 and GoD2

sudo docker cp GET_BSORT1 GoD1:/tmp
sudo docker exec GoD1 chmod u+x /tmp/GET_BSORT1

sudo docker cp GET_BSORT2 GoD2:/tmp
sudo docker exec GoD2 chmod u+x /tmp/GET_BSORT2

sudo docker cp GET_B GoD3:/tmp
sudo docker exec GoD3 chmod u+x /tmp/GET_B

# Execute the sort script in GoD1 and GoD2
sudo docker exec --workdir /tmp GoD1 bash GET_BSORT1
sudo docker exec --workdir /tmp GoD2 bash GET_BSORT2
sudo docker exec --workdir /tmp GoD3 bash GET_B

NUM2=$(sudo docker exec GoD2 ls /tmp/Docker2 | wc -l)
NUM3=$(sudo docker exec GoD3 ls /tmp/Docker3 | wc -l)
NUM1=$(sudo docker exec GoD1 ls /tmp/Docker1 | wc -l)

while [ $NUM1 -gt 0 ] && [ $NUM2 -gt 0 ] && [ $NUM3 -gt 0 ]
do 
GET_TXT GoD1 GET_BSORT1
GET_TXT GoD1 GET_BSORT1

GET_TXT GoD2 GET_BSORT2
GET_TXT GoD2 GET_BSORT2

GET_TXT GoD3 GET_B
GET_TXT GoD3 GET_B

done






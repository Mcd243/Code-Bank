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
sudo docker exec $1 cat /tmp/$2 >> final_chapter.txt
COUNTR=$(($COUNTR-1))
}


echo '#!/bin/bash' > GET_BSORT1
echo 'NUMB=$(ls ./Docker1 | wc -l)' >> GET_BSORT1
echo 'echo "$NUMB"' >> GET_BSORT1
echo 'cd Docker1' >> GET_BSORT1
echo 'for i in `seq 1 $NUMB`' >> GET_BSORT1
echo 'do' >> GET_BSORT1
echo 'mv $(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-) $i' >> GET_BSORT1
echo 'mv $i /tmp' >> GET_BSORT1
echo 'done' >> GET_BSORT1
echo 'cd ..' >> GET_BSORT1
echo 'rm -r Docker1' >> GET_BSORT1

echo '#!/bin/bash' > GET_BSORT2
echo 'NUMB=$(ls ./Docker2 | wc -l)' >> GET_BSORT2
echo 'echo "$NUMB"' >> GET_BSORT2
echo 'cd Docker2' >> GET_BSORT2
echo 'for i in `seq 1 $NUMB`' >> GET_BSORT2
echo 'do' >> GET_BSORT2
echo 'mv $(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-) $i' >> GET_BSORT2
echo 'mv $i /tmp' >> GET_BSORT2
echo 'done' >> GET_BSORT2
echo 'cd ..' >> GET_BSORT2
echo 'rm -r Docker2' >> GET_BSORT2

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

#echo '  ___                                __        ___            _                 '
#echo ' / __| __ _  _ __   ___        ___  / _|      |   \  ___  __ | |__ ___  _ _  ___'
#echo '| (_ |/ _` || '  \ / -_)      / _ \|  _|      | |) |/ _ \/ _|| / // -_)| '_|(_-/'
#echo ' \___|\__/_||_|_|_|\___|      \___/|_|        |___/ \___/\__||_\_\\___||_|  /__/'


echo 'Creating final_chapter.txt '
touch final_chapter.txt


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

#store the number of files to move
NUM1=$(sudo docker exec GoD1 ls /tmp/Docker1 | wc -l)
NUM2=$(sudo docker exec GoD2 ls /tmp/Docker2 | wc -l)
NUM3=$(sudo docker exec GoD3 ls /tmp/Docker3 | wc -l)
COUNTR=$((NUM1+NUM2+NUM3))

echo "Moving $COUNTR files..."

# Execute the sort script in GoD1 and GoD2 and import files locally
sudo docker exec --workdir /tmp GoD1 bash GET_BSORT1
sudo docker exec GoD1 rm /tmp/GET_BSORT1
sudo docker cp GoD1:/tmp ./tmp1

sudo docker exec --workdir /tmp GoD2 bash GET_BSORT2
sudo docker exec GoD2 rm /tmp/GET_BSORT2
sudo docker cp GoD2:/tmp ./tmp2

#import files localy
sudo docker exec --workdir /tmp GoD3 bash GET_B
sudo docker exec GoD3 rm /tmp/GET_B
sudo docker cp GoD3:/tmp ./tmp3

####################### ROUND ROBIN ###########################

FETCH1=1
FETCH2=$(($FETCH1+1))

while [[ $COUNTR -gt 0 ]]
do

# get2 form tmp1
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

# get 2 form tmp2
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

# get 2 form tmp1
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

# update file numbers to fetch
FETCH1=$(($FETCH1+2))
FETCH2=$(($FETCH1+1))

done

################## clean up ###################

# Stop the running containers and remove them
STOP() {
        sudo docker stop $1
        sudo docker rm $1
}
STOP GoD1
STOP GoD2
STOP GoD3
sudo rm -r ./tmp1
sudo rm -r ./tmp2
sudo rm -r ./tmp3

###################################################


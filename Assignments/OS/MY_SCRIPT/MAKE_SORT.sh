#!/bin/bash
# Create a script for sorting files in container GoD1
echo '#!/bin/bash' > SORT1



echo $'list=$(ls -l /tmp/Docker1 | sort -rnk5 | awk \'OFS=\" \" {print$9}\')' >> SORT1



echo 'echo $list' >> SORT1
echo 'echo ${#list[@]}' >> SORT1
echo 'NUMB=0' >> SORT1 
echo 'for i in {1..${#list[@]}}' >> SORT1
echo 'do' >> SORT1
echo 'cp ./Docker1/$i ./Docker1/$NUMB' >> SORT1
echo 'NUMB=$((NUMB+1))' >> SORT1
echo 'done' >> SORT1
echo 'ls -l /tmp/Docker1' >> SORT1
chmod u+x SORT1



#!/bin/bash

FC=$(ls /home/osboxes/Docker2 | wc -l)
echo $FC
ls -l ./Docker2 | sort -rnk5 | awk 'OFS=" " {print$9}' > SF 
echo $SF
files=()
for i in $(seq 1 $FC) 
do
cut -f$i -d" " SF
#files+=$(cut -f$i -d' ' SF)
done
echo $files 

#loop through files
for file in *; do mv $file $(wc -m $file | cut -f1 -d' ') ; done

#find the largest file
find . -type f -exec ls -al {} \; | sort -nr -k5 | head -n 1

find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" "

 find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-


mv $(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" ") /tmp/next



sudo docker cp GoD1:/tmp/Docker1/$(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" ") ./


#this works

sudo docker cp GoD1:/tmp/next ./


##doesnt read the command
GET_BIGGEST() {
    sudo docker exec $1 cp /tmp/$2/$(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-) /tmp/next
    sudo docker exec $1 cat /tmp/next >> final_chapter.txt
    sudo docker exec $1 rm /tmp/next 
}
GET_BIGGEST GoD1 Docker1
GET_BIGGEST GoD2 Docker2

sudo docker exec GoD3 cp /tmp/Docker3/$(find . -type f -exec ls -l {} \; | head -n 1 | cut -f11 -d" " | cut -c3-) /tmp/next
sudo docker exec GoD3 cat /tmp/next >> final_chapter.txt
sudo docker exec GoD3 rm /tmp/next 


if [[ "$(sudo docker exec GoD3 ls /Docker3 | wc -l)" != "0" ]] 
then
sudo docker exec GoD3 cat /tmp/Docker3/$(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-) /tmp 
sudo docker exec GoD3 cat /tmp/next >> final_chapter.txt 
sudo docker exec GoD3 rm /tmp/next 
fi 

NUMB=$(ls /Docker3 | wc -l)
if [[ "$NUMB" != "0" ]]
then
cp ./Docker3/$(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-) ./next
fi


#################################################################################################

echo '#!/bin/bash' > GET_BSORT1
echo 'NUMB=$(ls ./Docker1 | wc -l)' >> GET_BSORT1
echo 'echo "$NUMB"' >> GET_BSORT1
echo 'if [[ "$NUMB" != "0" ]]' >> GET_BSORT1
echo 'then' >> GET_BSORT1
echo 'cd Docker1' >> GET_BSORT1
echo 'echo "$(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-)"' >> GET_BSORT1
echo 'mv -u $(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-) tmp/next' >> GET_BSORT1
echo 'fi' >> GET_BSORT1

echo '#!/bin/bash' > GET_BSORT2
echo 'NUMB=$(ls ./Docker2 | wc -l)' >> GET_BSORT2
echo 'echo "$NUMB"' >> GET_BSORT2
echo 'if [[ "$NUMB" != "0" ]]' >> GET_BSORT2
echo 'then' >> GET_BSORT2
echo 'cd Docker2' >> GET_BSORT2
echo 'echo "$(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-)"' >> GET_BSORT2
echo 'mv -u $(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-) tmp/next' >> GET_BSORT2
echo 'fi' >> GET_BSORT2

echo '#!/bin/bash' > GET_B
echo 'NUMB=$(ls ./Docker3 | wc -l)' >> GET_B
echo 'echo "$NUMB"' >> GET_B
echo 'if [[ "$NUMB" != "0" ]]' >> GET_B
echo 'then' >> GET_B
echo 'cd Docker3' >> GET_B
echo 'echo "$(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-)"' >> GET_B
echo 'mv -u $(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-) tmp/next' >> GET_B
echo 'fi' >> GET_B

##################################################################################################################################
#V5

if [[ "$NUMB" != "0" ]]
then



#!/bin/bash' > GET_BSORT1
NUMB=$(ls ./Docker1 | wc -l)
COUNTR=1
echo "$NUMB"
cd Docker1
for i in (seq 1 $NUMB)
do
mv -u $(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-) tmp/$COUNT
COUNTR=$(($COUNTR + 1))
done

echo '#!/bin/bash' > GET_BSORT1
# get the number of files in the dir
echo 'NUMB=$(ls ./Docker1 | wc -l)' >> GET_BSORT1
#set counter to 1
echo 'COUNTR=1' >> GET_BSORT1
# check counter
echo 'echo "$NUMB"' >> GET_BSORT1
# enter dir
echo 'cd Docker1' >> GET_BSORT1
#for loop in range no of files in dor 
echo 'for i in {1..$NUMB}' >> GET_BSORT1
echo 'do' >> GET_BSORT1
# get the biggest file
echo 'mv -u $(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-) tmp/$COUNT' >> GET_BSORT1
# increment the counter
echo 'COUNTR=$(($COUNTR + 1))' >> GET_BSORT1
echo 'done' >> GET_BSORT1

sudo docker exec GoD1 cat /tmp/GET_BSORT1

########################################################################################################

#!/bin/bash
NUMB=$(ls ./Docker2 | wc -l)
echo "$NUMB"
cd Docker2
for i in `seq 1 $NUMB`
do
mv $(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-) $i
mv $i /home/osboxes
done



# GET_BSORT2
echo '#!/bin/bash' > GET_BSORT2
echo 'NUMB=$(ls ./Docker2 | wc -l)' >> GET_BSORT2
echo 'echo "$NUMB"' >> GET_BSORT2
echo 'cd Docker2' >> GET_BSORT2
echo 'for i in `seq 1 $NUMB`' >> GET_BSORT2
echo 'do' >> GET_BSORT2
echo 'mv $(find . -type f -exec ls -l {} \; | sort -nr -k5 | head -n 1 | cut -f11 -d" " | cut -c3-) $i' >> GET_BSORT2
echo 'mv $i /tmp' >> GET_BSORT2
echo 'done' >> GET_BSORT2




# GET_B
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



sudo docker exec GoD1 ls /tmp
sudo docker exec GoD2 ls /tmp
sudo docker exec GoD3 ls /tmp


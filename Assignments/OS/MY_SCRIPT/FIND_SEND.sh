#!/bin/bash
# A function to find the folders and send the files to the respective containe>
SEND() {
   find ~ -type d -name "$1" -exec sudo docker cp {} $2:/tmp/ \;
   sudo docker exec $2 ls -l /tmp/$1
}
SEND Docker1 GoD1
SEND Docker2 GoD2
SEND Docker3 GoD3

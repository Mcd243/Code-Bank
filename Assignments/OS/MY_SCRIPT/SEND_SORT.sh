#!/bin/bash
# A funtion to send the sort script to a docker container
SEND_SORT() {
    sudo docker cp SORT $1:/tmp/$2
}
SEND_SORT GoD1 Docker1
SEND_SORT GoD2 Docker2
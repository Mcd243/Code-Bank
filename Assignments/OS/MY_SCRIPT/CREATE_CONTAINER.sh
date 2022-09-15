#!/bin/bash
# A function to ctreate a container
function create_container() {
sudo docker run --name $1 -t -d ubuntu /bin/bash
}
create_container GoD1 
create_container GoD2
create_container GoD3

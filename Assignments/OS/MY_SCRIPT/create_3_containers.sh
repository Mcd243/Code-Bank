#!/bin/bash

create_and_copy() {
    # create first docker container and start it
    echo "Creating GoD1 docker container..."
    sleep 4
    sudo docker run --name GoD1 ubuntu /bin/bash
    sudo docker start GoD1
    # copy Docker1 to the GoD1 container
    echo "Copying Docker1 to GoD1..."
    sleep 4
    sudo docker cp Docker1 GoD1:/tmp/Docker1
    echo "Docker1 has been copied to the GoD1 container..."
    sudo docker exec GoD1 ls -l /tmp
    sleep 4

    # create the second docker container and start it
    echo "Creating GoD2 docker container..."
    sleep 4
    sudo docker run --name GoD2 ubuntu /bin/bash
    sudo docker start GoD2
    # copy Docker2 to the GoD2 container
    echo "Copying Docker1 to GoD2..."
    sleep 4
    sudo docker cp Docker2 GoD2:/tmp/Docker2
    echo "Docker2 has been copied to the GoD2 container..."
    sudo docker exec GoD2 ls -l /tmp
    sleep 4

    # create the third docker container and start it
    echo "Creating GoD3 docker container..."
    sleep 4
    sudo docker run --name GoD3 ubuntu /bin/bash
    sudo docker start GoD3
    # copy Docker3 to the GoD3 container
    echo "Copying Docker3 to GoD3..."
    sleep 4
    sudo docker cp Docker3 GoD3:/tmp/Docker3
    echo "Docker3 has been copied to the GoD3 container..."
    sudo docker exec GoD3 ls -l /tmp
} 

create_and_copy

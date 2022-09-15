#!/bin/sh
docker_check(){
docker -v
if [ $? -ne 128 ] ; then
        echo "Docker is installed on your machine. Lets create some containers..."
        sleep 4
else
        echo "Docker is not installed on your machine. Let us install it...."

        sudo apt-get install apt-transport-https ca certificates curl software-properties-common

        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

        sudo apt-get update

        sudo apt install docker.io

        sudo docker info
fi
}

docker_check

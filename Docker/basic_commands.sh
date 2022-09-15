# Create a new Docker image from the changes made in a Container
Docker Container commit

# Copy files between a local filesystem and Docker container
Docker Container cp

# Remove all stopped containers
Docker Container prune

# Termoinate one or more running Conrtainers
Docker Container kill

# Run a new command in a running Container
Docker Container exec

# List Docker Containers
Docker Container ls

# Remove one or more Containers
Docker Container rm

# Restart one or more Containers
Docker Container Restart

###############################################################

# look at docker images
sudo docker images

# look at docker containers that are live
sudo docker ps

# lookup all docker container that are running or have run on the machine
sudo docker ps -a

# create a container by running an image
# -d is in a detatched mode 
# -p is the port
sudo docker run -d -p0.0.0.0:80:80 ubuntu:latest

# get the alpine image and run it as a container
sudo docker run alpine:1.0

# get the alpine image and store it in the repository
sudo docker pull Alpine

# create a ubuntu docker container and name it mydockername 
sudo docker run -it --name mydockername ununtu /bin/bash

# start the new docker container 
sudo docker start mydockername
sudo docker start docker_id

# rename a container
sudo docker rename mycontainername mynewcontainername

# stop a container
sudo docker stop mydocker
sudo docker stop docker_id

# remove a container 
sudo docker rm mydocker 

# stop a active running container 
sudo docker kill mydocker

################################################################

# binding host port to container port
docker run -p6000:6379

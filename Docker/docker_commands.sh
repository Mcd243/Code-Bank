######################## Install docker ###########################

### adding packages ###

sudo apt-get install apt-transport-https ca certificates curl software-properties-common

### Add docker gpg key ###

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

### update APT sources

sudo apt-get update


### install docker packages on Ubuntu ###

sudo apt install docker.io


### get docker info ###

sudo docker info
 



###################### CONTAINERS ###############################

### download the alpine docker image ###

sudo docker pull alpine



######## enter your chosen container ###########

>>>sudo docker run -i -t alpine /bin/sh

# to exit
#exit


### run an ubuntu container ###

>>>sudo docker run -it ubuntu /bin/sh



### run the docker container with a user friendly name ###

>>>sudo docker run --name container_name -it ubuntu /bin/sh


### check it is renamed ###

>>>sudo docker ps


### run the container without an interactive shell ###

>>>sudo docker start container_name


### confirm it is running ###

>>>sudo docker ps


### stop the container running ###

>>>sudo docker stop  container_name 


### see all running containers ###

>>>sudo docker ps


### see all running containers that were created ###

>>>sudo docker ps -a


### view the resourse stats for the container that is running ###

>>>sudo docker stats
^C to exit


### view what images have been downloaded locally ###

>>>sudo docker images


### create an Nginx web server container and run it ###

sudo docker run -d -p 80:80 nginx


### list  running docker container ###

>>>sudo docker container ls


### go to web browser and type localhost ###


### create a simple html file with a <h1> ##

echo "<h1>Containerize all the things</h1>">>index.html


### send the file into the running container ###

sudo docker cp index.html pedantic_gauss:/usr/share/nginx/html/index.html


### copy docker config file to the host machine in the current directory ###

sudo docker cp sharp_bhabha:/etc/nginx/nginx.conf ./

### enter a container
docker exec -it container_ID_or_name /bin/bash


##########################################################################
#remove docker 
sudo apt-get purge docker.io


docker exec --workdir /tmp container-name pwd

docker exec --workdir /tmp container-name pwd


docker exec mycontainer /path/to/test.sh

docker exec mycontainer /bin/sh -c "cmd1;cmd2;...;cmdn"


docker exec --workdir /tmp/Docker2 GoD2 RUN [SORT]


docker run -it --rm -v $(pwd):/src ubuntu /src/SORT

sudo docker exec --workdir /tmp/Docker2 GoD2 bash SORT

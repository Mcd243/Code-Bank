##### Create a working directory and docker file ###

mkdir Dockerfile

cd Dockerfile

touch Dockerfile


### Define the base image with FROM ###


## open in text editor ###

nano Dockerfile

FROM alpine:3.4

RUN apk update
RUN apk add vim
RUN apk add curl

^O - to save
^X - to exit

### build the docker image from the dockerfile                               ####
### -t defines the tag or name                                               ###
### osboxes/alpine-smarter:1.0 this is the name and the version of the image ###
### . look here for the dockerfile                                           ###

>>>sudo docker build -t osboxes/alpine-smarter:1.0 .

### run the container ###

sudo docker run --rm -it osboxes/alpine-smarter:1.0 /bin/sh


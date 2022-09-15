##################### PROCESSES #############################
# process - an istance of a running programme


foreground process
# suspends the prompt
# output directly to the user via screen
# keyboard input
ls test*.txt

backgound process &
# excecutes in the background
# if needing keyboard input process stops and propmts 
# user to bring it into the foreground for keyboard input
# [job number] PID

################### list running processes #####################

ps
# process status

ps -f 
# more detail

-a 
# info about all users

-x
# shows info about processes without terminals

-u
# shows more detail... like -f

-e
# shows extended info


################# understanding the output #####################

UID
# User ID that process belongs to

PID
# Process ID

PPID
# Parent process id (process that initiated the current process)

C
# cpu utilisation

STIME
# process start time

TTY
# terminal type

TIME
# cpu time taken

CMD
# command that started the process

##############################################################

########## stop a process ##################

CTRL + C

kill 12236
# uses PID

kill -9 12236
# super kill (force kill)

#############################################################
############# PARENT and CHILD ################
# PPID / PID

# each process has PID and PPID

# most processes have the shell as the parent

############ ZOMBIES #########################
# Z state

# parent is killed
# orphaned process becomes the Zombie

orphan processes # parent dead but still running

zombie process   # parent dead, completed running but still visible as
# a ps


#############  Deamon Processes #############
# system related background processes wth root permissions

terminal type is - ?

# runs in the background waiting for something to happen

# you can make background processes into Daemons



############## TOP Command ####################
# show processes
# interactive frequently updated state of processes

top


############### JOB id #######################

# background or suspended processes
# manipulated with a job number

# job can consist of multiple processes ( groups processes )








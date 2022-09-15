##########################################################
# Output redirection

# redirects the output to the users file insted of stdout
# > overwrites the existing content
who >users

# >> appends to a file


##########################################################
# Input Redirection

# this uses the wordcount wc with -l lines
# it counts the lines in a file

wc -l <users
#1


###########################################################
# Here document

# Redirects input into an interactive shell
# Can run an interactive program within a shell script 
# without user action by supplying the input

command << delimiter
document
delimiter

# reads untill it finds the delimiter and sends to stdinput of 
# the command

# delimiter completes the here document, without it the it will 
# run forever

#!/bin/bash
$wc -l << EOF
    This is a simple lookup program
    for good coffee places
    in Edinburgh
EOF
3
# 3 lines

#!/bin/bash
cat << EOF
    This is a simple lookup program
    for good coffee places
    in Edinburgh
EOF
#    This is a simple lookup program
#    for good coffee places
#   in Edinburgh


##############################################################
# Discarding commands

command > /dev/null

# discard output and error messages

command > /dev/null 2>&1

# 2 is STDERR

# 1 is STDOUT

# display a message to DTDERR
echo message 1>&2



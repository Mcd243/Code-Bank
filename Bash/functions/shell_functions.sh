###################################################################
#################### SHELL FUNCTIONS #############################

FUNCTION_NAME() {
    list of commands
}


#################################################################

#!/bin/bash
#Define your function here
Hello() {
    echo "Hello world"
}
# onvoke your function
Hello

#################################################################
# Pass some perameters $1 $2 $3 etc

#!/bin/bash
# Define your function here
Hello() {
    echo "Hello world $1 $2"
}
# Invoke your function
Hello MrOne MrTwo

##################################################################
# Returning values

#!/bin/bash
# Define your function here
Hello() {
    echo "Hello world $1 $2"
    return 10
}
# Invoke your function
Hello MrOne MrTwo
# Capture the value returned from the last command
ret=$?
echo "Return value is $ret"

##################################################################
# Nested Functions

#!bin/bash
# Calling one function from another 
number_one() {
    echo "This is the first function speaking..."
    number_two
}
number_two() {
    echo "This is the second function running...."
}
# Calling function one
number_one

# This is the first function speaking...
# This is the second function running....

################ looking at arguments ########################

$0
# the filename

$1
# the first argument

$2 
# the second argument

$3
# the third argument

etc

# these are variables and can be called of printend with echo
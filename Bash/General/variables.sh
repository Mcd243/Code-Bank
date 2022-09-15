### GOOD NAMES ###

_NICK
TOKEN_A
VAR_1
VAR_2

### BAD NAMES ###

2_VAR
-VARIABLE
VAR1-VAR_2
VAR_A!

### DEFINE A VARIABLE ###

# SCALAR VARIABLES ONLY HOLD 1 VALUE AT A TIME
NAME="Nick"
VAR=123


### ACCESSING VARIABLES $ ###

#!/bin/bash
PERSON_NAME="Nick"
echo $PERSON_NAME

# Nick


### READ ONLY VARIABLES ###

# can only read this variable, can't change it

#!/bin/bash
PERSON_NAME="Nick"
readonly PERSON_NAME


### UNSETTING VARIABLES ###

# unset a defined variable

NAME="Nick"
unset NAME
echo $NAME

# its empty fool




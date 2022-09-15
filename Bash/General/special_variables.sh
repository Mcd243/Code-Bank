# retieve the value of PID
echo $$

# filename of the current script
$0

# nth position of an argument with which the script was invoked
$n

# numer af args supplied with the script. 
$#

# all args. Takes entire argument as 1 list.
$*

# all args if individually double quated. Separates arguments.
$@

# exit status of last command (0 if sucessfu 1 if error)
$?

# current shell PID
$$

# PID of last command
$!

### COMAND LINE ARGS ###

#!/bin/bash
echo "File Name: $0"
echo "First Parameter: $1"
echo "Second Parameter: $2"
echo "Quated Values: $@"
echo "Quoted Values: $*"
echo "Total Number of Parameters: $#"

# for each arg in the script it prints
#!/bin/bash
for TOKEN in $*
do
    echo $TOKEN
done
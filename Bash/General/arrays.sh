### DEFINING ARRAYS ###

array_name[index]=value

#initialise an empty array
declare -a LIST=()
declare –a arr1

# prints the number of values in the array from #
printf ${#arr1[@]}

# add items to the array using indexing
#!/bin/bash
NAME[0]="Nick"
NAME[1]="George"
NAME[2]="Sam"
NAME[3]="Adrien"
NAME[4]="Peter"

# append an item to an array
array=()
array+=("first")
echo ${array[@]}

### ACCESSING ARRAY VALUES ###

${array_name[index]}

#!/bin/bash
NAME[0]="Nick"
NAME[1]="George"
NAME[2]="Sam"
NAME[3]="Adrien"
NAME[4]="Peter"

echo "First Index: ${NAME[0]}"
echo "Second Index: ${NAME[1]}"

# First Index: Nick
# Second Index: George

${array_name[*]}  # get all values in array

${array_name[@]}  # get all values in array
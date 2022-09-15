a = "abc"
b = "efg"

### = equal ###
[ $a = $b ]
# false

### != not equal ###
[ $a != $b ]
# true

### -z is zero (empty) ###
[ -z $a ]
# false

### -n is not zero (not empty) ###
[ -n $a ]
# true

### str checks if there is a string ###
[ $a ]
# true
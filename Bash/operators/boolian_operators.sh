

### ! NOT ###
[ ! false ]
# true

### -o OR ###
[ $a -lt 20 -o $b -gt 100 ]
# true OR false = true
# false OR false = false
# true OR true = true

### -a AND ###
[ $a -lt 20 -a $b -gt 100 ]
# true AND false = false
# false AND false = false
# true AND true = true
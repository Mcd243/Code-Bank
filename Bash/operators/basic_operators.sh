### expr ##

#!/bin/bash
val=`expr 2 + 2`
echo "Total value : $val"

# 4

### + addition ###
`expr $a + $b`

### - subtraction ###
`expr $a - $b`

### * multiplication ###
`expr $a \* $b`

### / division ###
`expr $a / $b`

### % modulus ###
`expr $a % $b`

### = assignment ###
a = $b ????????????
### == equality ###
[ $a == $b]
# retuns false

### != not equality ###
[ $a != $b ]


file = test.sh (100 bytes)

-b
### is a block special file ###
[ -b $file ]
# false

-c
### is a character special file ###
[ -c $file ]
# false

-d
### is a directory ###
[ -d $file ]
# false

-f
### is an ordinary file ###
[ -f $file ]
# true

-g
### is the set group id (SGID) set ###
[ -g $file ]
# false

-k
### is sticky bit set ###
[ -k $file ]
# false

-p
### is a named pipe ###
[ -p $file ]
# false

-t
### is file descriptor open and associated with terminal ###
[ -t $file ]
# false

-u
### is set user id (SUID) set ###
[ -u $file ]
# false

-r
### is readable ###
[ -r $file ]
# true

-w
### is writable ###
[ -w $file ]
# true

-x
### is executable ###
[ -x $file ]
# true

-s
### has a size greater than 0 ###
[ -s $file ]
# true

-e
### does file exist ###
[ -e $file ]
# true
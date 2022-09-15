######################################################################
# Redirection Commands

pgm > file
# program output to file

pgm < file
# program reads input from file

pgm >> file
# Output appended to file

n > file
# output from stream to file

n >> file
# output from stream appended to file

n >& m
# merges output stream n with m

n <& m 
# merges input stream from m with n

|
# pipe

<<tag
# Standard input comes from here through next tag  at the start of line


0 
STDIN

1
STDOUT

2
STDERR
#########################################################################
############################ GREP #######################################

grep pattern file(s)

-v 
# print lines that do not match pattern

-n
# print matched line and line number

-l
# prints names of files with matching lines

-c 
# prints the amnt of matching lines

-i 
# matches either upper case or lower case

#################### line based pattern matching ######################

grep "string with spaces" file_name
# returns string and number of lines present

grep string file_name

grep -v
# only values not containing a strings

grep "^s" testfile
# ^ start of line, so charactor s at start of line

grep "2$" testfile
# $ end of the line







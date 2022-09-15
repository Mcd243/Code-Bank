######################### CUT #################################
# Cuts a charactors vertically in a file line by line

cut -c8 mydatatable.txt
# -c a particular charactor position in this case 8

cut -c8-15 mydatatable.txt
# cut in range charactor 8 to 15

cat testfile | cut -f2 -d","
# -f field or column. <TAB> is default delimiter
# show column 2 with delimiter ","

echo "/root/mydocs/mylogfile.mp3" | cut -f2 -d.


##################### CUT ###################

#cut 2cd charactor on each line
cut -c2 test.txt

#cuts charactors 1 to 3 on each line
cut -c1-3 test.txt

#cuts 3 till end of each line
cut -c3- test.txt

# cuts all characters up till 8 on each line
cut -c-8 test.txt

#cuts entire line
cut -c- 

# cuts fields 1 and 6 with ":" delimiter
grep "bin/bash" /etc/passwd | cut -d':' -f1,6

# if delimiter not there displays whole line
grep "bin/bash" /etc/passwd | cut -d'|' -f1,6

# -s only disply a line if delimiter condition met
grep "bin/bash" /etc/passwd | cut -d'|' -s -f1,6

# --complement means except field 7
grep "bin/bash" /etc/passwd | cut -d':' --complement -s -f7

# --output-delimiter change the output delimiter \n whill print each
# on a new line
grep "bin/bash" /etc/passwd | cut -d':' -s -f1,6,7 --output-delimiter=$'\n'

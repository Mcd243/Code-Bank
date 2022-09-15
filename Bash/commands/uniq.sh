####################### UNIQ #######################
# eliminate repetetive output


cat testfile | cut -f2 -d"," | uniq

##################### Uniq ######################

# remove all duplicate lines
uniq 

# -c count
uniq -c test

# rint only duplicates
uniq -d test

# displays duplicate lines only once
uniq -D test

# displays only unique lines
uniq -u test

# -c count -w with first 8
uniq -c -w 8 test2

# checks first 8 chars and prints only duplicates
uniq -D -w 8 test2

# -s skips comparing first 2 chars displays duplicates
uniq -D -s 2 test3

#  -f skips first 2 fields and displays duplicates
uniq -D -f 2 test


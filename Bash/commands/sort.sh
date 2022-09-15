##################### SORT ########################

-n
# Sorts numerically

-r
# reverse order sort

-f
# sorts upper and lower together

+x
# ignores first x fields when sorting (i think x is a number)]

ls | sort
# ls piped to sort the output alphabetically by default

ls | sort -r
# ls piped to sort the output alphabetically in reverse by default

ls | sort -n 
# ls piped to sort the output numerically

### COLUMNS -k ###

ls datatable | sort -k3
# sort the 3rd table. Default delimiter is whitespace. First column is 1

ls datatable | sort -k3 -t:
# sort the 3rd table. Delimiter is set as ":"


########################## Sort ##########################

# alphabetical sort
sort sorting.txt

# sort output redirection
sort sorting.txt > sorted.txt

# -r reverse sort
sort -r sorting.txt


sort -r sorting.txt > reversorted.txt

# -n numerical -k kolumn
sort -nk2 lsl.txt


sort -k9 lsl.txt

# pipe output to sort
ls -l /home/osboxes | sort -nk5

# remove duplicates
sort -u sorting.txt

# merge and remove duplicates
sort -u lsl.txt lsla.txt

# -t sort by time -n numerical sort on column 2 and 5
# column 9
ls -l /home/$osboxes | sort -t "," -nk2,5 -k9
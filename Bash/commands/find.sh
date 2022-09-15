################################# FIND #################################
# find files or directories


find . -name foobar.txt 
# look in current directory . of filename foobar.txt

find ~/public_html -name "*.html"
# find all html files in the public_html directory

find ~ -type f -mtime -7
# find files (-type f) in the home dir (~) that were modified in the last
# 7 days (-mtime -7)

find / -type f -mtime +31 -size +100000c
# search from root (/) all files bigger than 100000 characters/bytes(c)
# last modified more than (+) 31 days ago.


#########################################################################

-atime (n days)
# days since last accessed

-ctime (n days)
# days since created

-mtime (n days)
# days since last modifies

-newer filename
# file modified more recently than filename

-perm 755
# file permissions 755

-size (n size)b(bytes)or k(kilobytes)
# find files of n size

-type f (file)or d (directory)
# find files or directories

-user username
# find files owned by user.username

#########################################################################
####################### -exec #########################
# execute a command on found files

find / -size +500k -mtime +365 -exec rm {} \;
# find files bigger than 500 kilobytes and more than 1 year old and remove
# the bastards.
# {} found files
# terminated with \; (\ is the escape charactor)

find ~/public_html -name "*.html" -type f -perm 700 -exec chmod 744 {} \;
# find html files in the public_html directory 
# with permission 700 
# change permissions to 744 

################### Find ####################

# find anything matching name
find -name "MyCProgram.c"

# ignore case
find -iname "MyCProgram.c"

# look from root
sudo find / -name passwd

# look as far as one dir from root
sudo find /-maxdepth 2 -name passwd

# look from root to 3
sudo find / -mindepth 2 -maxdepth 3 -name passwd

# look from root between 2 and 4
sudo find / -mindepth 3 -maxdepth 5 -name passwd

# execute md5 algorithm on found file
find -iname "MyCProgram.c" -exec md5sum {} \;

# find files withour string maxdepth1 is current dir
find -maxdepth 1 -not -iname "MyCProgram.c" 

# view files and i-node numbers
ls -i1

# view inode for hidden files
ls -i1 test*

# find i-node execute rename to newname of found file
find -inum 7083112 -exec mv {} new-test-file-name \;

# -perm is permission files with (with permission 040)
find . -perm 040 -type f -exec ls -l {} \;

# group = read
find . -perm g=r -type f -exec ls -l {} \;

# find empty files (lock files and place holders)
find ~ -empty

# find empty files in this dir
find . -maxdepth 1 -empty

# find not hidden files in this directory
find . -maxdepth 1 -empty -not -name ".*"

# find files / execute ls -s (?) / top 5 biggest files
find . -type f -exec ls -s {} \; | sort -n -r | head -5

# find 5 smallest
find . -type f -exec ls -s {} \; | sort -n | head -5

# find not files top 5 smallest
find . -not -type f -exec ls -s {} \; | sort -n | head -5

# directory
find . -type d

# file
find . -type f

# hidden files
find . -type f -name ".*"

# hodden directories
find . -type d -name ".*"

# -l long -r reverse -t by time
ls -lrt
# same as above
find -newer file_name

# ~ user dir I think. Find files bigger than 100MB
find ~ -size +100M

# less than 100MB
find ~ -size -100M

# same as 100MB
find ~ -size 100M
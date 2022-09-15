#################### OS ##########################

import os

# GET CURRENT WORKING DIRECTORY
os.getcwd()


# LIST FILES IN CURRENT WORKING DIRECTORY
os.listdir()


# CHANGE DIR
# note the escape \
os.chdir("C:\\temp")

# using a raw string
os.chdir(r"C:\temp")

# platform current dir
os.curdir
# '.'

# platform separator
os.sep
# '\\'

# platform linestep
os.linesep
# '\r\n'

# platform file system name
os.name
# 'nt'

############### The os.path sub-module ###############

# joins all files in the current dir with the relative
# path of the current dir 
# os.listdir()
# os.path.curdir
# os.path.join()
import os

files = os.listdir()
for fname in files:
    path = os.path.join(os.path.curdir, fname)
    print(path)

#.\.ipynb_checkpoints
#.\client.py
#.\common.txt
#.\Lab4.ipynb
#.\Lab4_sockets.ipynb
#.\modules.txt
#.\outfile.txt
#.\quiz.py
#.\quiz_lab04.py
#.\server.py
#.\__pycache__

# prints files in the current dir with absolute paths
# os.listdir()
# os.path.curdir
# os.path.join()
# os.path.absolutepath()
import os

files = os.listdir()
for fname in files:
    path = os.path.join(os.path.curdir, fname)
    print(os.path.abspath(path))

# does a dir exist
os.path.exists(r"C:\temp")

# does current dir exist
os.path.exists(os.curdir)

# is it a file or a dir
os.path.isfile(os.curdir)
os.path.isdir(os.curdir)

############## Joining and Splitting Paths ################
#################### os.path.split() ######################

import os.path
path1 = r"c:\temp\common.txt"
print(os.path.dirname(path1))
print(os.path.basename(path1))
print(os.path.split(path1))
print(os.path.splitext(path1))

#c:\temp
#common.txt
#('c:\\temp', 'common.txt')
#('c:\\temp\\common', '.txt')

import os.path
path1 = r"C:\temp\common.txt"
path1.split(os.path.sep)
# ['C:', 'temp', 'common.txt']

#########################################################

import os

files = os.listdir()
for fname in files:
    print(os.path.abspath(fname))
# use len() to count how many files and directories
print(f"\t{len(files)} Files and Directories")

#######################################################

# copy and paste code from enhancement 16.1 here 
# then add code for enhancement 16.2
import os

files = os.listdir()
for fname in files:
    if os.path.isdir(fname):
        print(f" d {os.path.abspath(fname)}")
    else:
        print(f" - {os.path.abspath(fname)}")
# use len() to count how many files and directories
print(f"\t{len(files)} Files and Directories")

######################################################

# copy and paste code from enhancement 16.2 here 
# then add code for enhancement 16.3
import os
import datetime

files = os.listdir()
for fname in files:
    # get the type
    if os.path.isdir(fname):
        typ = "d"
    else:
        typ = "-"
    # gets the size of the file/directory
    size = os.path.getsize(fname)
    # creates a variable for the timestamp on file/directory
    timestamp = os.path.getctime(fname)
    # converts the timestamp into a human readble form
    # we only want seconds, so only use the integer part
    time = datetime.datetime.fromtimestamp(int(timestamp))
    # now we can print
    print(f"{typ} {size:8d} {time} {os.path.abspath(fname)}")

# use len() to count how many files and directories
print(f"\t{len(files)} Files and Directories")


########################################################
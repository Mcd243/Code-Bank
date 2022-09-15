# open the text file and read the contents to passwords

passwords = open("common.txt", "r")

type(passwords)
# <class'_io.TextIOWrapper'>

help(open)

#open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#    Open file and return a stream.  Raise OSError upon failure.

#========= ===============================================================
#    Character Meaning
#    --------- ---------------------------------------------------------------
#    'r'       open for reading (default)
#    'w'       open for writing, truncating the file first
#    'x'       create a new file and open it for writing
#    'a'       open for writing, appending to the end of the file if it exists
#    'b'       binary mode
#    't'       text mode (default)
#    '+'       open a disk file for updating (reading and writing)
#    'U'       universal newline mode (deprecated)
#    ========= ===============================================================

########### Reading a file stream - Iteration of Lines of File ##################

# read and print one line
print(passwords.readline())
# read and print the next line
print(passwords.readline())

for each_line in passwords:
    print(each_line)


# You can use the .tell() method to tell the pointer's current position in the file stream #

passwords.tell()

# seek(0) takes a byte offset as an argument, by putting 0 we get back to the beginning of the file.

passwords.seek(0)

# When you are done with the file stream, you should close it to free up resources, 
# and make the file available to other processes.

passwords.close()

############################## encoding ############################################
# alternatives to UTF-8

open("rockyou.txt", encoding="cp437") 
open("rockyou.txt", encoding="latin-1")

############################## using "with open" ###################################
# closes the file automatically

with open("common.txt", "r") as passwords:
    for each_line in passwords:
        print(each_line, end="")
# close() is now done automatically after the with: block ends



############### now split the items in the file up using .split() ##################

with open("common.txt") as passwords:
    for line in passwords:
        (passwd, variant) = line.split(", ")
        print(f"Password: {passwd}, Variant: {variant}")

# maxsplit=1 added
with open("common.txt") as passwords:
    for line in passwords:
        (passwd, variant) = line.split(", ", maxsplit=1)
        print(f"Password: {passwd}, Variant: {variant}")


#################### catching a file exception ################
# read txt file and isert individual items into a list
# open() 
# sys.stderr
# str.strip()
# str.split() 
import sys

passwds = []
my_file = "common.txt"
# if file does not open catch the exception
try:
    #open file with read permissions
    with open(my_file, "r") as passwords:
        for line in passwords:
            try:
                # appent each file item to the list strip spaces and new lines and split at the ", " 
                passwds.append(line.strip.split(", "))
            except Exception as err:
                print(f"Exception({err.__class__.__name__}): {err}", file=sys.stderr)
    print(f"{passwds=}")
except FileNotFoundError:
    print(f"Cannot open or find {my_file}", file=sys.stderr)

    import sys


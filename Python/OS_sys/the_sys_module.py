########################### SYS #########################


# open a text file and write the sys modules to the file
import sys

with open("modules.txt", "w") as f:
    f.write(str(sys.modules))


####################### sys.argv ##########################
# pass info (arguments) to a script at runtime
#Python stores these arguments in the sys.argv object.

# In jupterLabs
%run

!python

##########################################################
################### sys.argv script ######################

""" Manipulate Script Arguments - explore sys.argv
    Author: Petra L
    Modified: Oct 2021
    PEP8/pylint compliant
"""
import sys


def show_argv():
    """returns the arguments"""
    return sys.argv


def main():
    """calls show_argv() and handles printing"""
    args = show_argv()
    print("sys.argv is:")
    print(args)


# Standard boilerplate code to call main()
# to begin the program if run as a script.
if __name__ == "__main__":
    main()

###########################################################

!python args.py

#sys.argv is:
#['args.py']

!python args.py hello world

#sys.argv is:
['args.py', 'hello', 'world']

#sys.argv is a list.
#The first element is always the script/module name.
#The additional elements are the arguments passed in by the user.

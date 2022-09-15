######################## checking arguments ##########################



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
    """calls show_argv() and handles printing 
    In the file args.py, add some code to main(), 
    between lines 16 and 17, to check if the user has input any arguments. 
    If not, print a usage message, such as:
    Usage: python args.py argument1 [argument2] [argument3] ...
    Hint: use len() to check how may items are in sys.argv.
    """
    
    #iterate over the list
    #use f-strings to format the output
    #use .index() to get the "number".

    if len(sys.argv) < 2:
        print("Usage: python args.py argument1 [argument2] [argument3] ...")
        print("please rovide some arguments")
        sys.exit(1)
    args = show_argv()
    print("sys.argv is:")
    for i in args:
        if args.index(i) > 0:
            print(f"arg {args.index(i)}: {i}")


# Standard boilerplate code to call main()
# to begin the program if run as a script.
if __name__ == "__main__":
    main()

########################################################################

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

#####################################################################


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
    if len(args) == 1:
        print("Usage: python args.py argument1 [argument2] [argument3] ...")
    else:
        print("sys.argv is:")
        for arg in args[1:]:
            print(f"arg {args.index(arg)}: {arg}")


# Standard boilerplate code to call main()
# to begin the program if run as a script.
if __name__ == "__main__":
    main()


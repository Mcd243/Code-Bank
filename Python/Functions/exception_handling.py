

# Code wrapped in try/except blocks
# using sys.stderr for output
import sys

try:
    reply1 = input("Please enter a number: ")
    reply2 = input("Please enter a 2nd number: ")
    total = float(reply1) + float(reply2)
    print(f"Sum = {total}")
except ValueError:
    print("Please supply numbers", file=sys.stderr)


##########################################################################

    #Change this copy of the code so that it solves challenge A
import sys

reply1 = input("Please enter a number: ")
reply2 = input("Please enter a 2nd number: ")
try:
    reply1 = float(reply1)
    try:
        reply2 = float(reply2)
        # if we get here, both are floats
        total = reply1 + reply2
        print(f"Sum = {total}")
    except ValueError:
        # this means that reply1 was a float but reply2 was not
        print("Please supply either two numbers or two strings", file=sys.stderr)
except ValueError:
    # this means that reply1 was not a float
    try:
        reply2 = float(reply2)
        # if we get here, reply2 is a float
        print("Please supply either two numbers or two strings", file=sys.stderr)
    except ValueError:
        # if we get here, reply2 is not a float, so both are strings
        total = reply1 + reply2
        print(f"Sum = {total}")


########################################################################


# copy your solution from A, then modify
import sys

correct_input = False

while not correct_input:
    reply1 = input("Please enter a number: ")
    reply2 = input("Please enter a 2nd number: ")

    try:
        reply1 = float(reply1)
        try:
            reply2 = float(reply2)
            # if we get here, both are floats
            total = reply1 + reply2
            print(f"Sum = {total}")
            correct_input = True
        except ValueError:
            # this means that reply1 was a float but reply2 was not
            print("Please supply either two numbers or two strings", file=sys.stderr)
    except ValueError:
        # this means that reply1 was not a float
        try:
            reply2 = float(reply2)
            # if we get here, reply2 is a float
            print("Please supply either two numbers or two strings", file=sys.stderr)
        except ValueError:
            # if we get here, reply2 is not a float, so both are strings
            total = reply1 + reply2
            print(f"Sum = {total}")
            correct_input = True

###################################################################


with open("common.txt") as passwords:
    for line in passwords:
        try:
            (passwd, variant) = line.split(", ")
            print(f"Password: {passwd}, Variant(s): {variant}")
        except Exception as err:
            print("Line does not conform to expected format")

##################################################################

# This stopped the crash and the Traceback, but the line that causes the problem is not printed.
# We can fix this by adding another print statement in the except: block.
# Also, it may be useful to print the details of the Exception.


import sys

with open("common.txt") as passwords:
    for line in passwords:
        try:
            (passwd, variant) = line.split(", ")
            print(f"Password: {passwd}, Variant(s): {variant}")
        except Exception as err:
            print(f"{line=}", file=sys.stderr)
            print("Line does not conform to expected format", file=sys.stderr)
            print(f"Exception ({err.__class__.__name__}): {err}", file=sys.stderr)


#####################################################################

import sys

with open("common.txt") as passwords:
    for line in passwords:
        try:
            (passwd, variant) = line.split(", ")
            print(f"Password: {passwd}, Variant(s): {variant}")
        except ValueError:
            print(f"{line=}", file=sys.stderr)
            print("Line does not conform to expected format", file=sys.stderr)
        except Exception as err:
            print(f"Exception ({err.__class__.__name__}): {err}", file=sys.stderr)

#########################################################################


# Copy of the above code
# Task: add code to handle FileNotFoundError
import sys

my_file = "common.txt"
try:
    with open(my_file) as passwords:
        for line in passwords:
            try:
                (passwd, variant) = line.split(", ")
                print(f"Password: {passwd}, Variant(s): {variant}")
            except ValueError:
                print(f"{line=}", file=sys.stderr)
                print("Line does not conform to expected format", file=sys.stderr)
            except Exception as err:
                print(f"Exception({err.__class__.__name__}): {err}", file=sys.stderr)
except FileNotFoundError:
    print(f"cannot find {my_file}")
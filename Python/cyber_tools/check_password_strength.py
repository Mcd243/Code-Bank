"""Script:  passwd_checker_loop.py
   Desc:    Check whether a password is strong.
            uses getpass to hide user input,
            and keeps asking until a strong password is entered
   Author:  Petra L
   last modified: June 2021 pycodestyle, pylint and PEP8
"""
# module to hide the password input
import getpass


########################## THE FUNCTION DEFINITION ##############################

def check_strength(passwd: str) -> bool:
    """checks the strength of a password, printing the result"""
    ### check password length ###
    if len(passwd) < 8:
        return False

    ### check password for upper and numeric chars ###
    ### set up the variables with a starting value ###
    hasupper = False
    haslower = False
    digitcount = 0
    ### for loop to check conditions of the user password ###
    for char in passwd:
        # if elif statement
        if char.isupper():
            hasupper = True
        elif char.islower():
            haslower = True
        elif char.isnumeric():
            digitcount += 1
    # return the results out of the function       
    return hasupper and haslower and digitcount >= 3


################################## THE MAIN CODE ################################

def main():
    """ask user input, then check the input password's strength.
       keeps asking until a strong password is entered.
    """
    # ask user input. Could use PASWord123 and 123xY to test
    result = False
    while not result:
        # get password as hidden input
        passwd = getpass.getpass("Enter your password to check its strength: ")
        # run function and store result in variable
        result = check_strength(passwd)
        # if result is True (in this case if it has a value then it is True buy default)
        # then do first thing 
        # else do second thing
        if result:
            print(f"[*] Password {passwd} is strong")
        else:
            print(f"[*] Password {passwd} is NOT strong. Try again")


    # unit tests############## EXCEPTION HANDLING ###############################


    print("====\nUnit tests\n====")
    try:
        tests = {"aX238": False,
                 "Password123": True,
                 "Password": False,
                 "my_password1234": False,
                 "p3tral0vesP1thon": True}
        for test, result in tests.items():
            assert check_strength(test) == result, \
                   print(f"{test} should return {result}, check your code")
            print(f"{test} correctly returns {result}")
    except AssertionError:
        print("Remaining tests not carried out because the above failed")


############################ THE BOILER PLATE ##############################

if __name__ == "__main__":
    main()

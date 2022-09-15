##################### ENTROPY OF A PASSWORD #######################
                    #         BASIC         #

"""keyspace ANSWER CODE: NOT SHOWN IN LAB
A simple script that calculates the keyspace/entropy of password
Author:
Date: Revisited 09/06/2021
"""


def get_keyspace(passwd, char_set):
    """print the entropy value for an ascii password"""
    print("[*] keyspace")
    # number of possible charactors ** password length
    keyspace = char_set ** len(passwd)    
    avgAttempt = keyspace / 2
    # 200 000 000 attempts per hour
    avgTime = avgAttempt / 200000000
    # print out the results
    print(f"[*] Password: {passwd} - Total {keyspace} key combinations")
    print(f"[*] Average attempts to crack: {avgAttempt}")
    print(f"[*] Average Time: {avgTime} hours")


# test case
passwd = "ass"  # change the passwd variable to test
charset = 95    # printable ASCI charactors
# call keyspace calc function
get_keyspace(passwd, charset)

#################################################################


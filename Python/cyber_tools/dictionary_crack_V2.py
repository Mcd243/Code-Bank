""" Script: dict_crack_lab_4b_answers.py
    Description: Cracks password hash using a dictionary of common passwords.
    Author: Petra L
    Modified: June 2021
    PEP8 Compliant
    ================================================
    THIS VERSION INCLUDES THE SOLUTIONS FOR LAB 4:
    - Challenge A: read list of common passwords from an external file
    - Challenge B: script can be run from command line, giving hash to be cracked as argument
    I HAVE IMPLEMENTED THI SLIGHTLY DIFFERENTLY, SO THAT THE TEST CASES RUN IF NO ARGUMENT IS ENTERED
    ================================================
"""
import sys
import hashlib
from typing import Union, List  # for function annotations


def read_common(filename: str) -> List:
    """Read a file with common passwords into a list"""
    common_passwds = []
    with open(filename, "r") as contents:
        for line in contents:
            common_passwds.append(line.strip())
    return common_passwds


def dict_attack(passwd_hash: str, common: List) -> Union[str, None]:
    """Dictionary attack,
    checks password hash against a list of common passwords
    while using a for loop"""
    print(f"[*] Cracking hash: {passwd_hash}")
    passwd_found = None
    for word in common:
        hsh = hashlib.md5(word.encode())
        if hsh.hexdigest() == passwd_hash:
            passwd_found = word
            break
        # the next lines do not need else: because they only run if there was no break
        word1 = word.upper()
        hsh1 = hashlib.md5(word1.encode())
        if hsh1.hexdigest() == passwd_hash:
            passwd_found = word1
            break
        # the next lines do not need else: because they only run if there was no break
        word2 = word.capitalize()
        hsh2 = hashlib.md5(word2.encode())
        if hsh2.hexdigest() == passwd_hash:
            passwd_found = word2
            break

    if passwd_found:
        print(f"[+] Password recovered: {passwd_found}")
    else:
        print("[-] Password not recovered")
    return passwd_found


def main():
    """Runs test cases.
       If a hash is entered as command line argument, the script will attempt to crack that hash.
       Otherwise the test cases will be run
    """
    # read common passwords from file
    common = read_common("common3.txt")
    # check if a hash has been given at runtime
    if len(sys.argv) == 2:
        dict_attack(sys.argv[1], common)
    else:
        print("To crack a specific hash run script from command line:")
        print("    python dict_crack_lab04b_answers.py hash_to_crack")
        print("No argument given so running test cases instead...")
        # run test cases
        print("[dict_crack] Test cases")
        passwd_hash = "44ec94bbfc520c644ce2748eb3bdef6d"
        dict_attack(passwd_hash, common)
        passwd_hash = "d8578edf8458ce06fbc5bb76a58c5ca4"
        dict_attack(passwd_hash, common)
        passwd_hash = "478bf2de70f915a6320a5451c3d7fdb9"
        dict_attack(passwd_hash, common)
        passwd_hash = "a67778b3dcc82bfaace0f8bc0061f20e"
        dict_attack(passwd_hash, common)
        passwd_hash = "4297f44b13955235245b2497399d7a92"
        dict_attack(passwd_hash, common)


if __name__ == "__main__":
    main()

""" Script: dict_crack.py
    Description: Cracks password hash using a dictionary of common passwords.
    Author: Petra L
    Modified: Sept 2021
    Note: You will require this file for Lab 03, 04, and 05
"""

import hashlib
from typing import Union  # for function annotations

# list of common passwords
common = ["123", "1234", "12345", "123456", "1234567", "12345678",
          "password", "qwerty", "abc", "abcd", "abc123", "111111",
          "monkey", "arsenal", "letmein", "trustno1", "dragon",
          "baseball", "superman", "iloveyou", "starwars",
          "montypython", "cheese", "123123", "football", "batman"]


def dict_attack(passwd_hash: str) -> Union[str, None]:
    """Dictionary attack,
    checks password hash against a list of common passwords
    while using a for loop"""
    print(f"[*] Cracking hash: {passwd_hash}")
    passwd_found = None
    with open(common3.txt, "r") as passwords:
        for word in common:
            word_hash = hashlib.md5(word.encode("utf-8"))
            upper_word = word.upper()
            upper_word_hash = hashlib.md5(upper_word.encode("utf-8"))
            cap_word = word.capitalize()
            cap_word_hash = hashlib.md5(cap_word.encode("utf-8"))
            if word_hash.hexdigest() == passwd_hash:    
                passwd_found = word
            elif upper_word_hash.hexdigest() == passwd_hash:    
                passwd_found = upper_word
            elif cap_word_hash.hexdigest() == passwd_hash:    
                passwd_found = cap_word       
        if passwd_found:
            print(f"[+] Password recovered: {passwd_found}")
        else:
            print("[-] Password not recovered")
        return passwd_found


def main():

    """Test cases"""
    print("[dict_crack] Tests")
    passwd_hash = "d8578edf8458ce06fbc5bb76a58c5ca4"
    dict_attack(passwd_hash)
    passwd_hash = "478bf2de70f915a6320a5451c3d7fdb9"
    dict_attack(passwd_hash)
    passwd_hash = "44ec94bbfc520c644ce2748eb3bdef6d"
    dict_attack(passwd_hash)


if __name__ == "__main__":
    main()

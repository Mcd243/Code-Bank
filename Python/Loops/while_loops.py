


"""Module: add_ints.py
   Desc: Get numbers from the user and add them together
   Modified: July 2021
"""

reply_list = []
reply = True

while reply:
    reply = float(input("Enter a number (0 to finish): "))
    reply_list.append(reply)

total = sum(reply_list)
print(f"{total=}")



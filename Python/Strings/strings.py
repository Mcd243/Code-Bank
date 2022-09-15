####################### STRINGS #################################

str_var1 = "Don't Panic!!"
"Pan" in str_var1
# True

"pan" in str_var1
# False

"Snake" not in str_var1
# True

"Pan" not in str_var1
# False

################################################################
############ string.find() and string.index() methods ##########
################################################################

str_var2 = "Good morning every1"

str_var2.find("m")
# 5

str_var2.index("m")
# 5

# .find() returns -1 when not found // can't use find on lists //
# .index() gives an error when not found


################## Case of Strings #############################

str_var3 = "Please don't panic! Count to 10"
# upper case
str_upper = str_var3.upper()
# lower case
str_lower = str_var3.lower()
print(str_upper)
print(str_lower)

# title case (capitalize the first letter of each word)
str_capital = str_var2.title()
print(str_capital)

# capitalize the first letter of each string
str_var3.capitalize()
print("DON'T PANIC, take 5 mins ...".capitalize())

# is it upper or lower case??
"DON'T".isupper()
# True
"DON'T".islower()
# False

# is it a numeric string?
"12345".isnumeric()

######################## f STRINGS ###############################

home = "Forfar"
away = "East Fife"
home_score, away_score = 4, 5
str_var4 = f"Final score was {home} {home_score} {away} {away_score}..."
print(str_var4)

# Final score was Forfar 4 East Fife 5...


###################### Chomping a string ######################

import sys

passwds = []
my_file = "common.txt"
try:
    with open(my_file, "r") as passwords:
        for line in passwords:
            try:
                # strip() has been added to the line below
                passwds.append(line.strip().split(", "))
            except Exception as err:
                print(f"Exception({err.__class__.__name__}): {err}", file=sys.stderr)
    print(f"{passwds=}")
except FileNotFoundError:
    print(f"Cannot open or find {my_file}", file=sys.stderr)


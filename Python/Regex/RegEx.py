############################## RegEx ################################

############################# re.search() ###########################

#he re.search() method we have used so far finds only the first match of a pattern.

# syntax
match_obj = re.search(pattern_str, str_to_be_searched)

import re

str1 = "If I had a talking parrot, the first thing I'd teach it to say is 'Help! They've turned me into a parrot!'"
match = 
print(match)
match.span()

#The Match object has properties and methods used to retrieve information about the search, and the result:

#.span() returns a tuple containing the start-, and end positions of the match.
#.string returns the string passed into the function
#.group() returns the part of the string where there was a match

import re

str1 = "If I had a talking parrot, the first thing I'd teach it to say is 'Help! They've turned me into a parrot!'"
match = re.search("parrot", str1)
print(match)
span = match.span()
group = match.group()

print(f"Found: \"{group}\" between offset {span[0]} and {span[1]} ")

# Found: "parrot" between offset 19 and 25 

######################## re.findall() ############################

matches = re.findall(r"parrot", str1)
print(matches)

# ['parrot', 'parrot']


######################### PATTERN CHARACTORS ########################

#Special pattern characters used include:

 #   . (dot) Matches any single character
  #  \w matches any word character (letter or number or underscore) -equivalent to [0-9a-zA-Z_]
   # \d matches decimal numeric digits - equivalent to [0-9]
    #\s whitespace - equivalent to [\t\n\r\f\v]


import re
str1 = "string to be searched for the word parrot"
matches = re.findall(r"p\w\w\w\wt", str1)

print(f"{matches=}")

# matches=['parrot']

####################

str2 = "1 string to be searched, for 23, the age of the parrot"
matches = re.findall(r"\d\d", str2)

print(f"{matches=}")

# matches=['23']

###################


matches = re.findall("s......d", str3)

print(f"{matches=}")

# matches=['s3@rch3d']

##################

# We can match whitespace characters only with \s. 

str4 = "string to be 445 3665 searched for phone number"
matches = re.findall(r"\d\d\d\s\d\d\d", str4)

print(f"{matches=}")

# matches=['445 366']

#                   #

str5 = "string to be 445\t3665 searched for phone number"
print(str5)

matches = re.findall(r"\d\d\d\s\d\d\d", str5)
print(f"{matches=}")

# string to be 445	3665 searched for phone number
# matches=['445\t366']

#############################################################

### 5. Repeating Pattern Characters

# Often in a pattern we want to look for a sequence of several characters of the same type.

# + **+** matches one or more characters
# + **\*** matches zero or more characters
# + **?** matches zero or one characters


str7 = "reeeeeeeeeeepeating"
matches = re.findall("e+", str7)

print(f"{matches=}")

# matches=['eeeeeeeeeee', 'e']

##############################

# Sometimes we know how many characters are in parts of a pattern.

str8 = "Bill B Phone no: 07284739846 age:57"
matches = re.findall(r"\d{11}", str8)
print(f"{matches=}")

# matches=['07284739846']

############################

# Sometimes we do not know how many characters are in part of a pattern

str9 = "there are 7284739846 students in the uni"
matches = re.findall(r"\d+", str9)
print(f"found the pattern: {matches=}")

# found the pattern: matches=['7284739846']

###########################

str10 = "7 8"
matches = re.findall(r"\d\s*\d", str10)
print(f"{matches=}")

# matches=['7 8']


#There are many special pattern matching characters. Below is a small selection of common, and useful ones.

 #   \t matches tab character
 #   \n matches newline character
 #   \S matches non whitespace characters
 #   \ escapes a special pattern character
 #   \. matches on an actual dot, not any character
 #   Anchors:
 #       ^ matches position at the beginning of a string (does not match a char only the position)
 #       $ matches position at the end of a string (does not match a char only the position)
 #   ? possibly this

# Sometimes we want to escape special characters if we are looking for those literal characters. 
# For example, to match an actual '.' (dot) character, we need to escape it using **. 


str14 = "The DoS came from: 146.176.164.343 in the C27 lab"
matches = re.findall(r"\d+\.\d+\.\d+\.\d+", str14)

print(f"{matches=}")

# matches=['146.176.164.343']

##############################
# ^ anchors the beginning of the search to the start of the line

str16 = "146.166.55.2: host net scanning against 146.156.12.2"
matches = re.findall(r"^\d+\.\d+\.\d+\.\d+", str16)

print(f"found the pattern: {matches=}")

found the pattern: matches=['146.166.55.2']




##################  Sets and ranges of characters with [ ] (square brackets)¶ ###############

# - or space
str17 = "string to be (0)131 445 3665 searched, for phone number"
matches = re.findall(r"\d+[- ]\d+", str17)

print(f"Found the pattern: {matches[0]}")

# Found the pattern: 131 445

# The – (hyphen) can be used within [ ] to specify ranges of numeric or alphabetic characters

str24 = "Rich's password:aPP13s345 is strong"
matches = re.findall("[a-z]:[a-zA-Z0-9]+", str24)

print(f"found the pattern: {matches[0]}")

# found the pattern: d:aPP13s345

str33 = "146.176.123.9"
matches = re.findall(r"[0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]", str33)
# [0] shows us the actual value
print(f"found the pattern: {matches[0]}")
found the pattern: 146.176.123.9

######### ? #############possibly this

str35= "server 146.176.123.99"
matches = re.findall(r"146\.176\.123\.[0-9][0-9]?[0-9]?", str35)
print(f"{matches=}")
    
# matches=['146.176.123.99']



############ Groups - with ( ) round brackets ###############

# Groups can also be used to divide a regex into sub-expressions, 
# and to extract specific parts of the regex pattern.

e2 = "johncleese@montypython.com blah rich@napier.com blah"
match = re.search(r"(\w+)@(\w+.com)", e2)

if match:
    print(f"found the pattern: {match.group()}")

# found the pattern: johncleese@montypython.com

match.group(1)
# 'johncleese'
match.group(2)
# 'montypython.com'

################ findall() and groups #################

matches = re.findall(r"(\w+)@(\w+.com)", e2)
print(matches)

# [('johncleese', 'montypython.com'), ('rich', 'napier.com')]


for match in matches:
    print(match[1])

# montypython.com
# napier.com

    
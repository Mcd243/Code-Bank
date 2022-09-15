######################### REGEX #####################################

[abc]
# matches any one charactor

[^abc]
# matches all except these

[A-Z]
# matches single upper case

[0-9]
# matches single numeric

Mon|Tue
# matches either Mon or Tue string

^
# matches start point of line

$
# matches end point of line 

()
# used to group

\
# escape charactor \$ literal $

########################################################################
# Expression quantifiers

*
# matches any number of charactors (all)
# [0-9]* with all numbers
# [A-z]* with all letters

+
# matches 1 or more of the previous charactor
# a+

?
# matches one or none of the previous charactor
# a?

{n}
# matches exactly n(number) of the previous item.


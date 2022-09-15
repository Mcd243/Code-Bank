
########################################### AWK ##################################################
#It’s a full scripting language, as well as a complete text manipulation toolkit for the command line. 

#Patterns are enclosed in curly braces ({}). Together, a pattern and an action form a rule. 
#The entire awk program is enclosed in single quotes (').

who | awk '{print $1}'
#awk prints the first field and discards the rest of the line.

who | awk '{print $1,$4}'
# 
    $0: Represents the entire line of text.
    $1: Represents the first field.
    $2: Represents the second field.
    $7: Represents the seventh field.
    $45: Represents the 45th field.
    $NF: Stands for “number of fields,” and represents the last field.
#

awk '{print $1,$2,$NF}' dennis_ritchie.txt

# OFS (output field separator) variable to put a separator between the month, day, and year. 
# Note that below we enclose the command in single quotes ('), not curly braces ({}):

date | awk 'OFS="/" {print$2,$3,$6}'

date | awk 'OFS="-" {print$2,$3,$6}'


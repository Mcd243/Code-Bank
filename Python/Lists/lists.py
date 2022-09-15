################################################################
########################### LISTS ##############################
################################################################

# Lists in Python are objects which can contain collections of 
# other objects. They can be composed of any types of objects.

my_list = [1, "Brian", "Knight", 1.23, "this is a long string."]

passwords = ["passwords",
             "qwerty",
             "default",
             1234,
             12345,
             123456]

passwords[1]
# 'qwerty'

print(passwords)
# ['passwords', 'qwerty', 'default', 1234, 12345, 123456]

print(len(passwords))
# 6

print(len(passwords[2]))
# 7

######################### list Methods #########################


help(passwords)
dir(passwords)
passwords. #<TAB>#


# Add one to the end

passwords.append("sunshine")
print(passwords)

#['passwords', 'qwerty', 'default', 1234, 12345, 123456, 'sunshine']

# Remove one from the index (last is default)

passwords.pop()
print(passwords)

# ['passwords', 'qwerty', 'default', 1234, 12345, 123456']

# Single objects in a list can be removed by value using the 
# .remove() method:

passwords.remove(123456)
print(passwords)

# ['passwords', 'qwerty', 'default', 1234, 12345']


# .insert() at index

passwords.insert(2, "python")
print(passwords)

# ['passwords', 'qwerty', 'python', 'default', 1234, 12345']


# To add multiple objects at the end of the list, the .extend()
#  method can be used:

passwords.extend([123456, 1234567])
print(passwords)

# ['passwords', 'qwerty', 'python', 'default', 1234, 12345, 123456, 1234567'


# The list object method .sort() can be used to order the list in 
# various ways.

passwords.sort(key=str)
print(passwords)

# [1234, 12345, 'cat', 'default', 'passwords', 'python', 'qwerty', 
# 'sunshine']


#If you don't want to change the list itself but just see how it would 
#look when sorted, use the sorted() function instead.

sorted([passwords])




####################### Indexing/Slicing ########################



# Return the last indexed item
passwords[len(passwords)-1]

# return items starting at index 0 up to and including index 4
passwords[0:5]

# a string is like a list
"sunshine"[1:4]


# print each item out on a new line
passwords = [1234, 12345, "default", "password", "qwerty"]

for password_item in passwords:
    print(password_item)

# 1234
# 12345
# default
# password
# qwerty


######################## NESTED LISTS ##########################


passwords = [1234,
            12345,
            "default", ["default1", "default12", "default123"],
            "password",
             "qwerty"
            ]
# For loop to print list items each on a new line 
for password_item in passwords:
    print(password_item)

# 1234
# 12345
# default
# ['default1', 'default12', 'default123']
# password
# qwerty

print(passwords[3][2])
# default123

# Iterate through the items in the list
# If the list item is a list
# print each nested list item on a new line
# otherwise print each list item on a new line.

for password_item in passwords:
    if(isinstance(password_item, list)):
        for nested_item in password_item:
            print(nested_item)    
    else:
        print(password_item)

# 1234
# 12345
# default
# default1
# default12
# default123
# password
# qwerty


################## Flatten a list with join() ##################


# joins list items with and a string to a list with a space

str_var1 = "Don't Panic!"
list_var1 = [str_var1, "and", "carry", "on"]
" ".join(list_var1)
# "Don't Panic! and carry on"


# joins list values with an "and "

list_var2 = ["Lions", "Tigers", "Bears"]
" and ".join(list_var2)
# 'Lions and Tigers and Bears'


"???".join(str_var1)
# "D???o???n???'???t??? ???P???a???n???i???c???!"


str_var1.join("???")
# "?Don't Panic!?Don't Panic!?"


##################### LIST COMPREHENSION ########################


# creating a list with a list comprehension

numbers = [n for n in range(10)]
print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# doubled_numbers contains each of these numbers doubled

doubled = [ ]
for n in numbers:
    doubled.append(n*2)

# Could be replaced with:

doubled = [n*2 for n in numbers]
print(doubled)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]






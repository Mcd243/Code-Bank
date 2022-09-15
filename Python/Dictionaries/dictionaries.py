######################### DICTIONARIES #############################

# create a dictionary

dic = {"parrot": "dead", 42: "romans", "numbers": [1, 2, 3]}

# add key value pairs to an empty dictionary

dic = {}
dic["parrot"] = "dead"
dic[42] = "romans"
dic["numbers"] = [1, 2, 3]


# extract values using the key

dic["parrot"]
#'dead'

dic[42]
'romans'


# check if a key is in a dictionary

"parrot" in dic
# True

##########################################################

### python only looks at the keys of the dictionary. ####

###################### .get() ############################
### .get() takes as its argument a potential key in teh 
# dictionary. It returns the corresponding value. 
# If the key is not in the dictionary, it returns nothing 
# (None) - or, if a second argument is given, it returns 
# this second argument.


dic.get(42)
# 'romans'


####################### .pop() ###########################
# can be used. pop() needs the key of the key:value pair that you want to remove

dic.pop("extra")
# 'doomed'

print(dic)
# {'parrot': 'dead', 42: 'romans', 'numbers': [1, 2, 3]}


####################### .keys() ##########################
# can be used to output all keys in a dictionary:

dic.keys()
# dict_keys(['parrot', 42, 'numbers'])


###################### .items() #########################
# etrieves both keys and values in a dictionary. 
# It is usually the best to use when you loop over a dictionary

dic.items()
# dict_items([('parrot', 'dead'), (42, 'romans'), ('numbers', [1, 2, 3])])


###################### len() ############################
# find the number if items in a dictionary

len(dic)


###################### .copy() ###########################
# make  a copy of an entire Dictionary

dic2 = dic.copy()


###################### .clear() ##########################
# remove all elements from the dictionary 

dic2.clear()


####################### del ###############################
# delete the entire dictionary

del dic2


###################### zip() #############################
# creating a dictionary from two lists

english = ["good morning", "good evening", "see you soon", "thank you"]
french = ["bonjour", "bonsoir", "à bientôt", "merci"]

dic1 = dict(zip(english, french))
print(dic1)

# {'good morning': 'bonjour', 'good evening': 'bonsoir', 'see you soon': 'à bientôt', 'thank you': 'merci'}




#################  ITERATING OVER A DICTIONARY ############
####################### FOR LOOP ##########################
print(dic)
for key in dic:
    print(f"{key} -> {dic[key]}")

# {'parrot': 'dead', 42: 'romans', 'numbers': [1, 2, 3]}
# parrot -> dead
# 42 -> romans
# numbers -> [1, 2, 3]

for key in dic.keys():
    print(f"{key} -> {dic[key]}")

# parrot -> dead
# 42 -> romans
# numbers -> [1, 2, 3]

#################### FOR LOOP USING .items() ##################

for key, value in dic.items():
    print(f"{key} -> {value}")

# parrot -> dead
# 42 -> romans
# numbers -> [1, 2, 3]


##############################################################
########## Dictionary comprehensions *Important* #############
##############################################################

# concise and efficient method for creating a new list with an 
# "implicit loop".

dic4 = {fr:en for (en, fr) in dic1.items()}

# It creates a new dictionary dic4. 
# We iterate over (en, fr) key-value pairs, and make fr the new key, 
# en the new value (as shown by fr:en at the beginning). 
# So we're effectively "reversing" or "swapping" the keys and values. 
# we've used en and fr as explanatory variable names but could have 
# used anything - i and j, apples and pears, whatever.

##############################################################
# Using set to unpack a dictionary

programmers = {'Anne':'Python',
               'Sue': 'Java',
               'Tim': 'Python'}

programing = {}

for program in set(programmers.values()):
    print(f'{program} coder(s):')
    for name in programmers:
        if programmers[name]==program:
            print('   ' + name)


#Python coder(s):
#   Anne
#   Tim
#Java coder(s):
#   Sue
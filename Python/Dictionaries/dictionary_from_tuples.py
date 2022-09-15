############################ setdefault() method ########################


"""Demonstrate the creation of a dictionary where the values are lists,
   and the use of .setdefault() to add to the dictionary"""

# A list of students and the modules they are studying
study = [('Jane', 'CSN08114'),
        ('Jane', 'SET08101'),
        ('Tim', 'SET08101'),
        ('Sue', 'CSN08114')]

studies = {}

for name, module in study:
    studies.setdefault(name,[]).append(module)
    print(f"---Now studies is: {studies}")
    
print(f"Finally, we have\n{studies=}")

#---Now studies is: {'Jane': ['CSN08114']}
#---Now studies is: {'Jane': ['CSN08114', 'SET08101']}
#---Now studies is: {'Jane': ['CSN08114', 'SET08101'], 'Tim': ['SET08101']}
#---Now studies is: {'Jane': ['CSN08114', 'SET08101'], 'Tim': ['SET08101'], 'Sue': ['CSN08114']}
#Finally, we have
#studies={'Jane': ['CSN08114', 'SET08101'], 'Tim': ['SET08101'], 'Sue': ['CSN08114']}



# Here, setdefault(name, []) checks if the name already exists in the dictionary. 
# If it doe not, it adds name as a new key, with an empty list as its value. 
# If name does exist already, it returns its value, which is a list in our example. 
#This ensures that when we get to .append(), we always have a list as teh value, so teh append will always work. 
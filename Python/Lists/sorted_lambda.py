# In Python, we have sorted() and sort() functions available to sort a list.

# We can also use one parameter in these functions, which is the key parameter. 
# It allows us to create our very own sorting order. 
# We can use the lambda functions in this parameter, enabling us to create our own single-line function.

lst = ['id01', 'id10', 'id02', 'id12', 'id03', 'id13']
lst_sorted = sorted(lst, key=lambda x: int(x[2:]))
print(lst_sorted)

# ['id01', 'id02', 'id03', 'id10', 'id12', 'id13']


# In the above example, we have a list of IDs where every number is prefixed with the letters id. 
# In the key parameter, we specify a lambda function specifying that we have to ignore the first 
# two characters (id) and sort the list.

lst = [('Mark',1),('Jack',5),('Jake',7),('Sam',3)]
lst_sorted = sorted(lst, key=lambda x: x[1])
print(lst_sorted)

# [('Mark', 1), ('Sam', 3), ('Jack', 5), ('Jake', 7)]

#In the above example, we have a list of tuples. The tuple consists of a name and a number. 
# In the lambda function, we specify the function to sort based on the second element of the tuple, that is, the number.


# Note that we can change the order to descending using the reverse parameter and setting it to True.
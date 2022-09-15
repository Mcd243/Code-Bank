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



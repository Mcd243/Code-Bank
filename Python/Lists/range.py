###################### RANGE #################################


reply_list = []
for i in range(5):
    reply_list.append(float(input("Enter a number: ")))
total = sum(reply_list)
print(f"{total=}")

# Enter a number:  1
# Enter a number:  1
# Enter a number:  1
# Enter a number:  1
# Enter a number:  1

# total=5.0

# a range object
range(5)
# range(0, 5)


# a list object
list(range(5))
#[0, 1, 2, 3, 4]

# create a list that starts with 10, finishes before 100, 
# and goes up in increments of 7
list(range(10, 100, 7))
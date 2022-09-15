
############## FOR LOOP IN RANGE ####################

n = int(input())

"""Iterate over the given numbers in range 1 to 
(user input intiger),
check if they fulfill the conditions,
otherwise just print the number """

for x in range(1, n):
    # if elif else contitions 
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)

########################################################

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



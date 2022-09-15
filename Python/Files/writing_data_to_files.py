
##################### WRITE DATA TO A FILE ####################

# assign to a variable with write permissions
my_file = open("outfile.txt", "w")

# print to the buffer (when closed it will write to the file) 
print("Good morning", file=my_file)

# the .write() method
my_file.write("test line1\n") 
# outputs the length of the string the written

# .close() when closed the text is written from the buffer to the file
my_file.close() 

# APPEND MODE
my_file = open("outfile.txt", "a")
my_file.write("test line5\n")
my_file.write("test line6\n")
my_file.close()


# FLUSH THE BUFFER WITHOUT CLOSING
my_file = open("outfile.txt", "a")
my_file.write("test line7\n")
my_file.flush()


with open("modules.txt", "w") as f:
    f.write(str(sys.modules))


################################################################

import hashlib
import sys
from typing import Union  # for function annotations
# need to look into writeline()


pswd= ["123", "1234", "12345", "123456", "1234567", "12345678",
          "password", "qwerty", "abc", "abcd", "abc123", "111111",
          "monkey", "arsenal", "letmein", "trustno1", "dragon",
          "baseball", "superman", "iloveyou", "starwars",
          "montypython", "cheese", "123123", "football", "batman"]

pswd_file = "common3.txt"


def write_to_file(file, list1): 
    file = open(file, "w")
    for item in list1:
        file.write(item)
    file.close()
    

def main():
    write_to_file(pswd_file, pswd)
    
    


if __name__ == "__main__":
    main()



# checks if something is valid

import re

# data to be outputted
data = ['I', 'love', 'computers']
has_errors = "yes"
while has_errors == "yes":
    has_errors = "no"
    filename = input("Enter a filename: ")
    has_errors = "no"

    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter == " ":
            problem = "(no spaces allowed)"
        
        else:
            problem = "(no {}'s allowed)".format(letter)
        has_errors = "yes"

    if filename == "":
        problem = "can't be blank"
        has_errors = "yes"

    if has_errors == "yes":
        print("invalid filename - {}".format(problem))
    
    else:
        print("You entered a valid filename")


# add .txt suffix!
filename = filename + ".txt"

# create file to hold data
f = open(filename, "w+")

# add new line at end of each item
for item in data:
    f.write(item + "\n")

# close file
f.close()
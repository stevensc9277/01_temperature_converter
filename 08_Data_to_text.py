# source: https://www.guru99.com/reading-and-writing-files-in-python.html

# data to be converted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# get filename, can't be blank / invalid
# assume valid data for now
filename = input("Enter a Filename (leave off the extensions): ")

# add .txt suffix!
filename = filename + ".txt"

# create file to hold data
f = open(filename, "w+")

# add new line at end of each item
for item in data:
    f.write(item + "\n")

# close file
f.close()
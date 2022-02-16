# get data
# display the most recent three entries  nicely

# set up empty list
all_calculations = []

# get five items of Data
for i in range(0, 5):
    get_item = input("Enter an item: ")
    all_calculations.append(get_item)

# show that everything made it to the list
print()
print("*** The full list ***")
print(all_calculations)

print()

print("*** Most recent 3 ***")
# print items starting at the end of the list
for i in range(0, 3):
    print(all_calculations[len(all_calculations) - i - 1])
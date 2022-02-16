# get data
# display the most recent three entries  nicely

# set up empty list
all_calculations = []

# get five items of Data
get_item = ""

while get_item != "xxx":
    get_item = input("Enter an item: ")

    if get_item == "xxx":
        break

    all_calculations.append(get_item)

print()

if len(all_calculations) == 0:
    print("Oops - the list is empty")

else:
    # show that everything made it to the list
    print()
    print("*** The full list ***")
    print(all_calculations)

    # show that everything made it to the  list...
    print()
    print()

    print("*** Most recent 3 ***")
    # print items starting at the end of the list
    for i in range(0, 3):
        print(all_calculations[len(all_calculations) - i - 1])
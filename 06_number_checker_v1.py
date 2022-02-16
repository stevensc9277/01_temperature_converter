# number checker
def num_check(low):
    while True:
        try:
            response = float(input("Enter a number: "))

            if response < low:
                print("Too cold!")
            else:
                return response
                
        except ValueError:
            print("Please enter a number")

num_check(-273)
# quick component to convert degrees C to F
# Functions takes in value, does conversion and puts answer into a list

def to_c(from_f):
    celsius = (from_f * 9/5) + 32
    return celsius

# Main routine
temperature = [0, 32, 100]
converted = []

for i in temperature:
    answer = to_c(i)
    ans_statement = "{} degrees F is {} degrees C".format(i, answer)
    converted.append(ans_statement)

print(converted)
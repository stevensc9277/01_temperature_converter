# quick component to convert degrees C to F
# Functions takes in value, does conversion and puts answer into a list

def to_f(from_c):
    fahrenheit = (from_c * 9/5) + 32
    return fahrenheit

# Main routine
temperature = [0, 40, 100]
converted = []

for i in temperature:
    answer = to_f(i)
    ans_statement = "{} degrees C is {} degrees F".format(i, answer)
    converted.append(ans_statement)

print(converted)
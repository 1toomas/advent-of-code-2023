# https://adventofcode.com/2023/day/15
# Day 15: Lens Library

filename = "inputs/day15-input.txt"
# filename = "inputs/day15-input-test2.txt"

###
with open(filename, "r") as f:
  steps = f.readline().rstrip("\n").split(",")

sum_of_results = 0
for s in steps:
  current_value = 0
  for c in s:
    # Determine the ASCII code for the current character of the string.
    # Increase the current value by the ASCII code you just determined.
    current_value += ord(c)
    # Set the current value to itself multiplied by 17.
    current_value *= 17
    # Set the current value to the remainder of dividing itself by 256.
    current_value %= 256
  sum_of_results += current_value

print("The sum of the results is "+str(sum_of_results))

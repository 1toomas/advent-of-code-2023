# https://adventofcode.com/2023/day/1
# https://adventofcode.com/2023/day/1#part2
# Day 1: Trebuchet?!

filename = "inputs/day1-input.txt"
# filename = "inputs/day1-input-part2-test.txt"

import re

# spelled-out numbers and their replacements containing the corresponding integer
conversion_dict = { "one":"o1e", "two":"t2o", "three":"t3", "four":"4", "five":"5e", "six":"6", "seven":"7n", "eight":"e8t", "nine":"n9e" }

def line_value(line):
  # calculate the value of the line:
  #  find all digits in the line, take the first and last, concatenate those, return as an integer
  digits = re.findall("\d", line)
  if len(digits) > 0:
    return int(digits[0] + digits[-1])
  else:
    return 0

def convert(line):
  # convert all the spelled-out numbers in the line to text containing corresponding integers
  tmp = line
  for key in conversion_dict.keys():
    tmp = tmp.replace(key, conversion_dict[key])
  return tmp

###
f = open(filename, "r")
lines = f.readlines()

sum = 0
for l in lines:
  l = convert(l) # convert spelled-out numbers to integers
  sum += line_value(l) # calculate the value of the line

print("The sum of all of the calibration values is "+str(sum))

# https://adventofcode.com/2023/day/3
# Gear Ratios

import re

filename = "inputs/day3-input.txt"
# filename = "inputs/day3-input-test1.txt"

f = open(filename, "r")
lines = f.readlines()
line_count = len(lines)
line_len = len(lines[0]) # assume all lines are of equal length

sum_part_numbers = 0

for i in range(line_count):
  current_line = lines[i]
  more_numbers = True
  current_pos = 0
  while more_numbers:
    nr = re.search("\d+", current_line)
    if nr == None:
      more_numbers = False
    else:
      take_this_number = False
      nr_s = nr.span()[0]
      nr_e = nr.span()[1]
      if nr_s > 0:
        take_this_number = (current_line[nr_s-1] != ".")
      if (not take_this_number) and (nr_e < line_len-1):
        take_this_number = (current_line[nr_e] != ".")
      # check previous row
      if (not take_this_number) and (i > 0):
        other_line = lines[i-1]
        other_line = other_line[max(0,current_pos+nr_s-1):min(line_len-1,current_pos+nr_e+1)]
        other_line = other_line.replace(".","")
        symbol = re.search("\D", other_line)
        take_this_number = (symbol != None)
      # check next row
      if (not take_this_number) and (i < line_count-1):
        other_line = lines[i+1]
        other_line = other_line[max(0,current_pos+nr_s-1):min(line_len-1,current_pos+nr_e+1)]
        other_line = other_line.replace(".","")
        symbol = re.search("\D", other_line)
        take_this_number = (symbol != None)
      # strip the handled part of the line, remember the current position
      current_line = current_line[nr_e:]
      current_pos += nr_e
      if take_this_number:
        sum_part_numbers += int(nr.group())

print("Sum of part numbers: "+str(sum_part_numbers))

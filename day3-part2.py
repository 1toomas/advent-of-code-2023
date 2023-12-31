# https://adventofcode.com/2023/day/3#part2
# Gear Ratios

import re

filename = "inputs/day3-input.txt"
# filename = "inputs/day3-input-test3.txt"

f = open(filename, "r")
lines = f.readlines()
line_count = len(lines)
line_len = len(lines[0]) # assume all lines are of equal length

# find all numbers in all rows
all_numbers_arr = []
nums_dict = dict()
for i in range(line_count):
  current_line = lines[i]
  row_numbers = []
  more_numbers = True
  current_pos = 0
  while more_numbers:
    nr = re.search("\d+", current_line)
    if nr == None:
      more_numbers = False
    else:
      # record any found number as [line no, number start pos, number end pos, number value itself]
      nr_e = nr.span()[1]
      numarray = [nr.span()[0]+current_pos, nr_e+current_pos, int(nr.group())]
      row_numbers.append(numarray)
      # strip the handled part of the line, remember the current position
      current_line = current_line[nr_e:]
      current_pos += nr_e
  if row_numbers != []:
    all_numbers_arr.append([i, row_numbers])
    nums_dict[i] = row_numbers

sum_gear_ratios = 0

# find all asterisks and their adjacent numbers
for i in range(line_count):
  current_line = lines[i]
  more_asterisks = True
  current_pos = 0
  adjacents = []
  while more_asterisks:
    adjacents.clear()
    asterisk_pos = current_line.find("*", current_pos)
    if asterisk_pos != -1:
      more_asterisks = True
      # check touching numbers
      # the same line
      nums = nums_dict.get(i)
      if nums != None:
        for j in nums:
          if j[1] == asterisk_pos:
            adjacents.append(j[2])
          if j[0] == asterisk_pos+1:
            adjacents.append(j[2])
          if j[1] > asterisk_pos:
            break
      # previous line
      if i>0:
        nums = nums_dict.get(i-1)
        if nums != None:
          for j in nums:
            if j[0] <= asterisk_pos and j[1] == asterisk_pos or \
               j[0] <= asterisk_pos and j[1] >= asterisk_pos+1 or \
               j[0] == asterisk_pos+1 and j[1] >= asterisk_pos+1 \
            :
              adjacents.append(j[2])
            if j[1] > asterisk_pos+1:
              break
      # next line
      if i<line_count-1:
        nums = nums_dict.get(i+1)
        if nums != None:
          for j in nums:
            if j[0] <= asterisk_pos and j[1] == asterisk_pos or \
               j[0] <= asterisk_pos and j[1] >= asterisk_pos+1 or \
               j[0] == asterisk_pos+1 and j[1] >= asterisk_pos+1 \
            :
              adjacents.append(j[2])
            if j[1] > asterisk_pos+1:
              break
      # remember the current asterisk position to find next further from that
      current_pos = (asterisk_pos + 1)
      if len(adjacents) == 2:
        sum_gear_ratios += adjacents[0]*adjacents[1]
    else:
      more_asterisks = False

print("Sum of part numbers: "+str(sum_gear_ratios))
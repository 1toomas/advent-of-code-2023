# https://adventofcode.com/2023/day/11
# Day 11: Cosmic Expansion

import re

filename = "inputs/day11-input.txt"
# filename = "inputs/day11-input-test.txt"

###
with open(filename, "r") as f:
  lines = f.readlines()

line_len = len(lines[0])-1 # do not take the trailing newline into account
line_count = len(lines)

# find the coordinates of all galaxies
galaxies = []
empty_rows = []
empty_cols = [i for i in range(line_len)] # initally assume like all columns were without galaxies
for l in range(line_count):
  positions = [m.start() for m in re.finditer('#', lines[l])]
  if positions == []:
    empty_rows.append(l)
  else:
    for p in positions:
      galaxies.append([l,p])
      # as this position has galaxy, remove the column from the list of empty columns
      if p in empty_cols: # cannot remove more than once
        empty_cols.remove(p)

# expand empty rowa (i.e. increase the relevant coodinate of all positions that are located on further lines)
for i in reversed(range(len(empty_rows))):
  for g in range(len(galaxies)):
    if galaxies[g][0] > empty_rows[i]:
      galaxies[g] = [galaxies[g][0]+1,galaxies[g][1]]

# expand empty columns (i.e. increase the relevant coodinate of all positions located further)
for i in reversed(range(len(empty_cols))):
  for g in range(len(galaxies)):
    if galaxies[g][1] > empty_cols[i]:
      galaxies[g] = [galaxies[g][0],galaxies[g][1]+1]

sum_distance = 0
for i in range(len(galaxies)):
  for j in range(len(galaxies)):
    if galaxies[i] < galaxies[j]:
      distance = abs((galaxies[i][0] - galaxies[j][0])) + abs((galaxies[i][1] - galaxies[j][1]))
      sum_distance += distance

print("The sum of all the shortest distances is "+str(sum_distance))

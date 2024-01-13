# https://adventofcode.com/2023/day/14
# Day 14: Parabolic Reflector Dish

filename = "inputs/day14-input.txt"
# filename = "inputs/day14-input-test.txt"
round, cube, empty = "O", "#", "."

### read lines to a list of lists containing rocks
rocks = []
with open(filename, "r") as f:
  for line in f:
    r_line = []
    for j in range(len(line.rstrip("\n"))):
      r_line.append(line[j])
    rocks.append(r_line)

rowlen = len(rocks[0])
for i in range(1,len(rocks)):
  for j in range(rowlen):
    move_row = i
    while move_row >= 1 and rocks[move_row][j] == round and rocks[move_row-1][j] == empty:
      rocks[move_row][j] = empty
      rocks[move_row-1][j] = round
      move_row -= 1

sum_of_load = 0
for i in range(len(rocks)):
  load_multiplier = len(rocks) - i
  sum_of_load += rocks[i].count(round) * load_multiplier

print("The load caused by all of the rounded rocks is "+str(sum_of_load))

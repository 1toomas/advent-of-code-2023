# https://adventofcode.com/2023/day/14#part2
# Day 14: Parabolic Reflector Dish

filename = "inputs/day14-input.txt"
# filename = "inputs/day14-input-test.txt"
round, cube, empty = "O", "#", "."

def tilt_north():
  for i in range(1,row_count):
    for j in range(row_len):
      move_row = i
      while move_row >= 1 and rocks[move_row][j] == round and rocks[move_row-1][j] == empty:
        rocks[move_row][j] = empty
        rocks[move_row-1][j] = round
        move_row -= 1

def tilt_south():
  for i in range(row_count-2,-1,-1):
    for j in range(row_len):
      move_row = i
      while move_row <= row_count-2 and rocks[move_row][j] == round and rocks[move_row+1][j] == empty:
        rocks[move_row][j] = empty
        rocks[move_row+1][j] = round
        move_row += 1

def tilt_west():
  for k in range(1,row_len):
    for l in range(row_count):
      move_col = k
      while move_col >= 1 and rocks[l][move_col] == round and rocks[l][move_col-1] == empty:
        rocks[l][move_col] = empty
        rocks[l][move_col-1] = round
        move_col -= 1

def tilt_east():
  for k in range(row_len-2,-1,-1):
    for l in range(row_count):
      move_col = k
      while move_col  <= row_len-2 and rocks[l][move_col] == round and rocks[l][move_col+1] == empty:
        rocks[l][move_col] = empty
        rocks[l][move_col+1] = round
        move_col += 1

def find_total_load():
  # calculate the total load on the north support beams
  sum_of_load = 0
  for i in range(row_count):
    load_multiplier = row_count - i
    sum_of_load += rocks[i].count(round) * load_multiplier
  return sum_of_load


### read lines to a list of lists containing rocks
rocks = []
with open(filename, "r") as f:
  for line in f:
    r_line = []
    for j in range(len(line.rstrip("\n"))):
      r_line.append(line[j])
    rocks.append(r_line)

row_len = len(rocks[0])
row_count = len(rocks)

# find out after how many cycles the total load will start to cycle

map_dict = dict() # store maps to find when the same maps will start repeating
loads_on_cycles = [] # keep the load after each cycle
cycle = 1
while True:
  # cycle means tilting in every direction
  tilt_north()
  tilt_west()
  tilt_south()
  tilt_east()

  current_load = find_total_load() # find the load after the cycle
  loads_on_cycles.append(current_load) # and keep record of it

  map_string = ''.join([y for x in rocks for y in x]) # convert the current state of rocks to a string
  was_previously = map_dict.get(map_string) # check whether the same map/string has occured before
  if was_previously != None: # if the same map occured before then this is the cycle
    offset = was_previously # the previous occurrence is where the cycle of same maps started
    cycle_length = cycle - was_previously # the length of the cycle of same maps
    break
  else: # no such map before, so save it
    map_dict[map_string] = cycle

  cycle += 1

  # if len(load_indices) > 30:
  if cycle > 1000:
    break

# calculate the position in maps' cycles after the 1000000000th tilting cycle
pos = (1000000000 - offset) % cycle_length + offset
target_load = loads_on_cycles[pos-1] # take the load of that positiion

print("After 1000000000 cycles, the total load on the north support beams is "+str(target_load))

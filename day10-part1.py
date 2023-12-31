# https://adventofcode.com/2023/day/10
# Day 10: Pipe Maze

filename = "inputs/day10-input.txt"
# filename = "inputs/day10-input-test4.txt"

###
with open(filename, "r") as f:
  lines = f.readlines()

line_len = len(lines[0])
line_count = len(lines)

def move(previous, current):
  direction = lines[current[0]][current[1]]
  if direction == "|": # vertical pipe connecting north and south
    if current[0]-previous[0]==1 and current[1]==previous[1]: # came from north, go to south
      return (current[0]+1,current[1])
    elif previous[0]-current[0]==1 and current[1]==previous[1]: # came from south, go to north
      return (current[0]-1,current[1])
  elif direction == "-": # horizontal pipe connecting east and west
    if current[0]==previous[0] and current[1]-previous[1]==1: # came from west, go to east
      return (current[0],current[1]+1)
    elif current[0]==previous[0] and previous[1]-current[1]==1: # came from east, go to west
      return (current[0],current[1]-1)
  elif direction == "L": # 90-degree bend connecting north and east
    if current[0]-previous[0]==1 and current[1]==previous[1]: # came from north, go to east
      return (current[0],current[1]+1)
    elif current[0]==previous[0] and previous[1]-current[1]==1: # came from east, go to north
      return (current[0]-1,current[1])
  elif direction == "J": # 90-degree bend connecting north and west
    if current[0]-previous[0]==1 and current[1]==previous[1]: # came from north, go to west
      return (current[0],current[1]-1)
    elif current[0]==previous[0] and current[1]-previous[1]==1: # came from west, go to north
      return (current[0]-1,current[1])
  elif direction == "7": # 90-degree bend connecting south and west
    if current[0]==previous[0] and current[1]-previous[1]==1: # came from west, go to south
      return (current[0]+1,current[1])
    elif previous[0]-current[0]==1 and current[1]==previous[1]: # came from south, go to west
      return (current[0],current[1]-1)
  elif direction == "F": # 90-degree bend connecting south and east
    if current[0]==previous[0] and previous[1]-current[1]==1: # came from east, go to south
      return (current[0]+1,current[1])
    elif previous[0]-current[0]==1 and current[1]==previous[1]: # came from south, go to east
      return (current[0],current[1]+1)
  return (-1,-1) # not possible or somet

# the current and previous position during moving in two different directions in the loop
curr_pos_dir_1 = (0,0)
curr_pos_dir_2 = (0,0)
last_pos_dir_1 = (0,0)
last_pos_dir_2 = (0,0)

# find the start position
for i in range(line_count):
  s_pos = lines[i].find("S")
  if s_pos != -1:
    # store the position of S as the previous position in both the tracks
    last_pos_dir_1 = (i,s_pos)
    last_pos_dir_2 = (i,s_pos)
    # find the moving directions from the start
    found_count = 0
    for k in range(i-1,i+2):
      if k<0 or k>=line_count:
        continue
      for l in range(s_pos-1,s_pos+2):
        if k==i and l == s_pos:
          continue
        if l<0 or l>=line_len:
          continue
        legit_move = move(last_pos_dir_1,(k,l)) != (-1,-1)
        if legit_move and found_count == 0: # first legit move
          found_count += 1
          curr_pos_dir_1 = (k,l) # store as current position of the 1st track
        elif legit_move and found_count == 1: # second legit move
          found_count += 1
          curr_pos_dir_2 = (k,l) # store as current position of the 2nd track
        elif legit_move:
          print("How come?")
    break

# progress = lines.copy() # to debug the progress
step = 1
while curr_pos_dir_1 != curr_pos_dir_2:
  new_pos = move(last_pos_dir_1,curr_pos_dir_1)
  last_pos_dir_1 = curr_pos_dir_1
  curr_pos_dir_1 = new_pos
  new_pos = move(last_pos_dir_2,curr_pos_dir_2)
  last_pos_dir_2 = curr_pos_dir_2
  curr_pos_dir_2 = new_pos
  step += 1
  # debug the progress:
  # progress[curr_pos_dir_1[0]]=progress[curr_pos_dir_1[0]][:curr_pos_dir_1[1]] +str(step)+ progress[curr_pos_dir_1[0]][curr_pos_dir_1[1]+1:]
  # progress[curr_pos_dir_2[0]]=progress[curr_pos_dir_2[0]][:curr_pos_dir_2[1]] +str(step)+ progress[curr_pos_dir_2[0]][curr_pos_dir_2[1]+1:]

# print out the loop / debug the progress
# for l in progress:
#   print(l.strip())

print("It takes "+str(step)+" steps to get to the farthest point from the starting point.")

# https://adventofcode.com/2023/day/16#part2
# Day 16: The Floor Will Be Lava

filename = "inputs/day16-input.txt"
# filename = "inputs/day16-input-test.txt"

# constants
empty_space = "."
mirror_up, mirror_down = "/", "\\"
split_vertical, split_horizontal = "|", "-"
is_energized, not_energized = "#", "."
up, down, left, right = "up", "down", "left", "right"

energized = [] # matrix of tiles where to mark which ones are energized
visits = set() # the positions and directions that have been already visited
backlog = [] # keep the positions and directions that need yet to be visited


def move(position, direction):
  if position[0] >= line_count or position[1] >= line_len or position[0] < 0 or position[1] < 0:
    return
  energized[position[0]][position[1]] = is_energized
  if (position, direction) in visits:
    # the same position has already been visited from the same direction, do not go to cycle
    return

  visits.add((position, direction))
  tile = lines[position[0]][position[1]]

  if tile == empty_space \
    or (tile == split_horizontal and direction in [left,right]) \
    or (tile == split_vertical and direction in [up,down]):
    # move a step in the same direction
    if direction == right:
      position = (position[0],position[1]+1)
    elif direction == left:
      position = (position[0],position[1]-1)
    elif direction == down:
      position = (position[0]+1,position[1])
    elif direction == up:
      position = (position[0]-1,position[1])
    backlog.append((position,direction))
  elif direction == right and tile == mirror_up or direction == left and tile == mirror_down:
    # change direction and move up
    direction = up
    position = (position[0]-1,position[1])
    backlog.append((position,direction))
  elif direction == right and tile == mirror_down or direction == left and tile == mirror_up:
    # change direction and move down
    direction = down
    position = (position[0]+1,position[1])
    backlog.append((position,direction))
  elif direction == down and tile == mirror_up or direction == up and tile == mirror_down:
    # change direction and move left
    direction = left
    position = (position[0],position[1]-1)
    backlog.append((position,direction))
  elif direction == down and tile == mirror_down or direction == up and tile == mirror_up:
    # change direction and move right
    direction = right
    position = (position[0],position[1]+1)
    backlog.append((position,direction))

  elif tile == split_vertical and direction in [left,right]:
    # when moving left or right and a vertical split occurs, you go both up and down simultaneously
    direction = up
    new_position = (position[0]-1,position[1])
    backlog.append((new_position,direction))
    direction = down
    new_position = (position[0]+1,position[1])
    backlog.append((new_position,direction))
  elif tile == split_horizontal and direction in [up,down]:
    # when moving up or down and a horizontal split occurs, you go both left and right simultaneously
    direction = left
    new_position = (position[0],position[1]-1)
    backlog.append((new_position,direction))
    direction = right
    new_position = (position[0],position[1]+1)
    backlog.append((new_position,direction))


def calculate_energized(position, direction):
  global energized,backlog,visits
  energized = [ [not_energized]*line_len for i in range(line_count)]
  backlog = []
  visits.clear()

  backlog.append((position,direction))
  while len(backlog) >= 1:
    position,direction = backlog.pop(-1)
    move(position,direction)

  return "".join(["".join(e) for e in energized]).count(is_energized)

###
with open(filename, "r") as f:
  lines = [l.rstrip("\n") for l in f]

line_len = len(lines[0])
line_count = len(lines)

max_count_of_energized = 0
# find how many tiles are energized when starting from the left or right side
for i in range(line_len):
  # find the number of energized tiled if started from left side
  current_position = (i,0)
  current_direction = right
  count_of_energized = calculate_energized(current_position,current_direction)
  max_count_of_energized = max(max_count_of_energized,count_of_energized)
  # find the number of energized tiled if started from right side
  current_position = (i,line_len-1)
  current_direction = left
  count_of_energized = calculate_energized(current_position,current_direction)
  max_count_of_energized = max(max_count_of_energized,count_of_energized)

# find how many tiles are energized when starting from the top or bottom
for i in range(line_len):
  # find the number of energized tiled if started from the top side
  current_position = (0,i)
  current_direction = down
  count_of_energized = calculate_energized(current_position,current_direction)
  max_count_of_energized = max(max_count_of_energized,count_of_energized)
  # find the number of energized tiled if started from the bottom side
  current_position = (line_count-1,i)
  current_direction = up
  count_of_energized = calculate_energized(current_position,current_direction)
  max_count_of_energized = max(max_count_of_energized,count_of_energized)


print(max_count_of_energized,"tiles is the maximum number of tiles that can end up being energized.")

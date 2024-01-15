# https://adventofcode.com/2023/day/16
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
  # if out of range then nothing to do
  if position[0] >= line_count or position[1] >= line_len or position[0] < 0 or position[1] < 0:
    return
  # if the same position has already been visited from the same direction, do not repeat it
  if (position, direction) in visits:
    return

  energized[position[0]][position[1]] = is_energized # mark this visited tile as energized
  visits.add((position, direction)) # remember that this tile has been visited from this direction

  tile = lines[position[0]][position[1]] # tile to decide the action
  if tile == empty_space \
    or (tile == split_horizontal and direction in [left,right]) \
    or (tile == split_vertical and direction in [up,down]):
    # step further in the same direction
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


###
with open(filename, "r") as f:
  lines = [l.rstrip("\n") for l in f]

line_len = len(lines[0])
line_count = len(lines)
energized = [ [not_energized]*line_len for i in range(line_count)]

# initial position and moving direction
current_position = (0,0)
current_direction = right
# put the initial step to the backlog
backlog.append((current_position,current_direction))

# keep moving as long as there are steps in the backlog
while len(backlog) >= 1:
  # take the current position and direction from the backlog...
  current_position,current_direction = backlog.pop(-1)
  # ... and do the move
  move(current_position,current_direction)

# count how many of the tiles are energized now
count_of_energized = "".join(["".join(e) for e in energized]).count(is_energized)
print(count_of_energized,"tiles end up being energized.")

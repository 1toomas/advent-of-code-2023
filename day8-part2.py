# https://adventofcode.com/2023/day/8#part2
# Day 8: Haunted Wasteland

filename = "inputs/day8-input.txt"
# filename = "inputs/day8-part2-input-test.txt"

nodes = dict()
instructions = ""

def find_step_count(start_node):
  step = 0
  current_node = start_node
  instr_pos = 0
  while True:
    if current_node[2] == "Z":
      break
    step += 1
    current_node = nodes[current_node][int(instructions[instr_pos])]
    instr_pos = (instr_pos+1) % len(instructions)
  return step

###
with open(filename, "r") as f:
  lines = f.readlines()

# store instructions so that left is 0 and right is 1 - this way these can be used directly to get next node
instructions = lines[0].translate(str.maketrans("LR","01")).strip()

# store nodes as dictionary to be easy to get the label of the next node
for i in range(len(lines)-2):
  nodes[lines[i+2][0:3]] = (lines[i+2][7:10], lines[i+2][12:15])

# find all start nodes, i.e. the ones that end with A
start_nodes = []
for n in nodes:
  if n[2] == "A":
    start_nodes.append(n)

concurrent_tracks = len(start_nodes) # the number of tracks to navigate simultaneously

min_steps = []
for i in range(concurrent_tracks):
  min_steps.append(find_step_count(start_nodes[i]))

import math
# use least common multiple
step_count = math.lcm(*min_steps)

print(str(step_count)+" steps are required to reach to nodes that all are ending with Z.")

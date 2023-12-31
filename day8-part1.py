# https://adventofcode.com/2023/day/8
# Day 8: Haunted Wasteland

filename = "inputs/day8-input.txt"
# filename = "inputs/day8-input-test2.txt"

###
with open(filename, "r") as f:
  lines = f.readlines()

# store instructions so that left is 0 and right is 1 - this way these can be used directly to get next node
instructions = lines[0].translate(str.maketrans("LR","01")).strip()

# store nodes as dictionary to be easy to get the label of the next node
nodes = dict()
for i in range(len(lines)-2):
  nodes[lines[i+2][0:3]] = (lines[i+2][7:10], lines[i+2][12:15])

step = 0
current_node = "AAA"
instr_pos = 0
while True:
  if current_node == "ZZZ":
    break
  step += 1
  current_node = nodes[current_node][int(instructions[instr_pos])]
  instr_pos = (instr_pos+1) % len(instructions)

print(str(step)+" steps are required to reach ZZZ.")

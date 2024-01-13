# https://adventofcode.com/2023/day/13
# Day 13: Point of Incidence

filename = "inputs/day13-input.txt"
# filename = "inputs/day13-input-test1.txt"

def find_mirror_row(pattern):
  # find the number of rows before the mirror in the pattern
  mirror_location = 0 # return 0 if no mirror found
  for i in range(len(pattern)-1):
    # can the mirror be here?
    if pattern[i] == pattern[i+1]:
      # compare other lines as well
      is_mirror = True
      for j in range(min(i,len(pattern)-i-2)):
        if pattern[i-j-1] == pattern[i+1+j+1]:
          continue
        else:
          is_mirror = False
          break
      if is_mirror:
        mirror_location = i+1
        break
  return mirror_location

def find_mirrors(pattern):
  # find the sum of the notes of the given pattern
  # find the mirror row
  mirror_row = find_mirror_row(pattern)
  if mirror_row == 0: # need to look for the mirror in columns only if it wasn't in the rows
    # transpose the pattern
    transposed_pattern = [''.join(s) for s in zip(*pattern)]
    # find the mirror column, i.e. mirror row of the transposed pattern
    mirror_col = find_mirror_row(transposed_pattern)
  else:
    mirror_col = 0
  print(mirror_row,mirror_col) # debug
  return mirror_col + 100*mirror_row

###
with open(filename, "r") as f:
  lines = [l.rstrip("\n") for l in f]

sum_of_pattern_notes = 0
current_pattern = []
tmp = 0 # debug
for l in lines:
  if len(l) > 0:
    current_pattern.append(l)
  else:
    tmp += 1 # debug
    print("Pattern no",tmp) # debug
    sum_of_pattern_notes += find_mirrors(current_pattern)
    current_pattern = []

if current_pattern != []: # if the last pattern was not processed
  sum_of_pattern_notes += find_mirrors(current_pattern)

print("The sum of all pattern notes is "+str(sum_of_pattern_notes))

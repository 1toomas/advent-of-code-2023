# https://adventofcode.com/2023/day/13#part2
# Day 13: Point of Incidence

filename = "inputs/day13-input.txt"
# filename = "inputs/day13-input-test1.txt"

def compare_rows(row1,row2):
  # compares two rows. returns pair: (number of differences, position of the difference)
  diff_count = 0
  diff_pos = -1
  for i in range(len(row1)): # compare positions one by one
    if row1[i] != row2[i]:
      diff_count += 1
      diff_pos = i
      if diff_count > 1: # no need to look further as 2 differences are too many already
        break
  return (diff_count, diff_pos)

def find_mirror_row_and_smudge(pattern):
  # find the number of rows before the mirror in the pattern and the position of the smudge (there is exactly one smudge)
  mirror_location = 0 # return 0 if no mirror found; otherwise number of rows before the mirror (==mirror row + 1, i.e. starts from 1)
  smudge_pos_row = -1 # the row of the smudge (start from 0)
  smudge_pos_col = -1 # the position of the smudge in the row (start from 0)
  for i in range(len(pattern)-1):
    # can the mirror be here?
    difference = compare_rows(pattern[i], pattern[i+1])
    if difference[0] == 1:
      # if the smudge was in this row then remember it
      smudge_pos_row = i
      smudge_pos_col = difference[1]
    if difference[0] <= 1:
      # compare other lines as well
      is_mirror = True
      other_difference = (0,0)
      for j in range(min(i,len(pattern)-i-2)):
        # if the smudge was in either of these rows then all the other matching rows need to have exaxt match
        if  difference[0] + other_difference[0] == 1:
          if pattern[i-j-1] == pattern[i+1+j+1]:
            continue
          else:
            is_mirror = False
            break
        else:
          # if the next to each other rows were the same then the smudge may be in one of the matching rows
          other_difference = compare_rows(pattern[i-j-1], pattern[i+1+j+1])
          if other_difference[0] == 1:
            # if the smudge was in this row then remember it
            smudge_pos_row = j
            smudge_pos_col = other_difference[1]
          if other_difference[0] <= 1:
            continue
          else:
            is_mirror = False
            break
      if is_mirror:
        mirror_location = i+1
        break
  return (mirror_location,smudge_pos_row,smudge_pos_col)

def find_mirror_row(pattern):
  # find the number of rows before the mirror in the pattern and the position of the smudge (there is exactly one smudge)
  mirror_location = 0 # return 0 if no mirror found; otherwise number of rows before the mirror (==mirror row + 1, i.e. starts from 1)
  for i in range(len(pattern)-1):
    # can the mirror be here?
    difference = compare_rows(pattern[i], pattern[i+1])
    if difference[0] <= 1:
      # compare other lines as well
      is_mirror = True
      other_difference = (0,0)
      for j in range(min(i,len(pattern)-i-2)):
        # if the smudge was in either of these rows then all the other matching rows need to have exaxt match
        if  difference[0] + other_difference[0] == 1:
          if pattern[i-j-1] == pattern[i+1+j+1]:
            continue
          else:
            is_mirror = False
            break
        else:
          # if the next to each other rows were the same then the smudge may be in one of the matching rows
          other_difference = compare_rows(pattern[i-j-1], pattern[i+1+j+1])
          if other_difference[0] <= 1:
            continue
          else:
            is_mirror = False
            break
      # if the mirror was found with no smudges then this is not a valid case, so continue
      if is_mirror and difference[0] + other_difference[0] == 1:
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
  return mirror_col + 100*mirror_row

###
with open(filename, "r") as f:
  lines = [l.rstrip("\n") for l in f]

sum_of_pattern_notes = 0
current_pattern = []
for l in lines:
  if len(l) > 0:
    current_pattern.append(l)
  else:
    sum_of_pattern_notes += find_mirrors(current_pattern)
    current_pattern = []

if current_pattern != []: # if the last pattern was not processed
  sum_of_pattern_notes += find_mirrors(current_pattern)

print("The sum of all pattern notes is "+str(sum_of_pattern_notes))

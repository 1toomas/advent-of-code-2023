# https://adventofcode.com/2023/day/12
# Day 12: Hot Springs

import re

filename = "inputs/day12-input.txt"
# filename = "inputs/day12-input-test.txt"

def find_damaged_groups(record):
  # find the lengths of all damaged groups in the given record
  return [len(x) for x in re.findall("#+", record)]

def replace_pos(in_str, pos):
  # replace the char in pos of string with #
  return in_str[:pos] + "#" + in_str[pos+1:]

### read lines to a list of lists containing condition records and their damaged string groups
with open(filename, "r") as f:
  lines = [l.rstrip(r"\n").split(" ") for l in f]

sum_of_counts = 0
for l in lines:
  current_record = l[0]
  # put the list of group lengths checks into a list
  group_sizes = [int(n) for n in l[1].split(",")]
  # find the damaged groups in the record, calculate the lenght of each
  sizes_in_record = find_damaged_groups(current_record)
  if group_sizes == sizes_in_record:
    continue
  # find all the positions of ?, i.e. the ones where a repöacement can be done
  questionmarks = [m.start() for m in re.finditer(r"\?", current_record)]
  # the number of ? -> # replacments to do = (sum of lengths of damaged groups) - (sum of #-s in the record)
  replacements = sum(group_sizes) - sum(sizes_in_record)

  # iterate over all possible combinations of replacemets
  from itertools import combinations
  all_replace_combinations = combinations(questionmarks, replacements)
  # print("alustame reaga",current_record,"selles on gruppide algseis",sizes_in_record,"ja kontroll", group_sizes) #debug
  for r in all_replace_combinations:
    replaced_record = current_record
    for p in r:
      replaced_record = replace_pos(replaced_record, p)
    damaged_groups_in_replaced_record = find_damaged_groups(replaced_record)
    # print(replaced_record, damaged_groups_in_replaced_record)
    if damaged_groups_in_replaced_record == group_sizes:
      # print("jess, juurde",replaced_record, damaged_groups_in_replaced_record)
      sum_of_counts += 1

print("The sum of counts of all different arrangements is "+str(sum_of_counts))

# https://adventofcode.com/2023/day/9
# Day 9: Mirage Maintenance

filename = "inputs/day9-input.txt"
# filename = "inputs/day9-input-test.txt"

###
with open(filename, "r") as f:
  lines = f.readlines()

def calculate_diffs(num_list):
  diffs_list = []
  for i in range(len(num_list)-1):
    diffs_list.append(num_list[i+1]-num_list[i])
  return diffs_list

def find_extrapolate(num_list):
  all_zeros = True
  for i in num_list:
    if i != 0:
      all_zeros = False
      break
  if all_zeros:
    return 0
  else:
    next_num_list = calculate_diffs(num_list)
    return num_list[-1] + find_extrapolate(next_num_list)

extrapolates_sum = 0
for l in lines:
  num_row = list(map(int,l.split()))
  extrapolates_sum += find_extrapolate(num_row)


print("The sum of these extrapolated values is "+str(extrapolates_sum))

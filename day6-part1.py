# https://adventofcode.com/2023/day/6
# Day 6: Wait For It

import time

filename = "inputs/day6-input.txt"
# filename = "inputs/day6-input-test.txt"

with open(filename, "r") as f:
  lines = f.readlines()

# times = lines[0].split(":")[1].split()
# distances = lines[1].split(":")[1].split()
# times = list(map(int, lines[0].split(":")[1].split()))
times = [int(x) for x in lines[0].split(":")[1].split()]
distances = [int(x) for x in lines[1].split(":")[1].split()]
races_count = len(times)

start_time = time.time()

# brute force
faster_races = []
for i in range(races_count):
  faster_count = 0
  for speed in range(times[i]):
    distance_travelled = speed * (times[i]-speed)
    if distance_travelled > distances[i]:
      faster_count += 1
  faster_races.append(faster_count)

product = 1
for i in range(len(faster_races)):
  product *= faster_races[i]
print("The numbers of ways you can beat the record multiplied together is "+str(product))
print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
### calcuated ##
# find the first better result
faster_races.clear()
faster_races_count = 0
for i in range(races_count):
  faster_count = 0
  for speed in range(times[i]):
    distance_travelled = speed * (times[i]-speed)
    if distance_travelled > distances[i]:
      faster_races_count = (times[i])-speed+-(speed-1)
      break
  faster_races.append(faster_races_count)

print("The numbers of ways you can beat the record multiplied together is "+str(product))
print("--- %s seconds ---" % (time.time() - start_time))

# https://adventofcode.com/2023/day/6#part2
# Day 6: Wait For It

import time

filename = "inputs/day6-input.txt"
# filename = "inputs/day6-input-test.txt"

with open(filename, "r") as f:
  lines = f.readlines()

times = lines[0].split(":")[1].split()
distances = lines[1].split(":")[1].split()

the_time_str = ""
for xs in times:
  the_time_str += xs
the_time = int(the_time_str)
the_distance_str = ""
for xs in distances:
  the_distance_str += xs
the_distance = int(the_distance_str)

# times = list(map(int, lines[0].split(":")[1].split()))
# times = [int(x) for x in lines[0].split(":")[1].split()]
# distances = [int(x) for x in lines[1].split(":")[1].split()]
# races_count = len(times)


start_time = time.time()
### calcuated ##
# find the first better result
faster_races_count = 0
for speed in range(int(the_time)):
  distance_travelled = speed * (the_time-speed)
  if distance_travelled > the_distance:
    faster_races_count = (the_time)-speed+-(speed-1)
    break

print("The numbers of ways you can beat the record multiplied together is "+str(faster_races_count))
print("--- %s seconds ---" % (time.time() - start_time))

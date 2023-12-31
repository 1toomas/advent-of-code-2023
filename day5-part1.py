# https://adventofcode.com/2023/day/5
# Day 5: If You Give A Seed A Fertilizer

# filename = "inputs/day5-input.txt"
filename = "inputs/day5-input-test.txt"

f = open(filename, "r")
lines = f.readlines()
line_count = len(lines)

onemap = []
bigmap = []
for l in lines:
  if l.find("seeds:") != -1:
    seeds = l.split(":")[1].split()
  elif l.find("map:") != -1:
    # store if exists
    if len(onemap) > 0:
      onemap.sort()
      bigmap.append(onemap.copy())
    # start anew
    onemap.clear()
  elif len(l.strip()) > 0:
    row = l.split()
    mapping = [int(row[1])] # start of the source interval
    mapping.extend([int(row[1])+int(row[2])-1]) # end of the source interval
    mapping.extend([int(row[0])]) # start of the destination interval
    onemap.append(mapping)

# the last map also needs to be stored
if len(onemap) > 0:
  onemap.sort()
  bigmap.append(onemap.copy())

locations = []
# find locations for every seed
for ss in seeds:
  s = int(ss)
  # perform conversions step by step to find location of a seed
  for m in bigmap:
    # find the correct range to use conversion for the seed
    found = False
    for r in m:
      # position for the next comes from conversion
      if s >= r[0] and s <= r[1]:
        pos = r[2]+(s-r[0])
        found = True
    # no conversion found, i.e. direct mapping for position
    if not found:
      pos = s
    # outcome of this conversion step is input for the next step
    s = pos

  # store the location for this seed
  locations.append(s)

print(seeds) # DEBUG
print(locations) # DEBUG
nearest = min(locations)

print("The nearest location is "+str(nearest))

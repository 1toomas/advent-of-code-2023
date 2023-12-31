# https://adventofcode.com/2023/day/4
# Scratchcards

filename = "inputs/day4-input.txt"
# filename = "inputs/day4-input-test.txt"

f = open(filename, "r")
lines = f.readlines()

points = 0
for l in lines:
  parts = l.split(":")[1].split("|")
  winning = parts[0].split()
  my_card = parts[1].split()
  card_points = 0
  for n in my_card:
    if n in winning:
      card_points = max(card_points*2,1)
  points += card_points

print("Pile of scratchcards is worth: "+str(points))

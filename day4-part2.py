# https://adventofcode.com/2023/day/4#part2
# Scratchcards

filename = "inputs/day4-input.txt"
# filename = "inputs/day4-input-test.txt"

f = open(filename, "r")
lines = f.readlines()
line_count = len(lines)

card_copies = dict()
row_matches = [] # how many matches are for the row/card
row_copies = []  # how many copies of thw row/card you win

# initiate all cards with 1 copy
for i in range(line_count):
  row_copies.extend([1])

for i in range(line_count):
  parts = lines[i].split(":")[1].split("|")
  winning = parts[0].split()
  my_card = parts[1].split()

  # find matches in the row
  row_matches.extend([0]) # initiate with 0 matches
  for n in my_card:
    if n in winning:
      row_matches[i] += 1
  # add a copy of as many next rows as there was matches for this row
  for j in range(row_matches[i]):
    row_copies[i+j+1] += row_copies[i]

# count all the cards
cards_count = 0
for i in range(line_count):
  cards_count += row_copies[i]

print("You end up with "+str(cards_count)+" scratchcards in total.")

# https://adventofcode.com/2023/day/2
# Cube Conundrum

filename = "inputs/day2-input.txt"
# filename = "inputs/day2-input-test1.txt"

import re

# constants of red, green, and blue to test if the game is possible with
c_red = 12
c_green = 13
c_blue = 14


def line_value(line):
  digits = re.findall("\d", line)
  if len(digits) > 0:
    return int(digits[0] + digits[-1])
  else:
    return 0

f = open(filename, "r")
lines = f.readlines()

sum_possible = 0
sum_power_of_min_set = 0
for l in lines:
  colon_split = re.split(":", l)
  game_no = int(re.split("\s", colon_split[0])[1])
  grabbed_handfuls = re.split(";", colon_split[1])
  possible = True
  min_red = 0
  min_green = 0
  min_blue = 0
  for h in grabbed_handfuls:
    red = re.search("\d+ red", h)
    if red != None:
      count = int(re.findall("\d+", red.group())[0])
      possible = possible and (count <= c_red)
      min_red = max(min_red, count)
    blue = re.search("\d+ blue", h)
    if blue != None:
      count = int(re.findall("\d+", blue.group())[0])
      possible = possible and (count <= c_blue)
      min_blue = max(min_blue, count)
    green = re.search("\d+ green", h)
    if green != None:
      count = int(re.findall("\d+", green.group())[0])
      possible = possible and (count <= c_green)
      min_green = max(min_green, count)
    if not possible:
      print(grabbed_handfuls)
      print("game "+str(game_no)+" not possible")
  if possible:
    sum_possible += game_no
  power_of_min_set = min_red * min_green * min_blue
  sum_power_of_min_set += power_of_min_set
  if power_of_min_set == 0:
    print(grabbed_handfuls)
    print("game "+str(game_no)+" zero "+"(red "+min_red+", blue "+min_blue+", green"+ min_green + ")")


print("Sum of IDs of games that would have been possible: " + str(sum_possible))
print("Sum of powers of minimal set of cubes in all games: " +str(sum_power_of_min_set))

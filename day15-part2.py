# hhttps://adventofcode.com/2023/day/15#part2
# Day 15: Lens Library

filename = "inputs/day15-input.txt"
# filename = "inputs/day15-input-test2.txt"
equals_sign,dash = "=","-"

def calculate_hash(input_string):
  current_value = 0
  for c in input_string:
    # Determine the ASCII code for the current character of the string.
    # Increase the current value by the ASCII code you just determined.
    current_value += ord(c)
    # Set the current value to itself multiplied by 17.
    current_value *= 17
    # Set the current value to the remainder of dividing itself by 256.
    current_value %= 256
  return current_value


###
with open(filename, "r") as f:
  steps = f.readline().rstrip("\n").split(",")

lens_boxes = dict() # boxes to store the lens
focal_lenghts = dict() # the focal lengths corresponding to the lenses in boxes

# perform the steps in the initialization sequence
for s in steps:
  if equals_sign in s:
    # this instruction contains equal sign, so need to add
    [label,focal] = s.split(equals_sign) # [0] is the label, [1] is the focal length
    box_no = calculate_hash(label) # the box is determined by the hash of the label
    box_content = lens_boxes.get(box_no)
    if box_content == None:
      # if the box with such label is empty then both the label and focal length is the only item in the box
      lens_boxes[box_no] = [label]
      focal_lenghts[box_no] = [int(focal)]
    elif label in lens_boxes[box_no]:
      # if the box contains lens with such label then replace
      # need to update only the focal length
      new_focal_box = focal_lenghts[box_no]
      new_focal_box[box_content.index(label)] = int(focal)
      focal_lenghts[box_no] = new_focal_box
    else:
      # if such label is not in the box then add both the label and focal length
      box_content.append(label)
      lens_boxes[box_no] = box_content
      # take the content of focal length's box, append the length's item, and update the box
      new_focal_box = focal_lenghts[box_no]
      new_focal_box.append(int(focal))
      focal_lenghts[box_no] = new_focal_box
  elif dash in s:
    # this instruction contains dash, so need to remove
    label = s.split(dash)[0] # need only the label
    box_no = calculate_hash(label) # the box is determined by the hash of the label
    box_content = lens_boxes.get(box_no)
    if box_content != None and label in box_content:
      # first remove the focal length as here the position of the label in the list is needed
      new_focal_box = focal_lenghts[box_no] # take the content of focal length's box
      new_focal_box.pop(box_content.index(label)) # remove the length's item
      focal_lenghts[box_no] = new_focal_box # update the box
      # remove the label
      box_content.remove(label)
      lens_boxes[box_no] = box_content

# add up the focusing power of all of the lenses
sum_of_focusing_power = 0
for k in focal_lenghts.keys(): # the numbers of the boxes that contain something
  # print(k)
  # print(lens_boxes[k])
  # print(focal_lenghts[k])
  box_content = focal_lenghts[k] # the focal lenghts of the lens in that box
  for i in range(len(box_content)):
    # The focusing power of a single lens is the result of multiplying together:
    #  One plus the box number of the lens in question.
    #  The slot number of the lens within the box: 1 for the first lens, 2 for the second lens, and so on.
    #  The focal length of the lens.
    sum_of_focusing_power += (k+1) * (i+1) * box_content[i]

print("The focusing power of the resulting lens configuration "+str(sum_of_focusing_power))

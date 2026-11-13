from math import ceil

length = 50
width = 45

area = length * width
total_boxes = ceil(area / 12 + ((0.1 * area) / 12))

print(f"For a room with an area of {area} square feet, you need {total_boxes} boxes of tiles")
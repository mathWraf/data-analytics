from math import sqrt

x1 = 21
x2 = 50
y1 = 35
y2 = 72

dist = sqrt((x2-x1)**2 + (y2-y1)**2)

print(f"The distance between points ({x1},{y1}) and ({x2},{y2}) is {dist:.2f}")
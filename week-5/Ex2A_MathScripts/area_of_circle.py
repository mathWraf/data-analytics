from math import pi

diameter = int(input("What is the diameter of the circle: "))
radius = diameter/2
area = pi * (radius**2)

print(f"The area of a circle with radius {radius} is {area:.2f}")

'''
A possible pitfall of using input() is an error being thrown if the value of the input function 
isn't approapriately type casted.
'''
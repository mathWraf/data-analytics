import random
import math
import statistics

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi
area = pi * (radius ** 2)

print("_Experimenting with a subset of integers 1-100:")
print(f"Sum of 75 sample values: {math.fsum(vals_sample)}") # adds all of the sample values in vals_sample list together
print(f"Average of 75 sample values: {statistics.mean(vals_sample)}") # finds the average of the vals_sample list
print(f"Mode of 75 sample values: {statistics.mode(vals_sample)}") # finds the mode of the vals_sample list
print()
print("_Experimenting with a superset of 200 values, integers 1-100:")
print(f"Average of 200 sample values: {statistics.mean(vals_choices)}") # finds the average of the vals_choices list
print(f"Median of 200 sample values: {statistics.median(vals_choices)}") # finds the median of the vals_choices list
print(f"Standard deviation of 200 sample values: {statistics.stdev(vals_choices)}") # finds the standard deviation of the vals_choices list
print(f"Variance of 200 sample values: {statistics.variance(vals_choices)}") # finds the variance of the vals_choices list
print()
print("_Modeling a random circle:")
print(f"Radius = {radius}, area = {math.ceil(area)}") # finds the rounded up area of the circle
print(f"Radius = {radius}, area = {math.floor(area)}") # finds the rounded down area of the circle
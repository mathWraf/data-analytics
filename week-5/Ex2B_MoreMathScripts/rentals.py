from math import ceil

day = 1
tourists = 38
total_vans = ceil(tourists/15)
cost = 250 * day * total_vans
cost_per_person = 250 / 15

print(f"Cost Per Person: {cost_per_person:.2f}")
print(f"Total Collected: {cost_per_person * tourists:.2f}")
print(f"Total Cost for Vans: {cost:.2f}")
print("There is leftover money because the batch that had less than 15 passengers had to pay more, per person, for their van.")



import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

#4a
print(f"Product of the Day: {random.choice(products)}")

#4b
print(random.sample(products,k=3))

#4c
random.shuffle(products)
print(products)

#4d
print(f"Daily Transaction Count: {random.randint(50,300)}")
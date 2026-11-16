cities = ["Chicago", "Budapest", "New Orleans", "Athens", "Vienna"]

for i, city in enumerate(cities, start=1):
    
    if i == 1:
        print(f"{i}. {city} <- top pick!")
    else:
        print(f"{i}. {city}")
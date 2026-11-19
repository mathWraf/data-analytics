class Restaurant:
    
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")
        
    def rest_open(self):
        print(f"{self.rest_name} is open.")
        
        
        
rest1 = Restaurant("Krispin' Kreme", "Donuts & Coffee")
rest2 = Restaurant("Steak N' Ate", "Burgers & Shakes")

rest1.describe_rest()
rest1.rest_open()
print()
rest2.describe_rest()
rest2.rest_open()      

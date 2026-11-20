class Restaurant:
    
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []
        
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")
        
    def rest_open(self):
        print(f"{self.rest_name} is open.")
        
    def add_num_served(self, served):
        self.number_served += served
        
    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")
        
    def customer_rating(self, rating):
        
        if rating in [1,2,3,4,5]:
            self.customer_ratings.append(rating)
            print(f"Your rating was {rating}. The average rating for this restaurant is {sum(self.customer_ratings)/len(self.customer_ratings)}")
        else:
            print("Please enter a rating from 1-5.")
    
rest1 = Restaurant("Krispin' Kreme", "Donuts & Coffee")
rest2 = Restaurant("Steak N' Ate", "Burgers & Shakes")

#6a
rest1.print_num_served()
rest2.print_num_served()
 
rest1.add_num_served(53)
rest2.add_num_served(47)    

rest1.add_num_served(79)
rest2.add_num_served(58)    

rest1.print_num_served()
rest2.print_num_served()

#6b
rest1.customer_rating(5)
rest2.customer_rating(4)

rest1.customer_rating(4)
rest2.customer_rating(4)

rest1.customer_rating(4)
rest2.customer_rating(5)

rest1.customer_rating(3)
rest2.customer_rating(5)

#6c
rest1.customer_rating(6)
rest2.customer_rating("")

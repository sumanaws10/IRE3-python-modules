
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

# Main body of the program        

# Creating an instance of Restaurant
restaurant = Restaurant("Food Haven", "Italian")

# Printing individual attributes
print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)

# Calling methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Stretch and Challenge
restaurant1 = Restaurant("Taste of India", "Indian")
restaurant2 = Restaurant("Sushi Palace", "Japanese")
restaurant3 = Restaurant("Mexican Fiesta", "Mexican")

print(restaurant2.number_served)

restaurant2.set_number_served(100)

print(restaurant2.number_served)

restaurant2.increment_number_served(20)

print(restaurant2.number_served)

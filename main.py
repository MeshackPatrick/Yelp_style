from Restaurant import Restaurant
from Customer import Customer

# Creating instances
restaurant1 = Restaurant("JAVA COFFEE HOUSE")
restaurant2 = Restaurant("ARTCAFFEE")

customer1 = Customer("Shercie", "Wesh")
customer2 = Customer("Memer", "Shercie")

# Adding reviews
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

# Accessing methods
print(restaurant1.name())
print(customer1.full_name())
print(customer2.restaurant())
print(restaurant1.average_star_rating())
print(restaurant2.name())
print(customer2.full_name())
print(customer2.restaurant())
print(restaurant1.average_star_rating())

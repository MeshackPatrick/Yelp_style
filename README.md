# Yelp_style
## Description

This project contains classes for handling Customer, Restaurant, and Review entities, along with various methods to manage their interactions and attributes.

## Classes and Methods

Customer Class
Customer __init__()

Initializes a Customer instance with a given name and family name.
Customer given_name()

Returns the customer's given name.
Can be changed after the customer is created.
Customer family_name()

Returns the customer's family name.
Can be changed after the customer is created.
Customer full_name()

Returns the full name of the customer (given name + family name).
Customer all()

Returns a list of all customer instances.
Customer restaurants()

Returns a unique list of all restaurants a customer has reviewed.
Customer add_review(restaurant, rating)

Creates a new review and associates it with the customer and restaurant.
Requires a restaurant object and a star rating as an integer.
Customer num_reviews()

Returns the total number of reviews that a customer has authored.
Customer find_by_name(name) (class method)

Given a full name, returns the first customer whose full name matches.
Customer find_all_by_given_name(name) (class method)

Given a given name, returns a list containing all customers with that given name.
Restaurant Class
Restaurant __init__()

Initializes a Restaurant instance with a name.
Restaurant name()

Returns the restaurant's name.
Restaurant reviews()

Returns a list of all reviews for that restaurant.
Restaurant customers()

Returns a unique list of all customers who have reviewed the restaurant.
Restaurant average_star_rating()

Returns the average star rating for the restaurant based on its reviews.
Review Class
Review __init__()

Initializes a Review instance with a customer, restaurant, and a rating.
Review rating()

Returns the rating for a restaurant.
Review customer()

Returns the customer object for that review.
Review restaurant()

Returns the restaurant object for that given review.
Review all()

Returns a list of all reviews.
Usage

To use this library, create instances of the Customer, Restaurant, and Review classes and utilize their respective methods to manage and retrieve information about customers, restaurants, and reviews.

Example usage:

python
# Creating instances
customer1 = Customer("wesh", "mesh")
restaurant1 = Restaurant("Food Paradise")

# Adding a review
customer1.add_review(restaurant1, 4)

# Retrieving information
customer1_name = customer1.full_name()
restaurant1_name = restaurant1.name()
restaurant1_avg_rating = restaurant1.average_star_rating()

# Finding customers by name
matching_customers = Customer.find_all_by_given_name("mesh")

# Getting customer's reviewed restaurants
customer1_reviewed_restaurants = customer1.restaurants()
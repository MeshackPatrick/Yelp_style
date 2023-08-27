from Review import Review


class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self._review = []
        Customer.all_customers.append(self)

    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def restaurant(self):
        reviewed_restaurant = set()
        for review in self._review:
            reviewed_restaurant.add(review.restaurant())
        return list(reviewed_restaurant)

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self._review.append(new_review)
        restaurant.add_review(new_review)

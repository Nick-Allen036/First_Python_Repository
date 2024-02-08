# Completed Beginner OOP Example from Python Crash Course Chapter 9
# The Car Class
"""A class that can be used to represent a car""" # Module level docstr to descr. what module does

class Car:                                                         
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Default attributes can be assigned in __init__ method

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()  # "Dryer than putting .title() in each var above

    def read_odometer(self):
        """Print car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.\n")

    def update_odometer(self, mileage):
        """Set the odometer to the given value"""
        """Reject the value if it attempts to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        if miles >= 0:
            self.odometer_reading += miles  
        else:
            print("You can't roll back an odometer!")
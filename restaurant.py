class Restaurant:  # 9.1 TYS PCC
    """Take a restaurant's name and cuisine and print"""

    def __init__(self, name, cuisine):
        """Initialize name and cuisine type"""
        self.name = name.title() # title() for DRY 
        self.cuisine = cuisine.title()
        self.num_served = 0  # used to set inital state, attributes of objects

    def describe_restaurant(self):  # no param for name, already in self
        print(f"\nRestaurant: {self.name}")
        print(f"Cuisine type: {self.cuisine}")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

    def set_num_served(self, num=None):  # don't forget "self" in methods
        """Set initial value of number served. This serves as an alternate to __init__ attribute"""
        if num is not None:  # allows set to be optional
            self.num_served = num
        # don't forget self. when calling
        print(f"\nNumber of patrons served: {self.num_served}")

    def increment_num_served(self, num):
        """Passes number to add/increment sum of patrons served"""
        self.num_served += num
        print(f"Number of patrons served: {self.num_served}")

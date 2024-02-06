from car import Car

# Battery and Electric Car Class 
"""Battery class and ElectricCar class taken from Car"""
# Composition used by attributing an instance of Battery to ElectricCar. 
# This promotes clean, modular design. 
# Use .attribute.method notation when calling any methods from the attributed class.
# The Battery class is "encapsulated"

class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=40):
       """Initialize the battery's attributes"""
       self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(
            f"This car has a {self.battery_size}-kWh battery.")  # use self. in methods

    def get_range(self):
        """Print a statement about the range this battery provides"""
        battery_range = 0
        if self.battery_size == 40:
            battery_range = 150
        elif self.battery_size == 65:
            battery_range = 225
        elif self.battery_size >= 65:
            battery_range = 300
        print(f"This car can go about {battery_range} miles on a full charge.")

    def upgrade_battery(self):
        """Check battery size and set capacity to 65"""
        if self.battery_size != 65:
            self.battery_size = 65
            print(f"Battery size has been updated to {self.battery_size}.\n")


class ElectricCar(Car):
    # Parent class must come before child
    """"Represent aspects of car unique to electric vehicles"""

    def __init__(self, make, model, year):
        """Initalize attributes of the parent class. Then initialize attributes specific to EV"""
        super().__init__(make, model, year)
        """ 
         super() imports __init__ from parent class to child. Name comes from super/sub class 
         Super() is called INSIDE the __init__ method. Super DOES NOT NEED SELF argument
        """
        self.battery = Battery(
            80)                 # Now every ElectricCar class has Battery instance installed since it is in ElectricCar's __init__ method's attributes
        """assign new class to this att. w/in a class. This is where you can change Battery's default battery_size, 
            which was assigned in Battery() parameters. This addition was part of the section "Instances as Attributes. 
            This may seem like a lot of extra work, but now Battery() class can expand w/o cluttering ElectricCar() class"""

    # a same-name method in parent class would be overidden, related to polymorphism
    def fill_gas_tank(self):
        """Electric cars don't have gastanks"""
        print("This car does not have a gas tank!")
 
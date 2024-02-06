from car import Car
from electric_car import Battery as Bt, ElectricCar as ec

my_prius = ec('Toyota', 'Prius', 2019)
print()
print(my_prius.get_descriptive_name())
my_prius.battery.describe_battery() # Battery class not part of EC, use battery inst. att. from EC 
my_prius.battery.get_range() 
print() 

my_truck = Car('Ford', 'F150', 2007)
print(my_truck.get_descriptive_name())
my_truck.odometer_reading = 143_131
my_truck.read_odometer()


from car import Car # opens car module and imports class Car
my_second_car = Car('nissian', 'altima', 1997)
print(my_second_car.get_descriptive_name())
my_second_car.odometer_reading = 187_232 # updates attribute directely
my_second_car.read_odometer()
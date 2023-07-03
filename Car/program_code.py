# import Car class
from car_class import Car
import time

# create Car object
Car1 = Car("2017", "Mercedes Benz")

Car1.show_details()

# call accelerate & get_speed (5 times)
for i in range(0, 5):
    Car1.accelerate()
    Car1.get_speed()
    Car1.show_speed()
    time.sleep(0.6)

# call brake & get_speed (5 times)
for i in range(0, 5):
    Car1.brake()
    Car1.get_speed()
    Car1.show_speed()
    time.sleep(0.6)

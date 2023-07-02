# import Car class
from car_class import Car

# create Car object
Car1 = Car("2017", "Mercedes Benz")

# call accelerate & get_speed (5 times)
for i in range(0, 5):
    Car1.accelerate()
    Car1.get_speed()
    Car1.show()

# call brake & get_speed (5 times)
for i in range(0, 5):
    Car1.brake()
    Car1.get_speed()
    Car1.show()

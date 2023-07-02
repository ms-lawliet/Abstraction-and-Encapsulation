# create car class
class Car:
    def __init__(self, year_model, make, speed=0):  # make a constructor w/ required attributes
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    # create methods
    def accelerate(self):   # accelerate
        self.__speed = self.__speed + 5
        return self.__speed

    def brake(self):   # brake
        self.__speed = self.__speed - 5
        return self.__speed

    def get_speed(self):   # get speed
        return self.__speed

    def show(self):   # show details
        print(f"Car details: {self.__year_model} {self.__make}, {self.__speed} m/s")

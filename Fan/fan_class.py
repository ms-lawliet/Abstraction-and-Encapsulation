# create Fan class
class Fan:
    # assign speed constants
    slow = 1
    medium = 2
    fast = 3

    # create constructor
    def __init__(self, speed=slow, is_on=False, radius=5, color="Blue"):
        self.__speed = speed
        self.__is_on = is_on
        self.__radius = radius
        self.__color = color

    # create methods,
    def set_speed(self, speed):  # set speed
        self.__speed = speed

    def set_is_on(self, is_on):  # set on or off
        if is_on == "on":
            self.__is_on = True
        else:
            pass

    def set_radius(self, radius):  # set radius
        self.__radius = radius

    def set_color(self, color):  # set color
        self.__color = color

    def get_speed(self):  # get speed
        return self.__speed

    def get_is_on(self):  # get status (on or off)
        return self.__is_on
    
    # get radius
    # get color
    # show properties

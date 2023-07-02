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
        
    # set on or off
    # set radius
    # set color
    # get speed
    # get status (on or off)
    # get radius
    # get color
    # show properties

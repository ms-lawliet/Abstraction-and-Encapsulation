from colorama import Fore, Back
import time


class Car:   # create car class
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

    def show_details(self):   # show details
        print(Fore.MAGENTA + Back.BLACK + f"Car details: " + Fore.BLUE + f"{self.__year_model} {self.__make}" + Back.RESET)
        time.sleep(0.5)

    def show_speed(self):   # show details
        print(Fore.RED + Back.BLACK + f"Speed: {self.__speed} m/s" + Back.RESET)

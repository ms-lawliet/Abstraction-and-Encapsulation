# import pet and user interface class
from pet_class import Pet
from user_interface import UserInterface

ui = UserInterface()

# ask user for values
name = ui.ask_pet_name()
animal_type = ui.ask_animal_type()

# create object
# print out results

# import pet and user interface class
from pet_class import Pet
from user_interface import UserInterface

ui = UserInterface()

# ask user for values
name = ui.ask_pet_name()
animal_type = ui.ask_animal_type()
age = ui.ask_pet_age()

# create object
Pet1 = Pet(name, animal_type, age)

# print out results
print("Pet name: " + name + ", Animal type: " + animal_type + ", Age: " + str(age))

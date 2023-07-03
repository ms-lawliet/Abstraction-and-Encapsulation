from colorama import Fore


class UserInterface:   # create class for user interface
    def ask_pet_name(self):   # ask user for pet name,
        name = input(Fore.BLUE + "Enter pet name: ")
        return name

    def ask_animal_type(self):  # animal type
        animal_type = input(Fore.LIGHTBLUE_EX + "Enter animal type: ")
        return animal_type

    def ask_pet_age(self):  # pet age
        age = float(input(Fore.CYAN + "Enter pet age (in years): " + Fore.RESET))
        return age

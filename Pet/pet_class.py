# create pet class
class Pet:
    def __init__(self, name, animal_type, age):  # create constructor w/ required attributes
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # create methods,
    def set_name(self, name):  # set_name
        self.__name = name

    def set_animal_type(self, animal_type):  # set_animal_type
        self.__animal_type = animal_type

    def set_age(self, age):  # set_age
        self.__age = age

    def get_name(self):  # get name
        return self.__name
    
    # get_animal_type
    # get_age

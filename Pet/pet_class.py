# create pet class
class Pet:
    def __init__(self, name, animal_type, age):  # create constructor w/ required attributes
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # create methods,
    def set_name(self, name):  # set_name
        self.__name = name
        
    # set_animal_type
    # set_age
    # get name
    # get_animal_type
    # get_age

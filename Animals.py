#!/usr/bin/python3
"""Class that defines animals"""


class Animals:
    """Constructor method"""

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, species):
        self.__species = species

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    """Methods"""
    def move(self, move):
        print("This is my move:", move)
    def show(self, show):
        print("I'm showing my:", show)
    def sound(self, sound):
        print("I make this sound:", sound)

"""Class for aquatic animals"""

class Aquatics(Animals):
    def __init__(self, name, species, age):
        super().__init__(name, species, age)

"""Class for terrestrial animals"""

class Terrestrial(Animals):
    def __init__(self, name, species, age):
        super().__init__(name, species, age)

"""Aquatic"""

class Crab(Aquatics):
    def __init__(self, name, species, age):
        super().__init__(name, species, age)

class Whale(Aquatics):
    def __init__(self, name, species, age):
        super().__init__(name, species, age)

"""Terrestrial"""

class Cat(Terrestrial):
    def __init__(self, name, species, age):
        super().__init__(name, species, age)

class Dog(Terrestrial):
    def __init__(self, name, species, age):
        super().__init__(name, species, age)

"""Objects"""

crab1 = Crab("Crabbie", "Blue crab", 3)
whale1 = Whale("MobyDick", "White whale", 10)
cat1 = Cat("Aslam", "Native cat", 5)
dog1 = Dog("Rockie", "Pitbull dog", 4)
crab1.name = "Pepe"
cat1.species = "Angora"
dog1.age = 6
cat1.sound("Miaauu!!")

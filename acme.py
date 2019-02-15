"""
File name: acme.py
Developer: Shreyas Jothish
Description: Acme Corporation - Product class.
"""

import random


class Product():
    """
    Product class is used to better organize the vast quantities and
    variety of goods company manages and sells.
    """
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        assert(isinstance(name, str))
        self.name = name

        assert(isinstance(price, int))
        self.price = price

        assert(isinstance(weight, int))
        self.weight = weight

        assert(isinstance(flammability, float))
        self.flammability = flammability

        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        """
        Calculates the stealability based on Product's price and weight
        """
        stealability = self.price / self.weight

        if stealability < 0.5:
            return "Not so stealable..."
        elif stealability >= 0.5 and stealability < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """
        Calculates the changes of exploding based on Product's flammability
        and weight
        """
        explode = self.flammability * self.weight

        if explode < 10.0:
            return "...fizzle."
        elif explode >= 10.0 and explode < 50.0:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """
    BoxingGlove product
    """

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        Product.__init__(self, name, price, weight, flammability)

    def explode(self):
        """
        BoxingGlove does not explode
        """
        return "...it's a glove."

    def punch(self):
        """
        Get the puch impact based on BoxingGlove's weight
        """
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"

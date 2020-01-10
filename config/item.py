from random import *


class Items:
    """Describes an item"""
    def __init__(self, level):
        # Items position in boxes
        self.i = None
        # Level in which the items is located
        self.level = level
        self.case_x = 0
        self.case_y = 0

    def display_item(self):
        """Method for display all items"""
        self.display_ether()
        self.display_needle()
        self.display_tube()

    def random_case(self):
        """Method to get a random case"""
        self.case_x = randint(1, 14)
        self.case_y = randint(1, 14)
        self.i = self.level.structure[self.case_x][self.case_y]

    def generate(self, item):
        """Method general for generate randomly an items"""
        while True:
            self.random_case()
            if self.i in ' ':
                self.level.structure[self.case_x][self.case_y] = item
                break

    def display_ether(self):
        """Method for display randomly ether"""
        self.generate('1')

    def display_needle(self):
        """Method for display randomly needle"""
        self.generate('2')

    def display_tube(self):
        """Method for display randomly tube"""
        self.generate('3')



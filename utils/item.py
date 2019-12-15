from random import *


class Items:
    """Describes an item"""
    def __init__(self, level):
        # Items position in boxes
        self.case_x = 0
        self.case_y = 0
        self.i = None
        # Level in which the items is located
        self.level = level

    def random_case(self):
        self.case_x = randint(1, 14)
        self.case_y = randint(1, 14)
        self.i = self.level.structure[self.case_x][self.case_y]

    def display_ether(self):
        """Method for display randomly ether"""
        while True:
            self.random_case()
            if self.i in ' ':
                self.level.structure[self.case_x][self.case_y] = '1'
                break

    def display_needle(self):
        """Method for display randomly needle"""
        while True:
            self.random_case()
            if self.i in ' ':
                self.level.structure[self.case_x][self.case_y] = '2'
                break

    def display_tube(self):
        """Method for display randomly tube"""
        while True:
            self.random_case()
            if self.i in ' ':
                self.level.structure[self.case_x][self.case_y] = '3'
                break

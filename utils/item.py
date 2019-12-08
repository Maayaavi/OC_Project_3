from random import *


class Items:
    """Describes an item"""
    def __init__(self, level):
        # Items position in boxes
        self.case_x = 0
        self.case_y = 0
        # Level in which the items is located
        self.level = level

    def display_ether(self):
        """Method for display randomly ether"""
        item = True
        while item:
            self.case_x = randint(1, 14)
            self.case_y = randint(1, 14)
            i = choice(self.level.structure[self.case_x][self.case_y])
            if i in ' ':
                self.level.structure[self.case_x][self.case_y] = '1'
                item = False

    def display_needle(self):
        """Method for display randomly needle"""
        item = True
        while item:
            self.case_x = randint(1, 14)
            self.case_y = randint(1, 14)
            i = choice(self.level.structure[self.case_x][self.case_y])
            if i in ' ':
                self.level.structure[self.case_x][self.case_y] = '2'
                item = False

    def display_tube(self):
        """Method for display randomly tube"""
        item = True
        while item:
            self.case_x = randint(1, 14)
            self.case_y = randint(1, 14)
            i = choice(self.level.structure[self.case_x][self.case_y])
            if i in ' ':
                self.level.structure[self.case_x][self.case_y] = '3'
                item = False

from random import *


class Items:
    """Describes an item"""
    def __init__(self, level):
        # Items position in boxes and pixels
        self.case_x = 0
        self.case_y = 0
        # Level in which the items is located
        self.niveau = level

    def display_item(self):
        pass

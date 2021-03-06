import pygame
from utils.constants import *


class Character:
    """Class to create a character"""
    def __init__(self, level, item):
        # Sprite of the character
        self.character = pygame.image.load(IMAGE_CHARACTER).convert_alpha()
        # Character position in boxes and pixels
        self.case_x = 1
        self.case_y = 0
        self.x = 30
        self.y = 0
        self.data_item = item
        self.niveau = level

    def move_right(self):
        """Method for move the character to the right"""
        # Not to exceed the screen
        if self.case_x < (NUMBER_SPRITE_SIDE - 1):
            # Check that the destination box is not a wall
            if self.niveau.structure[self.case_y][self.case_x + 1] not in ['-', '+',  '|']:
                self.case_x += 1
                # Calculation of the "real" position in pixel
                self.x = self.case_x * SIZE_SPRITE

    def move_left(self):
        """Method for move the character to the left"""
        if self.case_x > 0:
            if self.niveau.structure[self.case_y][self.case_x - 1] not in ['-', '+', '|']:
                self.case_x -= 1
                self.x = self.case_x * SIZE_SPRITE

    def move_up(self):
        """Method for move up the character"""
        if self.case_y > 0:
            if self.niveau.structure[self.case_y - 1][self.case_x] not in ['-', '+', '|']:
                self.case_y -= 1
                self.y = self.case_y * SIZE_SPRITE

    def move_down(self):
        """Method for move down the character"""
        if self.case_y < (NUMBER_SPRITE_SIDE - 1):
            if self.niveau.structure[self.case_y + 1][self.case_x] not in ['-', '+', '|']:
                self.case_y += 1
                self.y = self.case_y * SIZE_SPRITE

    def find(self):
        """Method for find items"""
        # If the player go into the items it will be on the dictionary
        if self.niveau.structure[self.case_y][self.case_x] in '1':
            self.data_item["e"] = 1
            # Delete the item
            self.niveau.structure[self.case_y][self.case_x] = " "
        elif self.niveau.structure[self.case_y][self.case_x] in '2':
            self.data_item["n"] = 1
            self.niveau.structure[self.case_y][self.case_x] = " "
        elif self.niveau.structure[self.case_y][self.case_x] in '3':
            self.data_item["t"] = 1
            self.niveau.structure[self.case_y][self.case_x] = " "

    def exit(self):
        """Method for exit from the labyrinth"""
        if self.niveau.structure[self.case_y][self.case_x] in 'g':
            if self.data_item == {"e": 1, "n": 1, "t": 1}:
                # Transform the guardian to sleeping
                self.niveau.structure[self.case_y][self.case_x] = "s"
            else:
                return 'lose'
        elif self.niveau.structure[self.case_y][self.case_x] == 'a':
            return 'win'

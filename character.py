import pygame
from pygame.locals import *
from constantes import *


class Character:
    """Class to create a character"""
    def __init__(self, character, level):
        # Sprite of the character
        self.character = pygame.image.load(image_character).convert_alpha()
        # Character position in boxes and pixels
        self.case_x = 1
        self.case_y = 0
        self.x = 30
        self.y = 0
        # Default direction
        self.direction = self.character
        # Level in which the character is located
        self.niveau = level

    def move(self, direction):
        """Method for moving the character"""
        # Move to the right
        if direction == 'right':
            # Not to exceed the screen
            if self.case_x < (number_sprite_side - 1):
                # Check that the destination box is not a wall
                if self.niveau.structure[self.case_y][self.case_x + 1] != '-' and \
                        self.niveau.structure[self.case_y][self.case_x + 1] != '+' and\
                        self.niveau.structure[self.case_y][self.case_x + 1] != '|':
                        # Moving a box
                        self.case_x += 1
                        # Calculation of the "real" position in pixel
                        self.x = self.case_x * size_sprite
            # Image of the character
            self.direction = self.character
        # Move to the left
        if direction == 'left':
            if self.case_x > 0:
                if self.niveau.structure[self.case_y][self.case_x - 1] != '-' and \
                        self.niveau.structure[self.case_y][self.case_x - 1] != '+' and\
                        self.niveau.structure[self.case_y][self.case_x - 1] != '|':
                    self.case_x -= 1
                    self.x = self.case_x * size_sprite
            self.direction = self.character
        # Move up
        if direction == 'up':
            if self.case_y > 0:
                if self.niveau.structure[self.case_y - 1][self.case_x] != '-' and \
                        self.niveau.structure[self.case_y - 1][self.case_x] != '+' and \
                        self.niveau.structure[self.case_y - 1][self.case_x] != '|':
                    self.case_y -= 1
                    self.y = self.case_y * size_sprite
            self.direction = self.character
        # Move down
        if direction == 'down':
            if self.case_y < (number_sprite_side - 1):
                if self.niveau.structure[self.case_y + 1][self.case_x] != '-' and \
                        self.niveau.structure[self.case_y + 1][self.case_x] != '+' and \
                        self.niveau.structure[self.case_y + 1][self.case_x] != '|':
                    self.case_y += 1
                    self.y = self.case_y * size_sprite
            self.direction = self.character

    def find(self):
        """Method for find items"""
        # If the player go into the items it will be on the dictionary
        if self.niveau.structure[self.case_y][self.case_x] == '1':
            data_item["e"] = 1
            # Delete the item
            self.niveau.structure[self.case_y][self.case_x] = " "
            print(data_item)
        elif self.niveau.structure[self.case_y][self.case_x] == '2':
            data_item["n"] = 1
            self.niveau.structure[self.case_y][self.case_x] = " "
            print(data_item)
        elif self.niveau.structure[self.case_y][self.case_x] == '3':
            data_item["t"] = 1
            print(data_item)
            self.niveau.structure[self.case_y][self.case_x] = " "

    def exit(self):
        """Method for exit from the labyrinth"""
        if self.niveau.structure[self.case_y][self.case_x] == 'g':
            if data_item == {"e": 1, "n": 1, "t": 1}:
                # Transform the guardian to sleeping
                self.niveau.structure[self.case_y][self.case_x] = "s"
                print('ok')
            else:
                return "lost"
        elif self.niveau.structure[self.case_y][self.case_x] == 'a':
            return "win"


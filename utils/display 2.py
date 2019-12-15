"""Class for display the Macgyver Maze Game on Pygame or console"""

import pygame
from utils.constantes import *


class Display:

    def __init__(self, level, item):
        self.level = level
        self.data_item = item
        # Opening the Pygame window (square: width = height)
        self.window = pygame.display.set_mode((window_side, window_side + 40))
        # Loading images
        self.wall = pygame.image.load(image_wall).convert()
        self.background_counter = pygame.image.load(image_background_counter).convert()
        self.ether = pygame.image.load(image_ether).convert_alpha()
        self.needle = pygame.image.load(image_needle).convert_alpha()
        self.tube = pygame.image.load(image_tube).convert_alpha()
        self.character = pygame.image.load(image_character).convert_alpha()
        self.guardian = pygame.image.load(image_guardian).convert_alpha()
        self.guardian_sleep = pygame.image.load(image_guardian_sleep).convert_alpha()

    def display_window(self):
        pass

    def display_game(self):
        """Method for displaying the level according to
        of the structure list returned by generer ()"""
        # We go through the level list
        num_ligne = 0
        for ligne in self.level.structure:
            # We go through the lists of lines
            num_case = 0
            for sprite in ligne:
                # The actual position in pixels is calculated
                x = num_case * size_sprite
                y = num_ligne * size_sprite
                if sprite == '+' or sprite == '-' or sprite == '|':  # +, -, | = Mur
                    self.window.blit(self.wall, (x, y))
                elif sprite == '1':  # e = Ether
                    self.window.blit(self.ether, (x, y))
                elif sprite == '2':  # n = Needle
                    self.window.blit(self.needle, (x, y))
                elif sprite == '3':  # t = Tube
                    self.window.blit(self.tube, (x, y))
                elif sprite == 'X':  # X = Character
                    self.window.blit(self.character, (x, y))
                elif sprite == 'g':  # g = Guardian
                    self.window.blit(self.guardian, (x, y))
                elif sprite == 's':  # s = sleeping Guardian
                    self.window.blit(self.guardian_sleep, (x, y))
                num_case += 1
            num_ligne += 1

    def display_item_counter(self):
        self.window.blit(self.background_counter, (0, 450))
        if self.data_item["e"] == 1:
            self.window.blit(self.ether, (10, 455))

        if self.data_item["n"] == 1:
            self.window.blit(self.needle, (40, 455))

        if self.data_item["t"] == 1:
            self.window.blit(self.tube, (70, 455))

    def display_console(self):
        for i in range(len(self.level.structure)):
            for j in range(len(self.level.structure[i])):
                print(self.level.structure[i][j], end='')
            print()

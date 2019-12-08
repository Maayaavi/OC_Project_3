"""Class for display the Macgyver Maze Game on Pygame or console"""

import pygame
from utils.constantes import *


class Display:

    def __init__(self, level):
        self.level = level

    def display_pygame(self, fenetre):
        """Method for displaying the level according to
        of the structure list returned by generer ()"""
        # Loading images
        wall = pygame.image.load(image_wall).convert()
        ether = pygame.image.load(image_ether).convert_alpha()
        needle = pygame.image.load(image_needle).convert_alpha()
        tube = pygame.image.load(image_tube).convert_alpha()
        character = pygame.image.load(image_character).convert_alpha()
        guardian = pygame.image.load(image_guardian).convert_alpha()
        guardian_sleep = pygame.image.load(image_guardian_sleep).convert_alpha()

        # We go through the level list
        num_ligne = 0
        for ligne in self.level.structure:
            # We go through the lists of lines
            num_case = 0
            for sprite in ligne:
                # The actual position in pixels is calculated
                x = num_case * size_sprite
                y = num_ligne * size_sprite
                if sprite == '+' or sprite == '-' or sprite == '|':  # m = Mur
                    fenetre.blit(wall, (x, y))
                elif sprite == '1':  # e = Ether
                    fenetre.blit(ether, (x, y))
                elif sprite == '2':  # n = Needle
                    fenetre.blit(needle, (x, y))
                elif sprite == '3':  # t = Tube
                    fenetre.blit(tube, (x, y))
                elif sprite == 'X':  # X = Character
                    fenetre.blit(character, (x, y))
                elif sprite == 'g':  # g = Guardian
                    fenetre.blit(guardian, (x, y))
                elif sprite == 's':  # s = sleeping Guardian
                    fenetre.blit(guardian_sleep, (x, y))
                num_case += 1
            num_ligne += 1

    def display_console(self):
        for i in range(len(self.level.structure)):
            for j in range(len(self.level.structure[i])):
                print(self.level.structure[i][j], end='')
            print()

"""Class of the Macgyver Maze Game"""

import pygame
from pygame.locals import *
from constantes import *


class Level:
    """Class to create a level"""

    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0

    def generer(self):
        """Method for generating the level according to the file.
        We create a general list, containing a list by line to display"""
        # Open the file
        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            # We go through the lines of the file
            for ligne in fichier:
                ligne_niveau = []
                # We go through the sprites (letters) contained in the file
                for sprite in ligne:
                    # We ignore the end of line "\ n"
                    if sprite != '\n':
                        # We add the sprite to the list of the line
                        ligne_niveau.append(sprite)
                # Add the line to the level list
                structure_niveau.append(ligne_niveau)
            # We save this structure
            self.structure = structure_niveau

    def afficher(self, fenetre):
        """Method for displaying the level according to
        of the structure list returned by generer ()"""
        # Loading images
        wall = pygame.image.load(image_wall).convert()
        ether = pygame.image.load(image_ether).convert_alpha()
        syringe = pygame.image.load(image_syringe).convert_alpha()
        needle = pygame.image.load(image_needle).convert_alpha()
        tube = pygame.image.load(image_tube).convert()
        guardian = pygame.image.load(image_guardian).convert_alpha()
        start = pygame.image.load(image_depart).convert()
        end = pygame.image.load(image_arrivee).convert_alpha()

        # We go through the level list
        num_ligne = 0
        for ligne in self.structure:
            # We go through the lists of lines
            num_case = 0
            for sprite in ligne:
                # The actual position in pixels is calculated
                x = num_case * size_sprite
                y = num_ligne * size_sprite
                if sprite == 'm':  # m = Mur
                    fenetre.blit(wall, (x, y))
                elif sprite == 'd':  # d = Start
                    fenetre.blit(start, (x, y))
                elif sprite == 's':  # s = Syringe
                    fenetre.blit(syringe, (x, y))
                elif sprite == 'e':  # e = Ether
                    fenetre.blit(ether, (x, y))
                elif sprite == 'n':  # n = Needle
                    fenetre.blit(needle, (x, y))
                elif sprite == 't':  # n = Tube
                    fenetre.blit(tube, (x, y))
                elif sprite == 'g':  # g = Guardian
                    fenetre.blit(guardian, (x, y))
                elif sprite == 'a':  # a = End
                    fenetre.blit(end, (x, y))
                num_case += 1
            num_ligne += 1


class Perso:
    """Classe permettant de créer un personnage"""

    def __init__(self, right, left, up, down, level):
        # Sprites of the character
        self.right = pygame.image.load(right).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.up = pygame.image.load(up).convert_alpha()
        self.down = pygame.image.load(down).convert_alpha()
        # Character position in boxes and pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        # Default direction
        self.direction = self.right
        # Level in which the character is located
        self.niveau = level

    def move(self, direction):
        """Methode permettant de déplacer le personnage"""

        # Move to the right
        if direction == 'right':
            # Not to exceed the screen
            if self.case_x < (nombre_sprite_cote - 1):
                # Check that the destination box is not a wall
                if self.niveau.structure[self.case_y][self.case_x + 1] != 'm':
                    # Moving a box
                    self.case_x += 1
                    # Calculation of the "real" position in pixel
                    self.x = self.case_x * size_sprite
            # Image in the right direction
            self.direction = self.right

        # Move to the left
        if direction == 'left':
            if self.case_x > 0:
                if self.niveau.structure[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * size_sprite
            self.direction = self.left

        # Move up
        if direction == 'up':
            if self.case_y > 0:
                if self.niveau.structure[self.case_y - 1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * size_sprite
            self.direction = self.up

        # Move down
        if direction == 'down':
            if self.case_y < (nombre_sprite_cote - 1):
                if self.niveau.structure[self.case_y + 1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * size_sprite
            self.direction = self.down

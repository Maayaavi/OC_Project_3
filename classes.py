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

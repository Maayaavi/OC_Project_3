#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Macgyver Maze Game
A game in you have to move Macgyver to the exit door by collecting
some objects through the labyrinth to sleep the guardian.
"""

import pygame
from pygame.locals import *

from classes import *
from constantes import *

pygame.init()

# Opening the Pygame window (square: width = height)
window = pygame.display.set_mode((cote_fenetre, cote_fenetre))
# Icone
icon = pygame.image.load(image_icon)
pygame.display.set_icon(icon)
# Title
pygame.display.set_caption(window_title)

# MAIN LOOP
start = 1
while start:
    # Loading and viewing the home screen
    home = pygame.image.load(image_intro).convert()
    window.blit(home, (0, 0))

    # Refreshments
    pygame.display.flip()

    # These variables are reset to 1 at each loop turn
    continue_intro = 1
    continue_game = 1

    # HOME LOOP
    pygame.mixer.Sound(sound_intro).play()
    while continue_intro:

        # Speed limitation of the loop
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # If the user leaves, we put the variables
            # loop to 0 to browse none and close
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continue_game = 0
                continue_intro = 0
                start = 0
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

    # Welcome sound
    pygame.mixer.Sound(sound_intro).play()

    # HOME LOOP
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
                # Variable of choice of the level
                choice = 0

            elif event.type == KEYDOWN:
                # Launch of level 1
                if event.key == K_RETURN:
                    pygame.mixer.stop()
                    continue_intro = 0  # We leave home loop
                    choice = 'n1'  # We define the level to load

    # Check that the player has made a choice of level
    # to not load if he leaves
    if choice != 0:
        # Loading the background image
        background = pygame.image.load(image_background).convert()

        # Generating a level from a file
        niveau = Level(choice)
        niveau.generer()
        niveau.afficher(window)

        # Game sound
        pygame.mixer.Sound(sound_game).play(loops=-1)

    # GAME LOOP
    while continue_game:
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # If the user leaves, we put the variable that continues the game
            # AND the general variable to 0 to close the window
            if event.type == QUIT:
                continue_game = 0
                start = 0
            elif event.type == KEYDOWN:
                # If the user press Esc, we just go back to the menu
                if event.key == K_ESCAPE:
                    pygame.mixer.stop()
                    continue_game = 0

        # Displays at new positions
        window.blit(background, (0, 0))
        niveau.afficher(window)
        pygame.display.flip()

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
window = pygame.display.set_mode((window_side, window_side))
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
        level = Level(choice)
        level.generer()
        level.afficher(window)

        # Création de Macgyver
        mg = Perso("images/mg_right.png", "images/mg_left.png",
                   "images/mg_up.png", "images/mg_down.png", level)

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
                # Character Move Keys
                elif event.key == K_RIGHT:
                    mg.move('right')
                elif event.key == K_LEFT:
                    mg.move('left')
                elif event.key == K_UP:
                    mg.move('up')
                elif event.key == K_DOWN:
                    mg.move('down')

        # If the player go into the items it will be on the dictionary
        if level.structure[mg.case_y][mg.case_x] == 's':
            data["s"] = 1
            print(data)
        elif level.structure[mg.case_y][mg.case_x] == 'e':
            data["e"] = 1
            print(data)
        elif level.structure[mg.case_y][mg.case_x] == 'n':
            data["n"] = 1
            print(data)
        elif level.structure[mg.case_y][mg.case_x] == 't':
            data["t"] = 1
            print(data)

        # Displays at new positions
        window.blit(background, (0, 0))
        level.afficher(window)
        window.blit(mg.direction, (mg.x, mg.y))  # mg.direction = the image in the right direction
        pygame.display.flip()
        # Variable for lost or win
        continue_win = 1
        continue_lost = 1

        if level.structure[mg.case_y][mg.case_x] == 'g':
            if data["s"] == 1 and data["e"] == 1 and data["n"] == 1 and data["t"] == 1:
                None
            # Lost -> Message -> Back to intro
            else:
                # Reset data value
                data = {"s": 0, "e": 0, "n": 0, "t": 0}
                # Stop game music
                pygame.mixer.stop()
                # play lost sound
                pygame.mixer.Sound(sound_lost).play()
                # BOUCLE DU LOST
                while continue_lost:
                    pygame.time.Clock().tick(30)
                    for event in pygame.event.get():
                        if event.type == KEYDOWN and event.key == K_RETURN:
                            continue_lost = 0
                            continue_game = 0
                        elif event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                            continue_lost = 0
                            continue_game = 0
                            continue_intro = 0
                            start = 0
                            choice = 0
                    # Loading and viewing the lost screen
                    lost = pygame.image.load(image_lost).convert()
                    window.blit(lost, (0, 0))
                    pygame.display.flip()

        elif level.structure[mg.case_y][mg.case_x] == 'a'\
                and data["s"] == 1 and data["e"] == 1 and data["n"] == 1 and data["t"] == 1:
            data = {"s": 0, "e": 0, "n": 0, "t": 0}
            # Stop game music
            pygame.mixer.stop()
            # Start win sound
            pygame.mixer.Sound(sound_win).play()
            # VICTORY LOOP
            while continue_win:
                pygame.time.Clock().tick(30)
                for event in pygame.event.get():
                    if event.type == KEYDOWN and event.key == K_RETURN:
                        continue_win = 0
                        continue_game = 0
                    elif event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        continue_win = 0
                        continue_game = 0
                        continue_intro = 0
                        start = 0
                        choice = 0

                # Loading and viewing the victory screen
                win = pygame.image.load(image_win).convert()
                window.blit(win, (0, 0))
                pygame.display.flip()

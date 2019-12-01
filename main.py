#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Macgyver Maze Game
A game in you have to move Macgyver to the exit door by collecting
some objects through the labyrinth to sleep the guardian.
"""

import pygame
from pygame.locals import *

from labyrinth import Labyrinth
from constantes import *
from character import Character
from item import Items
from display import Display


def main():
    pygame.init()

    # Opening the Pygame window (square: width = height)
    window = pygame.display.set_mode((window_side, window_side + 40))
    # Icone
    icon = pygame.image.load(image_icon)
    pygame.display.set_icon(icon)
    # Title
    pygame.display.set_caption(window_title)

    # MAIN LOOP
    start = True
    while start:
        # Display the home screen
        home = pygame.image.load(image_intro).convert()
        window.blit(home, (0, 0))

        # Refreshments
        pygame.display.flip()

        # These variables are reset to 1 at each loop turn
        continue_intro = True
        continue_game = False

        # INTRO LOOP
        while continue_intro:
            # Speed limitation of the loop
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                # If the user leaves, we put the variables
                # loop to 0 to browse none and close
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    continue_intro = False
                    start = False
                    # Variable of choice of the level
                    choice = 0
                elif event.type == KEYDOWN:
                    # Launch the level
                    if event.key == K_RETURN:
                        pygame.mixer.stop()
                        choice = 'n1.txt'  # We define the level to load
                        continue_intro = False
                        continue_game = True
                        # Check that the player has made a choice of level
                        # to not load if he leaves
                        if choice != 0:
                            # Loading the background image
                            background = pygame.image.load(image_background).convert()

                            # Generating a level from the file
                            level = Labyrinth(choice)
                            level.load()

                            # Generate all items
                            level_item = Items(level)
                            level_item.display_ether()
                            level_item.display_needle()
                            level_item.display_tube()

                            # Generate the character
                            mg = Character(level)

                            # Display the labyrinth
                            level_display = Display(level)
                            level_display.display_pygame(window)


        # GAME LOOP
        while continue_game:
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                # If the user leaves, we put the variable that continues the game
                # AND the general variable to 0 to close the window
                if event.type == QUIT:
                    continue_game = False
                    continue_intro = False
                    start = False
                    # Reset data value
                    data_item = {"e": 0, "n": 0, "t": 0}
                elif event.type == KEYDOWN:
                    # If the user press Esc, we just go back to the menu
                    if event.key == K_ESCAPE:
                        pygame.mixer.stop()
                        continue_game = False
                        data_item = {"e": 0, "n": 0, "t": 0}
                    # Character Move Keys
                    elif event.key == K_RIGHT:
                        mg.move_right('right')
                    elif event.key == K_LEFT:
                        mg.move_left('left')
                    elif event.key == K_UP:
                        mg.move_up('up')
                    elif event.key == K_DOWN:
                        mg.move_down('down')

            # Displays at new positions
            window.blit(background, (0, 0))
            level_display.display_pygame(window)
            window.blit(mg.character, (mg.x, mg.y))
            mg.find()
            mg.exit()
            pygame.display.flip()

            if mg.exit() == 'lost':
                # Reset data value
                data_item = {"e": 0, "n": 0, "t": 0}
                # Stop game music
                pygame.mixer.stop()
                # play lost sound
                pygame.mixer.Sound(sound_lost).play()
                # Lost loop
                continue_lost = 1
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

            elif mg.exit() == 'win':
                data_item = {"e": 0, "n": 0, "t": 0}
                # Stop game music
                pygame.mixer.stop()
                # Start win sound
                pygame.mixer.Sound(sound_win).play()
                # Victory loop
                continue_win = 1
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


if __name__=="__main__":
    main()

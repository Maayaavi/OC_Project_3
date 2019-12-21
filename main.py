#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Macgyver Maze Game
A game in the player have to move Macgyver to the exit door by collecting
some objects through the labyrinth to sleep the guardian.
"""

import pygame
from pygame.locals import *

from utils.labyrinth import Labyrinth
from utils.character import Character
from utils.item import Items
from utils.display import Display

from utils.constantes import *


class Game:

    def __init__(self):
        self.data_item = data_item
        # Opening the Pygame window (square: width = height)
        self.window = pygame.display.set_mode((window_side, window_side + 40))
        self.choice = 0
        self.while_start = True
        self.while_intro = True
        self.while_game = True
        self.while_lose = True
        self.while_win = True

    def main(self):
        pygame.init()

        # Icone
        icon = pygame.image.load(image_icon)
        pygame.display.set_icon(icon)
        # Title
        pygame.display.set_caption(window_title)

        # MAIN LOOP
        while self.while_start:
            # Display the home screen
            home = pygame.image.load(image_intro).convert()
            self.window.blit(home, (0, 0))

            # Refreshments
            pygame.display.flip()

            self.intro()

    def intro(self):
        # INTRO LOOP
        while self.while_intro:
            # Speed limitation of the loop
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                # If the user leaves, we put the variables
                # loop to 0 to browse none and close
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.while_intro = False
                    self.while_start = False

                elif event.type == KEYDOWN:
                    # Launch the level
                    if event.key == K_RETURN:
                        pygame.mixer.stop()
                        self.choice = 'n1.txt'  # We define the level to load

                        # Check that the player has made a choice of level
                        # to not load if he leaves
                        if self.choice != 0:
                            # Loading the background image
                            background = pygame.image.load(image_background).convert()

                            # Generating a level from the file
                            level = Labyrinth(self.choice)
                            level.load()

                            # Generate all items
                            level_item = Items(level)
                            level_item.display_ether()
                            level_item.display_needle()
                            level_item.display_tube()
                            # level_item.display_item()

                            # Generate the character
                            mg = Character(level)

                            # Display the labyrinth
                            level_display = Display(level, self.data_item)
                            level_display.display_game()

                            # Stop intro loop
                            self.while_intro = False
                            self.while_start = False

                            self.game(level_display, background, mg)

    def game(self, level_display, background, mg):
        # GAME LOOP
        while self.while_game:
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                # If the user leaves, we put the variable that continues the game
                # AND the general variable to 0 to close the window
                if event.type == QUIT:

                    # Stop game loop
                    self.while_game = False

                elif event.type == KEYDOWN:
                    # If the user press Esc, we just go back to the menu
                    if event.key == K_ESCAPE:

                        # Reinitialize an object
                        self.reset()

                        # Go to the main loop
                        self.main()

                        # Close the game loop
                        self.while_game = False

                    # Character Move Keys
                    elif event.key == K_RIGHT:
                        mg.move_right()
                    elif event.key == K_LEFT:
                        mg.move_left()
                    elif event.key == K_UP:
                        mg.move_up()
                    elif event.key == K_DOWN:
                        mg.move_down()

            # Displays at new positions
            self.window.blit(background, (0, 0))
            level_display.display_game()
            level_display.display_item_counter()
            self.window.blit(mg.character, (mg.x, mg.y))
            mg.find()
            mg.exit()
            pygame.display.flip()

            if mg.exit() == 'lost':
                # Play lost sound
                pygame.mixer.Sound(sound_lost).play()

                # Lost loop
                while self.while_lose:
                    pygame.time.Clock().tick(30)
                    for event in pygame.event.get():
                        if event.type == KEYDOWN and event.key == K_RETURN:

                            self.reset()
                            self.main()
                            self.while_lose = False
                            self.while_game = False

                        elif event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:

                            self.while_lose = False
                            self.while_game = False

                    # Diplay the lost screen
                    lost = pygame.image.load(image_lost).convert()
                    self.window.blit(lost, (0, 0))
                    pygame.display.flip()

            elif mg.exit() == 'win':
                # Play win sound
                pygame.mixer.Sound(sound_win).play()
                # Victory loop
                while self.while_win:
                    pygame.time.Clock().tick(30)
                    for event in pygame.event.get():
                        if event.type == KEYDOWN and event.key == K_RETURN:

                            self.reset()
                            self.main()
                            self.while_win = False
                            self.while_game = False

                        elif event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:

                            self.while_win = False
                            self.while_game = False

                    # Display the victory screen
                    win = pygame.image.load(image_win).convert()
                    self.window.blit(win, (0, 0))
                    pygame.display.flip()

    def reset(self):
        """ Method for Reinitialize value """
        self.while_start = True
        self.while_intro = True
        self.while_game = True
        self.while_lose = True
        self.while_win = True
        self.data_item = {"e": 0, "n": 0, "t": 0}


if __name__ == "__main__":
    game = Game()
    game.main()

#!/usr/bin/python3
# -*- coding: Utf-8 -*
########################################################################
# Filename    : main.py                                                #
# Description : A maze game in the player have to move Macgyver to the #
#               exit by collecting some objects through the labyrinth  #
#               for sleep the guardian.                                #
# Author      : LAVANIYAN Jeyasiri                                     #
# Modification: 2020/01/10                                             #
########################################################################

import pygame
import sys
import config

from pygame.locals import *
from utils.constants import *

pygame.init()
clock = pygame.time.Clock()


class Game:
    """Class to execute the game"""
    def __init__(self):
        self.data_item = {"e": 0, "n": 0, "t": 0}
        # Initialize the Pygame window (square: width = height)
        self.window = pygame.display.set_mode((window_width, window_length))
        self.choice = 0

    def intro(self):
        """ Method for display intro screen """
        # Icon
        icon = pygame.image.load(image_icon)
        pygame.display.set_icon(icon)
        # Title
        pygame.display.set_caption(window_title)
        # Intro loop
        while_intro = True
        while while_intro:
            # Display the home screen
            home = pygame.image.load(image_intro).convert()
            self.window.blit(home, (0, 0))
            # Refreshment
            pygame.display.flip()
            # Speed limitation of the loop
            clock.tick(30)
            for event in pygame.event.get():
                # If the user close the window or press Esc, it will leave the program
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.gamequit()
                elif event.type == KEYDOWN:
                    # Launch the map
                    if event.key == K_RETURN:
                        # Define the map to load
                        self.choice = 'map/n1.txt'
                        # Loading the background image
                        background = pygame.image.load(image_background).convert()
                        # Generate a structure from the file
                        level = config.labyrinth.Labyrinth(self.choice)
                        level.load()
                        # Generate all items
                        level_item = config.item.Items(level)
                        level_item.display_item()
                        # Generate the character
                        mg = config.character.Character(level, self.data_item)
                        # Display the labyrinth
                        level_display = config.display.Display(level, self.data_item)
                        level_display.display_game()
                        self.game(level_display, background, mg)
                        # Stop intro loop
                        while_intro = False

    def game(self, level_display, background, mg):
        """ Method for display game screen """
        # Game loop
        while_game = True
        while while_game:
            clock.tick(30)
            for event in pygame.event.get():
                # If the user close the window, it leave the program
                if event.type == QUIT:
                    # Stop game loop
                    self.gamequit()
                elif event.type == KEYDOWN:
                    # If the user press Esc, we just go back to the menu
                    if event.key == K_ESCAPE:
                        # Reinitialize the counter value
                        self.reset()
                        # Go to the main loop
                        self.intro()
                        while_game = False
                    # Character move keys
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

            if mg.exit() == 'lose':
                self.reset()
                self.lose()
                while_game = False
            elif mg.exit() == 'win':
                self.reset()
                self.win()
                while_game = False

    def lose(self):
        """ Method for display lose screen """
        # Play lose sound
        pygame.mixer.Sound(sound_lose).play()
        # Lose loop
        while_lose = True
        while while_lose:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_RETURN:
                    self.intro()
                    while_lose = False
                elif event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.gamequit()

            # Diplay the lose screen
            lost = pygame.image.load(image_lose).convert()
            self.window.blit(lost, (0, 0))
            pygame.display.flip()

    def win(self):
        """ Method for display win screen """
        # Play win sound
        pygame.mixer.Sound(sound_win).play()
        # Victory loop
        while_win = True
        while while_win:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_RETURN:
                    self.intro()
                    while_win = False
                elif event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.gamequit()

            # Display the victory screen
            win = pygame.image.load(image_win).convert()
            self.window.blit(win, (0, 0))
            pygame.display.flip()

    def reset(self):
        """ Method for Reinitialize value """
        self.data_item = {"e": 0, "n": 0, "t": 0}

    def gamequit(self):
        """ Method for quit game """
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.intro()

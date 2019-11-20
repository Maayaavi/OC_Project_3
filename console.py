#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Macgyver Maze Game on Terminal
A game in you have to move Macgyver to the exit door by collecting
some objects through the labyrinth to sleep the guardian.
"""

import sys
import os

from labyrinth import Labyrinth
from constantes import *
from character import *

if __name__ == '__main__':
    character = "X"
    choice = 'n1.txt'


def clear_screen():
    """
        Efface l’écran de la console
    """
    if sys.platform.startswith("win"):
        os.system("cls")
        # Si OS Windows
    else:
        os.system("clear")
        # Si OS Linux ou OS X


# MAIN LOOP
start = True
while start:
    clear_screen()

    continue_intro = True

    # HOME LOOP
    while continue_intro:
        clear_screen()
        print("\t\t**********************************************")
        print("\t\t***          Macgyver Maze Game            ***")
        print("\t\t**********************************************")
        print("")
        input("\t\tAppuyer sur \"Enter\" pour lancer le jeu")
        continue_game = True

        # GAME LOOP
        while continue_game:
            clear_screen()
            level = Labyrinth(choice)
            level.load()
            level.display_console()

            Character(character, level)


            entry = input("Votre déplacement, Sélectionez entre:\n Haut: H, Bas: B, Droite: D, Gauche"
                          ": G, Acceuil: A, Quitter: Q \nVotre choix? ")
            if entry == "A":
                continue_game = 0
            elif entry == "Q":
                exit(1)


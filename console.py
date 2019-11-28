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
from display import Display
from item import Items


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


def main():
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
            print("")
            input("\t\tAppuyer sur \"Enter\" pour lancer le jeu")
            choice = 'n1.txt'
            continue_game = True

            # GAME LOOP
            while continue_game:
                clear_screen()
                level = Labyrinth(choice)
                level.load()

                # Generate all items
                level_item = Items(level)
                level_item.display_ether()
                level_item.display_needle()
                level_item.display_tube()

                # Generate the character

                # Display the labyrinth
                i = Display(level)
                i.display_console()

                entry = input("Votre déplacement, Sélectionez entre:\n Haut: H, Bas: B, Droite: D, Gauche"
                              ": G, Acceuil: A, Quitter: Q \nVotre choix? ")
                if entry == "A":
                    continue_game = 0
                elif entry == "Q":
                    exit(1)


if __name__ == '__main__':
    main()
    character = "X"

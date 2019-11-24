"""Class for display the Macgyver Maze Game on Pygame or console"""

from labyrinth import Labyrinth



class Display:

    def __init__(self):
        self.structure = 0

    def display_console(self, structure):
        for i in range(len(self.structure)):
            for j in range(len(self.structure[i])):
                print(self.structure[i][j], end='')
            print()

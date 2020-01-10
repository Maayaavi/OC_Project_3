class Labyrinth:
    """Class to create a structure"""
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0

    def load(self):
        """Method for generating the level according to the file.
        We create a general list, containing a list by line to display"""
        # Open the file
        with open(self.fichier, "r") as file:
            structure_niveau = []
            # We go through the lines of the file
            for ligne in file:
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
            file.close()

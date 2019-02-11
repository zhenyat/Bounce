################################################################################
#   game_gui.py
#
#   Game view
#
#   11.02.2019  Created by: zhenya
################################################################################
from tkinter import *

class GameGUI():
    def __init__(self, master, game):
        self.master = master

        # Default attribures
        master.title('Bouncing a ball')
        master.geometry(self.center(master))
        master.attributes("-topmost", True)         # Place master over all other windows
        master.config(background = 'lightyellow')
        master.resizable(False, False)

        # Widgets
        self.canvas = Canvas(master, width=500, height=400)      # Game area
        self.canvas.pack()
        self.master.update()         # Initializes itself for the game animation
    
            # Locates GUI window in the center of a screen
    def center(self, master):
        masterWidth  = 800
        masterHeight = 600

        screenWidth  = master.winfo_screenwidth()
        screenHeight = master.winfo_screenheight()

        masterX = (screenWidth  - masterWidth)  / 2
        masterY = (screenHeight - masterHeight) / 2

        return('%dx%d+%d+%d' % (masterWidth, masterHeight, masterX, masterY))

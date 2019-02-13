################################################################################
#   game_gui.py
#
#   Game view
#
#   11.02.2019  Created by: zhenya
################################################################################
from tkinter import *
from game    import *

class GameGUI():
    def __init__(self, master, game):
        self.master = master

        # Default attribures
        self.master.title('Bouncing a ball')
        self.master.geometry(self.center())
        self.master.attributes("-topmost", True)         # Place master over all other windows
        self.master.config(background = 'lightyellow')
        self.master.resizable(False, False)

        # Widgets
        self.canvas = Canvas(master, width=500, height=400)      # Game area
        self.canvas.pack()
        self.master.update()         # Initializes itself for the game animation
    
        self.ball = Ball(self.canvas, 'red')
        self.bat  = Bat(self.canvas,  'blue')

        game.go(self)

    # Locates GUI window in the center of a screen
    def center(self):
        masterWidth  = 800
        masterHeight = 600

        screenWidth  = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()

        masterX = (screenWidth  - masterWidth)  / 2
        masterY = (screenHeight - masterHeight) / 2

        return('%dx%d+%d+%d' % (masterWidth, masterHeight, masterX, masterY))

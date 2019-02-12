################################################################################
#   ball.py
#
#   Model: ball
#
#   11.02.2019  Created by: zhenya
################################################################################
import random

class Ball():
    def __init__(self, canvas, color):
        self.canvas  = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color, outline=color)  # x1, y1: 10,10 - top-left
                                                                                 # x2, y2: 25,25 - bottom-right
        self.canvas.move(self.id, 245, 100)
        
        # Canvas boundaries
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width  = self.canvas.winfo_width()
        
        # Ball starting movement vector
        x_starting = [-3, -2, -1, 1, 2, 3]
        random.shuffle(x_starting)
        self.x =  x_starting[0]
        self.y = -3

    # Moves Canvas' object on x and y
    def move(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)         # Ball object coordinates (x1,y1, x2,y2)
                                                  #                 pos[i]:   0  1   2  3
        # Check canvas borders
        if (pos[1] <= 0 or pos[3] >= self.canvas_height):   # Top / Bottom reached
            self.y = -self.y
        if (pos[0] <= 0 or pos[2] >= self.canvas_width):    # Left / Right reached
            self.x = -self.x
